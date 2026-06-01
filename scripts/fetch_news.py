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

# ── 配置 ───────────────────────────────────────
API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
API_URL = "https://api.deepseek.com/v1/chat/completions"
ZH_DIR = Path(__file__).parent.parent / "src" / "content" / "zh" / "news"
EN_DIR = Path(__file__).parent.parent / "src" / "content" / "en" / "news"

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; 1hcrypto-bot/4.0)"}

RSS_SOURCES = [
    ("CoinTelegraph", "https://cointelegraph.com/rss"),
    ("CoinDesk",     "https://www.coindesk.com/arc/outboundfeeds/rss/"),
    ("The Block",     "https://www.theblock.co/rss.xml"),
    ("Decrypt",       "https://decrypt.co/feed/"),
    ("BitcoinMag",    "https://bitcoinmagazine.com/.rss/full/"),
]

MAX_PER_RUN = 2      # 每天最多生成 2 篇聚合快讯
MAX_AGE_HOURS = 36   # 只取 36 小时内的新闻
NEWS_PER_ARTICLE = 3 # 每篇快讯聚合 3 条新闻
DAYS_BACK = 2

# ── 工具函数 ───────────────────────────────────

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
        name = f.stem
        try:
            date_str = name[:10]
            file_mtime = datetime.fromtimestamp(f.stat().st_mtime, tz=timezone.utc)
            if file_mtime >= cutoff:
                slugs.add(name)
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
            title = (item.findtext("title") or "").strip()
            link = (item.findtext("link") or "").strip()
            desc = (item.findtext("description") or "").strip()
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
    except Exception as e:
        print(f"[RSS Error] {source_name}: {e}")
    return entries

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
                        {"role": "system", "content": "You are a professional crypto market analyst. Always respond with valid JSON only."},
                        {"role": "user", "content": prompt},
                    ],
                    "temperature": 0.7,
                    "max_tokens": 3000,
                },
                timeout=90,
            )
            resp.raise_for_status()
            data = resp.json()
            content = data["choices"][0]["message"]["content"]
            content = re.sub(r'^```json\s*', '', content)
            content = re.sub(r'\s*```$', '', content)
            return json.loads(content)
        except Exception as e:
            print(f"[DeepSeek retry {attempt+1}/{max_retries}] {e}")
            time.sleep(2 ** attempt)
    raise RuntimeError("DeepSeek API failed after retries")

def generate_digest(entries: list) -> dict:
    """聚合多条新闻生成一篇综合快讯"""
    news_block = ""
    for i, e in enumerate(entries, 1):
        news_block += f"""
新闻 {i}：
标题：{e['title']}
来源：{e['source']}
摘要：{e['description']}
"""

    prompt = f"""你是一位专业的加密市场分析师。请根据以下 {len(entries)} 条新闻，整理成一篇综合快讯。

{news_block}

要求（请严格遵守）：
1. 标题简洁有力，15-25字，概括核心要点。标题中保留关键词如 BTC、ETH、ETF、SEC、监管、美联储等，便于搜索引擎收录
2. 正文用简短的段落分别概括每条新闻的核心信息，每条配一个二级标题（##）
3. 每条新闻后简要说明其市场影响（1-2句话）
4. 最后给出整体市场情绪判断（看涨/看跌/中性）及综合理由
5. 绝对不要在正文中输出原文链接、URL、来源网址
6. 绝对不要在正文中输出采集时间、采集日期等元信息
7. 绝对不要出现"原文"、"来源"、"采集"、"出处"、"链接"等字样
8. 正文中不要出现 "news 1"、"news 2" 等英文编号
9. 内容全部用中文
10. 正文总字数 400-700 字
11. 正文中保留重要的搜索关键词：具体币种名称（BTC、ETH、SOL 等）、机构名称（BlackRock、灰度、SEC 等）、数据指标（ETF 流入流出金额、资金费率、清算量等），这些关键词有利于 SEO

同时生成英文版本，要求相同，但内容全部用英文，情绪用 Bullish/Bearish/Neutral。

Output ONLY valid JSON in this exact format:
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
        sentiment = article.get("sentiment", "中性")
        title = article.get("title", "无标题")
        content = article.get("content", "")
        market_impact = article.get("market_impact", "")
    else:
        sentiment = article.get("sentiment", "Neutral")
        title = article.get("title", "Untitled")
        content = article.get("content", "")
        market_impact = article.get("market_impact", "")

    # 检测相关币种
    coin_pattern = re.compile(r'\b(BTC|ETH|SOL|XRP|ADA|DOGE|AVAX|LINK|UNI|AAVE|SUI|DOT|MATIC|ARB|OP|LTC|BCH|ETF)\b', re.I)
    coins = list(set(coin_pattern.findall(content)))
    coins = [c.upper() for c in coins]
    if not coins:
        coins = ["BTC"]

    # 确定重要度
    importance = "高" if lang == "zh" else "High"
    lower_content = content.lower()
    if any(k in lower_content for k in ["etf", "sec", "监管", "regulation", "批准", "approval", "暴跌", "crash", "大涨", "surge"]):
        pass
    else:
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

# ── 主流程 ─────────────────────────────────────

def main():
    print("=" * 50)
    print(f"1H Crypto News Digest - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 50)

    if not API_KEY:
        print("[Error] DEEPSEEK_API_KEY not set. Exiting.")
        return

    # 获取已有文章（去重）
    zh_slugs = get_recent_slugs(ZH_DIR)
    en_slugs = get_recent_slugs(EN_DIR)
    print(f"[Deduplicate] Recent ZH: {len(zh_slugs)}, EN: {len(en_slugs)}")

    # 抓取所有 RSS
    all_entries = []
    for source_name, url in RSS_SOURCES:
        entries = fetch_rss(source_name, url)
        print(f"[RSS] {source_name}: {len(entries)} entries")
        all_entries.extend(entries)

    # 过滤：36 小时内，按时间排序
    cutoff = datetime.now(timezone.utc) - timedelta(hours=MAX_AGE_HOURS)
    recent = [e for e in all_entries if e["published"] >= cutoff]
    recent.sort(key=lambda x: x["published"], reverse=True)
    print(f"[Filter] {len(recent)} entries within {MAX_AGE_HOURS}h")

    if len(recent) < 2:
        print("[Info] Not enough recent news to form a digest. Need at least 2.")
        return

    # 去重并聚合成组
    generated = 0
    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # 按原始标题去重
    seen_titles = set()
    unique_entries = []
    for e in recent:
        t = e["title"].lower()[:40]
        if t not in seen_titles:
            seen_titles.add(t)
            unique_entries.append(e)

    print(f"[Deduplicate] {len(unique_entries)} unique entries")

    # 每 NEWS_PER_ARTICLE 条聚合成一组
    batches = []
    for i in range(0, len(unique_entries), NEWS_PER_ARTICLE):
        batch = unique_entries[i:i + NEWS_PER_ARTICLE]
        if len(batch) >= 2:
            batches.append(batch)

    for batch in batches:
        if generated >= MAX_PER_RUN:
            break

        # 用所有新闻标题拼接做 slug 去重检查
        combined_title = " ".join(e["title"][:20] for e in batch)
        base_slug = slugify(combined_title)
        expected_file = f"{today_str}-{base_slug}"

        if any(expected_file in s for s in zh_slugs):
            print(f"[Skip] Similar digest exists: {base_slug}")
            continue

        sources = ", ".join(e["source"] for e in batch)
        print(f"\n[Process] Digest from: {sources}")

        try:
            result = generate_digest(batch)
        except Exception as e:
            print(f"[AI Error] {e}")
            continue

        # 保存中文版本
        zh_article = result.get("zh", {})
        if zh_article and zh_article.get("title") and zh_article.get("content"):
            zh_slug = slugify(zh_article["title"])
            if not zh_slug:
                zh_slug = base_slug
            save_article(ZH_DIR, zh_slug, today_str, zh_article, "zh")
        else:
            print("[Skip] Chinese version missing")

        # 保存英文版本
        en_article = result.get("en", {})
        if en_article and en_article.get("title") and en_article.get("content"):
            en_slug = slugify(en_article["title"])
            if not en_slug:
                en_slug = base_slug
            save_article(EN_DIR, en_slug, today_str, en_article, "en")
        else:
            print("[Skip] English version missing")

        generated += 1

    print(f"\n[Done] Generated {generated} digest(s) today.")

if __name__ == "__main__":
    main()
