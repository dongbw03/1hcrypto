#!/usr/bin/env python3
"""
generate_analysis.py
独立脚本：获取K线 → 调用 DeepSeek API → 输出 latest-analysis.json
供 generate_daily.py 和 auto_trade.py 读取
"""

import json
import os
import sys
import requests
from datetime import datetime, timezone, timedelta

# ============================================================
# 配置
# ============================================================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
SRC_ROOT = os.path.join(PROJECT_ROOT, "src")
DATA_DIR = os.path.join(SRC_ROOT, "data")
LATEST_JSON = os.path.join(DATA_DIR, "latest-analysis.json")

# DeepSeek API 配置
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "sk-ae8905a8936b4c8fad4c1bafc4e9cf03")

# ============================================================
# 工具函数
# ============================================================
def fetch_binance_klines(symbol="BTCUSDT", interval="1h", limit=100):
    """获取 Binance K线数据（公开API，无需密钥）"""
    try:
        url = f"https://api.binance.com/api/v3/klines"
        params = {
            "symbol": symbol,
            "interval": interval,
            "limit": limit
        }
        headers = {"User-Agent": "Mozilla/5.0 (compatible; CryptoBot/1.0)"}
        resp = requests.get(url, params=params, headers=headers, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(f"[WARN] Binance K线获取失败: {e}")
        return None

def fetch_coingecko_price():
    """获取 CoinGecko BTC 价格"""
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": "bitcoin,ethereum",
            "vs_currencies": "usd",
            "include_24hr_change": "true"
        }
        resp = requests.get(url, params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(f"[WARN] CoinGecko 获取失败: {e}")
        return None

def call_deepseek_for_analysis(klines, pair="BTC/USDT"):
    """
    调用 DeepSeek API 基于K线数据生成分析结论
    返回 dict 或 None
    """
    if not DEEPSEEK_API_KEY:
        print("[WARN] DEEPSSEEK_API_KEY 未设置")
        return None
    
    # 格式化 K 线数据（最近24小时）
    recent_klines = klines[-24:] if len(klines) > 24 else klines
    formatted = []
    for k in recent_klines:
        # k: [开盘时间, 开盘价, 最高价, 最低价, 收盘价, 成交量, ...]
        ts = int(k[0]) / 1000
        dt = datetime.fromtimestamp(ts).strftime('%m-%d %H:%M')
        formatted.append(f"[{dt}] O:{float(k[1]):.2f} H:{float(k[2]):.2f} L:{float(k[3]):.2f} C:{float(k[4]):.2f} V:{float(k[5]):.2f}")
    
    kline_text = "\n".join(formatted)
    current_price = float(klines[-1][4]) if klines else 68000.0
    
    prompt = f"""你是专业的加密货币价格行为分析师，精通 Al Brooks 价格行为学。

请分析以下 {pair} 的小时级K线数据，并给出交易建议。

K线数据（最近24小时）：
{kline_text}

当前价格：${current_price:,.2f}

请按以下 JSON 格式返回分析结果：
{{
  "direction": "long" | "short" | "neutral",
  "entry": {current_price * 0.995:.2f},
  "stop": {current_price * 0.985:.2f},
  "tp1": {current_price * 1.01:.2f},
  "tp2": {current_price * 1.025:.2f},
  "pivot": {current_price:.2f},
  "support": [{current_price * 0.99:.2f}, {current_price * 0.98:.2f}],
  "resistance": [{current_price * 1.01:.2f}, {current_price * 1.02:.2f}],
  "coreThesis": "核心分析结论（中文，100字以内）",
  "marketStructure": "市场结构描述（中文，100字以内）"
}}

要求：
1. direction 必须是 "long", "short", 或 "neutral" 之一
2. entry, stop, tp1, tp2, pivot 必须是合理的价格点位（基于 K 线数据）
3. support 和 resistance 必须是数组，包含2个价格点位
4. coreThesis 和 marketStructure 必须是中文
5. 返回纯 JSON，不要包含 markdown 代码块标记
"""
    
    try:
        headers = {
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "你是专业的加密货币价格行为分析师，精通 Al Brooks 价格行为学。你必须只返回纯 JSON 格式，不要包含任何 markdown 标记或额外文本。"},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.3,
            "max_tokens": 1000,
            "response_format": {"type": "json_object"}
        }
        
        print(f"[INFO] 调用 DeepSeek API...")
        resp = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload, timeout=60)
        resp.raise_for_status()
        content = resp.json()["choices"][0]["message"]["content"]
        
        # 解析 JSON
        result = json.loads(content)
        
        # 验证必需字段
        required_fields = ["direction", "entry", "stop", "tp1", "tp2", "pivot", "support", "resistance", "coreThesis", "marketStructure"]
        for field in required_fields:
            if field not in result:
                print(f"[WARN] DeepSeek 返回缺少字段: {field}")
                return None
        
        result["latestClose"] = current_price
        print(f"[OK] DeepSeek 分析完成: {result['direction']} @ {result['entry']}")
        return result
        
    except json.JSONDecodeError as e:
        print(f"[WARN] DeepSeek 返回不是有效 JSON: {e}")
        return None
    except Exception as e:
        print(f"[WARN] DeepSeek API 失败: {e}")
        return None

def fallback_analysis(pair="BTC"):
    """生成本地模拟分析（DeepSeek 失败时使用）"""
    import random
    direction = random.choice(["long", "short", "neutral"])
    
    # 获取当前价格（用于生成合理点位）
    cg_data = fetch_coingecko_price()
    if cg_data:
        if pair.upper() == "BTC":
            price = cg_data.get("bitcoin", {}).get("usd", 68000)
        else:
            price = cg_data.get("ethereum", {}).get("usd", 3500)
    else:
        price = 68000.0 if pair.upper() == "BTC" else 3500.0
    
    return {
        "direction": direction,
        "entry": price * 0.995,
        "stop": price * 0.985,
        "tp1": price * 1.01,
        "tp2": price * 1.025,
        "pivot": price,
        "support": [price * 0.99, price * 0.98],
        "resistance": [price * 1.01, price * 1.02],
        "coreThesis": f"{pair} 当前报价 ${price:,.2f}。等待市场数据接入后更新完整分析。",
        "marketStructure": f"CoinGecko 实时价格：${price:,.2f}。24h 变化：数据获取中。",
        "latestClose": price
    }

# ============================================================
# 主函数
# ============================================================
def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="生成每日研判分析")
    parser.add_argument("--pair", default="BTC/USDT", help="交易对（默认 BTC/USDT）")
    parser.add_argument("--skip-api", action="store_true", help="跳过 API 调用（使用模拟数据）")
    parser.add_argument("--output", default=LATEST_JSON, help="输出文件路径")
    args = parser.parse_args()
    
    date_str = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d")
    print(f"[INFO] 生成每日研判 for {date_str}...")
    
    analysis_btc = None
    analysis_eth = None
    
    if not args.skip_api:
        # 1. 获取 BTC K线
        print(f"[INFO] 获取 {args.pair} K线数据...")
        klines_btc = fetch_binance_klines(symbol="BTCUSDT", interval="1h", limit=100)
        
        if klines_btc:
            print(f"[OK] 获取到 {len(klines_btc)} 根K线")
            
            # 2. 调用 DeepSeek API
            analysis_btc = call_deepseek_for_analysis(klines_btc, args.pair)
        
        # 3. 如果 DeepSeek 失败，使用本地分析
        if analysis_btc is None:
            print("[WARN] DeepSeek API 失败，使用本地分析...")
            analysis_btc = fallback_analysis("BTC")
        
        # 4. 获取 CoinGecko 价格（用于展示）
        cg_data = fetch_coingecko_price()
        if cg_data:
            btc_price = cg_data.get("bitcoin", {}).get("usd", 0)
            eth_price = cg_data.get("ethereum", {}).get("usd", 0)
            print(f"[OK] BTC 价格: ${btc_price:,.2f}")
            print(f"[OK] ETH 价格: ${eth_price:,.2f}")
            
            # 更新分析中的价格
            analysis_btc["latestClose"] = btc_price
            
            # 为 ETH 生成分析（简化版）
            analysis_eth = fallback_analysis("ETH")
            analysis_eth["latestClose"] = eth_price
        else:
            analysis_eth = fallback_analysis("ETH")
    else:
        print("[INFO] 跳过 API 调用（--skip-api）")
        analysis_btc = fallback_analysis("BTC")
        analysis_eth = fallback_analysis("ETH")
    
    # 5. 输出 latest-analysis.json
    latest_analysis = {
        "date": date_str,
        "btc": {
            "direction": analysis_btc["direction"],
            "entry": analysis_btc["entry"],
            "stop": analysis_btc["stop"],
            "tp1": analysis_btc["tp1"],
            "tp2": analysis_btc["tp2"],
            "pivot": analysis_btc["pivot"],
            "support": analysis_btc["support"],
            "resistance": analysis_btc["resistance"],
            "coreThesis": analysis_btc["coreThesis"],
            "marketStructure": analysis_btc["marketStructure"],
            "latestClose": analysis_btc["latestClose"]
        },
        "eth": {
            "direction": analysis_eth["direction"],
            "entry": analysis_eth["entry"],
            "stop": analysis_eth["stop"],
            "tp1": analysis_eth["tp1"],
            "tp2": analysis_eth["tp2"],
            "pivot": analysis_eth["pivot"],
            "support": analysis_eth["support"],
            "resistance": analysis_eth["resistance"],
            "coreThesis": analysis_eth["coreThesis"],
            "marketStructure": analysis_eth["marketStructure"],
            "latestClose": analysis_eth["latestClose"]
        }
    }
    
    # 确保输出目录存在
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(latest_analysis, f, ensure_ascii=False, indent=2)
    
    print(f"\n[OK] 分析已生成: {args.output}")
    print(f"  BTC: {latest_analysis['btc']['direction']} @ {latest_analysis['btc']['entry']:,.2f}")
    print(f"  ETH: {latest_analysis['eth']['direction']} @ {latest_analysis['eth']['entry']:,.2f}")

if __name__ == "__main__":
    main()
