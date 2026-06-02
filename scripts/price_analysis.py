#!/usr/bin/env python3
"""
BTC & ETH 价格行为学分析（基于 Al Brooks 方法）
- 读取模拟盘数据（trades.json）
- 基于价格行为学进行分析（趋势线、支撑/阻力、价格行为信号）
- 调用 DeepSeek API 生成专业分析报告（中文 + 英文）
- 脚本自己生成交易复盘（避免 AI 编造数据）
- 写入 src/content/zh/analysis/ 和 src/content/en/analysis/
"""

import requests
import json
import os
import sys
from datetime import datetime, timezone
import time

# ========== 配置 ==========
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

SYMBOLS = ["BTCUSDT", "ETHUSDT"]
INTERVAL = "1h"
LOOKBACK_HOURS = 48  # 分析最近48小时

OUTPUT_DIR_ZH = "src/content/zh/analysis"
OUTPUT_DIR_EN = "src/content/en/analysis"
TRADES_FILE = "src/data/trades.json"

# ========== Al Brooks 价格行为学分析 ==========
def find_swing_highs_lows(klines, n=5):
    """找出摆动高点（Swing High）和摆动低点（Swing Low）
    Al Brooks: 价格行为学中的关键支撑/阻力位
    """
    swing_highs = []
    swing_lows = []
    
    for i in range(n, len(klines) - n):
        # 摆动高点：中间K线的高点 > 前后n根K线的高点
        if all(klines[i]["high"] > klines[j]["high"] for j in range(i-n, i+n+1) if j != i):
            swing_highs.append({"index": i, "price": klines[i]["high"], "timestamp": klines[i]["timestamp"]})
        
        # 摆动低点：中间K线的低点 < 前后n根K线的低点
        if all(klines[i]["low"] < klines[j]["low"] for j in range(i-n, i+n+1) if j != i):
            swing_lows.append({"index": i, "price": klines[i]["low"], "timestamp": klines[i]["timestamp"]})
    
    return swing_highs, swing_lows

def identify_trend(klines):
    """识别趋势（Al Brooks 方法）
    返回: "uptrend", "downtrend", "trading_range"
    """
    if len(klines) < 20:
        return "unknown"
    
    # 计算最近20根K线的摆动高点和低点
    swing_highs, swing_lows = find_swing_highs_lows(klines, n=3)
    
    if len(swing_highs) < 2 or len(swing_lows) < 2:
        return "trading_range"
    
    # 上升趋势：摆动高点越来越高，摆动低点越来越高
    recent_highs = [h["price"] for h in swing_highs[-3:]]
    recent_lows = [l["price"] for l in swing_lows[-3:]]
    
    highs_rising = all(recent_highs[i] < recent_highs[i+1] for i in range(len(recent_highs)-1))
    lows_rising = all(recent_lows[i] < recent_lows[i+1] for i in range(len(recent_lows)-1))
    
    highs_falling = all(recent_highs[i] > recent_highs[i+1] for i in range(len(recent_highs)-1))
    lows_falling = all(recent_lows[i] > recent_lows[i+1] for i in range(len(recent_lows)-1))
    
    if highs_rising and lows_rising:
        return "uptrend"
    elif highs_falling and lows_falling:
        return "downtrend"
    else:
        return "trading_range"

def find_price_action_signals(klines):
    """识别价格行为信号（Al Brooks 方法）
    - Pin Bar (锤子线/上吊线)
    - Inside Bar (内包线)
    - Engulfing (吞没形态)
    - Fakey (假突破)
    """
    signals = []
    
    for i in range(1, len(klines)):
        current = klines[i]
        prev = klines[i-1]
        
        # 计算实体和影线
        curr_body = abs(current["close"] - current["open"])
        curr_range = current["high"] - current["low"]
        curr_upper_shadow = current["high"] - max(current["open"], current["close"])
        curr_lower_shadow = min(current["open"], current["close"]) - current["low"]
        
        # Pin Bar (锤子线/上吊线)
        if curr_range > 0:
            if curr_lower_shadow > (curr_range * 0.6) and curr_upper_shadow < (curr_range * 0.2):
                # 锤子线（看涨）
                if current["close"] > current["open"]:
                    signals.append({
                        "index": i,
                        "type": "pin_bar_bullish",
                        "price": current["close"],
                        "timestamp": current["timestamp"],
                        "description": "看涨锤子线"
                    })
            elif curr_upper_shadow > (curr_range * 0.6) and curr_lower_shadow < (curr_range * 0.2):
                # 上吊线（看跌）
                if current["close"] < current["open"]:
                    signals.append({
                        "index": i,
                        "type": "pin_bar_bearish",
                        "price": current["close"],
                        "timestamp": current["timestamp"],
                        "description": "看跌上吊线"
                    })
        
        # Inside Bar (内包线)
        if current["high"] < prev["high"] and current["low"] > prev["low"]:
            signals.append({
                "index": i,
                "type": "inside_bar",
                "price": current["close"],
                "timestamp": current["timestamp"],
                "description": "内包线（突破信号）"
            })
        
        # Engulfing (吞没形态)
        if (current["open"] < prev["close"] and current["close"] > prev["open"] and
            prev["close"] < prev["open"]):
            # 看涨吞没
            signals.append({
                "index": i,
                "type": "engulfing_bullish",
                "price": current["close"],
                "timestamp": current["timestamp"],
                "description": "看涨吞没形态"
            })
        elif (current["open"] > prev["close"] and current["close"] < prev["open"] and
              prev["close"] > prev["open"]):
            # 看跌吞没
            signals.append({
                "index": i,
                "type": "engulfing_bearish",
                "price": current["close"],
                "timestamp": current["timestamp"],
                "description": "看跌吞没形态"
            })
    
    return signals

def calculate_support_resistance(klines):
    """计算支撑位和阻力位（Al Brooks 方法）
    基于摆动高点和摆动低点
    """
    swing_highs, swing_lows = find_swing_highs_lows(klines, n=3)
    
    # 阻力位：最近的摆动高点
    resistance = [h["price"] for h in swing_highs[-3:]] if swing_highs else []
    
    # 支撑位：最近的摆动低点
    support = [l["price"] for l in swing_lows[-3:]] if swing_lows else []
    
    # 当前价格
    current_price = klines[-1]["close"]
    
    # 找出最接近的支撑位和阻力位
    nearest_resistance = min(resistance, key=lambda x: abs(x - current_price)) if resistance else None
    nearest_support = min(support, key=lambda x: abs(x - current_price)) if support else None
    
    return {
        "resistance": resistance,
        "support": support,
        "nearest_resistance": nearest_resistance,
        "nearest_support": nearest_support
    }

def analyze_symbol_al_brooks(symbol):
    """对单个交易对进行 Al Brooks 价格行为学分析"""
    print(f"\n🔍 分析 {symbol} (Al Brooks 价格行为学)...")
    
    klines = fetch_klines(symbol)
    if not klines:
        return None
    
    # 1. 识别趋势
    trend = identify_trend(klines)
    
    # 2. 找出支撑/阻力位
    sr_levels = calculate_support_resistance(klines)
    
    # 3. 识别价格行为信号
    signals = find_price_action_signals(klines)
    recent_signals = [s for s in signals if s["index"] >= len(klines) - 10]  # 最近10根K线
    
    # 4. 当前价格信息
    current_price = klines[-1]["close"]
    prev_price = klines[-2]["close"]
    price_change_1h = ((current_price - prev_price) / prev_price) * 100
    
    high_24h = max(k["high"] for k in klines[-24:])
    low_24h = min(k["low"] for k in klines[-24:])
    
    # 5. 市场结构分析
    swing_highs, swing_lows = find_swing_highs_lows(klines, n=3)
    
    analysis = {
        "symbol": symbol,
        "current_price": current_price,
        "price_change_1h": price_change_1h,
        "high_24h": high_24h,
        "low_24h": low_24h,
        "trend": trend,
        "support_levels": sr_levels["support"],
        "resistance_levels": sr_levels["resistance"],
        "nearest_support": sr_levels["nearest_support"],
        "nearest_resistance": sr_levels["nearest_resistance"],
        "recent_signals": recent_signals,
        "swing_highs": swing_highs[-3:] if swing_highs else [],
        "swing_lows": swing_lows[-3:] if swing_lows else [],
        "all_signals": signals[-10:]  # 最近10个信号
    }
    
    print(f"✅ {symbol} 分析完成")
    print(f"   当前价格: ${current_price:,.2f}")
    print(f"   趋势: {trend}")
    print(f"   最近信号: {len(recent_signals)} 个")
    if sr_levels["nearest_support"]:
        print(f"   最近支撑: ${sr_levels['nearest_support']:,.2f}")
    if sr_levels["nearest_resistance"]:
        print(f"   最近阻力: ${sr_levels['nearest_resistance']:,.2f}")
    
    return analysis

# ========== 获取 K 线数据 ==========
def fetch_klines(symbol, interval=INTERVAL, limit=LOOKBACK_HOURS):
    """从 Binance 获取 K 线数据"""
    url = f"https://data-api.binance.vision/api/v3/klines"
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

# ========== 读取模拟盘数据 ==========
def load_trades():
    """读取模拟盘数据，支持列表和字典两种格式"""
    try:
        with open(TRADES_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            # 支持两种格式：列表 或 {"trades": [...]}
            if isinstance(data, list):
                return data
            elif isinstance(data, dict) and "trades" in data:
                return data["trades"]
            else:
                return []
    except Exception as e:
        print(f"⚠️  读取模拟盘数据失败: {e}")
        return []

def calculate_trades_pnl(klines, trades):
    """计算模拟盘盈亏
    根据实际交易记录和当前价格计算浮盈浮亏
    """
    if not trades:
        return None
    
    current_price = klines[-1]["close"] if klines else 0
    
    total_pnl = 0
    open_positions = []
    closed_trades = []
    
    for trade in trades:
        if trade.get("status") == "open":
            # 计算浮盈浮亏
            entry = trade.get("entryPrice", 0)
            if not entry:
                continue
            
            direction = trade.get("direction", "")
            if "long" in direction:
                pnl = (current_price - entry) / entry * 100
                pnl_usdt = (current_price - entry) * (100000 / entry)  # 假设10倍杠杆，10万USDT
            else:  # short
                pnl = (entry - current_price) / entry * 100
                pnl_usdt = (entry - current_price) * (100000 / entry)
            
            open_positions.append({
                "id": trade.get("id", "N/A"),
                "symbol": trade.get("pair", "N/A"),
                "direction": direction,
                "entry": entry,
                "current_price": current_price,
                "pnl_percent": pnl,
                "pnl_usdt": pnl_usdt,
                "stop": trade.get("stopLoss"),
                "target": trade.get("takeProfit"),
                "reason": trade.get("reason", "")
            })
            
            total_pnl += pnl_usdt
            
        elif trade.get("status") in ["hit_target", "hit_stop", "closed"]:
            closed_trades.append(trade)
    
    return {
        "total_pnl": total_pnl,
        "open_positions": open_positions,
        "closed_trades": closed_trades,
        "current_price": current_price
    }

# ========== 生成分析报告（Al Brooks 方法）==========
def generate_market_analysis_with_deepseek(analyses):
    """使用 DeepSeek API 生成基于 Al Brooks 价格行为学的市场分析
    ⚠️ 重要：只传入市场数据，不传入模拟盘数据（避免 AI 编造）
    """
    print("\n🤖 调用 DeepSeek API 生成市场分析（Al Brooks 价格行为学）...")
    
    # 构建提示词（只包含市场分析，不包含模拟盘数据）
    prompt = f"""你是一位专业的加密货币交易员，精通 Al Brooks 价格行为学（Price Action）。请根据以下分析数据，生成一份专业的市场分析报告（不包含交易复盘部分）。

## 分析方法：Al Brooks 价格行为学

Al Brooks 价格行为学的核心原则：
1. **趋势识别**：通过摆动高点（Swing High）和摆动低点（Swing Low）识别趋势
2. **支撑/阻力**：基于价格行为的关键位，而非指标
3. **价格行为信号**：Pin Bar, Inside Bar, Engulfing, Fakey
4. **市场结构**：Break of Structure (BoS), Change of Character (ChoCH)
5. **交易管理**：基于价格行为的止损和止盈，而非固定点数

## 分析数据

"""
    
    for analysis in analyses:
        symbol = analysis["symbol"]
        current_price = analysis["current_price"]
        trend = analysis["trend"]
        support = analysis["support_levels"]
        resistance = analysis["resistance_levels"]
        recent_signals = analysis["recent_signals"]
        
        prompt += f"""
### {symbol} 价格行为学分析
- **当前价格**: ${current_price:,.2f}
- **趋势 (Al Brooks 方法)**: {trend}
- **支撑位**: {', '.join([f'${x:,.2f}' for x in support]) if support else '无'}
- **阻力位**: {', '.join([f'${x:,.2f}' for x in resistance]) if resistance else '无'}
- **最近价格行为信号**:
"""
        for signal in recent_signals:
            prompt += f"  - {signal['description']} @ ${signal['price']:,.2f} ({datetime.fromtimestamp(signal['timestamp']/1000, tz=timezone.utc).strftime('%Y-%m-%d %H:%M')})\n"
    
    prompt += """
## 报告要求

请生成两份报告：中文和英文。

### 中文报告要求：
1. **标题**：吸引人且专业，体现 Al Brooks 价格行为学
2. **市场概览**：基于价格行为学的市场状态描述
3. **Al Brooks 价格行为学分析**（对每个币种）：
   - 趋势判断（基于摆动高点和低点）
   - 关键支撑位和阻力位（基于价格行为，而非指标）
   - 价格行为信号解读（Pin Bar, Inside Bar, Engulfing 等）
   - 市场结构分析（BoS, ChoCH）
4. **注意**：不要包含模拟盘交易复盘（会在另一部分添加）
5. **交易建议**：基于 Al Brooks 价格行为学的短期操作建议（1-4 小时级别）
6. **风险提示**：可能的市场风险和关键关注点
7. **字数**：800-1200 字

### 英文报告要求：
Same structure as Chinese, but in professional English. 800-1200 words.

## 输出格式

请以 JSON 格式输出：
```json
{
  "title_zh": "中文标题",
  "title_en": "English Title",
  "report_zh": "中文报告内容（Markdown 格式，不包含交易复盘）",
  "report_en": "English report content (Markdown format, without trading review)",
  "tags_zh": ["标签1", "标签2", "标签3"],
  "tags_en": ["tag1", "tag2", "tag3"],
  "importance": "high"
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
            {"role": "system", "content": "你是一位精通 Al Brooks 价格行为学的专业加密货币交易员。"},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 6000
    }
    
    try:
        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload, timeout=90)
        response.raise_for_status()
        
        result = response.json()
        content = result["choices"][0]["message"]["content"]
        
        # 调试：保存原始响应
        debug_file = f"debug_deepseek_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(debug_file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"📝 DeepSeek 原始响应已保存到: {debug_file}")
        
        # 提取 JSON（增强容错）
        json_str = ""
        
        # 方法1：提取 ```json ... ``` 块
        if "```json" in content:
            try:
                json_str = content.split("```json")[1].split("```")[0].strip()
            except:
                pass
        
        # 方法2：提取 { ... } （如果没有 ```json 块）
        if not json_str:
            # 找到第一个 { 和最后一个 }
            start = content.find("{")
            end = content.rfind("}")
            if start != -1 and end != -1 and start < end:
                json_str = content[start:end+1]
        
        # 方法3：如果还是没有，使用整个内容
        if not json_str:
            json_str = content.strip()
        
        # 清理 JSON 字符串（修复常见格式问题）
        # 移除 trailing commas
        import re
        json_str = re.sub(r',\s*}', '}', json_str)
        json_str = re.sub(r',\s*]', ']', json_str)
        
        if not json_str:
            print("❌ 无法从 DeepSeek 响应中提取 JSON")
            return None
        
        # 尝试解析 JSON
        try:
            data = json.loads(json_str)
            print("✅ DeepSeek API 调用成功（市场分析）")
            return data
        except json.JSONDecodeError as je:
            print(f"⚠️  JSON 解析失败（可能截断）: {je}")
            
            # 检查是否截断（检查最后一个字段是否完整）
            if not json_str.rstrip().endswith("}"):
                print("⚠️  检测到响应截断，尝试重试...")
                # 可以在这里添加重试逻辑（增加 max_tokens）
                # 暂时返回 None，使用备用方案
            
            # 保存提取的 JSON 以便调试
            with open("debug_json_failed.txt", "w", encoding="utf-8") as f:
                f.write(json_str)
            print("📝 提取的 JSON 已保存到: debug_json_failed.txt")
            return None
        
    except json.JSONDecodeError as je:
        print(f"❌ JSON 解析失败: {je}")
        print(f"提取的 JSON 字符串前 500 字符: {json_str[:500]}")
        # 保存提取的 JSON 以便调试
        with open("debug_json_failed.txt", "w", encoding="utf-8") as f:
            f.write(json_str)
        print("📝 提取的 JSON 已保存到: debug_json_failed.txt")
        return None
        
    except Exception as e:
        print(f"❌ DeepSeek API 调用失败: {e}")
        return None

def generate_trading_review(trades_pnl):
    """生成交易复盘部分（脚本自己生成，不使用 AI）
    确保使用真实数据，避免编造
    """
    if not trades_pnl:
        return "", ""
    
    # 中文复盘
    review_zh = "\n\n---\n\n## 📊 模拟盘交易复盘\n\n"
    
    if trades_pnl["open_positions"]:
        review_zh += "### 📈 当前持仓\n\n"
        review_zh += f"**总浮盈/浮亏:** ${trades_pnl['total_pnl']:+,.2f} USDT\n\n"
        review_zh += "| 交易ID | 交易对 | 方向 | 入场价 | 当前价 | 浮盈/浮亏 | 止损价 | 止盈价 | 入场理由 |\n"
        review_zh += "|---------|--------|------|--------|--------|------------|--------|--------|----------|\n"
        
        for pos in trades_pnl["open_positions"]:
            direction_zh = "做多 📈" if "long" in pos["direction"] else "做空 📉"
            pnl_emoji = "📈" if pos["pnl_percent"] > 0 else "📉"
            review_zh += f"| {pos['id']} | {pos['symbol']} | {direction_zh} | ${pos['entry']:,.2f} | ${pos['current_price']:,.2f} | {pnl_emoji} {pos['pnl_percent']:+.2f}% (${pos['pnl_usdt']:+,.2f}) | ${pos.get('stop', 0):,.2f} | ${pos.get('target', 0):,.2f} | {pos.get('reason', '')} |\n"
        
        review_zh += "\n"
    else:
        review_zh += "### 📈 当前持仓\n\n**当前无持仓**\n\n"
    
    if trades_pnl["closed_trades"]:
        review_zh += "### 📉 已平仓交易\n\n"
        review_zh += "| 交易ID | 交易对 | 方向 | 入场价 | 平仓价 | 盈亏 | 平仓理由 |\n"
        review_zh += "|---------|--------|------|--------|--------|------|----------|\n"
        
        for trade in trades_pnl["closed_trades"]:
            direction_zh = "做多 📈" if "long" in trade.get("direction", "") else "做空 📉"
            pnl = trade.get("pnl", 0)
            pnl_pct = trade.get("pnlPct", 0)
            pnl_emoji = "📈" if pnl > 0 else "📉"
            review_zh += f"| {trade.get('id', 'N/A')} | {trade.get('pair', 'N/A')} | {direction_zh} | ${trade.get('entryPrice', 0):,.2f} | ${trade.get('closePrice', 0):,.2f} | {pnl_emoji} {pnl_pct:+.2f}% (${pnl:+,.2f}) | {trade.get('exitReason', 'N/A')} |\n"
        
        review_zh += "\n"
    
    review_zh += "### 💡 交易总结\n\n"
    review_zh += "以上为模拟盘真实交易记录，基于 Al Brooks 价格行为学进行决策。\n\n"
    
    # 英文复盘
    review_en = "\n\n---\n\n## 📊 Simulated Trading Review\n\n"
    
    if trades_pnl["open_positions"]:
        review_en += "### 📈 Open Positions\n\n"
        review_en += f"**Total P&L**: ${trades_pnl['total_pnl']:+,.2f} USDT\n\n"
        review_en += "| Trade ID | Pair | Direction | Entry Price | Current Price | P&L | Stop Loss | Take Profit | Reason |\n"
        review_en += "|----------|------|-----------|-------------|--------------|-----|------------|-------------|--------|\n"
        
        for pos in trades_pnl["open_positions"]:
            direction_en = "Long 📈" if "long" in pos["direction"] else "Short 📉"
            pnl_emoji = "📈" if pos["pnl_percent"] > 0 else "📉"
            review_en += f"| {pos['id']} | {pos['symbol']} | {direction_en} | ${pos['entry']:,.2f} | ${pos['current_price']:,.2f} | {pnl_emoji} {pos['pnl_percent']:+.2f}% (${pos['pnl_usdt']:+,.2f}) | ${pos.get('stop', 0):,.2f} | ${pos.get('target', 0):,.2f} | {pos.get('reason', '')} |\n"
        
        review_en += "\n"
    else:
        review_en += "### 📈 Open Positions\n\n**No open positions**\n\n"
    
    if trades_pnl["closed_trades"]:
        review_en += "### 📉 Closed Trades\n\n"
        review_en += "| Trade ID | Pair | Direction | Entry Price | Exit Price | P&L | Exit Reason |\n"
        review_en += "|----------|------|-----------|-------------|------------|-----|------------|\n"
        
        for trade in trades_pnl["closed_trades"]:
            direction_en = "Long 📈" if "long" in trade.get("direction", "") else "Short 📉"
            pnl = trade.get("pnl", 0)
            pnl_pct = trade.get("pnlPct", 0)
            pnl_emoji = "📈" if pnl > 0 else "📉"
            review_en += f"| {trade.get('id', 'N/A')} | {trade.get('pair', 'N/A')} | {direction_en} | ${trade.get('entryPrice', 0):,.2f} | ${trade.get('closePrice', 0):,.2f} | {pnl_emoji} {pnl_pct:+.2f}% (${pnl:+,.2f}) | {trade.get('exitReason', 'N/A')} |\n"
        
        review_en += "\n"
    
    review_en += "### 💡 Trading Summary\n\n"
    review_en += "Above are real simulated trading records, decisions based on Al Brooks Price Action.\n\n"
    
    return review_zh, review_en

# ========== 写入文件 ==========
def write_analysis_files(analyses, market_analysis, trading_review_zh, trading_review_en):
    """写入分析报告到文件（市场分析 + 交易复盘）"""
    print("\n📝 写入分析报告...")
    
    # 确保目录存在
    os.makedirs(OUTPUT_DIR_ZH, exist_ok=True)
    os.makedirs(OUTPUT_DIR_EN, exist_ok=True)
    
    # 生成文件名（安全处理，避免 Windows 非法字符）
    def sanitize_filename(text: str, max_len: int = 50) -> str:
        import re
        # 替换 Windows 非法字符： : / \ ? * " < > |
        text = re.sub(r'[:/\\?*"<>\|\]]', '-', text)
        text = re.sub(r'[-\s]+', '-', text).strip('-')
        return text[:max_len]

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d-%H-%M")

    # 中文报告
    title_zh = market_analysis.get("title_zh", f"Al Brooks 价格行为学分析 {timestamp}")
    slug_zh = sanitize_filename(title_zh)
    filename_zh = f"{timestamp}-{slug_zh}.md"
    filepath_zh = os.path.join(OUTPUT_DIR_ZH, filename_zh)
    
    # 拼接市场分析 + 交易复盘
    content_zh = f"""---
title: "{title_zh}"
date: {datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")}
type: "analysis"
tags: {json.dumps(market_analysis.get("tags_zh", []), ensure_ascii=False)}
importance: "{market_analysis.get("importance", "high")}"
---

{market_analysis.get("report_zh", "")}
{trading_review_zh}
"""
    
    with open(filepath_zh, "w", encoding="utf-8") as f:
        f.write(content_zh)
    
    print(f"✅ 中文报告已写入: {filepath_zh}")
    
    # 英文报告
    title_en = market_analysis.get("title_en", f"Al Brooks Price Action Analysis {timestamp}")
    slug_en = sanitize_filename(title_en)
    filename_en = f"{timestamp}-{slug_en}.md"
    filepath_en = os.path.join(OUTPUT_DIR_EN, filename_en)
    
    # 拼接市场分析 + 交易复盘
    content_en = f"""---
title: "{title_en}"
date: {datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")}
type: "analysis"
tags: {json.dumps(market_analysis.get("tags_en", []))}
importance: "{market_analysis.get("importance", "high")}"
---

{market_analysis.get("report_en", "")}
{trading_review_en}
"""
    
    with open(filepath_en, "w", encoding="utf-8") as f:
        f.write(content_en)
    
    print(f"✅ 英文报告已写入: {filepath_en}")
    
    return filepath_zh, filepath_en

# ========== 主函数 ==========
def main():
    print("=" * 60)
    print("🚀 开始 BTC & ETH 价格行为学分析 (Al Brooks 方法)")
    print("=" * 60)
    
    # 1. 读取模拟盘数据
    print("\n📊 读取模拟盘数据...")
    trades_data = load_trades()
    if trades_data:
        print(f"✅ 模拟盘数据已加载: {len(trades_data)} 笔交易")
    
    # 2. Al Brooks 价格行为学分析（市场分析）
    analyses = []
    for symbol in SYMBOLS:
        analysis = analyze_symbol_al_brooks(symbol)
        if analysis:
            analyses.append(analysis)
        time.sleep(1)  # 避免 API 限流
    
    if not analyses:
        print("❌ 没有成功分析任何交易对")
        sys.exit(1)
    
    # 3. 计算模拟盘盈亏
    trades_pnl = None
    if trades_data:
        # 使用第一个币种的数据计算盈亏
        klines = fetch_klines(SYMBOLS[0])
        if klines:
            trades_pnl = calculate_trades_pnl(klines, trades_data)
            if trades_pnl:
                print(f"\n📊 模拟盘盈亏统计:")
                print(f"   总盈亏: ${trades_pnl['total_pnl']:+,.2f} USDT")
                print(f"   持仓中: {len(trades_pnl['open_positions'])} 笔")
                print(f"   已平仓: {len(trades_pnl['closed_trades'])} 笔")
    
    # 4. 生成市场分析（只传入市场数据，不传入模拟盘数据）
    market_analysis = generate_market_analysis_with_deepseek(analyses)
    if not market_analysis:
        print("⚠️  市场分析生成失败，使用备用方案...")
        # 备用方案：生成基础报告
        market_analysis = {
            "title_zh": f"Al Brooks 价格行为学分析 {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "title_en": f"Al Brooks Price Action Analysis {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "report_zh": "# 市场分析报告（自动生成）\n\nAl Brooks 价格行为学分析暂时无法生成，请稍后重试。",
            "report_en": "# Market Analysis Report (Auto-generated)\n\nAl Brooks price action analysis temporarily unavailable, please retry later.",
            "tags_zh": ["Al Brooks", "价格行为学", "BTC", "ETH"],
            "tags_en": ["Al Brooks", "Price Action", "BTC", "ETH"],
            "importance": "high"
        }
    
    # 5. 生成交易复盘（脚本自己生成，确保真实数据）
    print("\n📝 生成交易复盘（使用真实数据）...")
    trading_review_zh, trading_review_en = generate_trading_review(trades_pnl)
    
    # 6. 写入文件（拼接市场分析 + 交易复盘）
    write_analysis_files(analyses, market_analysis, trading_review_zh, trading_review_en)
    
    print("\n" + "=" * 60)
    print("✅ 价格行为学分析完成")
    print("=" * 60)

if __name__ == "__main__":
    main()
