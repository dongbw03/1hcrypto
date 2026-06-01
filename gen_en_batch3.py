import sys
sys.stdout.reconfigure(encoding='utf-8')

articles = [
    {
        "slug": "defi-intro",
        "title": "DeFi 101: What It Is and Why It Matters",
        "description": "Decentralized Finance (DeFi) lets you lend, borrow, and trade without banks. Here's how it works.",
        "content": """<div class="max-w-3xl mx-auto px-4 sm:px-6 py-12">
  <p class="text-[var(--text-muted)] text-sm mb-2">
    <a href="/en/learn/" class="text-primary hover:underline">← Back to Learning Center</a>
  </p>
  <h1 class="text-3xl font-bold mb-4">DeFi 101: What It Is and Why It Matters</h1>
  <p class="text-[var(--text-muted)] text-sm mb-8">January 2026 · 10 min read</p>

  <div class="prose prose-invert max-w-none text-[var(--text-secondary)] leading-relaxed">
    <p class="text-lg text-[var(--text-primary)] mb-6">DeFi (Decentralized Finance) is financial services running on smart contracts — no banks, no companies, no permission needed.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">What Problems Does DeFi Solve?</h2>
    <ul class="list-disc pl-6 space-y-2">
      <li><strong>Banking the Unbanked</strong>: 1.4B people worldwide have no bank account but do have a smartphone.</li>
      <li><strong>24/7 Markets</strong>: No "markets are closed" — DeFi runs on weekends and holidays.</li>
      <li><strong>Transparency</strong>: Every loan, swap, and yield payout is visible on-chain.</li>
      <li><strong>Composability</strong>: DeFi protocols can plug into each other like Lego blocks.</li>
    </ul>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Core DeFi Primitives</h2>
    <div class="space-y-4 mt-4">
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">Decentralized Exchanges (DEXs)</h3>
        <p class="text-[var(--text-secondary)] text-sm">Trade tokens directly from your wallet. No account, no KYC. Examples: Uniswap, Curve, PancakeSwap.</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">Lending & Borrowing</h3>
        <p class="text-[var(--text-secondary)] text-sm">Deposit ETH → borrow USDC → buy more ETH (leverage). Or deposit stablecoins → earn ~5-10% APY. Examples: Aave, Compound.</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">Yield Farming</h3>
        <p class="text-[var(--text-secondary)] text-sm">Provide liquidity to DEX pools and earn trading fees + rewards. Higher yield, higher risk (impermanent loss).</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">Stablecoin Protocols</h3>
        <p class="text-[var(--text-secondary)] text-sm">Mint decentralized stablecoins (like DAI) by locking crypto as collateral. No central company.</p>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Risks You Must Understand</h2>
    <div class="space-y-3 mt-4">
      <div class="flex items-start gap-3 p-4 rounded-xl bg-red-500/10 border border-red-500/30">
        <span class="text-red-400 mt-0.5">⚠️</span>
        <div>
          <p class="text-[var(--text-primary)] font-medium text-sm">Smart Contract Bugs</p>
          <p class="text-[var(--text-muted)] text-xs">Code vulnerabilities have led to $10B+ in DeFi hacks. Only use audited protocols with $1B+ TVL.</p>
        </div>
      </div>
      <div class="flex items-start gap-3 p-4 rounded-xl bg-red-500/10 border border-red-500/30">
        <span class="text-red-400 mt-0.5">⚠️</span>
        <div>
          <p class="text-[var(--text-primary)] font-medium text-sm">Impermanent Loss</p>
          <p class="text-[var(--text-muted)] text-xs">When providing liquidity, if one token moons, your position value drops vs. just holding. Understand this before farming.</p>
        </div>
      </div>
      <div class="flex items-start gap-3 p-4 rounded-xl bg-red-500/10 border border-red-500/30">
        <span class="text-red-400 mt-0.5">⚠️</span>
        <div>
          <p class="text-[var(--text-primary)] font-medium text-sm">Rug Pulls</p>
          <p class="text-[var(--text-muted)] text-xs">Developers can create a token, provide liquidity, then drain the pool. Always check if liquidity is locked.</p>
        </div>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">How to Get Started with DeFi (Safely)</h2>
    <ol class="list-decimal pl-6 space-y-2">
      <li>Get a self-custody wallet (MetaMask, Rabby, or Trust Wallet).</li>
      <li>Buy ETH on a major exchange and withdraw to your wallet.</li>
      <li>Start with a small amount ($100-500) to learn the mechanics.</li>
      <li>Use well-established protocols: Uniswap, Aave, Compound.</li>
      <li>Keep records for taxes — every DeFi transaction is a taxable event in most jurisdictions.</li>
    </ol>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">The Bottom Line</h2>
    <p>DeFi is powerful but unforgiving. There's no customer support — if you make a mistake, your money is gone. Start small, use established protocols, and never invest more than you can afford to lose while learning.</p>
  </div>

  <div class="mt-12 pt-8 border-t border-[var(--border-color)]">
    <p class="text-[var(--text-muted)] text-sm">📚 Part of <a href="/en/learn/" class="text-primary hover:underline">Learning Center</a>.</p>
  </div>
</div>"""
    },
    {
        "slug": "smart-contracts",
        "title": "Smart Contracts: Code That Runs Exactly As Written",
        "description": "Smart contracts are self-executing programs on the blockchain. Here's what they can (and can't) do.",
        "content": """<div class="max-w-3xl mx-auto px-4 sm:px-6 py-12">
  <p class="text-[var(--text-muted)] text-sm mb-2">
    <a href="/en/learn/" class="text-primary hover:underline">← Back to Learning Center</a>
  </p>
  <h1 class="text-3xl font-bold mb-4">Smart Contracts: Code That Runs Exactly As Written</h1>
  <p class="text-[var(--text-muted)] text-sm mb-8">January 2026 · 8 min read</p>

  <div class="prose prose-invert max-w-none text-[var(--text-secondary)] leading-relaxed">
    <p class="text-lg text-[var(--text-primary)] mb-6">A smart contract is a program deployed on a blockchain that automatically executes when predetermined conditions are met. No lawyers, no middlemen, no trust needed.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">The Vending Machine Analogy</h2>
    <p>Think of a smart contract like a vending machine:</p>
    <ul class="list-disc pl-6 space-y-1 mt-3">
      <li>You insert $2 (input condition met).</li>
      <li>The machine automatically gives you a soda (execution).</li>
      <li>No employee needed. The machine can't "change its mind."</li>
    </ul>
    <p class="mt-3">A smart contract is the same — but digital, and can handle millions of dollars.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">What Can Smart Contracts Do?</h2>
    <div class="space-y-4 mt-4">
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">DeFi Applications</h3>
        <p class="text-[var(--text-secondary)] text-sm">Automated market makers (AMMs), lending protocols, yield aggregators — all are smart contracts.</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">NFTs and Digital Ownership</h3>
        <p class="text-[var(--text-secondary)] text-sm">NFT minting, trading, and royalty payments are all enforced by smart contracts.</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">DAO Governance</h3>
        <p class="text-[var(--text-secondary)] text-sm">Decentralized Autonomous Organizations use smart contracts to let token holders vote on proposals.</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">Cross-Chain Bridges</h3>
        <p class="text-[var(--text-secondary)] text-sm">Move assets between blockchains (e.g., ETH → Solana) via smart contracts that lock on one side and mint on the other.</p>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">The "Code Is Law" Philosophy</h2>
    <p>In smart contract systems, the code is the ultimate authority. If there's a bug and someone drains $100M, <strong>there is no refund</strong>. This is both the greatest strength and the greatest weakness of DeFi.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Major Smart Contract Platforms (2026)</h2>
    <div class="overflow-x-auto mt-4">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="border-b border-[var(--border-color)]">
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Platform</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Language</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">TVL (approx)</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Ethereum</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Solidity</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">~$60B</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Solana</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Rust</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">~$5B</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Arbitrum</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Solidity (EVM)</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">~$3B</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Famous Smart Contract Hacks</h2>
    <div class="space-y-3 mt-4">
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <p class="text-[var(--text-primary)] font-medium text-sm">The DAO Hack (2016) — $60M</p>
        <p class="text-[var(--text-muted)] text-xs">A reentrancy bug allowed an attacker to drain funds repeatedly. Led to the controversial Ethereum hard fork (ETC/ETH split).</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <p class="text-[var(--text-primary)] font-medium text-sm">Wormhole Bridge (2022) — $326M</p>
        <p class="text-[var(--text-muted)] text-xs">A signature verification bug allowed fake minting of Wormhole-wrapped ETH.</p>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">The Bottom Line</h2>
    <p>Smart contracts are revolutionary — they enable trustless financial systems. But "code is law" means bugs are expensive. Only interact with audited, battle-tested contracts, and never put in more than you can afford to lose.</p>
  </div>

  <div class="mt-12 pt-8 border-t border-[var(--border-color)]">
    <p class="text-[var(--text-muted)] text-sm">📚 Part of <a href="/en/learn/" class="text-primary hover:underline">Learning Center</a>.</p>
  </div>
</div>"""
    },
    {
        "slug": "wallet-guide",
        "title": "Crypto Wallets Explained: Hot, Cold, and Everything In Between",
        "description": "Not all wallets are created equal. Learn the differences and pick the right one for your needs.",
        "content": """<div class="max-w-3xl mx-auto px-4 sm:px-6 py-12">
  <p class="text-[var(--text-muted)] text-sm mb-2">
    <a href="/en/learn/" class="text-primary hover:underline">← Back to Learning Center</a>
  </p>
  <h1 class="text-3xl font-bold mb-4">Crypto Wallets Explained: Hot, Cold, and Everything In Between</h1>
  <p class="text-[var(--text-muted)] text-sm mb-8">January 2026 · 9 min read</p>

  <div class="prose prose-invert max-w-none text-[var(--text-secondary)] leading-relaxed">
    <p class="text-lg text-[var(--text-primary)] mb-6">A "wallet" doesn't actually store your coins — it stores your <strong>private keys</strong>, which prove you own the coins on the blockchain. Lose the keys, lose the coins. No backup = gone forever.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Hot Wallets (Connected to Internet)</h2>
    <p>Hot wallets are convenient but riskier. They're suitable for small amounts and daily use.</p>
    <div class="overflow-x-auto mt-4">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="border-b border-[var(--border-color)]">
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Wallet</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Type</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Best For</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">MetaMask</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Browser Extension</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">DeFi on Ethereum</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Phantom</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Browser Extension</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Solana ecosystem</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Trust Wallet</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Mobile App</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Multi-chain mobile use</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Rabby</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Browser Extension</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Safer alternative to MetaMask</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Cold Wallets (Offline / Hardware)</h2>
    <p>Cold wallets store private keys offline. They're the gold standard for long-term holding.</p>
    <div class="space-y-4 mt-4">
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">Ledger Nano X</h3>
        <p class="text-[var(--text-secondary)] text-sm">Most popular. Bluetooth, supports 5,500+ coins. <a href="https://shop.ledger.com/?r=5b63cc287be03" class="text-primary hover:underline" target="_blank" rel="sponsored noopener">Buy via referral →</a></p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">Trezor Safe 5</h3>
        <p class="text-[var(--text-secondary)] text-sm">Open-source firmware. Recommended for privacy-conscious users.</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">OneKey Classic</h3>
        <p class="text-[var(--text-secondary)] text-sm">Best value for Chinese users. CC EAL6+ certified. <a href="https://www.onekey.so/" class="text-primary hover:underline" target="_blank" rel="sponsored noopener">Check OneKey →</a></p>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Custodial vs. Non-Custodial</h2>
    <div class="overflow-x-auto mt-4">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="border-b border-[var(--border-color)]">
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Type</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Example</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">You Hold Keys?</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Risk</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Custodial</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Binance, Coinbase</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">❌ No</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Exchange bankruptcy</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Non-Custodial</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">MetaMask, Ledger</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">✅ Yes</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">You lose the keys</td>
          </tr>
        </tbody>
      </table>
    </div>
    <p class="mt-3 text-sm text-[var(--text-muted)]">Rule of thumb: if you don't hold the private keys, you don't truly own the crypto. "Not your keys, not your coins."</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">How to Set Up a Hot Wallet (MetaMask Example)</h2>
    <ol class="list-decimal pl-6 space-y-2">
      <li>Download only from the official site: <code class="text-primary">metamask.io</code></li>
      <li>Choose "Create a Wallet" → write down the 12-word seed phrase <strong>on paper</strong></li>
      <li>Never share the seed phrase. Not with support, not with friends.</li>
      <li>Send a small test amount ($20) before depositing large sums.</li>
      <li>Install the official MetaMask extension only — fake versions are common.</li>
    </ol>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">The Bottom Line</h2>
    <p>Use a <strong>hot wallet for daily trading/small amounts</strong> (less than one month's salary). Use a <strong>hardware wallet for long-term holding</strong> (more than one month's salary). And always, always write down your seed phrase on paper — never digitally.</p>

    <div class="mt-8 p-5 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
      <p class="text-sm text-[var(--text-muted)] mb-1">🤝 Affiliate Disclosure</p>
      <p class="text-[var(--text-secondary)] text-sm">Some links on this page are referral links. You get discounts; I may earn a small commission to keep this site running. No extra cost to you.</p>
    </div>
  </div>

  <div class="mt-12 pt-8 border-t border-[var(--border-color)]">
    <p class="text-[var(--text-muted)] text-sm">📚 Part of <a href="/en/learn/" class="text-primary hover:underline">Learning Center</a>.</p>
  </div>
</div>"""
    },
    {
        "slug": "common-scams",
        "title": "Common Crypto Scams and How to Spot Them",
        "description": "Protect yourself. A practical guide to the most common cryptocurrency scams in 2026.",
        "content": """<div class="max-w-3xl mx-auto px-4 sm:px-6 py-12">
  <p class="text-[var(--text-muted)] text-sm mb-2">
    <a href="/en/learn/" class="text-primary hover:underline">← Back to Learning Center</a>
  </p>
  <h1 class="text-3xl font-bold mb-4">Common Crypto Scams and How to Spot Them</h1>
  <p class="text-[var(--text-muted)] text-sm mb-8">January 2026 · 11 min read</p>

  <div class="prose prose-invert max-w-none text-[var(--text-secondary)] leading-relaxed">
    <p class="text-lg text-[var(--text-primary)] mb-6">If you're in crypto, someone will try to scam you. This is a fact. Here are the most common scams and how to avoid them.</p>

    <div class="p-4 rounded-xl bg-red-500/10 border border-red-500/30 mb-8">
      <p class="text-red-400 text-sm font-medium">🚨 Golden Rule</p>
      <p class="text-[var(--text-secondary)] text-sm mt-1">No legitimate person or company will ever ask for your seed phrase, private key, or ask you to "verify" your wallet by connecting to a website. Ever.</p>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Scam #1: Fake Airdrops / "Free Token" Scams</h2>
    <p>You receive a random token in your wallet, then visit the token's website to "claim" more. <strong>Connecting your wallet to that site gives them access to drain your funds.</strong></p>
    <p class="mt-3 text-sm text-[var(--text-muted)]">✅ Protection: Ignore random tokens. Never visit a website linked from a random token's contract.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Scam #2: Phishing Websites</h2>
    <p>You get an email or DM: "Your Binance account is suspended, click here to verify." The link goes to <code class="text-red-400">binance.com</code> (with a subtle typo), which looks exactly like the real site.</p>
    <p class="mt-3 text-sm text-[var(--text-muted)]">✅ Protection: Always type URLs manually. Use bookmarks. Enable anti-phishing codes on exchanges.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Scam #3: "Support" DMs on Telegram / Discord</h2>
    <p>Someone DMs you claiming to be "official support" and asks for your seed phrase to "verify your wallet." <strong>This is 100% a scam.</strong> Real support never DMs first.</p>
    <p class="mt-3 text-sm text-[var(--text-muted)]">✅ Protection: Never share your seed phrase with anyone. Block anyone who DMs you first.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Scam #4: Rug Pulls (in DeFi and NFTs)</h2>
    <p>Developers create a token or NFT project, hype it up, then "pull the rug" — they drain the liquidity pool and disappear with everyone's money.</p>
    <div class="my-4 p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
      <p class="text-[var(--text-primary)] font-medium text-sm mb-1">Red Flags to Watch For:</p>
      <ul class="list-disc pl-6 space-y-1 text-sm text-[var(--text-secondary)]">
        <li>Anonymous team with no doxxed identity</li>
        <li>Liquidity is NOT locked (check on Uniswap info page)</li>
        <li>Promises of "guaranteed 100x returns"</li>
        <li>High-pressure tactics ("only 2 hours left!")</li>
      </ul>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Scam #5: Pig Butchering (恋爱杀猪盘)</h2>
    <p>A long-con scam where the attacker builds a romantic or friendship relationship with you over weeks/months, then convinces you to "invest together" in a fake crypto platform. The platform shows fake profits until you try to withdraw — then they ghost.</p>
    <p class="mt-3 text-sm text-[var(--text-muted)]">✅ Protection: Never invest in a platform someone else introduced you to via dating apps or social media. Only use well-known exchanges.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Scam #6: Fake Hardware Wallets</h2>
    <p>Buying a used or fake Ledger/Trezor from eBay or a third-party seller. The device arrives pre-configured with a seed phrase that the scammer also has — as soon as you deposit, they drain it.</p>
    <p class="mt-3 text-sm text-[var(--text-muted)]">✅ Protection: Only buy hardware wallets from the <strong>official website</strong>. If the device shows a pre-generated seed phrase, return it immediately.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">A Security Checklist You Can Actually Follow</h2>
    <div class="space-y-3 mt-4">
      <div class="flex items-start gap-3 p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <span class="text-green-400 mt-0.5">✅</span>
        <p class="text-[var(--text-secondary)] text-sm">Bookmark exchange URLs and only use those bookmarks</p>
      </div>
      <div class="flex items-start gap-3 p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <span class="text-green-400 mt-0.5">✅</span>
        <p class="text-[var(--text-secondary)] text-sm">Never share your seed phrase — not even with "support"</p>
      </div>
      <div class="flex items-start gap-3 p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <span class="text-green-400 mt-0.5">✅</span>
        <p class="text-[var(--text-secondary)] text-sm">Use a hardware wallet for any amount >$1,000</p>
      </div>
      <div class="flex items-start gap-3 p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <span class="text-green-400 mt-0.5">✅</span>
        <p class="text-[var(--text-secondary)] text-sm">Verify smart contract addresses before approving tokens</p>
      </div>
      <div class="flex items-start gap-3 p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <span class="text-green-400 mt-0.5">✅</span>
        <p class="text-[var(--text-secondary)] text-sm">Be skeptical of "too good to be true" APYs (>20%)</p>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">The Bottom Line</h2>
    <p>In crypto, <strong>you are your own bank</strong>. That means you also bear 100% of the responsibility for your security. If something feels off, it probably is. When in doubt, do nothing.</p>
  </div>

  <div class="mt-12 pt-8 border-t border-[var(--border-color)]">
    <p class="text-[var(--text-muted)] text-sm">📚 Part of <a href="/en/learn/" class="text-primary hover:underline">Learning Center</a>.</p>
  </div>
</div>"""
    },
    {
        "slug": "binance-review",
        "title": "Binance Review (2026): Still the King of Crypto Exchanges?",
        "description": "An honest, no-hype review of Binance — fees, security, supported coins, and whether it's right for you.",
        "content": """<div class="max-w-3xl mx-auto px-4 sm:px-6 py-12">
  <p class="text-[var(--text-muted)] text-sm mb-2">
    <a href="/en/learn/" class="text-primary hover:underline">← Back to Learning Center</a>
  </p>
  <h1 class="text-3xl font-bold mb-4">Binance Review (2026): Still the King of Crypto Exchanges?</h1>
  <p class="text-[var(--text-muted)] text-sm mb-8">January 2026 · 9 min read</p>

  <div class="prose prose-invert max-w-none text-[var(--text-secondary)] leading-relaxed">
    <p class="text-lg text-[var(--text-primary)] mb-6">Binance is the world's largest crypto exchange by volume. But is it the right choice for you in 2026? Here's my honest take.</p>

    <div class="flex items-center gap-4 p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)] mb-8">
      <div class="text-center">
        <p class="text-3xl font-bold text-primary">9.2</p>
        <p class="text-xs text-[var(--text-muted)]">Overall Score</p>
      </div>
      <div class="flex-1 grid grid-cols-2 gap-2 text-sm">
        <div><span class="text-[var(--text-muted)]">Fees:</span> <span class="text-green-400">0.1%</span></div>
        <div><span class="text-[var(--text-muted)]">Coins:</span> <span class="text-[var(--text-primary)]">600+</span></div>
        <div><span class="text-[var(--text-muted)]">KYC:</span> <span class="text-[var(--text-primary)]">Required</span></div>
        <div><span class="text-[var(--text-muted)]">Headquarters:</span> <span class="text-[var(--text-primary)]">Multiple</span></div>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Pros</h2>
    <div class="space-y-3 mt-4">
      <div class="flex items-start gap-3">
        <span class="text-green-400 mt-0.5">✅</span>
        <p class="text-[var(--text-secondary)] text-sm"><strong>Highest liquidity</strong> — your large orders won't slip as much</p>
      </div>
      <div class="flex items-start gap-3">
        <span class="text-green-400 mt-0.5">✅</span>
        <p class="text-[var(--text-secondary)] text-sm"><strong>Lowest fees</strong> — 0.1% spot, lower with BNB holdings</p>
      </div>
      <div class="flex items-start gap-3">
        <span class="text-green-400 mt-0.5">✅</span>
        <p class="text-[var(--text-secondary)] text-sm"><strong>Most coins</strong> — access to almost every major (and many minor) tokens</p>
      </div>
      <div class="flex items-start gap-3">
        <span class="text-green-400 mt-0.5">✅</span>
        <p class="text-[var(--text-secondary)] text-sm"><strong>Binance Earn</strong> — easy staking and yield products for passive income</p>
      </div>
      <div class="flex items-start gap-3">
        <span class="text-green-400 mt-0.5">✅</span>
        <p class="text-[var(--text-secondary)] text-sm"><strong>Auto-Invest (DCA)</strong> — set up recurring buys easily</p>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Cons</h2>
    <div class="space-y-3 mt-4">
      <div class="flex items-start gap-3">
        <span class="text-red-400 mt-0.5">❌</span>
        <p class="text-[var(--text-secondary)] text-sm"><strong>Regulatory uncertainty</strong> — has been fined or banned in several countries</p>
      </div>
      <div class="flex items-start gap-3">
        <span class="text-red-400 mt-0.5">❌</span>
        <p class="text-[var(--text-secondary)] text-sm"><strong>Complex interface</strong> — overwhelming for complete beginners</p>
      </div>
      <div class="flex items-start gap-3">
        <span class="text-red-400 mt-0.5">❌</span>
        <p class="text-[var(--text-secondary)] text-sm"><strong>Customer support</strong> — can be slow during market volatility</p>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Fee Structure (2026)</h2>
    <div class="overflow-x-auto mt-4">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="border-b border-[var(--border-color)]">
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Product</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Maker Fee</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Taker Fee</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Spot Trading</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0.1%</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0.1%</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Futures (USDⓈ-M)</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0.02%</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0.04%</td>
          </tr>
        </tbody>
      </table>
    </div>
    <p class="mt-3 text-sm text-[var(--text-muted)]">Fees can be reduced by holding BNB or increasing 30-day trading volume.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Security: Has It Ever Been Hacked?</h2>
    <p>Binance was hacked in 2019 (~7,000 BTC stolen). They used their SAFU (Secure Asset Fund for Users) insurance fund to cover all losses — <strong>no user lost money</strong>. Since then, their security has been significantly upgraded.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Is Binance Right for You?</h2>
    <div class="space-y-4 mt-4">
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <p class="text-[var(--text-primary)] font-medium text-sm mb-1">✅ You should use Binance if:</p>
        <p class="text-[var(--text-secondary)] text-sm">You want the lowest fees, highest liquidity, and access to the most coins. You're comfortable with a slightly complex interface.</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <p class="text-[var(--text-primary)] font-medium text-sm mb-1">❌ You might prefer another exchange if:</p>
        <p class="text-[var(--text-secondary)] text-sm">You're in the US (use Binance.US instead, or Coinbase). You want a simpler interface (try Coinbase). You need strong regulatory compliance (try Kraken).</p>
      </div>
    </div>

    <div class="mt-8 p-5 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
      <p class="text-sm text-[var(--text-muted)] mb-1">🤝 Affiliate Disclosure</p>
      <p class="text-[var(--text-secondary)] text-sm">Registering via this link gives you a 20% fee discount. I may earn a small commission. <a href="https://www.binance.com/en/register?ref=CPA_00ZIV33RO4" class="inline-block mt-2 px-4 py-2 bg-primary text-white rounded-lg text-sm font-medium hover:opacity-90 transition-opacity" target="_blank" rel="sponsored noopener">Register on Binance →</a></p>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">The Bottom Line</h2>
    <p>Binance is still the best all-around exchange for most international users in 2026. Low fees, massive liquidity, and the most features. Just be aware of the regulatory risks and keep large balances in a self-custody wallet.</p>
  </div>

  <div class="mt-12 pt-8 border-t border-[var(--border-color)]">
    <p class="text-[var(--text-muted)] text-sm">📚 Part of <a href="/en/learn/" class="text-primary hover:underline">Learning Center</a>.</p>
  </div>
</div>"""
    },
    {
        "slug": "okx-review",
        "title": "OKX Review (2026): The Trader's Choice",
        "description": "OKX is a top-tier exchange with excellent derivatives and a clean interface. Here's the full review.",
        "content": """<div class="max-w-3xl mx-auto px-4 sm:px-6 py-12">
  <p class="text-[var(--text-muted)] text-sm mb-2">
    <a href="/en/learn/" class="text-primary hover:underline">← Back to Learning Center</a>
  </p>
  <h1 class="text-3xl font-bold mb-4">OKX Review (2026): The Trader's Choice</h1>
  <p class="text-[var(--text-muted)] text-sm mb-8">January 2026 · 8 min read</p>

  <div class="prose prose-invert max-w-none text-[var(--text-secondary)] leading-relaxed">
    <p class="text-lg text-[var(--text-primary)] mb-6">OKX (formerly OKEx) is a top-3 exchange by volume, particularly strong in derivatives trading. Here's my detailed review.</p>

    <div class="flex items-center gap-4 p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)] mb-8">
      <div class="text-center">
        <p class="text-3xl font-bold text-primary">8.8</p>
        <p class="text-xs text-[var(--text-muted)]">Overall Score</p>
      </div>
      <div class="flex-1 grid grid-cols-2 gap-2 text-sm">
        <div><span class="text-[var(--text-muted)]">Fees:</span> <span class="text-green-400">0.08%</span></div>
        <div><span class="text-[var(--text-muted)]">Derivatives:</span> <span class="text-green-400">Excellent</span></div>
        <div><span class="text-[var(--text-muted)]">KYC:</span> <span class="text-[var(--text-primary)]">Required</span></div>
        <div><span class="text-[var(--text-muted)]">Chinese support:</span> <span class="text-green-400">✅ Yes</span></div>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">What OKX Does Best</h2>
    <div class="space-y-4 mt-4">
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">Derivatives Trading</h3>
        <p class="text-[var(--text-secondary)] text-sm">OKX has some of the best futures/perpetual contracts in the industry. Low slippage, high leverage (up to 100x), and excellent API stability.</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">Clean Interface</h3>
        <p class="text-[var(--text-secondary)] text-sm">The trading interface is more intuitive than Binance's. Easier for beginners to navigate.</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">Copy Trading</h3>
        <p class="text-[var(--text-secondary)] text-sm">You can automatically copy the trades of profitable traders. Great for beginners who don't know how to trade yet.</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">Web3 Wallet Built-In</h3>
        <p class="text-[var(--text-secondary)] text-sm">OKX has an integrated non-custodial Web3 wallet for DeFi and NFTs. No need for a separate MetaMask.</p>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Fee Structure</h2>
    <div class="overflow-x-auto mt-4">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="border-b border-[var(--border-color)]">
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Product</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Maker</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Taker</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Spot</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0.08%</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0.10%</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Futures</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0.02%</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0.05%</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">OKX vs. Binance: Quick Comparison</h2>
    <div class="overflow-x-auto mt-4">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="border-b border-[var(--border-color)]">
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Feature</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">OKX</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Binance</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Spot Fees</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0.08% / 0.10%</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">0.1% / 0.1%</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Derivatives</td>
            <td class="py-3 pr-4 text-green-400">Better</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Good</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Chinese Users</td>
            <td class="py-3 pr-4 text-green-400">✅ Strong</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Limited</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Coin Variety</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Good</td>
            <td class="py-3 pr-4 text-green-400">Best</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">The Bottom Line</h2>
    <p>OKX is excellent for derivatives traders and Chinese-speaking users. Fees are slightly lower than Binance for spot trading. The integrated Web3 wallet is a nice bonus. If you're focused on futures trading, OKX is arguably the best platform available.</p>

    <div class="mt-8 p-5 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
      <p class="text-sm text-[var(--text-muted)] mb-1">🤝 Affiliate Disclosure</p>
      <p class="text-[var(--text-secondary)] text-sm">Registering via this link may give you exclusive rewards. <a href="https://www.okx.com/join/47930867" class="inline-block mt-2 px-4 py-2 bg-primary text-white rounded-lg text-sm font-medium hover:opacity-90 transition-opacity" target="_blank" rel="sponsored noopener">Register on OKX →</a></p>
    </div>
  </div>

  <div class="mt-12 pt-8 border-t border-[var(--border-color)]">
    <p class="text-[var(--text-muted)] text-sm">📚 Part of <a href="/en/learn/" class="text-primary hover:underline">Learning Center</a>.</p>
  </div>
</div>"""
    }
]

base = "G:/wordbuddy/2026-05-29-15-38-18/1hcrypto/src/pages/en/learn/"

for article in articles:
    slug = article["slug"]
    title = article["title"]
    desc = article["description"]
    content = article["content"]

    file_content = f"""---
import BaseLayout from '../../../layouts/BaseLayout.astro';
---

<BaseLayout title="{title} - 1H Crypto" lang="en" description="{desc}">
{content}
</BaseLayout>
"""
    filepath = base + slug + ".astro"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(file_content)
    print(f"✅ Written: {slug}.astro")

print(f"\nDone. Total: {len(articles)} articles.")
