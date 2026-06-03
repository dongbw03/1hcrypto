#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每日分析自动生成脚本 - 1H Crypto (1H币研)
===============================================
功能：
  1. 拉取 BTC/ETH 市场数据（CoinGecko API - 无需API key）
  2. 基于 Al Brooks 价格行为规则生成分析文案
  3. 生成中英文双语 .astro 文章页面
  4. 更新 trades.json 中的 linkedAnalysis 字段

使用：
  python scripts/generate_daily.py                # 生成今日分析
  python scripts/generate_daily.py --date 2026-06-01  # 指定日期
  python scripts/generate_daily.py --dry-run     # 只打印不写入
"""

import json
import os
import re
import sys
import argparse
import time
from datetime import datetime, timezone, timedelta

# 导入链上数据模块
try:
    from chain_data import generate_onchain_data
    CHAIN_DATA_AVAILABLE = True
except ImportError:
    CHAIN_DATA_AVAILABLE = False
    print("[WARN] chain_data module not found, using fallback")

# ============================================================
# 配置
# ============================================================
SITE_ROOT   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_ROOT    = os.path.join(SITE_ROOT, "src")
CONTENT_ZH_DIR  = os.path.join(SRC_ROOT, "content", "zh", "daily")
CONTENT_EN_DIR  = os.path.join(SRC_ROOT, "content", "en", "daily")
TRADES_JSON  = os.path.join(SRC_ROOT, "data", "trades.json")

# ============================================================
# 市场数据拉取（CoinGecko - 免费，无需 API key）
# ============================================================
def call_deepseek_ai(prompt, api_key=None):
    """调用 DeepSeek API 生成分析文案"""
    if not api_key:
        api_key = os.environ.get("DEEPSEEK_API_KEY", "")
    if not api_key:
        print("[WARN] DEEPSSEEK_API_KEY 未设置，使用 fallback 分析")
        return None
    try:
        import requests
        url = "https://api.deepseek.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "你是专业的加密货币价格行为分析师，精通 Al Brooks 价格行为学。请用中文回答。"},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.3,
            "max_tokens": 800
        }
        resp = requests.post(url, headers=headers, json=payload, timeout=30)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"[WARN] DeepSeek API 失败: {e}", file=sys.stderr)
        return None


# ============================================================
# DeepSeek 分析（基于 K 线数据）
# ============================================================
def call_deepseek_for_analysis(klines, pair, api_key=None):
    """
    调用 DeepSeek API 基于 K 线数据生成分析结论
    返回 dict: {
        "direction": "long" | "short" | "neutral",
        "entry": float,
        "stop": float,
        "tp1": float,
        "tp2": float,
        "pivot": float,
        "support": [float, float],
        "resistance": [float, float],
        "coreThesis": str,
        "marketStructure": str,
        "latestClose": float,
    } or None（如果 API 调用失败）
    """
    if not api_key:
        api_key = os.environ.get("DEEPSEEK_API_KEY", "")
    if not api_key:
        print("[WARN] DEEPSSEEK_API_KEY 未设置，使用 fallback 分析")
        return None
    
    # 格式化 K 线数据（最近 24 小时）
    recent_klines = klines[-24:] if len(klines) > 24 else klines
    formatted = []
    for k in recent_klines:
        # k: [开盘时间, 开盘价, 最高价, 最低价, 收盘价, 成交量, ...]
        formatted.append(f"[{datetime.fromtimestamp(k[0]/1000).strftime('%m-%d %H:%M')}] O:{k[1]} H:{k[2]} L:{k[3]} C:{k[4]} V:{k[5]}")
    
    kline_text = "\n".join(formatted)
    current_price = float(klines[-1][4]) if klines else 0
    
    prompt = f"""你是专业的加密货币价格行为分析师，精通 Al Brooks 价格行为学。

请分析以下 {pair} 的小时级K线数据，并给出交易建议。

K线数据（最近24小时）：
{kline_text}

当前价格：${current_price:,}

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
        import requests
        url = "https://api.deepseek.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
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
            "response_format": {"type": "json_object"}  # 强制返回 JSON
        }
        resp = requests.post(url, headers=headers, json=payload, timeout=30)
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

# ===========================================================
# 调用 generate_analysis.py 获取分析（新增）
# ===========================================================
def get_analysis_from_script(pair="BTC/USDT"):
    """
    调用 generate_analysis.py 脚本获取分析结果
    返回 analysis dict 或 None
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    import subprocess
    import tempfile
    
    script_path = os.path.join(script_dir, "generate_analysis.py")
    if not os.path.exists(script_path):
        print(f"[WARN] {script_path} 不存在，无法调用")
        return None
    
    # 创建临时输出文件
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_output = f.name
    
    try:
        # 调用脚本
        cmd = [sys.executable, script_path, "--pair", pair, "--output", temp_output]
        print(f"[INFO] 调用分析脚本: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        
        if result.returncode != 0:
            print(f"[WARN] 分析脚本失败: {result.stderr}")
            return None
        
        # 读取结果
        if os.path.exists(temp_output):
            with open(temp_output, 'r', encoding='utf-8') as f:
                data = json.load(f)
            analysis = {
                "direction":      data["btc"]["direction"],
                "entry":          data["btc"]["entry"],
                "stop":           data["btc"]["stop"],
                "tp1":            data["btc"]["tp1"],
                "tp2":            data["btc"]["tp2"],
                "pivot":          data["btc"]["pivot"],
                "support":        data["btc"]["support"],
                "resistance":    data["btc"]["resistance"],
                "coreThesis":    data["btc"]["coreThesis"],
                "marketStructure": data["btc"]["marketStructure"],
                "latestClose":   data["btc"]["latestClose"],
                "keyLevel":      "N/A",
                "pinBar":        False,
                "volTrend":      "N/A",
            }
            print(f"[OK] 从脚本获取分析: {analysis['direction']} @ {analysis['entry']}")
            return analysis
        else:
            print("[WARN] 分析脚本未生成输出文件")
            return None
            
    except Exception as e:
        print(f"[WARN] 调用分析脚本失败: {e}")
        return None
    finally:
        # 清理临时文件
        if os.path.exists(temp_output):
            os.unlink(temp_output)



def fetch_coingecko_btc():
    """拉取 BTC 数据 from CoinGecko"""
    try:
        import requests
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": "bitcoin,ethereum",
            "vs_currencies": "usd",
            "include_24hr_change": "true",
            "include_24hr_vol": "true",
            "include_market_cap": "true",
        }
        resp = requests.get(url, params=params, timeout=15, verify=True)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(f"[WARN] CoinGecko API 失败: {e}", file=sys.stderr)
        return None

def fetch_binance_klines_fallback(symbol="BTCUSDT", interval="1h", limit=100):
    """Binance K线数据（fallback，处理SSL错误）"""
    try:
        import requests
        # 禁用 SSL 验证作为 fallback（仅用于开发环境）
        url = f"https://api.binance.com/api/v3/klines"
        params = {"symbol": symbol, "interval": interval, "limit": limit}
        resp = requests.get(url, params=params, timeout=10, verify=False)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(f"[WARN] Binance API 失败: {e}", file=sys.stderr)
        return None


def analyze_price_action(klines):
    """价格行为分析 → 返回 dict"""
    if not klines or len(klines) < 20:
        return _fallback_analysis()

    closes  = [float(k[4]) for k in klines]
    highs   = [float(k[2]) for k in klines]
    lows    = [float(k[3]) for k in klines]
    volumes = [float(k[5]) for k in klines]

    latest_close = closes[-1]
    sma20 = sum(closes[-20:]) / 20
    sma50 = sum(closes[-50:]) / 50 if len(closes) >= 50 else sma20

    if latest_close > sma20 and sma20 > sma50:
        direction = "long"
    elif latest_close < sma20 and sma20 < sma50:
        direction = "short"
    else:
        direction = "neutral"

    recent_high = max(highs[-20:])
    recent_low  = min(lows[-20:])
    pivot = round((recent_high + recent_low + latest_close) / 3, 1)

    last = klines[-1]
    o, h, l, c = float(last[1]), float(last[2]), float(last[3]), float(last[4])
    body = abs(c - o)
    upper = h - max(o, c)
    lower = min(o, c) - l
    has_pin = (upper > body * 2) or (lower > body * 2)

    pin_desc = ""
    if upper > body * 2:
        pin_desc = "出现看跌 Pin Bar（上影线较长）"
    elif lower > body * 2:
        pin_desc = "出现看涨 Pin Bar（下影线较长）"
    else:
        pin_desc = "无显著 Pin Bar"

    avg_vol = sum(volumes[-20:]) / 20
    if volumes[-1] > avg_vol * 1.3:
        vol_trend = "放量"
    elif volumes[-1] < avg_vol * 0.7:
        vol_trend = "缩量"
    else:
        vol_trend = "持平"

    r2   = round(recent_high, 1)
    r1   = round(recent_high - (recent_high - recent_low) * 0.382, 1)
    s1   = round(recent_low, 1)
    s2   = round(recent_low + (recent_high - recent_low) * 0.382, 1)

    market_structure = (
        f"近20根1H K线区间：{s1:,} - {r2:,}。"
        f"价格{'站上' if latest_close > sma20 else '跌破'} SMA20（{round(sma20):,}）。"
        f"{pin_desc}。成交量{vol_trend}。"
    )

    core_thesis = (
        f"关键位 ${pivot:,}。价格在此附近的反应决定方向。"
        f"{'等待回踩确认后做多。' if direction == 'long' else '等待反弹失效后做空。' if direction == 'short' else '等待区间突破确认方向。'}"
    )

    return {
        "direction":      direction,
        "marketStructure": market_structure,
        "keyLevel":       f"${pivot:,}",
        "coreThesis":     core_thesis,
        "resistance":     [r2, r1],
        "support":         [s1, s2],
        "pivot":           pivot,
        "pinBar":          has_pin,
        "volTrend":        vol_trend,
        "latestClose":      latest_close,
    }


def _fallback_analysis():
    import random
    d = random.choice(["long", "short", "neutral"])
    return {
        "direction":      d,
        "marketStructure": "(离线模式）暂无实时数据，请手动更新分析。",
        "keyLevel":       "N/A",
        "coreThesis":     "等待市场数据接入后更新。",
        "resistance":     [0, 0],
        "support":         [0, 0],
        "pivot":           0,
        "pinBar":         False,
        "volTrend":       "N/A",
        "latestClose":     0,
    }


def fetch_onchain_data(direction="neutral", symbol="BTC"):
    """链上数据 - 优先真实 API"""
    if CHAIN_DATA_AVAILABLE:
        try:
            return generate_onchain_data(direction, symbol)
        except Exception as e:
            print(f"[WARN] chain_data module failed: {e}, using fallback")
    
    # Fallback 模拟数据
    print("[INFO] Using fallback on-chain data")
    return {
        "exchangeBalance": "-3,200",
        "oiChange":       "+2.1%",
        "funding":         "0.03%",
        "netFlow7d":      "-1,800",
    }


# ============================================================
# 文章生成
# ============================================================
def make_zh_markdown(date_str, pair, analysis, onchain):
    """生成中文 markdown 内容（返回字符串）"""
    direction   = analysis["direction"]
    dir_label  = {"long": "偏多", "short": "偏空"}.get(direction, "中性")
    price      = analysis.get("latestClose", 0)
    core       = analysis.get("coreThesis", "")
    struct     = analysis.get("marketStructure", "")
    r          = analysis.get("resistance", [0, 0])
    s          = analysis.get("support", [0, 0])
    p          = analysis.get("pivot", 0)
    entry      = int(analysis.get("entry", 0))
    stop       = int(analysis.get("stop", 0))
    tp1        = int(analysis.get("tp1", 0))
    tp2        = int(analysis.get("tp2", 0))

    lines = [
        f'title: "{pair} 小时图价格行为分析 - {date_str}"',
        f'date: "{date_str}"',
        f'description: "{core[:80]}"',
        f'sentiment: "{dir_label}"',
        f'keywords: "{pair}, Al Brooks, 价格行为"',
        f'btc_entry: {entry}',
        f'btc_stop: {stop}',
        f'btc_tp1: {tp1}',
        f'btc_tp2: {tp2}',
        'eth_entry: 0',
        'eth_stop: 0',
        'eth_tp1: 0',
        'eth_tp2: 0',
        '---',
        '',
        f'## {pair} · 小时图',
        '',
        f'**市场结构** 　分析得出：{struct}',
        '',
        f'**核心判断** 　{core}',
        '',
        '**关键水平**',
        '',
        '| 角色 | 价格 | 说明 |',
        '|---|---|---|',
        f'| 阻力 R2 | {int(r[0]) if len(r) > 0 else 0} | 24h 高点 |',
        f'| 阻力 R1 | {int(r[1]) if len(r) > 1 else 0} | 前高 |',
        f'| 中枢 Pivot | {int(p)} | 成交量集中区 |',
        f'| 支撑 S1 | {int(s[0]) if len(s) > 0 else 0} | 24h 低点 |',
        f'| 支撑 S2 | {int(s[1]) if len(s) > 1 else 0} | 次级支撑 |',
        '',
        '**链上快照**',
        '',
        '| 指标 | 数值 | 方向 |',
        '|---|---|---|',
    ]

    ex_b = onchain.get("exchangeBalance", "N/A")
    oi   = onchain.get("oiChange", "N/A")
    fr   = onchain.get("funding", "N/A")
    nf   = onchain.get("netFlow7d", "N/A")
    lines += [
        f'| 交易所余额 | {ex_b} | {"流入 · 偏空" if "+" in str(ex_b) else "流出 · 偏多"} |',
        f'| 未平仓合约 | {oi} | {"增仓" if "+" in str(oi) else "减仓"} |',
        f'| 资金费率 | {fr} | {"偏多" if "-" not in str(fr) else "偏空"} |',
        f'| 净流量 7d | {nf} | {"流入" if "+" in str(nf) else "流出"} |',
        '',
        '---',
        '',
        '## ETH/USDT · 小时图',
        '',
        '**市场结构** 　待更新（请手动补充）',
        '',
        '**核心判断** 　待更新（请手动补充）',
        '',
        '**关键水平**',
        '',
        '| 角色 | 价格 | 说明 |',
        '|---|---|---|',
        '| 阻力 R2 | 2050 | 前高 |',
        '| 阻力 R1 | 2000 | 整数关口 |',
        '| 支撑 S1 | 1960 | 24h 低点 |',
        '| 支撑 S2 | 1880 | 次级支撑 |',
        '',
        '**链上快照**',
        '',
        '| 指标 | 数值 | 方向 |',
        '|---|---|---|',
        '| 交易所余额 | +3.2 万 | 流入 · 偏空 |',
        '| 未平仓合约 | -1.8% | 小幅减仓 |',
        '| 资金费率 | -0.02% | 略偏空 |',
        '',
        '---',
        '',
        '## 综合判断',
        '',
        f'**情绪：{dir_label}**',
        '',
        core,
        '',
        '*以上分析基于 Al Brooks 价格行为框架，仅供参考，不构成投资建议。*',
        '',
        '---',
        '',
        '> 🤝 **支持本站**：通过 [币安](https://accounts.binance.com/register?ref=CPA_00ZIV33RO4) 或 [OKX](https://www.okx.com/join/1HCRYPTO) 注册，不影响费率，本站获得佣金支持。',
        '',
    ]
    return "\n".join(lines)


def make_en_markdown(date_str, pair, analysis, onchain):
    """Generate English markdown content (returns string)"""
    direction   = analysis["direction"]
    dir_label  = {"long": "Bullish", "short": "Bearish"}.get(direction, "Neutral")
    price      = analysis.get("latestClose", 0)
    core       = analysis.get("coreThesis", "")
    struct     = analysis.get("marketStructure", "")
    r          = analysis.get("resistance", [0, 0])
    s          = analysis.get("support", [0, 0])
    p          = analysis.get("pivot", 0)
    entry      = int(analysis.get("entry", 0))
    stop       = int(analysis.get("stop", 0))
    tp1        = int(analysis.get("tp1", 0))
    tp2        = int(analysis.get("tp2", 0))

    lines = [
        f'title: "{pair} 1H Price Action - {date_str}"',
        f'date: "{date_str}"',
        f'description: "{core[:80]}"',
        f'sentiment: "{dir_label}"',
        f'keywords: "{pair}, Al Brooks, Price Action"',
        f'btc_entry: {entry}',
        f'btc_stop: {stop}',
        f'btc_tp1: {tp1}',
        f'btc_tp2: {tp2}',
        'eth_entry: 0',
        'eth_stop: 0',
        'eth_tp1: 0',
        'eth_tp2: 0',
        '---',
        '',
        f'## {pair} · 1H Chart',
        '',
        f'**Market Structure** {struct}',
        '',
        f'**Core Judgment** {core}',
        '',
        '**Key Levels**',
        '',
        '| Role | Price | Notes |',
        '|---|---|---|',
        f'| R2 | {int(r[0]) if len(r) > 0 else 0} | 24h High |',
        f'| R1 | {int(r[1]) if len(r) > 1 else 0} | Previous High |',
        f'| Pivot | {int(p)} | Volume Cluster |',
        f'| S1 | {int(s[0]) if len(s) > 0 else 0} | 24h Low |',
        f'| S2 | {int(s[1]) if len(s) > 1 else 0} | Secondary Support |',
        '',
        '**On-Chain Snapshot**',
        '',
        '| Metric | Value | Direction |',
        '|---|---|---|',
    ]

    ex_b = onchain.get("exchangeBalance", "N/A")
    oi   = onchain.get("oiChange", "N/A")
    fr   = onchain.get("funding", "N/A")
    nf   = onchain.get("netFlow7d", "N/A")
    lines += [
        f'| Exchange Balance | {ex_b} | {"Inflow" if "+" in str(ex_b) else "Outflow"} |',
        f'| Open Interest | {oi} | {"Increasing" if "+" in str(oi) else "Decreasing"} |',
        f'| Funding Rate | {fr} | {"Bullish" if "-" not in str(fr) else "Bearish"} |',
        f'| Net Flow (7d) | {nf} | {"Inflow" if "+" in str(nf) else "Outflow"} |',
        '',
        '---',
        '',
        '## ETH/USDT · 1H Chart',
        '',
        '**Market Structure** TBD (manual update needed)',
        '',
        '**Core Thesis** TBD (manual update needed)',
        '',
        '**Key Levels**',
        '',
        '| Role | Price | Notes |',
        '|---|---|---|',
        '| R2 | 2050 | Previous High |',
        '| R1 | 2000 | Psychological |',
        '| S1 | 1960 | 24h Low |',
        '| S2 | 1880 | Secondary |',
        '',
        '**On-Chain Snapshot**',
        '',
        '| Metric | Value | Direction |',
        '|---|---|---|',
        '| Exchange Balance | +32K | Inflow · Bearish |',
        '| Open Interest | -1.8% | Slight Decrease |',
        '| Funding Rate | -0.02% | Slightly Bearish |',
        '',
        '---',
        '',
        '## Comprehensive Judgment',
        '',
        f'**Sentiment: {dir_label}**',
        '',
        core,
        '',
        '*Analysis based on Al Brooks Price Action framework. For reference only, not financial advice.*',
        '',
        '---',
        '',
        '> 🤝 **Support 1H Crypto:** Sign up via [Binance](https://accounts.binance.com/register?ref=CPA_00ZIV33RO4) or [OKX](https://www.okx.com/join/1HCRYPTO) — no extra cost, we earn a small commission.',
        '',
    ]
    return "\n".join(lines)


def write_page(date_str, pair, analysis, onchain, lang="zh", dry_run=False):
    """写入 .md 文件到 content/ 目录（不触碰 pages/ 下的 .astro 模板）"""
    is_zh   = lang == "zh"
    base_dir = CONTENT_ZH_DIR if is_zh else CONTENT_EN_DIR
    out_file = os.path.join(base_dir, f"{date_str}.md")

    if is_zh:
        content = make_zh_markdown(date_str, pair, analysis, onchain)
    else:
        content = make_en_markdown(date_str, pair, analysis, onchain)

    if dry_run:
        print(f"[DRY-RUN] Would write {out_file} ({len(content)} bytes)")
        print(content[:500])
        return

    os.makedirs(base_dir, exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(content)
        f.write("\n")
    print(f"[OK] Written: {out_file}")


def update_trades_linked_analysis(date_str):
    """更新 trades.json 中的 linkedAnalysis 字段"""
    if not os.path.exists(TRADES_JSON):
        print(f"[WARN] {TRADES_JSON} not found, skipping linkedAnalysis update")
        return

    with open(TRADES_JSON, "r", encoding="utf-8") as f:
        trades = json.load(f)

    updated = 0
    for t in trades:
        if t.get("status") == "open" and (not t.get("linkedAnalysis") or t.get("linkedAnalysis") == "/zh/daily/"):
            t["linkedAnalysis"] = f"/zh/daily/{date_str}/"
            updated += 1

    if updated > 0:
        with open(TRADES_JSON, "w", encoding="utf-8") as f:
            json.dump(trades, f, ensure_ascii=False, indent=2)
        print(f"[OK] Updated {updated} trade(s) linkedAnalysis -> /zh/daily/{date_str}/")
    else:
        print(f"[INFO] No open trades to update linkedAnalysis")


# ============================================================
# 主程序
# ============================================================
def main():
    parser = argparse.ArgumentParser(description="生成每日分析文章（.astro）")
    parser.add_argument("--date",  default=datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d"), help="日期 YYYY-MM-DD（默认今天）")
    parser.add_argument("--dry-run", action="store_true", help="只打印不写入")
    parser.add_argument("--pair", default="BTC/USDT", help="交易对（默认 BTC/USDT）")
    parser.add_argument("--skip-api", action="store_true", help="跳过 API 调用，使用 fallbak")
    args = parser.parse_args()

    print(f"[INFO] Generating daily analysis for {args.date}...")


    # 1.0 先尝试从脚本获取分析（优先使用 DeepSeek API）
    analysis = get_analysis_from_script(args.pair)

    # 如果脚本成功返回分析，跳过 API 调用
    if analysis is not None:
        print(f"[OK] 使用脚本分析: {analysis['direction']} @ {analysis['entry']}")
        # 获取链上数据
        onchain = fetch_onchain_data(analysis["direction"], args.pair.replace("/", ""))
        # 跳转到页面生成（跳过 API 调用）
        goto_skip_api = True
    else:
        goto_skip_api = False
        print("[WARN] 脚本分析失败，尝试 API 调用...")

    if analysis is None:
        # 1. 拉取市场数据
        analysis = None
        klines = []

        if not args.skip_api:
            # 1.1 拉取小时级 K 线数据（用于分析）
            print(f"[INFO] Fetching hour-level K-lines for {args.pair}...")
            klines = fetch_binance_klines_fallback(
                symbol=args.pair.replace("/", ""),
                interval="1h",
                limit=100
            )
        
            if klines:
                print(f"[OK] Got {len(klines)} K-lines")
            
                # 1.2 调用 DeepSeek API 生成分析
                print(f"[INFO] Calling DeepSeek API for analysis...")
                analysis = call_deepseek_for_analysis(klines, args.pair)
        
            # 1.3 如果 DeepSeek 失败，使用本地分析
            if analysis is None:
                print("[WARN] DeepSeek API failed, using local analysis...")
                analysis = analyze_price_action(klines)
        
            # 1.4 获取 CoinGecko 价格（用于展示）
            cg_data = fetch_coingecko_btc()
            if cg_data:
                price = cg_data.get("bitcoin", {}).get("usd", 0)
                print(f"[INFO] BTC price from CoinGecko: ${price:,}")
                analysis["latestClose"] = price
                # 更新 marketStructure 和 coreThesis（如果它们是默认的）
                if "CoinGecko" not in analysis.get("marketStructure", ""):
                    analysis["marketStructure"] += f"\n\nCoinGecko 实时价格：${price:,}。"
                if "BTC 当前报价" not in analysis.get("coreThesis", ""):
                    analysis["coreThesis"] += f"\n\nBTC 当前报价 ${price:,}。"
        else:
            print("[INFO] Skipping API calls (--skip-api)")
            analysis = _fallback_analysis()

        if analysis is None:
            analysis = _fallback_analysis()

        onchain = fetch_onchain_data(analysis["direction"], args.pair.replace("/", ""))
    else:
        pass  # analysis 已有值，跳过 API 调用

    # 2. 生成中文页面
    write_page(args.date, args.pair, analysis, onchain, lang="zh", dry_run=args.dry_run)

    # 3. 生成英文页面
    write_page(args.date, args.pair, analysis, onchain, lang="en", dry_run=args.dry_run)

    # 4. 更新 trades.json
    if not args.dry_run:
        update_trades_linked_analysis(args.date)

    # 5. 输出 latest-analysis.json（供 auto_trade.py 读取）
    if not args.dry_run:
        import json
        # 获取 ETH 链上数据
        eth_onchain = fetch_onchain_data("neutral", "ETH")
        
        latest_analysis = {
            "date": args.date,
            "btc": {
                "direction": analysis["direction"],
                "price": analysis.get("latestClose", 0),
                "entry": analysis.get("entry", 0),
                "stop": analysis.get("stop", 0),
                "tp1": analysis.get("tp1", 0),
                "tp2": analysis.get("tp2", 0),
                "pivot": analysis.get("pivot", 0),
                "support": analysis.get("support", [0, 0]),
                "resistance": analysis.get("resistance", [0, 0]),
                "marketStructure": analysis.get("marketStructure", ""),
                "coreThesis": analysis.get("coreThesis", ""),
            },
            "eth": {
                "direction": "neutral",
                "price": 0,
                "entry": 0,
                "stop": 0,
                "tp1": 0,
                "tp2": 0,
                "pivot": 0,
                "support": [0, 0],
                "resistance": [0, 0],
                "marketStructure": "",
                "coreThesis": "",
            },
            "onchain": {
                "btc": onchain,
                "eth": eth_onchain
            }
        }
        latest_file = os.path.join(SRC_ROOT, "data", "latest-analysis.json")
        os.makedirs(os.path.dirname(latest_file), exist_ok=True)
        with open(latest_file, "w", encoding="utf-8") as f:
            json.dump(latest_analysis, f, ensure_ascii=False, indent=2)
        print(f"[OK] Written: {latest_file}")
    
    print(f"\n[OK] Daily analysis generated for {args.date}")
    print(f"[INFO] Next steps:")
    print(f"  1. npm run build")
    print(f"  2. npm run preview")


if __name__ == "__main__":
    main()
