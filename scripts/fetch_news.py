#!/usr/bin/env python3
# 1hcrypto 自动资讯整理脚本
# 抓取全球可访问的 RSS → DeepSeek 生成中英文摘要 → 输出到 zh/news/ 和 en/news/

import json, os, time, re
import requests
from datetime import datetime, timezone
from pathlib import Path
import xml.etree.ElementTree as ET

# ── 配置 ─────────────────────────────────────────
API_KEY  = os.environ.get("DEEPSEEK_API_KEY", "sk-ae8905a8936b4c8fad4c1bafc4e9cf03")
API_URL  = "https://api.deepseek.com/v1/chat/completions"
ZH_DIR  = Path(__file__).parent.parent / "src" / "content" / "zh" / "news"
EN_DIR  = Path(__file__).parent.parent / "src" / "content" / "en" / "news"

# 只用全球可访问的 RSS 源（GitHub Actions 能访问）
RSS_SOURCES = [
    ("CoinTelegraph", "https://cointelegraph.com/rss"),
    ("CoinDesk",     "https://www.coindesk.com/feed/"),
    ("The Block",     "https://www.theblock.co/rss.xml"),
    ("Decrypt",       "https://decrypt.co/feed/"),
    ("BitcoinMag",    "https://bitcoinmagazine.com/.rss/full/"),
]

MAX_AGE_DAYS = 3
MAX_PER_RUN  = 8   # 每次最多处理条数


# ── RSS 抓取 ─────────────────────────────────────
def fetch_rss(name, url):
    try:
        resp = requests.get(url, timeout=20, verify=False)
        resp.raise_for_status()
        root = ET.fromstring(resp.content)
    except Exception as e:
        print(f"  [WARN] {name} RSS 抓取失败: {e}")
        return []

    ns = "{http://www.w3.org/2005/Atom}"
    items = root.findall(".//item") or root.findall(f".//{ns}entry")
    articles = []
    for item in items:
        try:
            def _find(*tags):
                for t in tags:
                    el = item.find(t)
                    if el is not None and el.text and el.text.strip():
                        return el.text.strip()
                return ""
            title = _find("title", f"{ns}title")
            link_el = item.find("link") or item.find(f"{ns}link")
            link = ""
            if link_el is not None:
                link = (link_el.get("href") or link_el.text or "").strip()
            desc = _find("description", f"{ns}summary", f"{ns}content")
            pub  = _find("pubDate", "pubdate", f"{ns}published", f"{ns}updated")
            if title and link:
                articles.append({"title": title, "link": link, "desc": desc, "pub_str": pub, "source": name})
        except Exception:
            continue
    return articles


# ── 日期解析 ───────────────────────────────────
def parse_date(pub_str):
    for fmt in [
        "%a, %d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S %Z",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
    ]:
        try:
            return datetime.strptime(pub_str.strip(), fmt).replace(tzinfo=timezone.utc)
        except Exception:
            continue
    return None


# ── DeepSeek 调用 ──────────────────────────────
def call_deepseek(prompt, max_tokens=800):
    try:
        resp = requests.post(
            API_URL,
            headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
            json={"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}],
                  "max_tokens": max_tokens, "temperature": 0.3},
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"  [WARN] DeepSeek API 失败: {e}")
        return ""


def analyze_with_deepseek(title_en, desc_en):
    """用 DeepSeek 同时生成中文摘要 + 英文摘要 + 情绪分析"""
    prompt = f"""You are a crypto analyst. Analyze this news and output ONLY a JSON object (no ```json wrapper):

Title: {title_en}
Description: {desc_en}

Output JSON format:
{{"zh_summary": "Chinese summary within 100 words", "en_summary": "English summary within 100 words", "sentiment": "bullish|bearish|neutral", "coins": ["BTC"], "importance": "high|medium|low"}}"""
    raw = call_deepseek(prompt, max_tokens=600)
    try:
        cleaned = raw.strip()
        if cleaned.startswith("```"):
            idx = cleaned.find("\n")
            if idx >= 0:
                cleaned = cleaned[idx+1:]
            idx2 = cleaned.rfind("```")
            if idx2 >= 0:
                cleaned = cleaned[:idx2]
            cleaned = cleaned.strip()
        return json.loads(cleaned)
    except Exception:
        return {"zh_summary": title_en[:200], "en_summary": title_en[:200],
                "sentiment": "neutral", "coins": [], "importance": "low"}


# ── 生成 Markdown ───────────────────────────────
def make_slug(title):
    slug = re.sub(r'[^a-z0-9\u4e00-\u9fff\-]', '', title.lower().replace(' ', '-'))[:60]
    return slug.strip('-')

def generate_markdown_zh(article, analysis, date_str, slug):
    sentiment_map = {"bullish": "看涨", "bearish": "看跌", "neutral": "中性"}
    sentiment_cn = sentiment_map.get(analysis.get("sentiment", "neutral"), "中性")
    coins = analysis.get("coins", [])
    coins_str = ", ".join(coins) if coins else "无"
    importance_map = {"high": "高", "medium": "中", "low": "低"}
    importance_cn = importance_map.get(analysis.get("importance", "low"), "低")

    safe_title = article["title"].replace('"', "'")
    frontmatter = f"""---
title: "{safe_title}"
date: {date_str}
source: "{article['source']}"
url: "{article['link']}"
sentiment: "{sentiment_cn}"
coins: {json.dumps(coins, ensure_ascii=False)}
importance: "{importance_cn}"
tags: {json.dumps(coins[:3], ensure_ascii=False)}
draft: false
---

# {article['title']}

> 来源：[{article['source']}]({article['link']}) | 情绪：{sentiment_cn} | 影响币种：{coins_str} | 重要度：{importance_cn}

## 摘要（中文）

{analysis.get('zh_summary', '')}

## 原文链接

- 原文：{article['link']}
- 采集时间：{date_str[:10]}
"""
    return frontmatter


def generate_markdown_en(article, analysis, date_str, slug):
    sentiment_map = {"bullish": "Bullish", "bearish": "Bearish", "neutral": "Neutral"}
    sentiment_en = sentiment_map.get(analysis.get("sentiment", "neutral"), "Neutral")
    coins = analysis.get("coins", [])

    safe_title = article["title"].replace('"', "'")
    frontmatter = f"""---
title: "{safe_title}"
date: {date_str}
source: "{article['source']}"
url: "{article['link']}"
sentiment: "{sentiment_en}"
coins: {json.dumps(coins, ensure_ascii=False)}
importance: "{analysis.get('importance', 'low')}"
tags: {json.dumps(coins[:3], ensure_ascii=False)}
draft: false
---

# {article['title']}

> Source：[{article['source']}]({article['link']}) | Sentiment：{sentiment_en} | Coins：{', '.join(coins) if coins else 'N/A'}

## Summary

{analysis.get('en_summary', article.get('desc', '')[:300])}

## Original Link

- Original：{article['link']}
- Fetched：{date_str[:10]}
"""
    return frontmatter


def already_exists(dir_path, slug):
    if not dir_path.exists():
        return False
    for f in dir_path.iterdir():
        if f.stem.startswith(slug[:40]):
            return True
    return False


# ── 主流程 ─────────────────────────────────────
def main():
    print("=" * 50)
    print("[INFO] 1hcrypto 自动资讯开始运行")
    print("=" * 50)

    ZH_DIR.mkdir(parents=True, exist_ok=True)
    EN_DIR.mkdir(parents=True, exist_ok=True)

    # 1. 抓取所有 RSS
    all_articles = []
    for name, url in RSS_SOURCES:
        print(f"\n[INFO] 抓取 {name} ...")
        arts = fetch_rss(name, url)
        print(f"  → 获取 {len(arts)} 条")
        all_articles.extend(arts)
        time.sleep(1)

    # 2. 去重（标题前 50 字符）
    seen = set()
    unique = []
    for a in all_articles:
        key = a["title"][:50].lower()
        if key not in seen:
            seen.add(key)
            unique.append(a)
    print(f"\n[INFO] 去重后共 {len(unique)} 条")

    # 3. 过滤：最近 N 天 + 未生成过
    cutoff = time.time() - MAX_AGE_DAYS * 86400
    to_process = []
    for a in unique:
        pd = parse_date(a.get("pub_str", ""))
        if pd and pd.timestamp() < cutoff:
            continue
        slug = make_slug(a["title"])
        if already_exists(ZH_DIR, slug) and already_exists(EN_DIR, slug):
            print(f"  [SKIP] 已存在：{a['title'][:40]}")
            continue
        to_process.append(a)

    print(f"[INFO] 需要处理 {len(to_process)} 条新资讯（限制 {MAX_PER_RUN} 条）\n")

    # 4. 逐条分析 + 写文件
    count_zh = 0
    count_en = 0
    for a in to_process[:MAX_PER_RUN]:
        print(f"  [处理中] {a['title'][:50]} ...")
        analysis = analyze_with_deepseek(a["title"], a.get("desc", ""))

        now = datetime.now(timezone.utc)
        date_str = now.strftime("%Y-%m-%dT%H:%M:%S+08:00")
        slug = make_slug(a["title"])
        base_name = now.strftime("%Y-%m-%d-") + slug[:40]
        safe_name = re.sub(r'[\\/*?:"<>|]', '', base_name) + ".md"

        # 写中文版
        if not already_exists(ZH_DIR, slug):
            md_zh = generate_markdown_zh(a, analysis, date_str, slug)
            (ZH_DIR / safe_name).write_text(md_zh, encoding="utf-8")
            print(f"  → 写入中文：{safe_name}")
            count_zh += 1

        # 写英文版
        if not already_exists(EN_DIR, slug):
            md_en = generate_markdown_en(a, analysis, date_str, slug)
            (EN_DIR / safe_name).write_text(md_en, encoding="utf-8")
            print(f"  → 写入英文：{safe_name}")
            count_en += 1

        time.sleep(2)   # 避免触发 DeepSeek 速率限制

    print(f"\n{'=' * 50}")
    print(f"[INFO] 完成！中文 {count_zh} 篇，英文 {count_en} 篇")
    print(f"{'=' * 50}\n")

if __name__ == "__main__":
    main()
