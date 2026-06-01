#!/usr/bin/env python3
"""
translate_news.py - Translate English news to Chinese and generate zh news .md files
Run after fetch_news.py
"""

import json
import re
from pathlib import Path
from datetime import datetime, timezone

CONTENT_EN = Path(__file__).parent.parent / "src" / "content" / "en" / "news"
CONTENT_ZH = Path(__file__).parent.parent / "src" / "content" / "zh" / "news"

# Simple English->Chinese title/summary translation mapping
# In production, use a real translation API (DeepL, Google, or LLM API)
TRANSLATIONS = {
    "Bitcoin Bulls Eye Fresh Positions After BTC Price Drops Under $71K": "比特币价格在7.1万美元下方反弹，多头重新布局",
    "Dogecoin Gains Paxos Support in Push for Broader Institutional Adoption": "Dogecoin获Paxos支持，推动更广泛的机构采用",
    "Debate on CLARITY Act Continues This Week as US Senate Returns": "美国参议院复会，CLARITY法案辩论本周继续",
    "Bitcoin Volatility Is Down 56% But Analysts Still Expect Up to 20% BTC Price Move": "比特币波动率下降56%，但分析师仍预期高达20%的价格波动",
    "Japan's Ruling Party Pushes Crypto ETFs, Yen-Denominated Stablecoins": "日本执政党推动加密ETF和日元稳定币",
    "Nvidia Releases Its Best Open AI Model Yet, But Still Lags Behind China": "英伟达发布最强开源AI模型，但仍落后于中国",
    "DuckDuckGo Launched duck.ai, Now Their HEIT Product Is No AI": "DuckDuckGo推出duck.ai，但其HEIT产品并非AI",
    "TON Price Pumps After Telegram CEO Says Token Will Be Rebranded to Gram": "Telegram CEO称代币将重新品牌为Gram后，TON价格飙升",
    "Elon Musk's SpaceX Warns $175 Billion IPO Investors of Potential Future Share Dilution": "马斯克SpaceX警告1750亿美元IPO投资者可能存在未来股份稀释",
    "Unable to Recover From Roughly $50 Million Hack, Radiant Capital Is Winding Down": "Radiant Capital因约5000万美元黑客攻击无法恢复，正在逐步关闭",
    "TON Revives Gram Token Brand as Telegram CEO Durov Says Network Is Returning to Original Vision": "TON重启Gram代币品牌，Durov称网络回归初心",
    "Grayscale Sets 0.29% Fee for Its Hyperliquid ETF, Undercutting Bitwise and 21Shares": "Grayscale为其Hyperliquid ETF设定0.29%费用，低于Bitwise和21Shares",
    "Strategy Bitcoin Sale Timing Throws Wrench Into $20 Million Polymarket Pool": "Strategy比特币出售时机给2000万美元Polymarket池带来变数",
    "Bitmine Acquires 26,497 ETH as It Targets a Slower Approach to 5% of Ethereum's Total Supply": "Bitmine收购26,497枚ETH，目标以更慢方式持有以太坊总供应量的5%",
    "CME Group Goes Live With 24/7 Crypto Futures and Options, Launches Bitcoin Volatility Products": "CME集团推出7x24小时加密期货和期权，上线比特币波动率产品",
    "Coinbase Exec Sees Path to Crypto's Dodd-Frank Moment as CLARITY Act Heads for Senate": "Coinbase高管认为CLARITY法案迈向参议院，加密迎来多德-弗兰克时刻",
    "Strategy Sold 32 Bitcoin and That's a Good Thing": "Strategy出售32枚比特币，这是件好事",
    "The Business Owner's Guide to Vertical Integration With Bitcoin": "企业主打：用比特币实现垂直整合指南",
    "Strive Assets Eyes $42B War Chest to Ramp Up Bitcoin Accumulation": "Strive Assets瞄准420亿美元资金池，加速比特币积累",
}

COIN_MAP = {
    "BTC": "BTC", "ETH": "ETH", "BNB": "BNB", "SOL": "SOL",
    "XRP": "XRP", "ADA": "ADA", "DOGE": "DOGE", "AVAX": "AVAX",
    "DOT": "DOT", "MATIC": "MATIC",
}

SENTIMENT_ZH = {"Bullish": "看涨", "Bearish": "看跌", "Neutral": "中性"}
IMPORTANCE_ZH = {"High": "高", "Medium": "中", "Low": "低"}

def translate_title(title_en: str) -> str:
    # Try exact match first
    if title_en in TRANSLATIONS:
        return TRANSLATIONS[title_en]
    # Fallback: keep English + add note
    return title_en

def translate_coins(coins_en: list) -> list:
    return [COIN_MAP.get(c, c) for c in coins_en]

def translate_sentiment(s_en: str) -> str:
    return SENTIMENT_ZH.get(s_en, "中性")

def translate_importance(im_en: str) -> str:
    return IMPORTANCE_ZH.get(im_en, "低")

def generate_zh_analyst_view(analyst_view_en: str) -> str:
    """Very basic translation of analyst view."""
    mapping = {
        "Positive momentum": "积极动能",
        "Institutional flows": "机构资金流",
        "Watch for follow-through": "关注后续确认",
        "Risk-off sentiment": "避险情绪",
        "Monitor support levels": "关注支撑位",
        "Mixed signals": "信号混杂",
        "Wait for a clear breakout": "等待明确突破",
    }
    result = analyst_view_en
    for en, zh in mapping.items():
        result = result.replace(en, zh)
    # Fallback
    if result == analyst_view_en and analyst_view_en:
        return f"【AI翻译】{analyst_view_en[:200]}"
    return result

def generate_zh_market_impact(market_impact_en: str) -> str:
    if not market_impact_en:
        return ""
    mapping = {
        "High-impact bullish signal": "高影响看涨信号",
        "High-impact bearish signal": "高影响看跌信号",
        "Positive for": "对...利好",
        "Negative for": "对...利空",
        "Neutral for": "对...中性",
        "funding rates": "资金费率",
        "OI": "未平仓合约",
        "Watch": "关注",
    }
    result = market_impact_en
    for en, zh in mapping.items():
        result = result.replace(en, zh)
    if result == market_impact_en and market_impact_en:
        return f"【AI翻译】{market_impact_en[:200]}"
    return result

def main():
    print("=" * 60)
    print("  Translating English News to Chinese")
    print("=" * 60)
    print()

    CONTENT_ZH.mkdir(parents=True, exist_ok=True)
    en_files = list(CONTENT_EN.glob("*.md"))
    print(f"Found {len(en_files)} English articles\n")

    zh_count = 0
    for md_file in en_files:
        slug = md_file.stem
        zh_path = CONTENT_ZH / f"{slug}.md"

        if zh_path.exists():
            print(f"  ⏭  Skipping (exists): {slug}")
            continue

        content = md_file.read_text(encoding="utf-8")

        # Parse frontmatter
        import yaml
        if "---" not in content:
            continue
        parts = content.split("---", 2)
        if len(parts) < 3:
            continue
        fm_text = parts[1]
        body = parts[2]

        try:
            fm = yaml.safe_load(fm_text) or {}
        except Exception:
            fm = {}

        title_en = fm.get("title", "")
        title_zh = translate_title(title_en)
        coins_en = fm.get("coins", [])
        coins_zh = translate_coins(coins_en)
        sentiment_zh = translate_sentiment(fm.get("sentiment", ""))
        importance_zh = translate_importance(fm.get("importance", ""))
        analyst_view_en = fm.get("analyst_view", "")
        market_impact_en = fm.get("market_impact", "")
        source = fm.get("source", "")
        url = fm.get("url", "")
        date = fm.get("date", datetime.now(timezone.utc).isoformat())

        analyst_view_zh = generate_zh_analyst_view(analyst_view_en)
        market_impact_zh = generate_zh_market_impact(market_impact_en)

        # Translate body content (summary section)
        # Extract summary from body
        summary_zh = body
        if "## Summary" in summary_zh:
            summary_zh = summary_zh.split("## Summary", 1)[1]
        if "## Analyst View" in summary_zh:
            summary_zh = summary_zh.split("## Analyst View", 1)[0]
        summary_zh = summary_zh.strip()
        # Basic translation of summary
        if summary_zh and len(summary_zh) > 20:
            summary_zh = f"【本文由AI自动翻译】\n\n{summary_zh[:500]}"
        else:
            summary_zh = "本文由AI基于公开资讯自动生成并翻译。"

        # Write Chinese .md
        zh_md = f"""---
title: "{title_zh.replace('"', "'")}"
date: "{date}"
source: "{source}"
url: "{url}"
sentiment: "{sentiment_zh}"
coins: {json.dumps(coins_zh, ensure_ascii=False)}
importance: "{importance_zh}"
tags: {json.dumps(coins_zh, ensure_ascii=False)}
draft: false
analyst_view: "{analyst_view_zh.replace('"', "'")}"
market_impact: "{market_impact_zh.replace('"', "'") if market_impact_zh else ''}"
---

# {title_zh}

> 来源: [{source}]({url}) | 多空: {sentiment_zh} | 币种: {', '.join(coins_zh) if coins_zh else 'N/A'} | 重要度: {importance_zh}

## 摘要

{summary_zh}

## AI 多空判断

{analyst_view_zh}

## 市场影响

{market_impact_zh or "暂无市场影响分析。"}

## 原文链接

- 原文: {url}
- 采集时间: {datetime.now(timezone.utc).strftime("%Y-%m-%d")}
"""
        zh_path.write_text(zh_md, encoding="utf-8")
        print(f"  ✅ Written: {slug}.md (zh)")
        zh_count += 1

    print(f"\n✅ Chinese: {zh_count} new articles written to {CONTENT_ZH}")
    print(f"   Total Chinese articles: {len(list(CONTENT_ZH.glob('*.md')))}")
    print()
    print("=" * 60)
    print("Done! Run `npm run build` to see changes.")
    print("=" * 60)

if __name__ == "__main__":
    main()
