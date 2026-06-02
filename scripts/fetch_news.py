#!/usr/bin/env python3
# 1hcrypto 自动资讯脚本 v4
# 聚合多篇新闻为综合快讯，每天 1-2 篇
# AI 精写改写，不链原文，直接多空判断
# 中文文章全部中文，英文文章全部英文，不混淆

import json, os, re, time
import requests
from datetime import datetime, timezone, timedelta
from pathlib import Path
import xml.etree.ElementTree as ET

# ── 配置 ──────────────────────────────────
API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
API_URL = "https://api.deepseek.com/v1/chat/completions"
ZH_DIR  = Path(__file__).parent.parent / "src" / "content" / "zh" / "news"
EN_DIR  = Path(__file__).parent.parent / "src" / "content" / "en" / "news"

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; 1hcrypto-bot/4.0)"}

RSS_SOURCES = [
    ("CoinTelegraph", "https://cointelegraph.com/rss"),
    ("CoinDesk",     "https://www.coindesk.com/arc/outboundFeeds/rss/"),
    ("The Block",     "https://www.theblock.co/rss.xml"),
    ("Decrypt",       "https://decrypt.co/feed/"),
    ("BitcoinMag",    "https://bitcoinmagazine.com/.rss/full/"),
]

MAX_PER_RUN  = 2       # 每天最多生成 2 篇聚合快讯
MAX_AGE_HOURS = 36      # 只取 36 小时内的新闻
NEWS_PER_ARTICLE = 3    # 每篇快讯聚合 3 条新闻
DAYS_BACK = 2

# ── 工具函数 ──────────────────────────────────

def slugify(text: str) -> str:
    s = re.sub(r'[^\w\s-]', '', text).strip().lower()
    s = re.sub(r'[-\s]+', '-', s)
    return s[:50]

def get_recent_slugs(directory: Path, days: int = DAYS_BACK) -> set:
    if not directory.exists():
        return set()
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    slugs = set()
    for f in directory.glob("*.md"):
        try:
            if f.stat().st_mtime >= cutoff.timestamp():
                slugs.add(f.stem)
        except Exception:
            continue
    return slugs

def fetch_rss(source_name: str, url: str) -> list:
    try:
        resp = requests.get(url, headers=HEADERS, timeout=20)
        resp.raise_for_status()
        root = ET.fromstring(resp.content)
        channel = root.find("channel") or root
        items = channel.findall("item") if channel is not None else []
        entries = []
        for item in items:
            title    = (item.findtext("title") or "").strip()
            link     = (item.findtext("link") or "").strip()
            desc     = (item.findtext("description") or "").strip()
            pub_date = (item.findtext("pubDate") or item.findtext("published") or "").strip()
            if not title:
                continue
            dt = None
            for fmt in ("%a, %d %b %Y %H:%M:%S %z", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%SZ"):
                try:
                    dt = datetime.strptime(pub_date, fmt)
                    break
                except ValueError:
                    continue
            if dt is None:
                dt = datetime.now(timezone.utc)
            entries.append({
                "title": title,
                "url": link,
                "published": dt,
                "source": source_name,
                "description": (desc or "")[:500],
            })
        return entries
    except Exception as e:
        print(f"[RSS Error] {source_name}: {e}")
        return []

def call_deepseek(prompt: str, max_retries: int = 3) -> dict:
    if not API_KEY:
        raise RuntimeError("DEEPSEEK_API_KEY not set")
    for attempt in range(max_retries):
        try:
            resp = requests.post(
                API_URL,
                headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
                json={
                    "model": "deepseek-chat",
                    "messages": [
                        {"role": "system", "content": "You are a professional crypto market analyst. Always respond with valid JSON only, no code blocks, no markdown fences."},
                        {"role": "user", "content": prompt},
                    ],
                    "temperature": 0.7,
                    "max_tokens": 3000,
                },
                timeout=90,
            )
            resp.raise_for_status()
            content = resp.json()["choices"][0]["message"]["content"]
            content = re.sub(r'^```json\s*', '', content)
            content = re.sub(r'\s*```$', '', content)
            return json.loads(content)
        except Exception as e:
            print(f"[DeepSeek retry {attempt+1}/{max_retries}] {e}")
            time.sleep(2 ** attempt)
    raise RuntimeError("DeepSeek API failed after retries")

def generate_digest(entries: list) -> dict:
    """聚合多条新闻生成一篇综合快讯（中英文分别撰写，不是翻译）"""
    news_block = ""
    for i, e in enumerate(entries, 1):
        news_block += f"\n新闻 {i}：\n标题：{e['title']}\n来源：{e['source']}\n摘要：{e['description']}\n"

    prompt = f"""你是一位专业的加密货币市场分析师。请根据以下 {len(entries)} 条新闻，分别用中文和英文各撰写一篇综合快讯（不是翻译，是分别撰写）。

{news_block}

请严格遵守以下要求：

【中文版要求】
1. 标题简洁有力，15-25字，概括核心要点。标题中保留关键词如 BTC、ETH、ETF、SEC、监管、美联储等
2. 正文用简短的段落分别概括每条新闻的核心信息，每条配一个二级标题（##）
3. 每条新闻后简要说明其市场影响（1-2句话）
4. 最后给出整体市场情绪判断（看涨/看跌/中性）及综合理由
5. 绝对不要在正文中输出原文链接、URL、来源网址
6. 绝对不要在正文中输出采集时间、采集日期等元信息
7. 绝对不要出现"原文"、"来源"、"采集"、"出处"、"链接"等字样
8. 正文中不要出现 "news 1"、"news 2" 等英文编号
9. 内容全部用中文
10. 正文总字数 400-700 字
11. 正文中保留重要的搜索关键词：具体币种名称（BTC、ETH、SOL等）、机构名称（BlackRock、灰度、SEC等）、数据指标（ETF流入流出金额、资金费率、清算量等）

【英文版要求】
1. Title: concise and punchy, 10-20 words, include keywords like BTC, ETH, ETF, SEC, regulation, Fed
2. Body: use ## headings for each news item, 1-2 paragraphs each, explain market impact after each
3. End with overall sentiment (Bullish/Bearish/Neutral) and reasoning
4. NO links, NO URLs, NO source URLs in body
5. NO "collected on", NO timestamps, NO meta info in body
6. NO "news 1", "news 2" labels
7. All English, native style
8. Body length: 300-600 words
9. Keep SEO keywords: coin names, institution names, data figures

Output ONLY valid JSON in this exact format (no markdown fences, no code blocks):
{{
  "zh": {{
    "title": "中文标题",
    "content": "中文正文，使用 Markdown 格式",
    "sentiment": "看涨|看跌|中性",
    "market_impact": "对市场影响的综合分析（中文）"
  }},
  "en": {{
    "title": "English Title",
    "content": "English body, use Markdown format",
    "sentiment": "Bullish|Bearish|Neutral",
    "market_impact": "Comprehensive market impact analysis (English)"
  }}
}}"""
    return call_deepseek(prompt)

def save_article(directory: Path, slug: str, date_str: str, article: dict, lang: str):
    directory.mkdir(parents=True, exist_ok=True)
    filename = f"{date_str}-{slug}.md"
    filepath = directory / filename
    if filepath.exists():
        print(f"[Skip] {filepath} already exists")
        return False

    if lang == "zh":
        sentiment     = article.get("sentiment", "中性")
        title         = article.get("title", "无标题")
        content       = article.get("content", "")
        market_impact = article.get("market_impact", "")
    else:
        sentiment     = article.get("sentiment", "Neutral")
        title         = article.get("title", "Untitled")
        content       = article.get("content", "")
        market_impact = article.get("market_impact", "")

    coin_pattern = re.compile(r'\b(BTC|ETH|SOL|XRP|ADA|DOGE|AVAX|LINK|UNI|AAVE|SUI|DOT|MATIC|ARB|OP|LTC|BCH|ETF)\b', re.I)
    coins = list(set(coin_pattern.findall(content)))
    coins = [c.upper() for c in coins]
    if not coins:
        coins = ["BTC"]

    importance = "高" if lang == "zh" else "High"
    lower_content = content.lower()
    if not any(k in lower_content for k in ["etf", "sec", "监管", "regulation", "批准", "approval", "暴跌", "crash", "大涨", "surge"]):
        importance = "中" if lang == "zh" else "Medium"

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+08:00")

    if lang == "zh":
        md = f"""---
title: "{title}"
date: "{now}"
sentiment: "{sentiment}"
coins: {json.dumps(coins, ensure_ascii=False)}
importance: "{importance}"
tags: {json.dumps(coins, ensure_ascii=False)}
draft: false
---

{content}

## 多空判断

**{sentiment}**

{market_impact}

---
*以上分析基于公开信息整理，仅供参考，不构成投资建议。*
"""
    else:
        md = f"""---
title: "{title}"
date: "{now}"
sentiment: "{sentiment}"
coins: {json.dumps(coins)}
importance: "{importance}"
tags: {json.dumps(coins)}
draft: false
---

{content}

## Market Outlook

**{sentiment}**

{market_impact}

---
*Analysis based on public information for reference only. Not investment advice.*
"""

    filepath.write_text(md, encoding="utf-8")
    print(f"[Saved] {filepath}")
    return True

# ── 主流程 ──────────────────────────────────

def main():
    print("=" * 50)
    print(f"1H Crypto News Digest - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 50)

    if not API_KEY:
        print("[Error] DEEPSEEK_API_KEY not set. Exiting.")
        return

    zh_slugs = get_recent_slugs(ZH_DIR)
    en_slugs = get_recent_slugs(EN_DIR)
    print(f"[Dedup] Recent ZH: {len(zh_slugs)}, EN: {len(en_slugs)}")

    all_entries = []
    for source_name, url in RSS_SOURCES:
        entries = fetch_rss(source_name, url)
        print(f"[RSS] {source_name}: {len(entries)} entries")
        all_entries.extend(entries)

    cutoff = datetime.now(timezone.utc) - timedelta(hours=MAX_AGE_HOURS)
    recent = [e for e in all_entries if e["published"] >= cutoff]
    recent.sort(key=lambda x: x["published"], reverse=True)
    print(f"[Filter] {len(recent)} entries within {MAX_AGE_HOURS}h")

    if len(recent) < 2:
        print("[Info] Not enough recent news to form a digest. Need at least 2.")
        return

    seen_titles = set()
    unique_entries = []
    for e in recent:
        t = e["title"].lower()[:40]
        if t not in seen_titles:
            seen_titles.add(t)
            unique_entries.append(e)
    print(f"[Dedup] {len(unique_entries)} unique entries")

    batches = []
    for i in range(0, len(unique_entries), NEWS_PER_ARTICLE):
        batch = unique_entries[i:i + NEWS_PER_ARTICLE]
        if len(batch) >= 2:
            batches.append(batch)

    generated = 0
    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    for batch in batches:
        if generated >= MAX_PER_RUN:
            break
        combined_title = " ".join(e["title"][:20] for e in batch)
        base_slug = slugify(combined_title)
        expected_zh  = f"{today_str}-{base_slug}"
        if any(expected_zh in s for s in zh_slugs):
            print(f"[Skip] Similar digest exists: {base_slug}")
            continue

        sources = ", ".join(e["source"] for e in batch)
        print(f"\n[Process] Digest from: {sources}")

        try:
            result = generate_digest(batch)
        except Exception as e:
            print(f"[AI Error] {e}")
            continue

        zh_article = result.get("zh", {})
        if zh_article and zh_article.get("title") and zh_article.get("content"):
            zh_slug = slugify(zh_article["title"])
            if not zh_slug:
                zh_slug = base_slug
            save_article(ZH_DIR, zh_slug, today_str, zh_article, "zh")
            zh_slugs.add(f"{today_str}-{zh_slug}")
        else:
            print("[Skip] Chinese version missing")

        en_article = result.get("en", {})
        if en_article and en_article.get("title") and en_article.get("content"):
            en_slug = slugify(en_article["title"])
            if not en_slug:
                en_slug = base_slug
            save_article(EN_DIR, en_slug, today_str, en_article, "en")
            en_slugs.add(f"{today_str}-{en_slug}")
        else:
            print("[Skip] English version missing")

        generated += 1

    print(f"\n[Done] Generated {generated} digest(s) today.")

if __name__ == "__main__":
    main()
