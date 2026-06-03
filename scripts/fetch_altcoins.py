#!/usr/bin/env python3
"""
fetch_altcoins.py
抓取主流山寨币行情数据，写入 src/data/altcoins.json
数据源：Binance Public API（无需 API Key，免费，GitHub Actions 云端可用）
用法：python scripts/fetch_altcoins.py
"""
import requests
import json
import os
from datetime import datetime, timezone

# ── 配置 ──────────────────────────────────────────────────────────
# 目标山寨币（符号 → 显示用名称）
COINS = [
    {"symbol": "SOLUSDT",  "id": "solana",      "name": "Solana"},
    {"symbol": "BNBUSDT",  "id": "binancecoin",  "name": "BNB"},
    {"symbol": "XRPUSDT",  "id": "ripple",       "name": "XRP"},
    {"symbol": "ADAUSDT",  "id": "cardano",      "name": "Cardano"},
    {"symbol": "DOGEUSDT", "id": "dogecoin",     "name": "Dogecoin"},
    {"symbol": "DOTUSDT",  "id": "polkadot",    "name": "Polkadot"},
    {"symbol": "AVAXUSDT", "id": "avalanche-2",  "name": "Avalanche"},
    {"symbol": "LINKUSDT", "id": "chainlink",     "name": "Chainlink"},
    {"symbol": "MATICUSDT","id": "polygon",      "name": "Polygon"},
]

# 脚本目录 → 项目根目录
SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
DATA_DIR     = os.path.join(PROJECT_ROOT, "src", "data")
OUT_FILE     = os.path.join(DATA_DIR, "altcoins.json")

# Binance 免费公开接口（无需 Key）
BINANCE_API = "https://api.binance.com/api/v3"


# ── 主逻辑 ──────────────────────────────────────────────────────────
def fetch_binance_ticker():
    """逐个获取 Binance 24h ticker 数据（避开 symbol 参数编码问题）"""
    results = []
    headers = {"User-Agent": "1HCryptoBot/1.0 (+https://1hcrypto.com)"}
    for coin in COINS:
        sym = coin["symbol"]
        url = f"{BINANCE_API}/ticker/24hr?symbol={sym}"
        try:
            resp = requests.get(url, headers=headers, timeout=10)
            resp.raise_for_status()
            results.append(resp.json())
        except Exception as e:
            print(f"[WARN] 获取 {sym} 失败: {e}")
    return results or None


def parse_to_coins(binance_data):
    """将 Binance 返回数据解析为统一格式"""
    # 建立 symbol → coin 信息的映射
    symbol_map = {c["symbol"]: c for c in COINS}
    result = []

    for item in binance_data:
        sym = item["symbol"]
        if sym not in symbol_map:
            continue
        info = symbol_map[sym]
        try:
            price     = float(item.get("lastPrice", 0))
            change_pct = float(item.get("priceChangePercent", 0))
            volume     = float(item.get("quoteVolume", 0))  # USDT 成交额
        except (ValueError, TypeError):
            price, change_pct, volume = 0, 0, 0

        result.append({
            "id":         info["id"],
            "symbol":     info["symbol"].replace("USDT", ""),
            "name":       info["name"],
            "price":      price,
            "change24h":  change_pct,
            "volume24h":  volume,
            "rank":       999,   # Binance 不提供排名，默认 999
        })

    # 按币种名称排序
    result.sort(key=lambda x: COINS.index(next(c for c in COINS if c["id"] == x["id"])))
    return result


def read_existing():
    """读取现有数据文件（用于保护机制）"""
    if not os.path.exists(OUT_FILE):
        return None
    try:
        with open(OUT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def write_json(data: dict):
    """写入 src/data/altcoins.json"""
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    size = os.path.getsize(OUT_FILE)
    print(f"[OK] 已写入 {OUT_FILE}  ({size:,} bytes)")


# ── 入口 ────────────────────────────────────────────────────────────
def main():
    print("── 开始抓取山寨币行情（Binance）──")
    raw = fetch_binance_ticker()
    if not raw:
        print("[WARN] API 无响应，保留现有数据，不覆盖")
        return

    coins = parse_to_coins(raw)
    if not coins:
        print("[WARN] API 返回空数据，保留现有数据，不覆盖")
        return

    output = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "coins":      coins,
    }
    write_json(output)
    print(f"[OK] 共获取 {len(coins)} 个山寨币行情")


if __name__ == "__main__":
    main()
