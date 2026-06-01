# 每日分析自动生成指南

## 快速开始

```bash
# 生成今日分析（中英文双语）
python scripts/generate_daily.py

# 指定日期
python scripts/generate_daily.py --date 2026-06-01

# 仅预览不写入
python scripts/generate_daily.py --dry-run
```

## 脚本做了什么

1. **拉取市场数据**
   - Binance API：BTC/ETH 1H K线（最近50根）
   - 自动计算 SMA20 / SMA50
   - 检测 Pin Bar（上/下影线 > 2倍实体）
   - 判断成交量趋势（放量/缩量/持平）

2. **生成分析结论**
   - 方向判断：long / short / neutral
   - 市场结构描述（区间/SMA关系）
   - 支撑/阻力自动计算（最近20根K线）
   - Pivot Point 计算

3. **写入文章**
   - `src/pages/zh/daily/YYYY-MM-DD/index.astro`
   - `src/pages/en/daily/YYYY-MM-DD/index.astro`
   - 自动填充 Article Schema（结构化数据，利于SEO）

4. **关联交易**
   - 自动在 `src/data/trades.json` 中匹配当日交易
   - 设置 `linkedAnalysis` 字段

## 数据来源配置

脚本当前使用：
- **价格数据**：Binance 公开 API（无需API Key）
- **链上数据**：Fallback 模拟数据（接入 CryptoQuant/Glassnode API 需自行配置）

如需接入真实链上数据，修改 `fetch_onchain_data()` 函数：

```python
def fetch_onchain_data():
    import requests
    # 示例：CryptoQuant API（需注册获取 KEY）
    headers = {"X-CQ-Token": "YOUR_API_KEY"}
    resp = requests.get(
        "https://api.cryptoquant.com/v1/btc/exchange-flows",
        headers=headers, timeout=10
    )
    data = resp.json()
    return {
        "exchangeBalance": f"{data['balance_change']:,}",
        "oiChange":       f"{data['oi_change']:.1f}%",
        "funding":         f"{data['funding_rate']:.3f}%",
        "netFlow7d":      f"{data['net_flow_7d']:,}",
    }
```

## 自动化部署

### 方案 A：GitHub Actions（推荐）

在 `.github/workflows/daily.yml`：

```yaml
name: Daily Analysis
on:
  schedule:
    - cron: "0 0 * * *"  # 北京时间 08:00 = UTC 00:00
  workflow_dispatch:

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.13"
      - run: pip install requests
      - run: python scripts/generate_daily.py
      - run: npm install && npm run build
      - run: npx wrangler pages deploy dist
```

### 方案 B：本地定时任务（Windows）

创建 `scripts/daily_task.bat`：

```batch
@echo off
cd /d "G:\wordbuddy\2026-05-29-15-38-18\1hcrypto"
python scripts\generate_daily.py
npm run build
git add .
git commit -m "daily: %DATE:~0,4%-%DATE:~5,2%-%DATE:~8,2%"
git push
```

任务计划程序中设置每天 08:00 执行。

## 文章质量检查清单

生成后手动检查：
- [ ] 价格数据是否异常（如价格为0或极端值）
- [ ] 方向判断是否符合当前图表
- [ ] 支撑/阻力位是否合理
- [ ] 链上数据是否最新
- [ ] 中文/英文文案是否通顺

## 故障排查

| 问题 | 原因 | 解决 |
|------|------|------|
| `Binance API 失败` | 网络不通 / API限流 | 检查网络，脚本会自动 fallback |
| `ModuleNotFoundError: requests` | 未安装依赖 | `pip install requests` |
| 生成的价格异常 | K线数据解析错误 | 检查 Binance API 返回格式 |
| 构建失败 | 文章模板语法错误 | 检查生成的 `.astro` 文件 |
