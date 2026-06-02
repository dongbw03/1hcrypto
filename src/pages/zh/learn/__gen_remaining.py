import sys
sys.stdout.reconfigure(encoding='utf-8')

articles = [
    {
        "slug": "hardware-wallet-guide",
        "title": "硬件钱包选购指南——不让黑客替你保管比特币",
        "description": "深度对比 Ledger、Trezor、OneKey 等主流硬件钱包，帮你选出真正安全的加密货币存储方案。",
        "content": """<div class="max-w-3xl mx-auto px-4 sm:px-6 py-12">
  <p class="text-[var(--text-muted)] text-sm mb-2">
    <a href="/zh/learn/" class="text-primary hover:underline">← 返回学习中心</a>
  </p>
  <h1 class="text-3xl font-bold mb-4">硬件钱包选购指南——不让黑客替你保管比特币</h1>
  <p class="text-[var(--text-muted)] text-sm mb-8">2026年1月 · 阅读时间约 9 分钟</p>

  <div class="prose prose-invert max-w-none text-[var(--text-secondary)] leading-relaxed">
    <p class="text-lg text-[var(--text-primary)] mb-6">交易所暴雷、钓鱼网站、剪贴板恶意软件——过去十年，散户丢币的原因千百种，但归根结底只有一句话：<strong>私钥碰过网。</strong></p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">为什么手机钱包不够安全？</h2>
    <p>手机是"热钱包"——私钥存储在联网设备上，理论上任何能入侵你手机的人（恶意App、系统漏洞、物理接触）都能把币转走。对于打算长期持有（HODL）超过几个月、金额超过一个月工资的人，热钱包只适合做"零花钱账户"。</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">硬件钱包的核心原理</h2>
    <p>硬件钱包是一台<strong>永远不联网的小型计算机</strong>，专门用来生成和存储私钥。交易签名在硬件内部完成，然后只把"签完名的交易数据"传到电脑/手机——私钥从头到尾没有离开过硬件。</p>
    <p class="mt-3">即使你的电脑中了病毒，黑客也只能看到"签名结果"，看不到私钥本身。</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">主流硬件钱包对比（2026年更新）</h2>

    <div class="overflow-x-auto mt-4">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="border-b border-[var(--border-color)]">
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">型号</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">芯片安全等级</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">支持的链</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">价格区间</th>
            <th class="py-3 text-[var(--text-primary)] font-semibold">适合人群</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Ledger Nano X</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">CC EAL5+</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">5500+ 链和代币</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">~$149</td>
            <td class="py-3 text-[var(--text-secondary)]">综合首选，生态最成熟</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Trezor Safe 5</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">开源固件</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">BTC/ETH/更多</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">~$169</td>
            <td class="py-3 text-[var(--text-secondary)]">重视开源透明度的用户</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">OneKey Classic</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">CC EAL6+</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">BTC/ETH/BSC/更多</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">~$79</td>
            <td class="py-3 text-[var(--text-secondary)]">中文用户，性价比首选</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Ledger Stax</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">CC EAL5+</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">5500+ 链和代币</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">~$279</td>
            <td class="py-3 text-[var(--text-secondary)]">重视屏幕体验和便携</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">选购时的关键判断标准</h2>
    <ul class="list-disc pl-6 space-y-2">
      <li><strong>是否开源固件</strong>：开源意味着全球开发者可以审计代码，后门风险更低。Trezor 是全开源的；Ledger 闭源但芯片经过第三方认证。</li>
      <li><strong>助记词是否离线生成</strong>：正规硬件钱包的助记词只在硬件屏幕上显示，不会出现在电脑/手机屏幕上。</li>
      <li><strong>是否有安全芯片认证</strong>：CC EAL5+ 或更高等级意味着芯片能抵抗物理提取攻击。</li>
      <li><strong>是否支持你持有的链</strong>：如果你主要持有 BTC 和 ETH，几乎所有硬件钱包都支持；如果持有 SOL/ATOM 等，需要提前确认。</li>
    </ul>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">新手推荐方案</h2>
    <p>如果你是第一次买硬件钱包，综合推荐 <strong>Ledger Nano X</strong>（生态最成熟，教程最多）或 <strong>OneKey Classic</strong>（中文支持好，性价比高）。</p>
    <p class="mt-3">预算有限（&lt;100美元）可以选 Trezor Model One（~$69），但屏幕较小，操作体验略逊。</p>

    <div class="mt-10 p-5 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
      <p class="text-sm text-[var(--text-muted)] mb-1">🛡️ 联盟推荐</p>
      <p class="text-[var(--text-secondary)] text-sm">如果你决定购买 Ledger，可以通过本站联盟链接购买，你会获得专属折扣，我也能获得少量佣金用于网站维护：</p>
      <a href="https://shop.ledger.com/?r=5b63cc287be03" class="inline-block mt-2 px-4 py-2 bg-primary text-white rounded-lg text-sm font-medium hover:opacity-90 transition-opacity" target="_blank" rel="sponsored noopener">前往 Ledger 官网购买 →</a>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">使用硬件钱包的 5 条铁律</h2>
    <ol class="list-decimal pl-6 space-y-2">
      <li>助记词<strong>必须手写在纸上</strong>（或刻在金属板上），绝对不要截图、不要存电脑、不要发微信。</li>
      <li>购买渠道只选<strong>官方旗舰店或官网</strong>，二手/拆封设备可能有预装恶意固件。</li>
      <li>收到设备后，<strong>第一次开机必须生成新助记词</strong>——如果设备已经预装了助记词，立刻退货。</li>
      <li>测试小额转账（例如 $20 等值）确认"恢复助记词能找回资产"之后再存入大额资金。</li>
      <li>固件更新只从官方渠道获取，不要点击邮件/短信里的"更新链接"。</li>
    </ol>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">总结</h2>
    <p>硬件钱包不是"可选配件"——对于认真持有加密货币的人来说，它是<strong>必需品</strong>。成本只有你总资产的 0.5%~1%，但能防止 99% 的线上盗窃风险。</p>
    <p class="mt-3">买一个，学会用，你的币就真正属于你了。</p>
  </div>

  <div class="mt-12 pt-8 border-t border-[var(--border-color)]">
    <p class="text-[var(--text-muted)] text-sm">📚 本文属于<a href="/zh/learn/" class="text-primary hover:underline">学习中心</a>系列，持续更新中。</p>
  </div>
</div>"""
    },
    {
        "slug": "how-to-read-candle",
        "title": "如何理解K线图——从一根蜡烛看透多空博弈",
        "description": "不需要任何技术分析基础，用最直白的语言讲清楚K线图的每一个细节，附实战案例。",
        "content": """<div class="max-w-3xl mx-auto px-4 sm:px-6 py-12">
  <p class="text-[var(--text-muted)] text-sm mb-2">
    <a href="/zh/learn/" class="text-primary hover:underline">← 返回学习中心</a>
  </p>
  <h1 class="text-3xl font-bold mb-4">如何理解K线图——从一根蜡烛看透多空博弈</h1>
  <p class="text-[var(--text-muted)] text-sm mb-8">2026年1月 · 阅读时间约 10 分钟</p>

  <div class="prose prose-invert max-w-none text-[var(--text-secondary)] leading-relaxed">
    <p class="text-lg text-[var(--text-primary)] mb-6">K线图（Candlestick Chart）是技术分析的"字母表"——不懂K线，后面的均线、MACD、布林带全是空中楼阁。这篇文章用最直白的方式，把K线讲透。</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">一根K线的四个价格</h2>
    <p>每根K线代表一个时间段（比如1小时、1天）内的四样东西：</p>
    <ul class="list-disc pl-6 space-y-1 mt-3">
      <li><strong>开盘价（Open）</strong>：这个时间段的第一笔成交价</li>
      <li><strong>收盘价（Close）</strong>：这个时间段的最后一笔成交价</li>
      <li><strong>最高价（High）</strong>：这个时间段内的最高成交价</li>
      <li><strong>最低价（Low）</strong>：这个时间段内的最低成交价</li>
    </ul>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">阳线 vs 阴线（国内外差异）</h2>
    <div class="overflow-x-auto mt-4">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="border-b border-[var(--border-color)]">
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">类型</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">国际惯例（TradingView等）</th>
            <th class="py-3 text-[var(--text-primary)] font-semibold">中国A股惯例</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">收盘 &gt; 开盘</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]"><span class="text-green-400">🟢 绿色（涨）</span></td>
            <td class="py-3 text-[var(--text-secondary)]"><span class="text-red-400">🔴 红色（涨）</span></td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">收盘 &lt; 开盘</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]"><span class="text-red-400">🔴 红色（跌）</span></td>
            <td class="py-3 text-[var(--text-secondary)]"><span class="text-green-400">🟢 绿色（跌）</span></td>
          </tr>
        </tbody>
      </table>
    </div>
    <p class="mt-3 text-sm text-[var(--text-muted)]">⚠️ 加密货币交易默认遵循<strong>国际惯例</strong>（绿涨红跌）。如果你是从A股过来的，需要重新适应颜色含义。</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">实体和影线的含义</h2>
    <ul class="list-disc pl-6 space-y-2">
      <li><strong>实体（Body）</strong>：开盘价和收盘价之间的矩形区域。实体越长，说明这个时间段内买卖力量越一边倒。</li>
      <li><strong>上影线（Upper Shadow）</strong>：实体上方的细线，代表最高价。上影线越长，说明上方抛压越重。</li>
      <li><strong>下影线（Lower Shadow）</strong>：实体下方的细线，代表最低价。下影线越长，说明下方有支撑。</li>
    </ul>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">必须认识的 6 种单K线形态</h2>

    <div class="space-y-6 mt-4">
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-2">1. 大阳线（Long Bullish Candle）</h3>
        <p class="text-[var(--text-secondary)] text-sm">收盘价远高于开盘价，实体很长。说明买方完全主导，短期内继续上涨的概率较高。出现在底部时尤其值得关注。</p>
      </div>

      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-2">2. 大阴线（Long Bearish Candle）</h3>
        <p class="text-[var(--text-secondary)] text-sm">收盘价远低于开盘价，实体很长。说明卖方完全主导，短期内继续下跌的概率较高。不要盲目"抄底"。</p>
      </div>

      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-2">3. 锤子线（Hammer）</h3>
        <p class="text-[var(--text-secondary)] text-sm">实体小、下影线很长（&gt;2倍实体）。出现在下跌趋势底部时，是潜在的<strong>反转信号</strong>——说明卖方试图打压但被买方收复失地。</p>
      </div>

      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-2">4. 上吊线（Hanging Man）</h3>
        <p class="text-[var(--text-secondary)] text-sm">形态和锤子线一样，但出现在<strong>上涨趋势顶部</strong>。是潜在的见顶信号，需要下一根K线确认（跌破实体底部）。</p>
      </div>

      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-2">5. 十字星（Doji）</h3>
        <p class="text-[var(--text-secondary)] text-sm">开盘价≈收盘价，实体几乎是一条线。说明多空力量均衡，市场犹豫不决。出现在趋势末端时，是潜在的变盘信号。</p>
      </div>

      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-2">6. 吞没形态（Engulfing）</h3>
        <p class="text-[var(--text-secondary)] text-sm">后一根K线的实体完全"吞没"前一根的实体。看涨吞没（底部）和看跌吞没（顶部）都是较强的反转信号，需要配合成交量确认。</p>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">实战胜率提升技巧</h2>
    <ul class="list-disc pl-6 space-y-2">
      <li><strong>永远看多时间周期</strong>：1分钟K线的信号噪声极大，建议从4小时或日线开始学起。</li>
      <li><strong>结合成交量看</strong>：一根大阳线如果伴随巨量，说明是真涨；如果量能萎缩，可能是诱多。</li>
      <li><strong>支撑阻力位上的K线信号更有效</strong>：在已知支撑位出现的锤子线，远比随机出现的锤子线可靠。</li>
      <li><strong>不要孤立即K线</strong>：单根K线的信号强度有限，必须结合趋势、均线、成交量一起判断。</li>
    </ul>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">新手推荐工具</h2>
    <p>学习K线最推荐 <strong>TradingView</strong>，免费版就支持几乎所有交易所的K线数据，画图工具也很完善。</p>
    <a href="https://cn.tradingview.com/pricing/?share_your_love=dongbw03" class="inline-block mt-3 px-4 py-2 bg-primary text-white rounded-lg text-sm font-medium hover:opacity-90 transition-opacity" target="_blank" rel="sponsored noopener">免费注册 TradingView →</a>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">总结</h2>
    <p>K线是技术分析的起点，但不是终点。学会读K线是必须的，但别指望"看一根K线就能稳定盈利"——那是不存在的。把K线作为"感知市场情绪"的工具，而不是"预测未来的水晶球"。</p>
  </div>

  <div class="mt-12 pt-8 border-t border-[var(--border-color)]">
    <p class="text-[var(--text-muted)] text-sm">📚 本文属于<a href="/zh/learn/" class="text-primary hover:underline">学习中心</a>系列，持续更新中。</p>
  </div>
</div>"""
    },
    {
        "slug": "how-to-buy-crypto-p2p",
        "title": "如何用法币买币——P2P交易完整指南",
        "description": "从银行账户到持有USDT，手把手教你在没有境外银行账户的情况下，安全低成本地买入加密货币。",
        "content": """<div class="max-w-3xl mx-auto px-4 sm:px-6 py-12">
  <p class="text-[var(--text-muted)] text-sm mb-2">
    <a href="/zh/learn/" class="text-primary hover:underline">← 返回学习中心</a>
  </p>
  <h1 class="text-3xl font-bold mb-4">如何用法币买币——P2P交易完整指南</h1>
  <p class="text-[var(--text-muted)] text-sm mb-8">2026年1月 · 阅读时间约 8 分钟</p>

  <div class="prose prose-invert max-w-none text-[var(--text-secondary)] leading-relaxed">
    <p class="text-lg text-[var(--text-primary)] mb-6">对于中国用户来说，"怎么把人民币变成USDT"是进入加密货币世界的第一道门槛。这篇文章把P2P（点对点）买币的完整流程讲清楚。</p>

    <div class="p-4 rounded-xl bg-amber-500/10 border border-amber-500/30 mb-8">
      <p class="text-amber-400 text-sm font-medium">⚠️ 风险提示</p>
      <p class="text-[var(--text-secondary)] text-sm mt-1">P2P交易涉及银行账户风控、冻卡等风险。本文仅供教育参考，不构成金融建议。操作前请了解当地法律法规。</p>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">什么是P2P？</h2>
    <p>P2P（Peer-to-Peer）就是"个人对个人"交易——你通过交易所的担保平台，直接用人民币向其他用户购买USDT（或USDC），资金和币都不经过交易所的"资金池"，而是由平台作为<strong>担保方</strong>托管。</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">推荐平台对比</h2>

    <div class="overflow-x-auto mt-4">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="border-b border-[var(--border-color)]">
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">平台</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">支持支付渠道</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">手续费</th>
            <th class="py-3 text-[var(--text-primary)] font-semibold">备注</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Binance P2P</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">支付宝、微信、银行卡</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0%（商家加点差）</td>
            <td class="py-3 text-[var(--text-secondary)]">流动性最好，商家最多</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">OKX P2P</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">支付宝、微信、银行卡</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0%（商家加点差）</td>
            <td class="py-3 text-[var(--text-secondary)]">中文体验好，KYC较严</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Gate.io P2P</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">银行卡、微信</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0%（商家加点差）</td>
            <td class="py-3 text-[var(--text-secondary)]">币种较多，流动性一般</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Binance P2P 买币完整步骤</h2>
    <ol class="list-decimal pl-6 space-y-3">
      <li><strong>注册并完成KYC</strong>：在 Binance 完成手机/邮箱注册，上传身份证完成实名认证。</li>
      <li><strong>进入P2P页面</strong>：App 首页点击"买币"→"P2P交易"。</li>
      <li><strong>筛选商家</strong>：选择 USDT，筛选条件设为"支付宝/微信支付"，商家认证等级选"已认证商家"，完成订单数 &gt;500。</li>
      <li><strong>下单</strong>：输入购买金额，点击"购买USDT"。系统会把资金托管在平台。</li>
      <li><strong>付款</strong>：按照商家提供的收款信息，在<strong>15分钟内</strong>完成转账。备注里<strong>不要写</strong>"比特币""USDT"等字眼，只写纯数字备注（如果商家要求）。</li>
      <li><strong>确认收款</strong>：商家确认收到款项后，平台会把USDT释放到你的现货钱包。</li>
    </ol>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">降低冻卡风险的 7 条铁律</h2>
    <ul class="list-disc pl-6 space-y-2">
      <li>只和<strong>平台认证商家</strong>交易，不要私下转账。</li>
      <li>单笔金额不要过大，建议 &lt;1万元人民币。</li>
      <li>专卡专用：准备一张<strong>不常用的银行卡</strong>专门用于P2P收款，主卡资金通过"中转卡"转移。</li>
      <li>收到款后<strong>不要立刻转出</strong>，在交易所内停留至少24小时。</li>
      <li>避免夜间（22:00-6:00）大额交易，银行风控系统此时最敏感。</li>
      <li>如果商家要求"分笔转账"，拒绝——这通常是洗钱行为。</li>
      <li>保留所有交易截图和聊天记录，万一银行卡被冻结可以作为申诉材料。</li>
    </ul>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">买完USDT之后呢？</h2>
    <p>USDT到手后，你有几个选择：</p>
    <ul class="list-disc pl-6 space-y-2 mt-3">
      <li><strong>持有USDT</strong>：等合适的时机买入BTC/ETH。</li>
      <li><strong>转入硬件钱包</strong>：如果金额较大，从交易所提到自己的硬件钱包（先小额测试）。</li>
      <li><strong>参与DeFi</strong>：把USDT/ETH转入MetaMask等钱包，参与去中心化交易或质押（高风险）。</li>
    </ul>

    <div class="mt-8 p-5 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
      <p class="text-sm text-[var(--text-muted)] mb-1">🛡️ 联盟推荐</p>
      <p class="text-[var(--text-secondary)] text-sm">注册 Binance 并通过P2P买币，使用以下推荐链接可获得手续费折扣：</p>
      <a href="https://www.bsmkweb.cc/activity/referral-entry/CPA?ref=CPA_00ZIV33RO4" class="inline-block mt-2 px-4 py-2 bg-primary text-white rounded-lg text-sm font-medium hover:opacity-90 transition-opacity" target="_blank" rel="sponsored noopener">注册 Binance（推荐链接）→</a>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">总结</h2>
    <p>P2P是目前中国用户入金的主要通道，但也是风险最高的环节。选择大平台、认证商家、专卡专用、小额分散——这四条能做到，风险就能控制在一个可接受的范围内。</p>
  </div>

  <div class="mt-12 pt-8 border-t border-[var(--border-color)]">
    <p class="text-[var(--text-muted)] text-sm">📚 本文属于<a href="/zh/learn/" class="text-primary hover:underline">学习中心</a>系列，持续更新中。</p>
  </div>
</div>"""
    },
    {
        "slug": "ethereum-gas-fees",
        "title": "以太坊Gas费详解——为什么转一次账要花30美元？",
        "description": "深入讲解以太坊Gas费的运作机制、如何节省Gas费，以及Layer2方案如何彻底解决高手续费问题。",
        "content": """<div class="max-w-3xl mx-auto px-4 sm:px-6 py-12">
  <p class="text-[var(--text-muted)] text-sm mb-2">
    <a href="/zh/learn/" class="text-primary hover:underline">← 返回学习中心</a>
  </p>
  <h1 class="text-3xl font-bold mb-4">以太坊Gas费详解——为什么转一次账要花30美元？</h1>
  <p class="text-[var(--text-muted)] text-sm mb-8">2026年1月 · 阅读时间约 9 分钟</p>

  <div class="prose prose-invert max-w-none text-[var(--text-secondary)] leading-relaxed">
    <p class="text-lg text-[var(--text-primary)] mb-6">如果你在2021-2022年用过以太坊主网，应该对"转一次账花$50"记忆犹新。Gas费是以太坊经济模型的核心，也是它被诟病最多的地方。这篇文章把它讲透。</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Gas是什么？</h2>
    <p>Gas 是以太坊的"燃料"——每执行一笔交易（转账、合约调用、DeFi操作），都需要消耗计算资源，Gas费就是你付给矿工（现在是验证者）的"劳务费"。</p>
    <p class="mt-3">公式很简单：</p>
    <div class="my-4 p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)] font-mono text-sm text-[var(--text-primary)] text-center">
      Gas费 = Gas使用费 × Gas单价（Gwei）
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">EIP-1559：Gas费机制的革命</h2>
    <p>2021年8月的伦敦升级（EIP-1559）改变了Gas费的计算方式：</p>
    <ul class="list-disc pl-6 space-y-2 mt-3">
      <li><strong>基础费用（Base Fee）</strong>：由协议自动调节，随网络拥堵程度上涨或下降。<strong>这部分会被销毁</strong>（不再给验证者），这是ETH通缩的核心机制。</li>
      <li><strong>优先费（Priority Fee / Tip）</strong>：你额外付的小费，用来激励验证者优先打包你的交易。</li>
    </ul>
    <p class="mt-3">所以现在的Gas费 = <code class="text-primary">Base Fee + Tip</code>。</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">为什么Gas费有时候特别贵？</h2>
    <p>以太坊每个区块的Gas上限是 <strong>30,000,000 Gas</strong>。当很多人都想在同一个区块里打包交易时（比如新NFT发行、热门DeFi项目启动），就会竞价——谁给的Tip高，谁先被打包。</p>
    <p class="mt-3">极端情况下（如2021年NFT狂热），Base Fee 能涨到 200+ Gwei，一笔简单转账就要 $50~$100。</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">如何节省Gas费？</h2>

    <div class="space-y-4 mt-4">
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-2">① 选择低峰时段操作</h3>
        <p class="text-[var(--text-secondary)] text-sm">美国东部时间凌晨（北京时间中午12-14点）是以太坊网络最不拥堵的时候，Gas费通常最低。</p>
      </div>

      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-2">② 使用 Layer2</h3>
        <p class="text-[var(--text-secondary)] text-sm">Arbitrum、Optimism、Base 等Layer2的Gas费通常 &lt;$0.1，比主网便宜几百倍。大额资金才需要考虑Layer2的安全权衡。</p>
      </div>

      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-2">③ 批量操作</h3>
        <p class="text-[var(--text-secondary)] text-sm">如果你需要批准代币（approve）然后交易，先在主网做一次，然后在Layer2上多做——每次approve都要花Gas。</p>
      </div>

      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-2">④ 手动设置Gas参数</h3>
        <p class="text-[var(--text-secondary)] text-sm">在 MetaMask 中可以选择"慢速/普通/快速"三个档位，或者自定义Gas单价。如果不急，选"慢速"能省30%~50%。</p>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Layer2 对比（2026年）</h2>

    <div class="overflow-x-auto mt-4">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="border-b border-[var(--border-color)]">
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Layer2</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">技术路线</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">TPS</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">提回主网时间</th>
            <th class="py-3 text-[var(--text-primary)] font-semibold">生态成熟度</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Arbitrum One</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Optimistic Rollup</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">~40,000</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">~7天（挑战期）</td>
            <td class="py-3 text-[var(--text-secondary)]">⭐⭐⭐⭐⭐</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Optimism</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Optimistic Rollup</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">~20,000</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">~7天</td>
            <td class="py-3 text-[var(--text-secondary)]">⭐⭐⭐⭐</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Base</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Optimistic Rollup</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">~13,000</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">~7天</td>
            <td class="py-3 text-[var(--text-secondary)]">⭐⭐⭐⭐</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">zkSync Era</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">ZK Rollup</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">~100,000</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">~1小时</td>
            <td class="py-3 text-[var(--text-secondary)]">⭐⭐⭐</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">总结</h2>
    <p>Gas费高昂是以太坊成长中的阵痛。对于小额用户，<strong>直接使用Layer2</strong>是最实际的解决方案；对于大额用户，选择低峰时段 + 批量操作可以显著降低成本。</p>
    <p class="mt-3">长期来看，以太坊向分片（Sharding）和更高效的Rollup方案演进，Gas费问题会逐渐缓解——但短期内，Layer2是你最好的朋友。</p>
  </div>

  <div class="mt-12 pt-8 border-t border-[var(--border-color)]">
    <p class="text-[var(--text-muted)] text-sm">📚 本文属于<a href="/zh/learn/" class="text-primary hover:underline">学习中心</a>系列，持续更新中。</p>
  </div>
</div>"""
    },
    {
        "slug": "position-management-basics",
        "title": "仓位管理入门——比预测涨跌更重要的事",
        "description": "绝大多数人亏钱不是因为方向看错了，而是因为仓位管理混乱。本文讲解固定比例、固定金额、金字塔加仓等核心策略。",
        "content": """<div class="max-w-3xl mx-auto px-4 sm:px-6 py-12">
  <p class="text-[var(--text-muted)] text-sm mb-2">
    <a href="/zh/learn/" class="text-primary hover:underline">← 返回学习中心</a>
  </p>
  <h1 class="text-3xl font-bold mb-4">仓位管理入门——比预测涨跌更重要的事</h1>
  <p class="text-[var(--text-muted)] text-sm mb-8">2026年1月 · 阅读时间约 10 分钟</p>

  <div class="prose prose-invert max-w-none text-[var(--text-secondary)] leading-relaxed">
    <p class="text-lg text-[var(--text-primary)] mb-6">一个残酷的事实：<strong>绝大多数散户亏钱，不是因为方向看错了，而是因为仓位管理混乱。</strong>看对方向但爆仓，比看错方向更令人绝望。</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">仓位管理的核心目标</h2>
    <ul class="list-disc pl-6 space-y-2">
      <li><strong>生存第一</strong>：确保任何单次亏损都不会让你出局（爆仓或睡不好觉）。</li>
      <li><strong>让利润奔跑</strong>：做对的仓位要能随着趋势发展而变大。</li>
      <li><strong>控制回撤</strong>：账户净值从最高点到最低点的跌幅要可控。</li>
    </ul>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">策略一：固定比例法（最推荐新手）</h2>
    <p>每次交易的风险不超过总资金的 <strong>1%~2%</strong>。</p>
    <p class="mt-3">举例：你有10万本金，单笔最大亏损 = 10万 × 2% = <strong>2000元</strong>。</p>
    <p class="mt-3">如果止损幅度是入场价的 5%，那么：</p>
    <div class="my-4 p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)] font-mono text-sm text-[var(--text-primary)] text-center">
      仓位价值 = 2000 ÷ 5% = 40,000元
    </div>
    <p>也就是说，你用10万本金中的4万来开仓，止损5%时亏损2000元（总资金的2%）。</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">策略二：固定金额法</h2>
    <p>每次用固定金额开仓，不考虑总资产变化。适合资金量较小（&lt;5万）且交易频率较高的人。</p>
    <p class="mt-3">缺点：随着资金增长，固定金额占比会越来越小，资金利用率低；随着资金萎缩，固定金额占比会越来越大，加速亏损。</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">策略三：金字塔加仓法</h2>
    <p>趋势确认后，<strong>顺着盈利方向分批加仓，但每次加仓量递减</strong>。这样平均成本始终有利，且风险可控。</p>
    <div class="overflow-x-auto mt-4">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="border-b border-[var(--border-color)]">
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">批次</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">价格</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">加仓金额</th>
            <th class="py-3 text-[var(--text-primary)] font-semibold">备注</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">第1笔（底仓）</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">$100</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">$2,000</td>
            <td class="py-3 text-[var(--text-secondary)]">趋势初步确认</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">第2笔（加仓）</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">$105</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">$1,500</td>
            <td class="py-3 text-[var(--text-secondary)]">趋势延续，止损移到成本价</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">第3笔（加仓）</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">$110</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">$1,000</td>
            <td class="py-3 text-[var(--text-secondary)]">趋势强劲，移动止损保护利润</td>
          </tr>
        </tbody>
      </table>
    </div>
    <p class="mt-3 text-sm text-[var(--text-muted)]">⚠️ 金字塔加仓只适用于<strong>趋势行情</strong>，震荡行情中会反复打止损。</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">合约交易的仓位管理铁律</h2>
    <ul class="list-disc pl-6 space-y-2">
      <li><strong>杠杆不超过5倍</strong>（新手建议2倍以内）。高杠杆 = 高概率归零。</li>
      <li><strong>全仓模式慎用</strong>：全仓模式下，一个仓位的亏损会吞噬整个账户的保证金。建议用<strong>逐仓模式</strong>。</li>
      <li><strong>永远设置止损</strong>：合约没有止损，等于在高速公路上不系安全带。</li>
      <li><strong>单边持仓不超过总资金的30%</strong>：分散到2-3个不相关的标的，降低相关性风险。</li>
    </ul>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">凯利公式：科学的最优仓位</h2>
    <p>凯利公式给出了理论上最优的仓位比例：</p>
    <div class="my-4 p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)] font-mono text-sm text-[var(--text-primary)] text-center">
      f* = (p × b - q) / b
    </div>
    <p>其中：</p>
    <ul class="list-disc pl-6 space-y-1 mt-3 text-sm">
      <li>f* = 最优仓位比例</li>
      <li>p = 胜率（盈利交易占比）</li>
      <li>q = 败率（1 - p）</li>
      <li>b = 盈亏比（平均盈利 ÷ 平均亏损）</li>
    </ul>
    <p class="mt-3">举例：如果你的策略胜率55%，盈亏比2:1，那么 f* = (0.55×2 - 0.45) / 2 = <strong>32.5%</strong>。</p>
    <p class="mt-3 text-sm text-[var(--text-muted)]">⚠️ 实际应用中建议把凯利公式的结果<strong>减半</strong>使用（即"半凯利"），因为胜率和盈亏比的估计通常有误差。</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">总结</h2>
    <p>仓位管理是交易的"生存系统"。比起精准预测下一次涨跌，<strong>控制每笔交易的风险在总资金的1%~2%</strong>更能让你长期存活下来——而活下来，才有资格谈盈利。</p>
  </div>

  <div class="mt-12 pt-8 border-t border-[var(--border-color)]">
    <p class="text-[var(--text-muted)] text-sm">📚 本文属于<a href="/zh/learn/" class="text-primary hover:underline">学习中心</a>系列，持续更新中。</p>
  </div>
</div>"""
    },
    {
        "slug": "dca-strategy",
        "title": "定投策略——普通人最靠谱的加密货币投资方式",
        "description": "不需要择时、不需要看K线、不需要预测市场，定投（DCA）是用时间换空间的长期投资策略，适合绝大多数上班族。",
        "content": """<div class="max-w-3xl mx-auto px-4 sm:px-6 py-12">
  <p class="text-[var(--text-muted)] text-sm mb-2">
    <a href="/zh/learn/" class="text-primary hover:underline">← 返回学习中心</a>
  </p>
  <h1 class="text-3xl font-bold mb-4">定投策略——普通人最靠谱的加密货币投资方式</h1>
  <p class="text-[var(--text-muted)] text-sm mb-8">2026年1月 · 阅读时间约 8 分钟</p>

  <div class="prose prose-invert max-w-none text-[var(--text-secondary)] leading-relaxed">
    <p class="text-lg text-[var(--text-primary)] mb-6">如果你是一边上班一边想配置一点加密货币，但没有时间盯盘、也不确定什么时候是"好价格"——<strong>定投（DCA, Dollar-Cost Averaging）</strong>就是为你设计的策略。</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">定投是什么？</h2>
    <p>定投就是<strong>不管价格高低，每隔固定时间买入固定金额的资产</strong>。比如每月1号买1000元的BTC，风雨无阻，持续几年。</p>
    <p class="mt-3">这样做的结果是：价格低时买到更多份额，价格高时买到较少份额，长期来看你的<strong>平均成本会低于平均市场价格</strong>。</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">定投 vs 一次性买入：数据说话</h2>
    <p>假设你在2022年1月~2024年12月期间投资BTC，对比两种策略：</p>

    <div class="overflow-x-auto mt-4">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="border-b border-[var(--border-color)]">
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">策略</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">总投入</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">期末市值（2024-12）</th>
            <th class="py-3 text-[var(--text-primary)] font-semibold">收益率</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">一次性买入（2022-01-01）</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">$12,000</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">~$28,000</td>
            <td class="py-3 text-green-400 font-medium">+133%</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">定投（每月$500）</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">$12,000</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">~$22,000</td>
            <td class="py-3 text-green-400 font-medium">+83%</td>
          </tr>
        </tbody>
      </table>
    </div>
    <p class="mt-3 text-sm text-[var(--text-muted)]">结论：牛市中一次性买入略优于定投；但在包含熊市的完整周期中，定投能显著降低"买在最高点"的风险。</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">定投的核心优势</h2>
    <ul class="list-disc pl-6 space-y-2">
      <li><strong>不需要择时</strong>：你永远不知道"底"在哪里，定投让你不需要知道。</li>
      <li><strong>克服情绪干扰</strong>：跌的时候害怕、涨的时候FOMO——定投把决策自动化，情绪不再干扰。</li>
      <li><strong>降低归零风险</strong>：一次性买入如果遇到暴跌，心理承受压力极大；定投分批入场，任何单月的损失都有限。</li>
      <li><strong>强制储蓄</strong>：把投资变成"必选项"，而不是"有剩钱才投"。</li>
    </ul>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">如何设计一个定投计划？</h2>

    <div class="space-y-4 mt-4">
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-2">① 确定周期和金额</h3>
        <p class="text-[var(--text-secondary)] text-sm">推荐<strong>每周或每两周</strong>执行一次。金额建议为月收入的 <strong>5%~15%</strong>，确保即使全部损失也不会影响生活。</p>
      </div>

      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-2">② 选择标的</h3>
        <p class="text-[var(--text-secondary)] text-sm">新手建议80% BTC + 20% ETH。这两个是加密货币中的"大盘蓝筹"，长期存活概率最高。资金量增大后可以加入SOL/BNB等。</p>
      </div>

      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-2">③ 设置自动买入</h3>
        <p class="text-[var(--text-secondary)] text-sm">Binance 的"定投"（Auto-Invest）功能可以设置自动扣款和买入，不需要手动操作。OKX 也有类似功能。</p>
      </div>

      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-2">④ 设定退出规则</h3>
        <p class="text-[var(--text-secondary)] text-sm">定投不是"永远不卖"。建议设定目标收益率（如100%），到达后开始分批止盈，而不是一次性清仓。</p>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Binance 定投设置步骤</h2>
    <ol class="list-decimal pl-6 space-y-2">
      <li>登录 Binance → 点击"理财" → "定投（Auto-Invest）"</li>
      <li>选择要定投的币种（建议BTC或ETH）</li>
      <li>设置定投金额和频率（建议每周一次，金额根据收入定）</li>
      <li>选择"用USDT定投"或"用信用卡/借记卡定投"</li>
      <li>确认并启用——之后系统会自动执行</li>
    </ol>

    <div class="mt-8 p-5 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
      <p class="text-sm text-[var(--text-muted)] mb-1">🛡️ 联盟推荐</p>
      <p class="text-[var(--text-secondary)] text-sm">使用 Binance 定投功能，注册时通过推荐链接可获得手续费折扣：</p>
      <a href="https://www.bsmkweb.cc/activity/referral-entry/CPA?ref=CPA_00ZIV33RO4" class="inline-block mt-2 px-4 py-2 bg-primary text-white rounded-lg text-sm font-medium hover:opacity-90 transition-opacity" target="_blank" rel="sponsored noopener">注册 Binance 开启定投 →</a>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">定投的局限性</h2>
    <ul class="list-disc pl-6 space-y-2">
      <li>在持续上涨的牛市中，定投的收益低于一次性买入（但你永远不知道牛市什么时候开始）。</li>
      <li>需要<strong>极强的纪律性</strong>——熊市中看着账户亏损还能坚持买入，是反人性的。</li>
      <li>如果选择的标的长期归零（比如某些小币），定投只会让你亏得更多。</li>
    </ul>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">总结</h2>
    <p>定投不会让你"暴富"，但能让你以极低的压力参与加密货币的长期增长。对于没有时间盯盘、不想承受高波动的上班族来说，这是<strong>最靠谱的入场方式</strong>。</p>
    <p class="mt-3">开始定投的最好时机是去年，第二名是今天。</p>
  </div>

  <div class="mt-12 pt-8 border-t border-[var(--border-color)]">
    <p class="text-[var(--text-muted)] text-sm">📚 本文属于<a href="/zh/learn/" class="text-primary hover:underline">学习中心</a>系列，持续更新中。</p>
  </div>
</div>"""
    }
]

base = "G:/wordbuddy/2026-05-29-15-38-18/1hcrypto/src/pages/zh/learn/"

for article in articles:
    slug = article["slug"]
    title = article["title"]
    desc = article["description"]
    content = article["content"]

    # Fix import path - should be ../../layouts/ (2 levels up from /zh/learn/)
    file_content = f"""---
import BaseLayout from '../../layouts/BaseLayout.astro';
---

<BaseLayout title="{title} - 1H币研" lang="zh" description="{desc}">
{content}
</BaseLayout>
"""
    filepath = base + slug + ".astro"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(file_content)
    print(f"✅ Written: {slug}.astro")

print("\nDone. Total:", len(articles), "articles.")
