#!/usr/bin/env python3
# 1hcrypto 自动资讯整理脚本
# 中文源 → src/content/zh/news/   英文源 → src/content/en/news/

import json, os, time, re
import requests
from datetime import datetime, timezone
from pathlib import Path
import xml.etree.ElementTree as ET

# ── 配置 ─
API_KEY  = os.environ.get("DEEPSEEK_API_KEY", "sk-ae8905a8936b4c8fad4c1bafc4e9cf03")
API_URL  = "https://api.deepseek.com/v1/chat/completions"
TIMEOUT  = 20

ZH_DIR = Path(__file__).parent.parent / "src" / "content" / "zh" / "news"
EN_DIR = Path(__file__).parent.parent / "src" / "content" / "en" / "news"

ZH_SOURCES = [
    ("金色财经", "https://www.jinse.cn/feed"),
    ("币世界",   "https://www.bishijie.com/rss"),
    ("8BTC",     "https://www.8btc.com/feed"),
]
EN_SOURCES = [
    ("CoinDesk",    "https://www.coindesk.com/arc/outboundfeeds/rss/"),
    ("CoinTelegraph", "https://cointelegraph.com/rss"),
    ("The Block",     "https://www.theblock.co/rss.xml"),
]

MAX_AGE_DAYS = 3
MAX_PER_RUN   = 5   # 每次最多处理条数


# ── RSS 抓取（用 requests，SSL 更稳） ─
def fetch_rss(url):
    try:
        resp = requests.get(url, timeout=TIMEOUT, verify=False)
        resp.raise_for_status()
        root = ET.fromstring(resp.content)
    except Exception as e:
        print(f"  [WARN] RSS 抓取失败 {url}: {e}")
        return []

    articles = []
    ns = "{http://www.w3.org/2005/Atom}"
    items = root.findall(".//item") or root.findall(f".//{ns}entry")
    for item in items:
        try:
            def _find(*tags):
                for t in tags:
                    el = item.find(t)
                    if el is not None and el.text:
                        return el.text.strip()
                return ""
            title = _find("title", f"{ns}title")
            link_el = item.find("link") or item.find(f"{ns}link")
            link    = (link_el.get("href") or link_el.text or "").strip() if link_el is not None else ""
            desc    = _find("description", f"{ns}summary")
            pub     = _find("pubDate", "pubdate", f"{ns}published", f"{ns}updated")
            if title and link:
                articles.append({"title": title, "link": link, "desc": desc, "pub_str": pub})
        except Exception:
            continue
    return articles


# ── 日期解析 ─
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


# ── DeepSeek 调用 ─
def call_deepseek(prompt, max_tokens=500):
    try:
        resp = requests.post(
            API_URL,
            json={
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": max_tokens,
                "temperature": 0.3,
            },
            headers={"Authorization": "Bearer " + API_KEY, "Content-Type": "application/json"},
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"  [WARN] DeepSeek API 失败: {e}")
        return ""


# ── 单篇分析 ─
def analyze_article(title, desc, lang="zh"):
    if lang == "zh":
        prompt = (
            "你是加密货币分析师。请分析以下新闻，直接输出纯 JSON（不要 ```json 包裹）：\n"
            f"标题：{title}\n摘要：{desc}\n\n"
            '输出格式：{"summary": "100字内中文摘要", "sentiment": "bullish/bearish/neutral", '
            '"coins": ["BTC"], "importance": "high/medium/low"}'
        )
    else:
        prompt = (
            "You are a crypto analyst. Analyze the news and output pure JSON only (no ```json):\n"
            f"Title: {title}\nSummary: {desc}\n\n"
            'Output: {"summary": "100-word English summary", "sentiment": "bullish/bearish/neutral", '
            '"coins": ["BTC"], "importance": "high/medium/low"}'
        )
    raw = call_deepseek(prompt)
    try:
        cleaned = raw.strip()
        if cleaned.startswith("```"):
            cleaned = cleaned.split("\n", 1)[1].rsplit("```", 1)[0].strip()
        return json.loads(cleaned)
    except Exception:
        return {"summary": raw[:200] or title, "sentiment": "neutral", "coins": [], "importance": "low"}


# ── 生成 Markdown ─
def generate_markdown(article, analysis, source_name, lang="zh"):
    now = datetime.now(timezone.utc)
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%Y-%m-%dT%H:%M:%S+08:00")

    smap = {"bullish": "看涨" if lang == "zh" else "Bullish",
             "bearish": "看跌" if lang == "zh" else "Bearish",
             "neutral": "中性" if lang == "zh" else "Neutral"}
    sentiment = smap.get(analysis.get("sentiment", "neutral"), smap["neutral"])

    coins = analysis.get("coins", [])
    coins_str = ", ".join(coins) if coins else ("无" if lang == "zh" else "N/A")
    imap = {"high": "高" if lang == "zh" else "High",
             "medium": "中" if lang == "zh" else "Medium",
             "low": "低" if lang == "zh" else "Low"}
    importance = imap.get(analysis.get("importance", "low"), imap["low"])

    safe_title = article["title"].replace('"', "'")
    coins_yaml = "[" + ", ".join('"' + c + '"' for c in coins) + "]" if coins else "[]"
    tags_yaml  = "[" + ", ".join('"' + c + '"' for c in coins[:3]) + "]" if coins[:3] else "[]"

    slug = re.sub(r"[^a-z0-9\u4e00-\u9fff\-]", "", article["title"].lower().replace(" ", "-")[:60])

    lines = []
    lines.append("---")
    lines.append(f'title: "{safe_title}"')
    lines.append(f"date: {time_str}")
    lines.append(f'source: "{source_name}"')
    lines.append(f'url: "{article["link"]}"')
    lines.append(f'sentiment: "{sentiment}"')
    lines.append(f"coins: {coins_yaml}")
    lines.append(f'importance: "{importance}"')
    lines.append(f"tags: {tags_yaml}")
    lines.append("draft: false")
    lines.append("---\n")
    lines.append(f"# {article['title']}\n")
    lines.append(f"> 来源：[{source_name}]({article['link']}) | 情绪：{sentiment} | 影响币种：{coins_str} | 重要度：{importance}\n")
    lines.append("## 摘要\n")
    lines.append(analysis.get("summary", article.get("desc", "")[:300]) + "\n")
    lines.append("## 原文链接\n")
    lines.append(f"- 原文：{article['link']}")
    lines.append(f"- 采集时间：{date_str}\n")

    return "\n".join(lines), slug


# ── 去重检查 ─
def already_exists(slug, directory):
    if not directory.exists():
        return False
    for f in directory.iterdir():
        if f.stem.startswith(slug[:40]):
            return True
    return False


# ── 处理一组源 ─
def process_sources(sources, lang, directory):
    print(f"[INFO] 处理 {lang.upper()} 源，目标目录：{directory}")
    directory.mkdir(parents=True, exist_ok=True)

    all_articles = []
    for name, url in sources:
        print(f"  [抓取] {name} ...")
        items = fetch_rss(url)
        print(f"    → 获取 {len(items)} 条")
        for a in items[:12]:
            a["source"] = name
            all_articles.append(a)
        time.sleep(1)

    # 去重
    seen = set()
    unique = []
    for a in all_articles:
        k = a["title"][:60].lower()
        if k not in seen:
            seen.add(k)
            unique.append(a)

    # 过滤已存在 + 时间
    cutoff = time.time() - MAX_AGE_DAYS * 86400
    to_process = []
    for a in unique:
        if already_exists(re.sub(r"[^a-z0-9\-]", "", a["title"].lower().replace(" ", "-")[:50]), directory):
            print(f"  [SKIP] 已存在：{a['title'][:40]}")
            continue
        pd = parse_date(a.get("pub_str", ""))
        if pd and pd.timestamp() < cutoff:
            continue
        to_process.append(a)

    print(f"[INFO] {lang.upper()} 需处理 {min(len(to_process), MAX_PER_RUN)} 条（限制 {MAX_PER_RUN} 条）")

    count = 0
    for a in to_process[:MAX_PER_RUN]:
        print(f"  [分析] {a['title'][:50]} ...")
        analysis = analyze_article(a["title"], a.get("desc", ""), lang=lang)
        md_content, slug = generate_markdown(a, analysis, a["source"], lang=lang)

        base_name = datetime.now().strftime("%Y-%m-%d") + "-" + slug[:40]
        safe_name = re.sub(r'[\\/*?:"<>|]', "", base_name) + ".md"
        filepath = directory / safe_name
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"  → 已写入 {safe_name}")
        count += 1
        time.sleep(2)

    print(f"[INFO] {lang.upper()} 完成！写入 {count} 篇 → {directory}\n")
    return count


# ── 主流程 ─
def main():
    print("=" * 50)
    print("[INFO] 1hcrypto 自动资讯开始运行")
    print("=" * 50)
    t0 = time.time()

    n_zh = process_sources(ZH_SOURCES, "zh", ZH_DIR)
    n_en = process_sources(EN_SOURCES, "en", EN_DIR)

    elapsed = int(time.time() - t0)
    print("=" * 50)
    print(f"[INFO] 全部完成！中文 {n_zh} 篇，英文 {n_en} 篇，耗时 {elapsed}s")
    print("=" * 50)


if __name__ == "__main__":
    main()
