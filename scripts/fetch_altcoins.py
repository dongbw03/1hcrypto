#!/usr/bin/env python3
"""
fetch_altcoins.py
抓取主流山寨币行情数据，写入 src/data/altcoins.json
数据源：CoinGecko 免费 API（无需 API Key）
用法：python scripts/fetch_altcoins.py
"""
import requests
import json
import os
from datetime import datetime, timezone

# ── 配置 ──────────────────────────────────────────────────────────────
# 目标山寨币（CoinGecko ID → 显示用符号/名称）
COINS = [
    {"id": "solana",             "symbol": "SOL",  "name": "Solana"},
    {"id": "binancecoin",       "symbol": "BNB",  "name": "BNB"},
    {"id": "ripple",             "symbol": "XRP",  "name": "XRP"},
    {"id": "cardano",            "symbol": "ADA",  "name": "Cardano"},
    {"id": "dogecoin",           "symbol": "DOGE", "name": "Dogecoin"},
    {"id": "polkadot",          "symbol": "DOT",  "name": "Polkadot"},
    {"id": "avalanche-2",       "symbol": "AVAX", "name": "Avalanche"},
    {"id": "chainlink",           "symbol": "LINK", "name": "Chainlink"},
    {"id": "polygon",            "symbol": "MATIC", "name": "Polygon"},
    {"id": "uniswap",            "symbol": "UNI",  "name": "Uniswap"},
]

# 脚本目录 → 项目根目录
SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)  # scripts/ → 项目根目录
DATA_DIR     = os.path.join(PROJECT_ROOT, "src", "data")
OUT_FILE     = os.path.join(DATA_DIR, "altcoins.json")

# CoinGecko 免费接口（无需 Key，限速 ~10-50 req/min）
CG_API = "https://api.coingecko.com/api/v3"


# ── 主逻辑 ────────────────────────────────────────────────────────────
def fetch_altcoins():
    """调用 CoinGecko /coins/markets 批量获取山寨币数据"""
    ids = ",".join([c["id"] for c in COINS])
    url = (
        f"{CG_API}/coins/markets"
        f"?vs_currency=usd"
        f"&ids={ids}"
        f"&order=market_cap_desc"
        f"&per_page=20&page=1"
        f"&sparkline=false&price_change_percentage=24h"
    )
    headers = {"User-Agent": "1HCryptoBot/1.0 (+https://1hcrypto.com)"}
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        if resp.status_code == 429:
            print("[WARN] CoinGecko 限速(429)，请稍后重试")
            return None
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(f"[ERROR] 获取 CoinGecko 数据失败: {e}")
        return None


def parse_to_coins(cg_data):
    """将 CoinGecko 返回数据解析为统一格式"""
    result = []
    for item in cg_data:
        result.append({
            "id":           item.get("id", ""),
            "symbol":       item.get("symbol", "").upper(),
            "name":         item.get("name", ""),
            "price":        float(item.get("current_price") or 0),
            "change24h":    float(item.get("price_change_percentage_24h") or 0),
            "market_cap":   float(item.get("market_cap") or 0),
            "volume24h":    float(item.get("total_volume") or 0),
            "rank":         int(item.get("market_cap_rank") or 999),
        })
    # 按市值排名排序（API 已排好，保险起见再排一次）
    result.sort(key=lambda x: x["rank"])
    return result


def write_json(data: dict):
    """写入 src/data/altcoins.json"""
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    size = os.path.getsize(OUT_FILE)
    print(f"[OK] 已写入 {OUT_FILE}  ({size:,} bytes)")


# ── 入口 ────────────────────────────────────────────────────────────────
def main():
    print("── 开始抓取山寨币行情 ──")
    raw = fetch_altcoins()
    if not raw:
        # 如果 API 失败，写入空结构，页面显示"数据准备中"
        fallback = {"timestamp": datetime.now(timezone.utc).isoformat(), "coins": []}
        write_json(fallback)
        return

    coins = parse_to_coins(raw)
    output = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "coins":      coins,
    }
    write_json(output)
    print(f"[OK] 共获取 {len(coins)} 个山寨币行情")


if __name__ == "__main__":
    main()
