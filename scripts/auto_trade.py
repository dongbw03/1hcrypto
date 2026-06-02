#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
模拟盘自动交易脚本 - 1H Crypto (1H币研)
==========================================
功能：
  1. 读取最新研判结论（src/data/latest-analysis.json）
  2. 根据研判方向自动开仓/平仓
  3. 严格遵循止损止盈规则
  4. 成交记录写入 trades.json

使用：
  python scripts/auto_trade.py                # 完整运行（检查平仓 + 开新仓）
  python scripts/auto_trade.py --check-only  # 只检查平仓，不开新仓
  python scripts/auto_trade.py --dry-run     # 只打印不写入
"""

import json
import os
import sys
import argparse
import requests
from datetime import datetime, timezone, timedelta

# ============================================================
# 配置
# ============================================================
SITE_ROOT   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目根目录
SRC_ROOT    = os.path.join(SITE_ROOT, "src")
DATA_DIR     = os.path.join(SRC_ROOT, "data")
LATEST_JSON  = os.path.join(DATA_DIR, "latest-analysis.json")
TRADES_JSON  = os.path.join(DATA_DIR, "trades.json")  # 修正路径：src/data/trades.json

# 交易配置
MAX_POSITION = 0.1  # 最大仓位（10%）
STOP_LOSS    = 0.02  # 止损百分比（2%）
TAKE_PROFIT = 0.05  # 止盈百分比（5%）


# ============================================================
# 数据读取
# ============================================================
def load_latest_analysis():
    """读取最新研判结论"""
    if not os.path.exists(LATEST_JSON):
        print(f"[WARN] {LATEST_JSON} not found, skipping")
        return None
    
    try:
        with open(LATEST_JSON, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"[OK] Loaded latest analysis for {data.get('date', 'unknown')}")
        return data
    except Exception as e:
        print(f"[ERROR] Failed to load {LATEST_JSON}: {e}")
        return None


def load_trades():
    """读取模拟盘交易记录"""
    if not os.path.exists(TRADES_JSON):
        print(f"[WARN] {TRADES_JSON} not found, creating new")
        return []
    
    try:
        with open(TRADES_JSON, "r", encoding="utf-8") as f:
            trades = json.load(f)
        print(f"[OK] Loaded {len(trades)} trade(s)")
        return trades
    except Exception as e:
        print(f"[ERROR] Failed to load {TRADES_JSON}: {e}")
        return []


def save_trades(trades):
    """保存模拟盘交易记录"""
    try:
        os.makedirs(os.path.dirname(TRADES_JSON), exist_ok=True)
        with open(TRADES_JSON, "w", encoding="utf-8") as f:
            json.dump(trades, f, ensure_ascii=False, indent=2)
        print(f"[OK] Saved {len(trades)} trade(s) to {TRADES_JSON}")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to save {TRADES_JSON}: {e}")
        return False


# ============================================================
# 价格获取
# ============================================================
def get_current_price(symbol="BTCUSDT"):
    """获取当前价格（Binance 公开 API）"""
    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        price = float(resp.json()["price"])
        return price
    except Exception as e:
        print(f"[ERROR] Failed to get price for {symbol}: {e}")
        return None


# ============================================================
# 交易逻辑
# ============================================================
def check_stop_tp(trade, current_price):
    """
    检查是否触及止损/止盈
    返回：("stop", reason) 或 ("tp", reason) 或 (None, None)
    """
    direction = trade.get("direction", "")
    entry = trade.get("entry", 0)
    stop = trade.get("stop", 0)
    tp1 = trade.get("tp1", 0)
    tp2 = trade.get("tp2", 0)
    
    if direction == "long":
        if current_price <= stop:
            return ("stop", f"价格 {current_price} 触及止损 {stop}")
        if current_price >= tp1:
            return ("tp1", f"价格 {current_price} 触及止盈1 {tp1}")
        if current_price >= tp2:
            return ("tp2", f"价格 {current_price} 触及止盈2 {tp2}")
    elif direction == "short":
        if current_price >= stop:
            return ("stop", f"价格 {current_price} 触及止损 {stop}")
        if current_price <= tp1:
            return ("tp1", f"价格 {current_price} 触及止盈1 {tp1}")
        if current_price <= tp2:
            return ("tp2", f"价格 {current_price} 触及止盈2 {tp2}")
    
    return (None, None)


def close_trade(trade, exit_price, reason, dry_run=False):
    """平仓"""
    trade["status"] = "closed"
    trade["exitPrice"] = exit_price
    trade["closeReason"] = reason
    trade["closedAt"] = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%dT%H:%M:%S+08:00")
    
    # 计算收益
    direction = trade.get("direction", "")
    entry = trade.get("entry", 0)
    if direction == "long":
        pnl = (exit_price - entry) / entry * 100
    elif direction == "short":
        pnl = (entry - exit_price) / entry * 100
    else:
        pnl = 0
    
    trade["pnl"] = round(pnl, 2)
    
    print(f"[OK] Closed trade: {trade.get('id', 'unknown')} @ {exit_price} ({reason}, PnL: {pnl:.2f}%)")
    return trade


def open_trade(pair, direction, entry, stop, tp1, tp2, dry_run=False):
    """开仓"""
    # 生成交易 ID
    trade_id = f"auto-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    
    # 当前时间
    now = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%dT%H:%M:%S+08:00")
    
    trade = {
        "id": trade_id,
        "pair": pair,
        "direction": direction,
        "status": "open",
        "entryPrice": entry,
        "stopLoss": stop,
        "takeProfit1": tp1,
        "takeProfit2": tp2,
        "riskPercent": STOP_LOSS * 100,
        "linkedAnalysis": f"/zh/daily/{datetime.now().strftime('%Y-%m-%d')}/",
        "createdAt": now,
        "updatedAt": now,
        "exitPrice": None,
        "closeReason": None,
        "closedAt": None,
        "pnl": None
    }
    
    if dry_run:
        print(f"[DRY-RUN] Would open trade: {trade_id} {direction} {pair} @ {entry}")
        return trade
    
    print(f"[OK] Opened trade: {trade_id} {direction} {pair} @ {entry}")
    return trade


# ============================================================
# 主程序
# ============================================================
def main():
    parser = argparse.ArgumentParser(description="模拟盘自动交易")
    parser.add_argument("--dry-run", action="store_true", help="只打印不写入")
    parser.add_argument("--check-only", action="store_true", help="只检查平仓，不开新仓")
    parser.add_argument("--pair", default="BTC/USDT", help="交易对（默认 BTC/USDT）")
    args = parser.parse_args()

    print(f"[INFO] Auto trade started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}...")

    # 1. 读取最新研判
    analysis = load_latest_analysis()
    if not analysis:
        print("[ERROR] No analysis data available, exiting")
        return

    # 2. 读取当前持仓
    trades = load_trades()
    open_trades = [t for t in trades if t.get("status") == "open"]
    
    print(f"[INFO] Current open trades: {len(open_trades)}")

    # 3. 检查平仓（所有 open 状态的交易）
    current_price = get_current_price(args.pair.replace("/", ""))
    if current_price is None:
        print("[ERROR] Cannot get current price, skipping check")
    else:
        for trade in open_trades:
            action, reason = check_stop_tp(trade, current_price)
            if action:
                if not args.dry_run:
                    trade = close_trade(trade, current_price, reason)
                else:
                    print(f"[DRY-RUN] Would close trade: {trade.get('id', 'unknown')} ({reason})")
    
    # 4. 如果 --check-only，跳过开仓
    if args.check_only:
        print("[INFO] --check-only mode, skipping open new trade")
        if not args.dry_run:
            save_trades(trades)
        return

    # 5. 开新仓（如果没有 open 状态的交易）
    if len(open_trades) == 0:
        # 获取 BTC 研判
        btc_analysis = analysis.get("btc", {})
        direction = btc_analysis.get("direction", "neutral")
        
        if direction == "neutral":
            print("[INFO] Direction is neutral, skipping open new trade")
        else:
            entry = btc_analysis.get("entry", 0)
            stop = btc_analysis.get("stop", 0)
            tp1 = btc_analysis.get("tp1", 0)
            tp2 = btc_analysis.get("tp2", 0)
            
            if entry == 0 or stop == 0:
                print("[WARN] Invalid entry/stop, skipping open new trade")
            else:
                new_trade = open_trade(
                    pair=args.pair,
                    direction=direction,
                    entry=entry,
                    stop=stop,
                    tp1=tp1,
                    tp2=tp2,
                    dry_run=args.dry_run
                )
                trades.append(new_trade)
    else:
        print(f"[INFO] Already have {len(open_trades)} open trade(s), skipping open new trade")

    # 6. 保存交易记录
    if not args.dry_run:
        save_trades(trades)
    
    print(f"\n[OK] Auto trade completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()
