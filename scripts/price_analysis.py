#!/usr/bin/env python3
"""
BTC & ETH 小时线价格技术分析
- 获取 Binance 1h K 线数据
- 计算技术指标（MA, RSI, MACD, 布林带, 成交量）
- 调用 DeepSeek API 生成专业分析报告（中文 + 英文）
- 写入 src/content/zh/analysis/ 和 src/content/en/analysis/
"""

import requests
import json
import os
import sys
from datetime import datetime, timezone
import time

# ========== 配置 ==========
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "sk-ae8905a8936b4c8fad4c1bafc4e9cf03")
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

SYMBOLS = ["BTCUSDT", "ETHUSDT"]
INTERVAL = "1h"
LOOKBACK_HOURS = 48  # 分析最近48小时

OUTPUT_DIR_ZH = "src/content/zh/analysis"
OUTPUT_DIR_EN = "src/content/en/analysis"

# ========== 技术指标计算 ==========
def calculate_ma(closes, period):
    """计算移动平均线"""
    if len(closes) < period:
        return None
    return sum(closes[-period:]) / period

def calculate_rsi(closes, period=14):
    """计算 RSI 指标"""
    if len(closes) < period + 1:
        return None
    
    gains = []
    losses = []
    
    for i in range(1, len(closes)):
        change = closes[i] - closes[i-1]
        if change > 0:
            gains.append(change)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(abs(change))
    
    if len(gains) < period:
        return None
    
    avg_gain = sum(gains[-period:]) / period
    avg_loss = sum(losses[-period:]) / period
    
    if avg_loss == 0:
        return 100
    
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return round(rsi, 2)

def calculate_macd(closes, fast=12, slow=26, signal=9):
    """计算 MACD 指标"""
    if len(closes) < slow:
        return None, None, None
    
    # 简化版 EMA 计算
    def ema(prices, period):
        multiplier = 2 / (period + 1)
        ema_val = prices[0]
        for price in prices[1:]:
            ema_val = (price - ema_val) * multiplier + ema_val
        return ema_val
    
    fast_ema = ema(closes[-fast:], fast)
    slow_ema = ema(closes[-slow:], slow)
    macd_line = fast_ema - slow_ema
    
    # 简化：用 macd_line 作为 signal 的近似
    signal_line = macd_line * 0.9  # 近似值
    histogram = macd_line - signal_line
    
    return round(macd_line, 2), round(signal_line, 2), round(histogram, 2)

def calculate_bollinger_bands(closes, period=20, std_dev=2):
    """计算布林带"""
    if len(closes) < period:
        return None, None, None
    
    recent = closes[-period:]
    middle = sum(recent) / period
    
    variance = sum((x - middle) ** 2 for x in recent) / period
    std = variance ** 0.5
    
    upper = middle + (std * std_dev)
    lower = middle - (std * std_dev)
    
    return round(upper, 2), round(middle, 2), round(lower, 2)

def calculate_volume_trend(volumes, period=24):
    """计算成交量趋势"""
    if len(volumes) < period:
        return None, None
    
    recent_vol = volumes[-period:]
    avg_vol = sum(recent_vol) / period
    current_vol = volumes[-1]
    
    vol_change = ((current_vol - avg_vol) / avg_vol) * 100
    
    return round(current_vol, 2), round(vol_change, 2)

# ========== 获取 K 线数据 ==========
def fetch_klines(symbol, interval=INTERVAL, limit=LOOKBACK_HOURS):
    """从 Binance 获取 K 线数据"""
    url = f"https://api.binance.com/api/v3/klines"
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # 解析数据
        klines = []
        for k in data:
            klines.append({
                "timestamp": k[0],
                "open": float(k[1]),
                "high": float(k[2]),
                "low": float(k[3]),
                "close": float(k[4]),
                "volume": float(k[5])
            })
        
        return klines
    
    except Exception as e:
        print(f"❌ 获取 {symbol} K 线失败: {e}")
        return None

# ========== 技术分析 ==========
def analyze_symbol(symbol):
    """对单个交易对进行技术分析"""
    print(f"\n🔍 分析 {symbol}...")
    
    klines = fetch_klines(symbol)
    if not klines:
        return None
    
    closes = [k["close"] for k in klines]
    volumes = [k["volume"] for k in klines]
    
    # 当前价格
    current_price = closes[-1]
    prev_price = closes[-2]
    price_change = ((current_price - prev_price) / prev_price) * 100
    
    # 24小时前价格
    price_24h = closes[-24] if len(closes) >= 24 else closes[0]
    price_change_24h = ((current_price - price_24h) / price_24h) * 100
    
    # 技术指标
    ma_7 = calculate_ma(closes, 7)
    ma_25 = calculate_ma(closes, 25)
    ma_50 = calculate_ma(closes, 50)
    
    rsi = calculate_rsi(closes, 14)
    
    macd, macd_signal, macd_hist = calculate_macd(closes)
    
    bb_upper, bb_middle, bb_lower = calculate_bollinger_bands(closes)
    
    current_vol, vol_change = calculate_volume_trend(volumes)
    
    # 价格区间
    high_24h = max(closes[-24:]) if len(closes) >= 24 else max(closes)
    low_24h = min(closes[-24:]) if len(closes) >= 24 else min(closes)
    
    analysis = {
        "symbol": symbol,
        "current_price": current_price,
        "price_change_1h": price_change,
        "price_change_24h": price_change_24h,
        "high_24h": high_24h,
        "low_24h": low_24h,
        "ma_7": ma_7,
        "ma_25": ma_25,
        "ma_50": ma_50,
        "rsi": rsi,
        "macd": macd,
        "macd_signal": macd_signal,
        "macd_histogram": macd_hist,
        "bb_upper": bb_upper,
        "bb_middle": bb_middle,
        "bb_lower": bb_lower,
        "volume": current_vol,
        "volume_change": vol_change
    }
    
    print(f"✅ {symbol} 分析完成")
    print(f"   当前价格: ${current_price:,.2f}")
    print(f"   24h 变化: {price_change_24h:+.2f}%")
    print(f"   RSI: {rsi}")
    print(f"   MACD: {macd}")
    
    return analysis

# ========== 生成分析报告 ==========
def generate_analysis_with_deepseek(analyses):
    """使用 DeepSeek API 生成专业分析报告"""
    print("\n🤖 调用 DeepSeek API 生成分析报告...")
    
    # 构建提示词
    prompt = f"""你是一位专业的加密货币技术分析师，拥有10年以上交易经验。请根据以下技术指标数据，生成一份专业的价格分析报告。

## 分析数据

"""
    
    for analysis in analyses:
        symbol = analysis["symbol"]
        price = analysis["current_price"]
        change_24h = analysis["price_change_24h"]
        rsi = analysis["rsi"]
        macd = analysis["macd"]
        macd_hist = analysis["macd_histogram"]
        ma_7 = analysis["ma_7"]
        ma_25 = analysis["ma_25"]
        bb_upper = analysis["bb_upper"]
        bb_lower = analysis["bb_lower"]
        vol_change = analysis["volume_change"]
        
        prompt += f"""
### {symbol} 技术指标
- 当前价格: ${price:,.2f}
- 24h 涨跌幅: {change_24h:+.2f}%
- RSI (14): {rsi}
- MACD: {macd} (Signal: {analysis['macd_signal']}, Histogram: {macd_hist})
- MA7: ${ma_7:,.2f}
- MA25: ${ma_25:,.2f}
- 布林带上轨: ${bb_upper:,.2f}
- 布林带下轨: ${bb_lower:,.2f}
- 成交量变化: {vol_change:+.2f}%
"""
    
    prompt += """
## 报告要求

请生成两份报告：中文和英文。

### 中文报告要求：
1. 标题：吸引人且专业
2. 市场概览：简要描述当前市场状态
3. 技术面分析（对每个币种）：
   - 趋势判断（多头/空头/震荡）
   - 关键支撑位和阻力位
   - RSI、MACD、布林带等技术指标解读
   - 成交量分析
4. 交易建议：基于技术分析的短期操作建议（1-4小时级别）
5. 风险提示：可能的市场风险和关键关注点
6. 字数：800-1200字

### 英文报告要求：
Same structure as Chinese, but in professional English. 800-1200 words.

## 输出格式

请以 JSON 格式输出：
```json
{
  "title_zh": "中文标题",
  "title_en": "English Title",
  "report_zh": "中文报告内容（Markdown 格式）",
  "report_en": "English report content (Markdown format)",
  "tags_zh": ["标签1", "标签2", "标签3"],
  "tags_en": ["tag1", "tag2", "tag3"],
  "importance": "high"  // high, medium, low
}
```

重要：只返回 JSON，不要有其他文字。
"""
    
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "你是一位专业的加密货币技术分析师。"},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 3000
    }
    
    try:
        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        
        result = response.json()
        content = result["choices"][0]["message"]["content"]
        
        # 提取 JSON
        if "```json" in content:
            json_str = content.split("```json")[1].split("```")[0].strip()
        else:
            json_str = content.strip()
        
        data = json.loads(json_str)
        print("✅ DeepSeek API 调用成功")
        return data
        
    except Exception as e:
        print(f"❌ DeepSeek API 调用失败: {e}")
        return None

# ========== 写入文件 ==========
def write_analysis_files(analyses, report_data):
    """写入分析报告到文件"""
    print("\n📝 写入分析报告...")
    
    # 确保目录存在
    os.makedirs(OUTPUT_DIR_ZH, exist_ok=True)
    os.makedirs(OUTPUT_DIR_EN, exist_ok=True)
    
    # 生成文件名
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d-%H-%M")
    
    # 中文报告
    title_zh = report_data.get("title_zh", f"加密货币技术分析 {timestamp}")
    slug_zh = title_zh.replace(" ", "-").replace("/", "-")[:50]
    filename_zh = f"{timestamp}-{slug_zh}.md"
    filepath_zh = os.path.join(OUTPUT_DIR_ZH, filename_zh)
    
    content_zh = f"""---
title: "{title_zh}"
date: {datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")}
type: "analysis"
tags: {json.dumps(report_data.get("tags_zh", []), ensure_ascii=False)}
importance: "{report_data.get("importance", "medium")}"
---

{report_data.get("report_zh", "")}
"""
    
    with open(filepath_zh, "w", encoding="utf-8") as f:
        f.write(content_zh)
    
    print(f"✅ 中文报告已写入: {filepath_zh}")
    
    # 英文报告
    title_en = report_data.get("title_en", f"Crypto Technical Analysis {timestamp}")
    slug_en = title_en.replace(" ", "-").replace("/", "-")[:50]
    filename_en = f"{timestamp}-{slug_en}.md"
    filepath_en = os.path.join(OUTPUT_DIR_EN, filename_en)
    
    content_en = f"""---
title: "{title_en}"
date: {datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")}
type: "analysis"
tags: {json.dumps(report_data.get("tags_en", []))}
importance: "{report_data.get("importance", "medium")}"
---

{report_data.get("report_en", "")}
"""
    
    with open(filepath_en, "w", encoding="utf-8") as f:
        f.write(content_en)
    
    print(f"✅ 英文报告已写入: {filepath_en}")
    
    return filepath_zh, filepath_en

# ========== 主函数 ==========
def main():
    print("=" * 60)
    print("🚀 开始 BTC & ETH 技术分析")
    print("=" * 60)
    
    # 1. 技术分析
    analyses = []
    for symbol in SYMBOLS:
        analysis = analyze_symbol(symbol)
        if analysis:
            analyses.append(analysis)
        time.sleep(1)  # 避免 API 限流
    
    if not analyses:
        print("❌ 没有成功分析任何交易对")
        sys.exit(1)
    
    # 2. 生成报告
    report_data = generate_analysis_with_deepseek(analyses)
    if not report_data:
        print("❌ 报告生成失败")
        sys.exit(1)
    
    # 3. 写入文件
    write_analysis_files(analyses, report_data)
    
    print("\n" + "=" * 60)
    print("✅ 技术分析完成")
    print("=" * 60)

if __name__ == "__main__":
    main()
