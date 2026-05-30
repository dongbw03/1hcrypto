#!/usr/bin/env python3
"""
Binance Futures 衍生品数据抓取（免费 API，无需 API Key）
数据包括：资金费率、未平仓合约、多空账户比、大户持仓比、主动买卖量比
"""

import requests
import json
import os
import time
from datetime import datetime, timezone

# ========== 配置 ==========
SYMBOLS = ["BTCUSDT", "ETHUSDT"]
OUTPUT_FILE = "src/data/derivatives.json"
BASE_URL = "https://fapi.binance.com"

# ========== 工具函数 ==========
def ts_to_iso(ts):
    return datetime.fromtimestamp(ts / 1000, tz=timezone.utc).isoformat()

# ========== 1. 资金费率 ==========
def fetch_funding_rate(symbol, limit=24):
    url = f"{BASE_URL}/fapi/v1/fundingRate"
    params = {"symbol": symbol, "limit": limit}
    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
        result = []
        for item in data:
            result.append({
                "timestamp": item["fundingTime"],
                "rate": float(item["fundingRate"]) * 100,
                "datetime": ts_to_iso(item["fundingTime"])
            })
        return result
    except Exception as e:
        print(f"  ❌ 资金费率失败: {e}")
        return []

# ========== 2. 未平仓合约（当前） ==========
def fetch_open_interest(symbol):
    url = f"{BASE_URL}/fapi/v1/openInterest"
    params = {"symbol": symbol}
    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
        return {
            "open_interest": float(data["openInterest"]),
            "timestamp": data["time"],
            "datetime": ts_to_iso(data["time"])
        }
    except Exception as e:
        print(f"  ❌ 未平仓合约失败: {e}")
        return None

# ========== 3. 多空账户比 ==========
def fetch_long_short_ratio(symbol, period="1h", limit=24):
    url = f"{BASE_URL}/futures/data/globalLongShortAccountRatio"
    params = {"symbol": symbol, "period": period, "limit": limit}
    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
        result = []
        for item in data:
            result.append({
                "timestamp": item["timestamp"],
                "long_ratio": float(item["longAccount"]),
                "short_ratio": float(item["shortAccount"]),
                "datetime": ts_to_iso(item["timestamp"])
            })
        return result
    except Exception as e:
        print(f"  ❌ 多空账户比失败: {e}")
        return []

# ========== 4. 大户持仓比 ==========
def fetch_top_trader_ls_ratio(symbol, period="1h", limit=24):
    url = f"{BASE_URL}/futures/data/topLongShortPositionRatio"
    params = {"symbol": symbol, "period": period, "limit": limit}
    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
        result = []
        for item in data:
            result.append({
                "timestamp": item["timestamp"],
                "long_ratio": float(item["longAccount"]),
                "short_ratio": float(item["shortAccount"]),
                "datetime": ts_to_iso(item["timestamp"])
            })
        return result
    except Exception as e:
        print(f"  ❌ 大户持仓比失败: {e}")
        return []

# ========== 5. 主动买卖量比 ==========
def fetch_taker_longshort_ratio(symbol, period="1h", limit=24):
    """Binance 实际端点: /futures/data/takerlongshortRatio"""
    url = f"{BASE_URL}/futures/data/takerlongshortRatio"
    params = {"symbol": symbol, "period": period, "limit": limit}
    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
        result = []
        for item in data:
            # 实际返回字段: buySellRatio (字符串), sellVol, buyVol
            ratio = float(item["buySellRatio"])
            result.append({
                "timestamp": item["timestamp"],
                "buy_sell_ratio": ratio,
                "buy_vol": float(item["buyVol"]),
                "sell_vol": float(item["sellVol"]),
                "datetime": ts_to_iso(item["timestamp"])
            })
        return result
    except Exception as e:
        print(f"  ❌ 主动买卖量比失败: {e}")
        return []

# ========== 情绪分析 ==========
def analyze_sentiment(symbol_data):
    signals = []
    sentiment = "neutral"

    # 分析资金费率
    if "funding_rate" in symbol_data and symbol_data["funding_rate"]:
        rates = [x["rate"] for x in symbol_data["funding_rate"][-3:]]
        avg_rate = sum(rates) / len(rates)
        if avg_rate > 0.01:
            signals.append(f"资金费率偏高({avg_rate:.4f}%)，市场看涨情绪强烈")
            sentiment = "bullish"
        elif avg_rate < -0.01:
            signals.append(f"资金费率为负({avg_rate:.4f}%)，市场看跌情绪较强")
            sentiment = "bearish"
        else:
            signals.append(f"资金费率中性({avg_rate:.4f}%)")

    # 分析多空比
    if "long_short_ratio" in symbol_data and symbol_data["long_short_ratio"]:
        latest = symbol_data["long_short_ratio"][-1]
        long_r = latest["long_ratio"]
        short_r = latest["short_ratio"]
        if long_r > 0.6:
            signals.append(f"多头账户占比{long_r*100:.1f}%，市场过度看涨，警惕反转")
            if sentiment == "neutral":
                sentiment = "contrarian_bearish"
        elif short_r > 0.6:
            signals.append(f"空头账户占比{short_r*100:.1f}%，市场过度看跌，可能反弹")
            if sentiment == "neutral":
                sentiment = "contrarian_bullish"

    return {"sentiment": sentiment, "signals": signals}

# ========== 主流程 ==========
def fetch_all():
    print("=" * 60)
    print("📊 获取 Binance Futures 衍生品数据")
    print("=" * 60)

    result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "symbols": {}
    }

    for symbol in SYMBOLS:
        print(f"\n🔍 处理 {symbol}...")

        sd = {}

        # 1. 资金费率
        print("  ⏳ 资金费率...", end=" ", flush=True)
        fr = fetch_funding_rate(symbol)
        if fr:
            sd["funding_rate"] = fr
            print(f"✅ 最新 {fr[-1]['rate']:.4f}%")
        else:
            print("❌")
        time.sleep(0.3)

        # 2. 未平仓合约
        print("  ⏳ 未平仓合约...", end=" ", flush=True)
        oi = fetch_open_interest(symbol)
        if oi:
            sd["open_interest"] = oi
            unit = "BTC" if "BTC" in symbol else "ETH"
            print(f"✅ {oi['open_interest']:,.0f} {unit}")
        else:
            print("❌")
        time.sleep(0.3)

        # 3. 多空账户比
        print("  ⏳ 多空账户比...", end=" ", flush=True)
        ls = fetch_long_short_ratio(symbol)
        if ls:
            sd["long_short_ratio"] = ls
            l = ls[-1]
            print(f"✅ 多{l['long_ratio']*100:.1f}% / 空{l['short_ratio']*100:.1f}%")
        else:
            print("❌")
        time.sleep(0.3)

        # 4. 大户持仓比
        print("  ⏳ 大户持仓比...", end=" ", flush=True)
        ts = fetch_top_trader_ls_ratio(symbol)
        if ts:
            sd["top_trader_ls_ratio"] = ts
            l = ts[-1]
            print(f"✅ 多{l['long_ratio']*100:.1f}% / 空{l['short_ratio']*100:.1f}%")
        else:
            print("❌")
        time.sleep(0.3)

        # 5. 主动买卖量比
        print("  ⏳ 主动买卖量比...", end=" ", flush=True)
        tls = fetch_taker_longshort_ratio(symbol)
        if tls:
            sd["taker_longshort_ratio"] = tls
            l = tls[-1]
            print(f"✅ 买量比{l['buy_sell_ratio']*100:.1f}%")
        else:
            print("❌")
        time.sleep(0.3)

        # 6. 情绪分析
        analysis = analyze_sentiment(sd)
        sd["sentiment_analysis"] = analysis

        result["symbols"][symbol] = sd
        time.sleep(0.5)

    print(f"\n{'=' * 60}")
    print("✅ 衍生品数据获取完成")
    print(f"{'=' * 60}\n")
    return result

def save(data):
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ 数据已保存: {OUTPUT_FILE}")

def main():
    data = fetch_all()
    save(data)

    # 打印摘要
    print("📊 数据摘要:")
    for sym, sd in data["symbols"].items():
        print(f"\n  {sym}:")
        if "funding_rate" in sd and sd["funding_rate"]:
            print(f"    - 资金费率: {sd['funding_rate'][-1]['rate']:.4f}%")
        if "open_interest" in sd:
            print(f"    - 未平仓: {sd['open_interest']['open_interest']:,.0f}")
        if "sentiment_analysis" in sd:
            s = sd["sentiment_analysis"]
            print(f"    - 情绪: {s['sentiment']}")
            for sig in s["signals"]:
                print(f"    - 💡 {sig}")

if __name__ == "__main__":
    main()
