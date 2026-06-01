#!/usr/bin/env python3
"""
fetch_news.py - Fetch real crypto news and generate markdown files
Sources: CoinDesk RSS, Cointelegraph RSS, Decrypt RSS, The Block RSS
"""

import os
import json
import hashlib
from datetime import datetime, timezone, timedelta
import feedparser
import requests
from pathlib import Path
import re

# ── Config ──────────────────────────────────────────────────
CONTENT_EN = Path(__file__).parent.parent / "src" / "content" / "en" / "news"
CONTENT_ZH = Path(__file__).parent.parent / "src" / "content" / "zh" / "news"
MAX_ARTICLES_PER_SOURCE = 5
HOURS_AGO = 48  # Only fetch articles from last 48 hours

# ── RSS Sources ─────────────────────────────────────────────
RSS_SOURCES = [
    ("CoinDesk",    "https://www.coindesk.com/arc/outboundfeeds/rss/"),
    ("Cointelegraph", "https://cointelegraph.com/rss"),
    ("Decrypt",      "https://decrypt.co/feed"),
    ("The Block",     "https://www.theblock.co/rss.xml"),
    ("Bitcoin Magazine", "https://bitcoinmagazine.com/feed"),
]

# ── Coin tickers for coin tag extraction ───────────────────
COIN_PATTERNS = {
    "BTC":  [r"\bbitcoin\b", r"\bbtc\b"],
    "ETH":  [r"\bethereum\b", r"\beth\b"],
    "BNB":  [r"\bbnb\b", r"\bbinance coin\b"],
    "SOL":  [r"\bsolana\b", r"\bsol\b"],
    "XRP":  [r"\bxrp\b", r"\bripple\b"],
    "ADA":  [r"\bcardano\b", r"\bada\b"],
    "DOGE": [r"\bdogecoin\b", r"\bdoge\b"],
    "AVAX": [r"\bavalanche\b", r"\bavax\b"],
    "DOT":  [r"\bpolkadot\b", r"\bdot\b"],
    "MATIC":[r"\bmatic\b", r"\bpolygon\b"],
}

def slugify(title: str) -> str:
    s = title.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[-\s]+", "-", s)
    return s.strip("-")[:80]

def extract_coins(text: str):
    found = set()
    for coin, patterns in COIN_PATTERNS.items():
        for pat in patterns:
            if re.search(pat, text, re.IGNORECASE):
                found.add(coin)
                break
    return sorted(found)

def simple_sentiment(title: str, summary: str) -> str:
    """Basic keyword-based sentiment analysis."""
    text = (title + " " + summary).lower()
    bullish_words = [
        "surge", "rally", "jump", "gain", "bull", "bullish", "soar",
        "record", "high", "adoption", "buy", "accumulate", "institution",
        "etf inflow", "approval", "partnership", "launch", "upgrade",
        "突破", "上涨", "牛市", "增持", "机构",
    ]
    bearish_words = [
        "crash", "plunge", "sell", "bear", "bearish", "drop", "fall",
        "ban", "crackdown", "fine", "sec", "lawsuit", "hack", "exploit",
        "liquidate", "default", "下跌", "熊市", "暴跌", "冻结",
    ]
    bull_score = sum(w in text for w in bullish_words)
    bear_score = sum(w in text for w in bearish_words)
    if bull_score > bear_score + 1:
        return "Bullish"
    elif bear_score > bull_score + 1:
        return "Bearish"
    return "Neutral"

def importance_level(title: str, source: str) -> str:
    """Determine article importance."""
    title_lower = title.lower()
    high_keywords = ["etf", "sec", "fed", "rate", "binance", "coinbase", "bitcoin etf",
                     "regulation", "ban", "approval", "etf inflow", "etf outflow"]
    medium_keywords = ["launch", "partnership", "upgrade", "halving", "fork", "listing"]
    if any(k in title_lower for k in high_keywords):
        return "High"
    if any(k in title_lower for k in medium_keywords):
        return "Medium"
    return "Low"

def fetch_article_summary(url: str, max_len: int = 800) -> str:
    """Try to fetch article summary via requests."""
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        if resp.status_code == 200:
            text = resp.text[:max_len].replace("\n", " ").strip()
            return text
    except Exception:
        pass
    return ""

def generate_analyst_view(title: str, sentiment: str, coins: list) -> str:
    """Generate a brief analyst view based on sentiment and coins."""
    coin_str = ", ".join(coins) if coins else "the market"
    if sentiment == "Bullish":
        return (f"Positive momentum for {coin_str}. "
                "Institutional flows and on-chain metrics suggest continued interest. "
                "Watch for follow-through in the next 4-12H K-line.")
    elif sentiment == "Bearish":
        return (f"Risk-off sentiment for {coin_str}. "
                "Monitor support levels and funding rates. "
                "Al Brooks traders: look for price action confirmation before shorting.")
    return (f"Mixed signals for {coin_str}. "
            "Wait for a clear breakout or breakdown before taking position. "
            "Watch volume and order book depth.")

def generate_market_impact(sentiment: str, importance: str, coins: list) -> str:
    if not coins:
        return "Broad market sentiment shift possible. Monitor BTC dominance and total market cap."
    coin = coins[0]
    if sentiment == "Bullish" and importance == "High":
        return (f"High-impact bullish signal for {coin}. "
                "Expect increased volatility. Check funding rates and OI on Binance Futures.")
    if sentiment == "Bearish" and importance == "High":
        return (f"High-impact bearish signal for {coin}. "
                "Watch for liquidations cascades. Check derivatives data at /derivatives.")
    if sentiment == "Bullish":
        return f"Positive for {coin}. Monitor spot buying pressure and exchange netflows."
    if sentiment == "Bearish":
        return f"Negative for {coin}. Watch support levels and on-chain movement."
    return f"Neutral for {coin}. Wait for clearer directional signal."

def already_exists(slug: str, content_dir: Path) -> bool:
    return (content_dir / f"{slug}.md").exists()

def fetch_all_news():
    cutoff = datetime.now(timezone.utc) - timedelta(hours=HOURS_AGO)
    all_articles = []

    for source_name, rss_url in RSS_SOURCES:
        print(f"  Fetching {source_name}...")
        try:
            feed = feedparser.parse(rss_url)
            count = 0
            for entry in feed.entries:
                if count >= MAX_ARTICLES_PER_SOURCE:
                    break
                title = entry.get("title", "Untitled")
                link  = entry.get("link", "")
                published_str = entry.get("published", "")
                summary = ""
                if "summary" in entry:
                    summary = re.sub(r"<[^>]+>", "", entry.summary)[:500]
                elif "description" in entry:
                    summary = re.sub(r"<[^>]+>", "", entry.description)[:500]

                # Parse date
                pub_date = None
                for date_key in ["published_parsed", "updated_parsed"]:
                    if hasattr(entry, date_key) and getattr(entry, date_key):
                        try:
                            import time
                            pub_date = datetime.fromtimestamp(
                                time.mktime(getattr(entry, date_key)), tz=timezone.utc
                            )
                            break
                        except Exception:
                            pass
                if pub_date is None:
                    pub_date = datetime.now(timezone.utc)
                if pub_date < cutoff:
                    continue

                coins = extract_coins(title + " " + summary)
                sentiment = simple_sentiment(title, summary)
                importance = importance_level(title, source_name)
                analyst_view = generate_analyst_view(title, sentiment, coins)
                market_impact = generate_market_impact(sentiment, importance, coins)

                slug = slugify(title)
                # Ensure unique slug
                if not slug:
                    slug = hashlib.md5(link.encode()).hexdigest()[:12]
                slug = slug[:80]

                all_articles.append({
                    "slug": slug,
                    "title": title,
                    "date": pub_date.strftime("%Y-%m-%dT%H:%M:%S+08:00"),
                    "source": source_name,
                    "url": link,
                    "sentiment": sentiment,
                    "coins": coins,
                    "importance": importance,
                    "analyst_view": analyst_view,
                    "market_impact": market_impact,
                    "summary": summary,
                    "lang": "en",
                })
                count += 1
        except Exception as e:
            print(f"    ❌ Error fetching {source_name}: {e}")

    return all_articles

def write_md(article: dict, content_dir: Path):
    slug = article["slug"]
    if already_exists(slug, content_dir):
        print(f"  ⏭  Skipping (exists): {slug}")
        return False

    # Build markdown content
    md = f"""---
title: "{article['title'].replace('"', "'")}"
date: "{article['date']}"
source: "{article['source']}"
url: "{article['url']}"
sentiment: "{article['sentiment']}"
coins: {json.dumps(article['coins'], ensure_ascii=False)}
importance: "{article['importance']}"
tags: {json.dumps(article['coins'], ensure_ascii=False)}
draft: false
analyst_view: "{article['analyst_view'].replace('"', "'")}"
market_impact: "{article['market_impact'].replace('"', "'")}"
---

# {article['title']}

> Source: [{article['source']}]({article['url']}) | Sentiment: {article['sentiment']} | Coins: {', '.join(article['coins']) if article['coins'] else 'N/A'} | Importance: {article['importance']}

## Summary

{article['summary'] or 'No summary available.'}

## Analyst View

{article['analyst_view']}

## Market Impact

{article['market_impact']}

## Original Link

- Original: {article['url']}
- Collected: {datetime.now(timezone.utc).strftime("%Y-%m-%d")}
"""
    out_path = content_dir / f"{slug}.md"
    out_path.write_text(md, encoding="utf-8")
    print(f"  ✅ Written: {slug}.md")
    return True

def main():
    print("=" * 60)
    print("  Crypto News Fetcher")
    print("=" * 60)
    print()

    # Ensure directories exist
    CONTENT_EN.mkdir(parents=True, exist_ok=True)
    CONTENT_ZH.mkdir(parents=True, exist_ok=True)

    print(f"Fetching news from last {HOURS_AGO} hours...")
    articles = fetch_all_news()
    print(f"\n✅ Fetched {len(articles)} articles\n")

    if not articles:
        print("⚠️  No new articles found. Try increasing HOURS_AGO.")
        return

    # De-duplicate by slug
    seen_slugs = set()
    unique_articles = []
    for a in articles:
        if a["slug"] not in seen_slugs:
            seen_slugs.add(a["slug"])
            unique_articles.append(a)

    print(f"After de-duplication: {len(unique_articles)} articles\n")

    # Write English articles
    print("─" * 60)
    print("Writing English articles...")
    print("─" * 60)
    en_count = 0
    for article in unique_articles:
        if write_md(article, CONTENT_EN):
            en_count += 1

    print(f"\n✅ English: {en_count} new articles written to {CONTENT_EN}")
    print(f"   Total English articles: {len(list(CONTENT_EN.glob('*.md')))}")

    # Also create Chinese versions (same content, with Chinese translation of key fields)
    # For now, copy English articles to Chinese dir with Chinese frontmatter fields
    print(f"\n✅ Total: {en_count} new articles")
    print()
    print("=" * 60)
    print("Done! Run `npm run build` to see changes.")
    print("=" * 60)

if __name__ == "__main__":
    main()
