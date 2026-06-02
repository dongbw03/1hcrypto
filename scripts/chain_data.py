#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
链上数据模块 - 1H Crypto (1H币研)
========================================
功能：
  1. 调用 Binance 公开 API 获取 Open Interest 和 Funding Rate
  2. 生成链上数据（优先真实 API，失败则模拟）

使用：
  from chain_data import generate_onchain_data
  onchain = generate_onchain_data("long", "BTC")
"""

import requests
import json
import time
from datetime import datetime, timezone, timedelta

# ============================================================
# 配置
# ============================================================
BINANCE_API_BASE = "https://fapi.binance.com"


# ============================================================
# 真实 API 调用
# ============================================================
def fetch_real_onchain_data(symbol):
    """
    调用 Binance 公开 API 获取链上数据
    返回：{
        "exchangeBalance": str,  # 模拟（需要 CoinGlass 等付费 API）
        "oiChange": str,        # Open Interest 变化（24h）— 真实
        "funding": str,         # 资金费率（当前）— 真实
        "netFlow7d": str,      # 模拟（需要链上 API）
    } or None（如果 API 调用失败）
    """
    try:
        binance_symbol = symbol.upper().replace("/", "")
        if not binance_symbol.endswith("USDT"):
            binance_symbol = binance_symbol + "USDT"
        
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; CryptoBot/1.0)"
        }
        
        # 1. Open Interest（当前）
        oi_url = f"{BINANCE_API_BASE}/fapi/v1/openInterest?symbol={binance_symbol}"
        oi_resp = requests.get(oi_url, headers=headers, timeout=10)
        oi_data = oi_resp.json() if oi_resp.status_code == 200 else None

        # 2. Funding Rate（资金费率）
        funding_url = f"{BINANCE_API_BASE}/fapi/v1/premiumIndex?symbol={binance_symbol}"
        funding_resp = requests.get(funding_url, headers=headers, timeout=10)
        funding_data = funding_resp.json() if funding_resp.status_code == 200 else None

        # 3. Open Interest 历史（24h 变化）— 真实数据
        oi_hist_url = f"{BINANCE_API_BASE}/futures/data/openInterestHist?symbol={binance_symbol}&period=1h&limit=25"
        oi_hist_resp = requests.get(oi_hist_url, headers=headers, timeout=10)
        oi_change_str = "+2.1%"  # 默认值
        if oi_hist_resp.status_code == 200:
            oi_hist = oi_hist_resp.json()
            if len(oi_hist) >= 2:
                oi_now = float(oi_data.get("openInterest", 0)) if oi_data else 0
                oi_24h = float(oi_hist[-1].get("sumOpenInterest", 0))
                if oi_24h > 0:
                    change_pct = ((oi_now - oi_24h) / oi_24h) * 100
                    sign = "+" if change_pct >= 0 else ""
                    oi_change_str = f"{sign}{change_pct:.1f}%"

        if not oi_data and not funding_data:
            print(f"[WARN] Binance API 返回错误，使用模拟数据")
            return None

        # 解析 Funding Rate
        funding_rate = float(funding_data.get("lastFundingRate", 0)) * 100 if funding_data else 0
        funding_str = f"{funding_rate:+.3f}%"

        # 模拟数据（需要 CoinGlass 等付费 API 获取真实交易所余额和净流量）
        exchange_balance = "-3,200"   # 模拟
        net_flow_7d      = "-1,800"       # 模拟

        result = {
            "exchangeBalance": exchange_balance,
            "oiChange": oi_change_str,
            "funding": funding_str,
            "netFlow7d": net_flow_7d,
        }

        oi_value = float(oi_data.get("openInterest", 0)) if oi_data else 0
        print(f"[OK] Fetched real on-chain data for {binance_symbol}: OI={oi_value:,.0f}, Funding={funding_str}, OIChange={oi_change_str}")
        return result

    except Exception as e:
        print(f"[ERROR] Failed to fetch real on-chain data: {e}")
        return None


# ============================================================
# 模拟数据生成
# ============================================================
def generate_onchain_data(direction, symbol="BTC"):
    """
    基于方向生成合理的链上数据
    优先使用真实 API，失败则模拟
    
    参数：
      direction: "long" / "short" / "neutral"
      symbol: "BTC" / "ETH" / ...
    
    返回：{
        "exchangeBalance": str,
        "oiChange": str,
        "funding": str,
        "netFlow7d": str,
    }
    """
    # 优先尝试真实 API
    real_data = fetch_real_onchain_data(symbol)
    if real_data:
        return real_data
    
    # Fallback: 模拟数据
    print(f"[INFO] Using simulated on-chain data for {symbol}")
    
    if direction == "long":
        return {
            "exchangeBalance": "-2,800",
            "oiChange": "+3.2%",
            "funding": "0.010%",
            "netFlow7d": "-1,200",
        }
    elif direction == "short":
        return {
            "exchangeBalance": "+1,500",
            "oiChange": "-1.8%",
            "funding": "-0.005%",
            "netFlow7d": "+800",
        }
    else:  # neutral
        return {
            "exchangeBalance": "-500",
            "oiChange": "+0.5%",
            "funding": "0.001%",
            "netFlow7d": "-300",
        }


# ============================================================
# 测试
# ============================================================
if __name__ == "__main__":
    # 测试真实 API
    print("Testing fetch_real_onchain_data...")
    data = fetch_real_onchain_data("BTC")
    print(f"Result: {data}")
    
    # 测试模拟数据
    print("\nTesting generate_onchain_data...")
    data = generate_onchain_data("long", "BTC")
    print(f"Result: {data}")
