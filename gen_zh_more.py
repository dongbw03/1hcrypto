import sys
sys.stdout.reconfigure(encoding='utf-8')

# 继续生成中文文章（交易所介绍、更多实用主题）
articles = [
    {
        "slug": "binance-review",
        "title": "Binance 交易所全面评测（2026）",
        "description": "深度评测全球最大加密货币交易所 Binance：手续费、安全性、支持的币种、P2P 体验。",
        "content": """<div class="max-w-3xl mx-auto px-4 sm:px-6 py-12">
  <p class="text-[var(--text-muted)] text-sm mb-2">
    <a href="/zh/learn/" class="text-primary hover:underline">← 返回学习中心</a>
  </p>
  <h1 class="text-3xl font-bold mb-4">Binance 交易所全面评测（2026）</h1>
  <p class="text-[var(--text-muted)] text-sm mb-8">2026年1月 · 阅读时间约 10 分钟</p>

  <div class="prose prose-invert max-w-none text-[var(--text-secondary)] leading-relaxed">
    <p class="text-lg text-[var(--text-primary)] mb-6">Binance 是全球交易量最大的加密货币交易所，但它是不是适合你？这篇评测从手续费、安全性、用户体验等多个维度深度分析。</p>

    <div class="flex items-center gap-4 p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)] mb-8">
      <div class="text-center">
        <p class="text-3xl font-bold text-primary">9.2</p>
        <p class="text-xs text-[var(--text-muted)]">综合评分</p>
      </div>
      <div class="flex-1 grid grid-cols-2 gap-2 text-sm">
        <div><span class="text-[var(--text-muted)]">手续费：</span> <span class="text-green-400">0.1%</span></div>
        <div><span class="text-[var(--text-muted)]">币种：</span> <span class="text-[var(--text-primary)]">600+</span></div>
        <div><span class="text-[var(--text-muted)]">KYC：</span> <span class="text-[var(--text-primary)]">需要</span></div>
        <div><span class="text-[var(--text-muted)]">中文：</span> <span class="text-green-400">✅ 支持</span></div>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">核心优势</h2>
    <div class="space-y-4 mt-4">
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">① 流动性最高</h3>
        <p class="text-[var(--text-secondary)] text-sm">全球最大的订单簿深度，大额交易滑点最低。对于日交易额 >10万美元的用户，Binance 是唯一选择。</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">② 手续费最低</h3>
        <p class="text-[var(--text-secondary)] text-sm">现货交易 0.1%，持有 BNB 可再打 75 折。合约交易费率更低（Maker 0.02%）。</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">③ 产品线最全</h3>
        <p class="text-[var(--text-secondary)] text-sm">现货、合约、期权、理财产品、Launchpad（新币上线）、NFT 市场——应有尽有。</p>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">手续费详解</h2>
    <div class="overflow-x-auto mt-4">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="border-b border-[var(--border-color)]">
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">产品</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Maker 费率</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Taker 费率</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">现货交易</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0.1%</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0.1%</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">合约交易（U 本位）</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0.02%</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0.04%</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">合约交易（币本位）</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0.01%</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0.05%</td>
          </tr>
        </tbody>
      </table>
    </div>
    <p class="mt-3 text-sm text-[var(--text-muted)]">持有 BNB 抵扣手续费可享受额外 25% 折扣。</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">安全性评估</h2>
    <div class="space-y-3 mt-4">
      <div class="flex items-start gap-3 p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <span class="text-green-400 mt-0.5">✅</span>
        <div>
          <p class="text-[var(--text-primary)] font-medium text-sm">SAFU 基金</p>
          <p class="text-[var(--text-muted)] text-xs">用户资产保险基金，覆盖极端情况下的用户损失。</p>
        </div>
      </div>
      <div class="flex items-start gap-3 p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <span class="text-green-400 mt-0.5">✅</span>
        <div>
          <p class="text-[var(--text-primary)] font-medium text-sm">冷钱包存储</p>
          <p class="text-[var(--text-muted)] text-xs">95% 的用户资产存储在离线冷钱包中。</p>
        </div>
      </div>
      <div class="flex items-start gap-3 p-4 rounded-xl bg-amber-500/10 border border-amber-500/30">
        <span class="text-amber-400 mt-0.5">⚠️</span>
        <div>
          <p class="text-[var(--text-primary)] font-medium text-sm">监管风险</p>
          <p class="text-[var(--text-muted)] text-xs">在多个国家和地区面临监管压力，美国用户需使用 Binance.US（功能受限）。</p>
        </div>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">适合人群</h2>
    <div class="space-y-4 mt-4">
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <p class="text-[var(--text-primary)] font-medium text-sm mb-1">✅ 推荐：活跃交易者</p>
        <p class="text-[var(--text-secondary)] text-sm">低手续费 + 高流动性 = 频繁交易者的首选。</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <p class="text-[var(--text-primary)] font-medium text-sm mb-1">✅ 推荐：山寨币猎手</p>
        <p class="text-[var(--text-secondary)] text-sm">上新币最快，很多小币在 Binance 上线后才会被市场发现。</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <p class="text-[var(--text-primary)] font-medium text-sm mb-1">❌ 不推荐：美国用户</p>
        <p class="text-[var(--text-secondary)] text-sm">Binance.US 功能大幅缩水，建议使用 Coinbase 或 Kraken。</p>
      </div>
    </div>

    <div class="mt-10 p-5 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
      <p class="text-sm text-[var(--text-muted)] mb-1">🛡️ 联盟推荐</p>
      <p class="text-[var(--text-secondary)] text-sm">通过以下推荐链接注册 Binance，可获得手续费折扣：</p>
      <a href="https://www.bsmkweb.cc/activity/referral-entry/CPA?ref=CPA_00ZIV33RO4" class="inline-block mt-2 px-4 py-2 bg-primary text-white rounded-lg text-sm font-medium hover:opacity-90 transition-opacity" target="_blank" rel="sponsored noopener">注册 Binance（推荐链接）→</a>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">总结</h2>
    <p>Binance 在 2026 年依然是<strong>综合性最强</strong>的加密货币交易所。如果你只能选一个交易所，选它不会错。但要注意监管风险，大额资产建议提到硬件钱包。</p>
  </div>

  <div class="mt-12 pt-8 border-t border-[var(--border-color)]">
    <p class="text-[var(--text-muted)] text-sm">📚 本文属于<a href="/zh/learn/" class="text-primary hover:underline">学习中心</a>系列，持续更新中。</p>
  </div>
</div>"""
    },
    {
        "slug": "okx-review",
        "title": "OKX 交易所评测（2026）——合约交易的首选",
        "description": "深度评测 OKX：合约交易体验、手续费、安全性、中文支持，以及与 Binance 的对比。",
        "content": """<div class="max-w-3xl mx-auto px-4 sm:px-6 py-12">
  <p class="text-[var(--text-muted)] text-sm mb-2">
    <a href="/zh/learn/" class="text-primary hover:underline">← 返回学习中心</a>
  </p>
  <h1 class="text-3xl font-bold mb-4">OKX 交易所评测（2026）——合约交易的首选</h1>
  <p class="text-[var(--text-muted)] text-sm mb-8">2026年1月 · 阅读时间约 9 分钟</p>

  <div class="prose prose-invert max-w-none text-[var(--text-secondary)] leading-relaxed">
    <p class="text-lg text-[var(--text-primary)] mb-6">OKX（原 OKEx）在合约交易领域的体验是全球顶尖的。对于中文用户来说，它可能是比 Binance 更好的选择。</p>

    <div class="flex items-center gap-4 p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)] mb-8">
      <div class="text-center">
        <p class="text-3xl font-bold text-primary">8.8</p>
        <p class="text-xs text-[var(--text-muted)]">综合评分</p>
      </div>
      <div class="flex-1 grid grid-cols-2 gap-2 text-sm">
        <div><span class="text-[var(--text-muted)]">手续费：</span> <span class="text-green-400">0.08%</span></div>
        <div><span class="text-[var(--text-muted)]">合约：</span> <span class="text-green-400">⭐⭐⭐⭐⭐</span></div>
        <div><span class="text-[var(--text-muted)]">KYC：</span> <span class="text-[var(--text-primary)]">需要</span></div>
        <div><span class="text-[var(--text-muted)]">中文：</span> <span class="text-green-400">✅ 原生</span></div>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">核心优势</h2>
    <div class="space-y-4 mt-4">
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">① 合约交易体验最佳</h3>
        <p class="text-[var(--text-secondary)] text-sm">OKX 的合约系统是全球最稳定的之一，支持 100+ 种合约品种，API 延迟极低。</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">② 中文支持最好</h3>
        <p class="text-[var(--text-secondary)] text-sm">客服、界面、帮助文档全中文，对中文用户极其友好。</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">③ 跟单交易</h3>
        <p class="text-[var(--text-secondary)] text-sm">可以自动跟随优秀交易员的下单，适合还没掌握交易技巧的新手。</p>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">OKX vs. Binance 对比</h2>
    <div class="overflow-x-auto mt-4">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="border-b border-[var(--border-color)]">
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">维度</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">OKX</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Binance</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">现货流动性</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">⭐⭐⭐⭐</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">⭐⭐⭐⭐⭐</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">合约交易</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">⭐⭐⭐⭐⭐</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">⭐⭐⭐⭐</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">中文支持</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">⭐⭐⭐⭐⭐</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">⭐⭐⭐</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">币种数量</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">~350</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">600+</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">跟单交易：新手利器</h2>
    <p>OKX 的"跟单"功能让你可以选择收益率高的交易员，自动复制他们的开仓/平仓操作。</p>
    <div class="my-4 p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
      <p class="text-[var(--text-primary)] font-medium text-sm mb-2">使用跟单的注意事项：</p>
      <ul class="list-disc pl-6 space-y-1 text-sm text-[var(--text-secondary)]">
        <li>看历史收益率，不要只看最近一周</li>
        <li>选择回撤小（<30%）的交易员</li>
        <li>跟单金额不要超过总资金的 20%</li>
        <li>定期检查跟单效果，及时停止亏损的跟单</li>
      </ul>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">手续费结构</h2>
    <div class="overflow-x-auto mt-4">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="border-b border-[var(--border-color)]">
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">产品</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Maker</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Taker</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">现货</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0.08%</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0.10%</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">永续合约</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0.02%</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0.05%</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="mt-10 p-5 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
      <p class="text-sm text-[var(--text-muted)] mb-1">🛡️ 联盟推荐</p>
      <p class="text-[var(--text-secondary)] text-sm">通过以下推荐链接注册 OKX，可获得专属奖励：</p>
      <a href="https://www.kxmqpwrlvjt.com/join/47930867" class="inline-block mt-2 px-4 py-2 bg-primary text-white rounded-lg text-sm font-medium hover:opacity-90 transition-opacity" target="_blank" rel="sponsored noopener">注册 OKX（推荐链接）→</a>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">总结</h2>
    <p>OKX 是<strong>合约交易者</strong>和<strong>中文用户</strong>的最佳选择。如果你主要做合约交易，OKX 的产品体验明显优于 Binance。如果你主要买现货山寨币，Binance 的币种更多。</p>
  </div>

  <div class="mt-12 pt-8 border-t border-[var(--border-color)]">
    <p class="text-[var(--text-muted)] text-sm">📚 本文属于<a href="/zh/learn/" class="text-primary hover:underline">学习中心</a>系列，持续更新中。</p>
  </div>
</div>"""
    },
    {
        "slug": "bybit-review",
        "title": "Bybit 交易所评测（2026）——合约交易的新锐力量",
        "description": "Bybit 以清晰的界面和低延迟合约交易著称，本文深度评测其优劣势。",
        "content": """<div class="max-w-3xl mx-auto px-4 sm:px-6 py-12">
  <p class="text-[var(--text-muted)] text-sm mb-2">
    <a href="/zh/learn/" class="text-primary hover:underline">← 返回学习中心</a>
  </p>
  <h1 class="text-3xl font-bold mb-4">Bybit 交易所评测（2026）——合约交易的新锐力量</h1>
  <p class="text-[var(--text-muted)] text-sm mb-8">2026年1月 · 阅读时间约 8 分钟</p>

  <div class="prose prose-invert max-w-none text-[var(--text-secondary)] leading-relaxed">
    <p class="text-lg text-[var(--text-primary)] mb-6">Bybit 成立于 2018 年，虽然比 Binance 和 OKX 年轻，但凭借清晰的界面和低延迟的交易引擎，已经成为<strong>合约交易者</strong>的热门选择。</p>

    <div class="flex items-center gap-4 p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)] mb-8">
      <div class="text-center">
        <p class="text-3xl font-bold text-primary">8.5</p>
        <p class="text-xs text-[var(--text-muted)]">综合评分</p>
      </div>
      <div class="flex-1 grid grid-cols-2 gap-2 text-sm">
        <div><span class="text-[var(--text-muted)]">手续费：</span> <span class="text-green-400">0.1%</span></div>
        <div><span class="text-[var(--text-muted)]">界面：</span> <span class="text-green-400">⭐⭐⭐⭐⭐</span></div>
        <div><span class="text-[var(--text-muted)]">KYC：</span> <span class="text-[var(--text-primary)]">需要</span></div>
        <div><span class="text-[var(--text-muted)]">中文：</span> <span class="text-green-400">✅ 支持</span></div>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">核心优势</h2>
    <div class="space-y-4 mt-4">
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">① 界面最清晰</h3>
        <p class="text-[var(--text-secondary)] text-sm">Bybit 的交易界面被认为是主流交易所中最干净、最易用的。新手能快速上手。</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">② 合约交易延迟低</h3>
        <p class="text-[var(--text-secondary)] text-sm">交易引擎基于高频交易架构，API 延迟极低，适合量化交易。</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">③ 模拟盘功能</h3>
        <p class="text-[var(--text-secondary)] text-sm">提供完整的模拟交易环境，新手可以零风险练习合约交易。</p>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">手续费结构</h2>
    <div class="overflow-x-auto mt-4">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="border-b border-[var(--border-color)]">
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">产品</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Maker</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Taker</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">现货</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0.1%</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0.1%</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">永续合约</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0.02%</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0.055%</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Bybit vs. OKX vs. Binance</h2>
    <div class="overflow-x-auto mt-4">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="border-b border-[var(--border-color)]">
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">维度</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Bybit</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">OKX</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Binance</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">界面易用性</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">⭐⭐⭐⭐⭐</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">⭐⭐⭐⭐</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">⭐⭐⭐</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">合约品种</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">~200</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">100+</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">~300</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">现货币种</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">~350</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">~350</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">600+</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">适合人群</h2>
    <div class="space-y-4 mt-4">
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <p class="text-[var(--text-primary)] font-medium text-sm mb-1">✅ 推荐：合约交易新手</p>
        <p class="text-[var(--text-secondary)] text-sm">界面清晰 + 模拟盘 = 学习成本最低。</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <p class="text-[var(--text-primary)] font-medium text-sm mb-1">✅ 推荐：量化交易者</p>
        <p class="text-[var(--text-secondary)] text-sm">API 延迟低，WebSocket 推送稳定。</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <p class="text-[var(--text-primary)] font-medium text-sm mb-1">❌ 不推荐：山寨币猎手</p>
        <p class="text-[var(--text-secondary)] text-sm">上币速度慢于 Binance，小币种数量有限。</p>
      </div>
    </div>

    <div class="mt-10 p-5 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
      <p class="text-sm text-[var(--text-muted)] mb-1">🛡️ 联盟推荐</p>
      <p class="text-[var(--text-secondary)] text-sm">通过以下推荐链接注册 Bybit，可获得专属奖励：</p>
      <a href="https://www.bybit.com/invite?ref=BKWZKJN&medium=referral&utm_campaign=evergreen&share_to=link" class="inline-block mt-2 px-4 py-2 bg-primary text-white rounded-lg text-sm font-medium hover:opacity-90 transition-opacity" target="_blank" rel="sponsored noopener">注册 Bybit（推荐链接）→</a>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">总结</h2>
    <p>Bybit 是<strong>合约交易新手</strong>的最佳入门平台——界面清晰、模拟盘完善、客服响应快。如果你已经是有经验的交易者，OKX 和 Binance 的币种更多、流动性更好。</p>
  </div>

  <div class="mt-12 pt-8 border-t border-[var(--border-color)]">
    <p class="text-[var(--text-muted)] text-sm">📚 本文属于<a href="/zh/learn/" class="text-primary hover:underline">学习中心</a>系列，持续更新中。</p>
  </div>
</div>"""
    },
    {
        "slug": "tradingview-guide",
        "title": "TradingView 完全指南——加密货币技术分析的最佳工具",
        "description": "TradingView 是加密货币技术分析的标准工具，本文教你如何使用它进行K线分析和画线。",
        "content": """<div class="max-w-3xl mx-auto px-4 sm:px-6 py-12">
  <p class="text-[var(--text-muted)] text-sm mb-2">
    <a href="/zh/learn/" class="text-primary hover:underline">← 返回学习中心</a>
  </p>
  <h1 class="text-3xl font-bold mb-4">TradingView 完全指南——加密货币技术分析的最佳工具</h1>
  <p class="text-[var(--text-muted)] text-sm mb-8">2026年1月 · 阅读时间约 9 分钟</p>

  <div class="prose prose-invert max-w-none text-[var(--text-secondary)] leading-relaxed">
    <p class="text-lg text-[var(--text-primary)] mb-6">如果你认真做技术分析，<strong>TradingView</strong> 是唯一的选择。它免费版就足够新手使用，付费版则提供专业级功能。</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">为什么选择 TradingView？</h2>
    <ul class="list-disc pl-6 space-y-2">
      <li><strong>数据最准确</strong>：直接对接各大交易所，K线数据比大部分交易所自带图表更准确。</li>
      <li><strong>画线工具最全</strong>：趋势线、斐波那契、江恩角度——应有尽有。</li>
      <li><strong>社区最活跃</strong>：你可以看到其他分析师的观点和画线，作为参考。</li>
      <li><strong>多平台同步</strong>：网页版、桌面端、手机 App 完全同步。</li>
    </ul>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">免费版 vs. 付费版对比</h2>
    <div class="overflow-x-auto mt-4">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="border-b border-[var(--border-color)]">
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">功能</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">免费版</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Pro（$14.95/月）</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">同时打开图表数</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">1</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">2</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">指标数量/图表</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">3</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">10</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">广告</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">有</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">无</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">K线数据保存</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">3个月</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">无限</td>
          </tr>
        </tbody>
      </table>
    </div>
    <p class="mt-3 text-sm text-[var(--text-muted)]">结论：新手用免费版足够。当你需要同时看多个交易对时，再升级 Pro。</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">新手必学的 5 个功能</h2>
    <div class="space-y-4 mt-4">
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-2">1. 切换交易对</h3>
        <p class="text-[var(--text-secondary)] text-sm">在顶部搜索框输入 "BTCUSDT" 或 "ETHUSDT"，选择 Binance 或 OKX 数据源。</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-2">2. 添加指标</h3>
        <p class="text-[var(--text-secondary)] text-sm">点击图表上方的 "指标" 按钮，搜索 "MACD"、"RSI"、"布林带" 等常用指标。</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-2">3. 画线工具</h3>
        <p class="text-[var(--text-secondary)] text-sm">左侧工具栏选择 "趋势线" 或 "斐波那契回调"，在K线图上画出支撑/阻力位。</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-2">4. 多时间周期分析</h3>
        <p class="text-[var(--text-secondary)] text-sm">同时打开日线（判断趋势）和 4 小时线（找入场点），提高交易胜率。</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-2">5. 设置价格提醒</h3>
        <p class="text-[var(--text-secondary)] text-sm">右键点击K线图 → "添加价格提醒"，当价格到达指定位置时推送通知到手机。</p>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">加密货币专用的交易对推荐</h2>
    <ul class="list-disc pl-6 space-y-2">
      <li><strong>BTC/USDT（Binance）</strong>：流动性最好，适合大资金。</li>
      <li><strong>ETH/USDT（Binance）</strong>：以太坊价格的标准参考。</li>
      <li><strong>BTC/USD（Coinbase）</strong>：机构资金偏好的交易对，走势更"干净"。</li>
    </ul>

    <div class="mt-10 p-5 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
      <p class="text-sm text-[var(--text-muted)] mb-1">🛡️ 联盟推荐</p>
      <p class="text-[var(--text-secondary)] text-sm">通过以下推荐链接注册 TradingView Pro，可获得折扣：</p>
      <a href="https://cn.tradingview.com/pricing/?share_your_love=dongbw03" class="inline-block mt-2 px-4 py-2 bg-primary text-white rounded-lg text-sm font-medium hover:opacity-90 transition-opacity" target="_blank" rel="sponsored noopener">注册 TradingView Pro →</a>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">总结</h2>
    <p>TradingView 是加密货币技术分析的<strong>标准工具</strong>。免费版就能满足大部分新手需求。当你开始认真交易时，Pro 版的"多图表"和"无广告"体验非常值得 $14.95/月。</p>
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

    file_content = f"""---
import BaseLayout from '../../../layouts/BaseLayout.astro';
---

<BaseLayout title="{title} - 1H币研" lang="zh" description="{desc}">
{content}
</BaseLayout>
"""
    filepath = base + slug + ".astro"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(file_content)
    print(f"✅ 写入: {slug}.astro")

print(f"\n完成。共写入 {len(articles)} 篇文章。")
