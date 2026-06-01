import sys
sys.stdout.reconfigure(encoding='utf-8')

articles = [
    {
        "slug": "what-is-ethereum",
        "title": "What is Ethereum? More Than Just 'Bitcoin 2.0'",
        "description": "Ethereum powers DeFi, NFTs, and thousands of dApps. Here's what it actually does.",
        "content": """<div class="max-w-3xl mx-auto px-4 sm:px-6 py-12">
  <p class="text-[var(--text-muted)] text-sm mb-2">
    <a href="/en/learn/" class="text-primary hover:underline">← Back to Learning Center</a>
  </p>
  <h1 class="text-3xl font-bold mb-4">What is Ethereum? (Not Just 'Bitcoin 2.0')</h1>
  <p class="text-[var(--text-muted)] text-sm mb-8">January 2026 · 9 min read</p>

  <div class="prose prose-invert max-w-none text-[var(--text-secondary)] leading-relaxed">
    <p class="text-lg text-[var(--text-primary)] mb-6">If Bitcoin is "digital gold," Ethereum is "digital oil" — a platform that powers millions of applications, not just a store of value.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">The One-Line Definition</h2>
    <p>Ethereum is a <strong>decentralized global computer</strong> that runs smart contracts — programs that execute exactly as written, without downtime or censorship.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Smart Contracts: The Killer Feature</h2>
    <p>A smart contract is code that runs on the blockchain. Once deployed, no one can stop it, modify it, or censor it (assuming it's written correctly).</p>
    <div class="my-4 p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)] font-mono text-sm text-[var(--text-primary)] text-center">
      Example: A smart contract can hold $1M in USDC and automatically release it to a freelancer when their client clicks "Approve" — no lawyer needed.
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">ETH (Ether): The Fuel</h2>
    <p>Every operation on Ethereum costs "gas" (paid in ETH). If you want to send USDC, swap tokens, or mint an NFT, you need ETH to pay for the computation.</p>
    <p class="mt-3">This makes ETH <strong>ultraound money</strong>: as network activity grows, more ETH is burned than minted, making it deflationary.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">The 2022 Merge: Proof-of-Stake</h2>
    <p>In September 2022, Ethereum switched from Proof-of-Work (mining) to Proof-of-Stake, reducing its energy consumption by ~99.95%.</p>
    <p class="mt-3">Now, instead of miners with ASICs, the network is secured by "validators" who stake 32 ETH to participate.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Major Use Cases (2026)</h2>
    <div class="space-y-4 mt-4">
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">DeFi (Decentralized Finance)</h3>
        <p class="text-[var(--text-secondary)] text-sm">Lend, borrow, and trade without banks. Aave, Uniswap, and Compound run entirely on Ethereum smart contracts.</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">Stablecoins</h3>
        <p class="text-[var(--text-secondary)] text-sm">USDC, USDT, and DAI mostly live on Ethereum. $150B+ in stablecoins settle on Ethereum daily.</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">Tokenized Real-World Assets (RWAs)</h3>
        <p class="text-[var(--text-secondary)] text-sm">BlackRock's BUIDL fund, real estate tokens, and government bonds are now on Ethereum. Trillions in RWAs expected by 2030.</p>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Ethereum vs. Bitcoin: Quick Comparison</h2>
    <div class="overflow-x-auto mt-4">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="border-b border-[var(--border-color)]">
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Feature</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Bitcoin</th>
            <th class="py-3 text-[var(--text-primary)] font-semibold">Ethereum</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Primary Use</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Store of value</td>
            <td class="py-3 text-[var(--text-secondary)]">Smart contract platform</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">TPS (base layer)</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">~7</td>
            <td class="py-3 text-[var(--text-secondary)]">~15</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Scaling Solution</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Lightning Network</td>
            <td class="py-3 text-[var(--text-secondary)]">Layer 2s (Arbitrum, etc.)</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Monetary Policy</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Fixed supply (21M)</td>
            <td class="py-3 text-[var(--text-secondary)]">Deflationary (EIP-1559)</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Where to Buy ETH?</h2>
    <p>The easiest way is through a major exchange. If you're in the US, Coinbase or Binance.US. Internationally, Binance or OKX.</p>
    <a href="https://www.binance.com/en/register?ref=CPA_00ZIV33RO4" class="inline-block mt-3 px-4 py-2 bg-primary text-white rounded-lg text-sm font-medium hover:opacity-90 transition-opacity" target="_blank" rel="sponsored noopener">Register on Binance →</a>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">The Bottom Line</h2>
    <p>Ethereum is the infrastructure layer of the crypto economy. If you believe DeFi, stablecoins, and tokenized assets are the future, ETH is the most direct way to bet on that future.</p>
  </div>

  <div class="mt-12 pt-8 border-t border-[var(--border-color)]">
    <p class="text-[var(--text-muted)] text-sm">📚 Part of <a href="/en/learn/" class="text-primary hover:underline">Learning Center</a>.</p>
  </div>
</div>"""
    },
    {
        "slug": "stablecoins-guide",
        "title": "Stablecoins Explained: USDT, USDC, and DAI",
        "description": "Not all stablecoins are created equal. Learn the differences and which ones are actually safe.",
        "content": """<div class="max-w-3xl mx-auto px-4 sm:px-6 py-12">
  <p class="text-[var(--text-muted)] text-sm mb-2">
    <a href="/en/learn/" class="text-primary hover:underline">← Back to Learning Center</a>
  </p>
  <h1 class="text-3xl font-bold mb-4">Stablecoins Explained: USDT, USDC, and DAI</h1>
  <p class="text-[var(--text-muted)] text-sm mb-8">January 2026 · 8 min read</p>

  <div class="prose prose-invert max-w-none text-[var(--text-secondary)] leading-relaxed">
    <p class="text-lg text-[var(--text-primary)] mb-6">Stablecoins are the "USD of crypto" — you use them to trade, earn yield, and move money without touching a bank.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">What is a Stablecoin?</h2>
    <p>A stablecoin is a cryptocurrency designed to maintain a 1:1 peg with a fiat currency (usually USD). You can think of it as "programmable dollars."</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">The Big Three Compared</h2>
    <div class="overflow-x-auto mt-4">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="border-b border-[var(--border-color)]">
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Name</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Backing</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Transparency</th>
            <th class="py-3 text-[var(--text-primary)] font-semibold">Risk Level</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">USDT (Tether)</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Fiat reserves (opaque)</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Low (quarterly attestations)</td>
            <td class="py-3 text-amber-400 font-medium">Medium</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">USDC (Circle)</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Fiat (fully reserved)</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">High (monthly audits)</td>
            <td class="py-3 text-green-400 font-medium">Low</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">DAI (MakerDAO)</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Crypto collateral (on-chain)</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Very High (fully on-chain)</td>
            <td class="py-3 text-green-400 font-medium">Low</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">USDT: The King (But Controversial)</h2>
    <p>USDT has the most liquidity and is accepted everywhere. But Tether has never provided a full audit — only "attestations" from a Caribbean accounting firm.</p>
    <p class="mt-3 text-sm text-[var(--text-muted)]">If you're holding &gt;$50K in stablecoins, consider splitting between USDT and USDC.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">USDC: The Regulated Choice</h2>
    <p>USDC is issued by Circle, a US-regulated company. It has full reserves, monthly audits, and is the choice for institutions.</p>
    <p class="mt-3">If you're in the US or EU, USDC is the safer choice for regulatory reasons.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">DAI: The Decentralized Option</h2>
    <p>DAI is minted by locking ETH (or other assets) into MakerDAO's smart contracts. No single company controls it. The trade-off: it's slightly more complex to understand.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">De-peg Risk: What Happens When It Breaks?</h2>
    <p>In March 2023, USDC briefly de-pegged to $0.87 after Circle disclosed $3.3B stuck at Silicon Valley Bank. It eventually recovered — but the panic was real.</p>
    <p class="mt-3">Rule of thumb: if you need absolute stability, keep your stablecoins split across 2-3 issuers.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Where to Earn Yield on Stablecoins?</h2>
    <div class="space-y-3 mt-4">
      <div class="flex items-start gap-3 p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <span class="text-green-400 mt-0.5">✅</span>
        <div>
          <p class="text-[var(--text-primary)] font-medium text-sm">Centralized Lending (Binance Earn, Nexo)</p>
          <p class="text-[var(--text-muted)] text-xs">~4-8% APY. Counterparty risk: the platform could freeze or go bankrupt.</p>
        </div>
      </div>
      <div class="flex items-start gap-3 p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <span class="text-green-400 mt-0.5">✅</span>
        <div>
          <p class="text-[var(--text-primary)] font-medium text-sm">DeFi Lending (Aave, Compound)</p>
          <p class="text-[var(--text-muted)] text-xs">~3-10% APY. Smart contract risk: code could be exploited.</p>
        </div>
      </div>
      <div class="flex items-start gap-3 p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <span class="text-amber-400 mt-0.5">⚠️</span>
        <div>
          <p class="text-[var(--text-primary)] font-medium text-sm">CeFi Yield Platforms (Celsius-type)</p>
          <p class="text-[var(--text-muted)] text-xs">Avoid. If it sounds too good to be true (12%+ APY on USDC), it probably is.</p>
        </div>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">The Bottom Line</h2>
    <p>Use USDC for large amounts and long-term holding. Use USDT for trading (better liquidity). Use DAI if you care about decentralization. Never put all your stablecoins in one basket.</p>
  </div>

  <div class="mt-12 pt-8 border-t border-[var(--border-color)]">
    <p class="text-[var(--text-muted)] text-sm">📚 Part of <a href="/en/learn/" class="text-primary hover:underline">Learning Center</a>.</p>
  </div>
</div>"""
    },
    {
        "slug": "what-is-nft",
        "title": "What is an NFT? (No Hype, Just Facts)",
        "description": "NFTs aren't just JPEGs. Here's what they are, how they work, and whether they're worth anything.",
        "content": """<div class="max-w-3xl mx-auto px-4 sm:px-6 py-12">
  <p class="text-[var(--text-muted)] text-sm mb-2">
    <a href="/en/learn/" class="text-primary hover:underline">← Back to Learning Center</a>
  </p>
  <h1 class="text-3xl font-bold mb-4">What is an NFT? (No Hype, Just Facts)</h1>
  <p class="text-[var(--text-muted)] text-sm mb-8">January 2026 · 7 min read</p>

  <div class="prose prose-invert max-w-none text-[var(--text-secondary)] leading-relaxed">
    <p class="text-lg text-[var(--text-primary)] mb-6">NFT stands for "Non-Fungible Token." In plain English: a unique digital asset that cannot be copied or replaced with something identical.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Fungible vs. Non-Fungible (Why It Matters)</h2>
    <div class="overflow-x-auto mt-4">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="border-b border-[var(--border-color)]">
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Type</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Example</th>
            <th class="py-3 text-[var(--text-primary)] font-semibold">Interchangeable?</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Fungible</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">1 BTC = any other 1 BTC</td>
            <td class="py-3 text-[var(--text-secondary)]">✅ Yes</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Non-Fungible</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Your house deed ≠ neighbor's deed</td>
            <td class="py-3 text-[var(--text-secondary)]">❌ No</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">What Can an NFT Represent?</h2>
    <ul class="list-disc pl-6 space-y-2">
      <li><strong>Digital Art</strong>: The most common use case (CryptoPunks, BAYC).</li>
      <li><strong>Music / Videos</strong>: Artists can sell directly to fans without a label.</li>
      <li><strong>Gaming Items</strong>: Skins, weapons, land — that you truly own and can sell.</li>
      <li><strong>Real-World Assets</strong>: Property deeds, event tickets, university diplomas.</li>
      <li><strong>Membership / Access</strong>: "Token-gated" communities (e.g., hold this NFT → access Discord).</li>
    </ul>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">The 2021-2022 NFT Bubble (and What Happened After)</h2>
    <p>In 2021, NFT trading volume peaked at $17B. A "Bored Ape" sold for $3.4M. Then the market crashed ~95% in 2022-2023.</p>
    <p class="mt-3">In 2026, NFTs are (mostly) no longer about speculation. The surviving use cases are gaming, music royalties, and token-gated communities.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">How to Buy an NFT (Step-by-Step)</h2>
    <ol class="list-decimal pl-6 space-y-2">
      <li>Set up a wallet (MetaMask for Ethereum, Phantom for Solana).</li>
      <li>Buy ETH (or SOL) from an exchange.</li>
      <li>Send ETH to your wallet.</li>
      <li>Go to <a href="https://opensea.io/" class="text-primary hover:underline" target="_blank" rel="noopener">OpenSea</a> or <a href="https://magiceden.io/" class="text-primary hover:underline" target="_blank" rel="noopener">Magic Eden</a>.</li>
      <li>Connect your wallet, browse, and click "Buy Now."</li>
      <li>Pay the gas fee (in ETH) + the NFT price.</li>
    </ol>

    <div class="mt-6 p-4 rounded-xl bg-amber-500/10 border border-amber-500/30">
      <p class="text-amber-400 text-sm font-medium">⚠️ Warning</p>
      <p class="text-[var(--text-secondary)] text-sm mt-1">Most NFTs are illiquid — you might not be able to sell them when you want. Only buy what you can afford to hold indefinitely.</p>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Royalties: How Creators Get Paid</h2>
    <p>One genuinely useful NFT feature: creators can embed a royalty (e.g., 5%) into the smart contract. Every time the NFT is resold, the creator automatically gets paid. This was hard to enforce before NFTs.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">The "Right-Click Save" Argument</h2>
    <p>Critics say: "I can just right-click and save the image for free, so why pay?"</p>
    <p class="mt-3">Response: owning the NFT is like owning the <strong>original Mona Lisa</strong> — you can buy a poster, but you don't own the original. Whether that matters is up to you.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">The Bottom Line</h2>
    <p>NFTs are a technology, not an asset class. The technology enables verifiable ownership of digital (and eventually physical) assets. The 2021 speculation bubble is over — but the tech is still being built on.</p>
    <p class="mt-3">If you're buying an NFT in 2026, make sure you actually <em>want</em> what it represents (art, game item, community access) — not just because you hope it'll 10x.</p>
  </div>

  <div class="mt-12 pt-8 border-t border-[var(--border-color)]">
    <p class="text-[var(--text-muted)] text-sm">📚 Part of <a href="/en/learn/" class="text-primary hover:underline">Learning Center</a>.</p>
  </div>
</div>"""
    },
    {
        "slug": "private-key-security",
        "title": "Private Keys, Public Keys, and Seed Phrases — Explained",
        "description": "If you don't understand this, don't put real money into crypto. Here's the plain-English version.",
        "content": """<div class="max-w-3xl mx-auto px-4 sm:px-6 py-12">
  <p class="text-[var(--text-muted)] text-sm mb-2">
    <a href="/en/learn/" class="text-primary hover:underline">← Back to Learning Center</a>
  </p>
  <h1 class="text-3xl font-bold mb-4">Private Keys, Public Keys, and Seed Phrases — Explained</h1>
  <p class="text-[var(--text-muted)] text-sm mb-8">January 2026 · 10 min read</p>

  <div class="prose prose-invert max-w-none text-[var(--text-secondary)] leading-relaxed">
    <p class="text-lg text-[var(--text-primary)] mb-6">This is the single most important article you'll read about crypto. If you don't understand keys and seed phrases, <strong>you will eventually lose money</strong>.</p>

    <div class="p-4 rounded-xl bg-red-500/10 border border-red-500/30 mb-8">
      <p class="text-red-400 text-sm font-medium">🚨 Critical Rule</p>
      <p class="text-[var(--text-secondary)] text-sm mt-1"><strong>Never share your private key or seed phrase with anyone.</strong> Not support staff, not "verification bots," not your best friend. Anyone with these can steal all your funds instantly.</p>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">The Mailbox Analogy (Best Way to Understand)</h2>
    <ul class="list-disc pl-6 space-y-2">
      <li><strong>Public Key (Address)</strong> = Your mailbox address. You give it to people so they can send you letters (crypto).</li>
      <li><strong>Private Key</strong> = The key to your mailbox. Only YOU should have it. If someone else has it, they can take your letters.</li>
      <li><strong>Seed Phrase (Recovery Phrase)</strong> = A master key that can generate ALL your mailbox keys. If you lose your keys, this can restore them.</li>
    </ul>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">What a Seed Phrase Looks Like</h2>
    <div class="my-4 p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)] font-mono text-sm text-[var(--text-primary)] text-center">
      word1 word2 word3 word4 word5 word6 word7 word8 word9 word10 word11 word12
    </div>
    <p>Standard is 12 or 24 words (BIP-39 standard). The order matters. One wrong word = wrong wallet.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Hot Wallets vs. Cold Wallets</h2>
    <div class="overflow-x-auto mt-4">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="border-b border-[var(--border-color)]">
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Type</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Example</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Private Key Stored On</th>
            <th class="py-3 text-[var(--text-primary)] font-semibold">Risk</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Hot Wallet</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">MetaMask, Trust Wallet</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Internet-connected device</td>
            <td class="py-3 text-amber-400 font-medium">Higher</td>
          </tr>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Cold Wallet</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Ledger, Trezor, OneKey</td>
            <td class="py-3 pr-4 text-[var(--text-secondary)]">Air-gapped hardware</td>
            <td class="py-3 text-green-400 font-medium">Lower</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">How to Store Your Seed Phrase Safely</h2>
    <div class="space-y-3 mt-4">
      <div class="flex items-start gap-3 p-4 rounded-xl bg-green-500/10 border border-green-500/30">
        <span class="text-green-400 mt-0.5">✅</span>
        <div>
          <p class="text-[var(--text-primary)] font-medium text-sm">Write it on paper (2 copies, different locations)</p>
        </div>
      </div>
      <div class="flex items-start gap-3 p-4 rounded-xl bg-green-500/10 border border-green-500/30">
        <span class="text-green-400 mt-0.5">✅</span>
        <div>
          <p class="text-[var(--text-primary)] font-medium text-sm">Use a metal seed plate (fire/waterproof)</p>
        </div>
      </div>
      <div class="flex items-start gap-3 p-4 rounded-xl bg-red-500/10 border border-red-500/30">
        <span class="text-red-400 mt-0.5">❌</span>
        <div>
          <p class="text-[var(--text-primary)] font-medium text-sm">Never screenshot it or save it in a text file</p>
        </div>
      </div>
      <div class="flex items-start gap-3 p-4 rounded-xl bg-red-500/10 border border-red-500/30">
        <span class="text-red-400 mt-0.5">❌</span>
        <div>
          <p class="text-[var(--text-primary)] font-medium text-sm">Never type it into a website or share it via messaging apps</p>
        </div>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">What Happens If You Lose Your Seed Phrase?</h2>
    <p>If you lose your seed phrase AND your device is lost/broken, <strong>your funds are gone forever</strong>. There is no "forgot password" button. No bank can help you. This is why writing it down matters.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">The "Blind Signing" Trap</h2>
    <p>When you connect your wallet to a DeFi app, it'll ask you to "sign" a transaction. Sometimes the details are hidden (blind signing). If you sign without knowing what you're approving, you might be giving the app permission to drain your entire wallet.</p>
    <p class="mt-3 text-sm text-[var(--text-muted)]">Always read what you're signing. If an app asks for "unlimited approval," set a specific limit instead.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Bottom Line</h2>
    <p>Your crypto is only as safe as your key management. Buy a hardware wallet if you have &gt;$1,000 in crypto. Write down your seed phrase on paper (and metal). Never share it with anyone. These three rules will protect you from 99% of crypto theft.</p>

    <div class="mt-8 p-5 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
      <p class="text-sm text-[var(--text-muted)] mb-1">🛡️ Recommended Hardware Wallet</p>
      <p class="text-[var(--text-secondary)] text-sm">I use and recommend <a href="https://shop.ledger.com/?r=5b63cc287be03" class="text-primary hover:underline" target="_blank" rel="sponsored noopener">Ledger</a> or <a href="https://www.onekey.so/" class="text-primary hover:underline" target="_blank" rel="sponsored noopener">OneKey</a>. Using these links supports this site at no extra cost to you.</p>
    </div>
  </div>

  <div class="mt-12 pt-8 border-t border-[var(--border-color)]">
    <p class="text-[var(--text-muted)] text-sm">📚 Part of <a href="/en/learn/" class="text-primary hover:underline">Learning Center</a>.</p>
  </div>
</div>"""
    },
    {
        "slug": "how-to-read-candles",
        "title": "How to Read Candlestick Charts (No Experience Needed)",
        "description": "Before you trade, you need to understand what those green and red candles actually mean. Start here.",
        "content": """<div class="max-w-3xl mx-auto px-4 sm:px-6 py-12">
  <p class="text-[var(--text-muted)] text-sm mb-2">
    <a href="/en/learn/" class="text-primary hover:underline">← Back to Learning Center</a>
  </p>
  <h1 class="text-3xl font-bold mb-4">How to Read Candlestick Charts (No Experience Needed)</h1>
  <p class="text-[var(--text-muted)] text-sm mb-8">January 2026 · 10 min read</p>

  <div class="prose prose-invert max-w-none text-[var(--text-secondary)] leading-relaxed">
    <p class="text-lg text-[var(--text-primary)] mb-6">If you're going to trade crypto, you need to understand candlesticks. This is the "alphabet" of technical analysis.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">What Each Candle Shows</h2>
    <p>Every single candle shows four prices for that time period:</p>
    <ul class="list-disc pl-6 space-y-1 mt-3">
      <li><strong>Open</strong>: Price at the start</li>
      <li><strong>Close</strong>: Price at the end</li>
      <li><strong>High</strong>: Highest price during the period</li>
      <li><strong>Low</strong>: Lowest price during the period</li>
    </ul>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Green vs. Red (International Standard)</h2>
    <div class="overflow-x-auto mt-4">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="border-b border-[var(--border-color)]">
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Candle</th>
            <th class="py-3 pr-4 text-[var(--text-primary)] font-semibold">Close > Open</th>
            <th class="py-3 text-[var(--text-primary)] font-semibold">Close < Open</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-[var(--border-color)]">
            <td class="py-3 pr-4 text-[var(--text-primary)] font-medium">Color (Crypto standard)</td>
            <td class="py-3 pr-4 text-green-400">🟢 Green (Bullish)</td>
            <td class="py-3 text-red-400">🔴 Red (Bearish)</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Body and Wicks (Shadows)</h2>
    <ul class="list-disc pl-6 space-y-2">
      <li><strong>Body</strong>: The rectangle between Open and Close. A long body = strong buying or selling pressure.</li>
      <li><strong>Upper Wick</strong>: How high price went above the body. Long upper wick = buyers tried but were rejected.</li>
      <li><strong>Lower Wick</strong>: How low price went below the body. Long lower wick = sellers tried but were rejected.</li>
    </ul>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">6 Candlestick Patterns Every Beginner Should Know</h2>
    <div class="space-y-4 mt-4">
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">1. Hammer (Bottom Reversal)</h3>
        <p class="text-[var(--text-secondary)] text-sm">Small body at the top, long lower wick. After a downtrend, it suggests sellers are exhausted and buyers are stepping in.</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">2. Shooting Star (Top Reversal)</h3>
        <p class="text-[var(--text-secondary)] text-sm">Small body at the bottom, long upper wick. After an uptrend, it suggests buyers are exhausted and sellers may take over.</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">3. Doji (Indecision)</h3>
        <p class="text-[var(--text-secondary)] text-sm">Open ≈ Close. The market doesn't know which direction to go. Often appears at trend reversals.</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">4. Bullish Engulfing</h3>
        <p class="text-[var(--text-secondary)] text-sm">A green candle that completely "engulfs" the previous red candle's body. Strong bullish signal when confirmed by volume.</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">5. Morning Star (3-Candle Reversal)</h3>
        <p class="text-[var(--text-secondary)] text-sm">A large red candle → a small candle → a large green candle. Signals a potential bottom.</p>
      </div>
      <div class="p-4 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-color)]">
        <h3 class="text-lg font-bold text-[var(--text-primary)] mb-1">6. Evening Star (3-Candle Top)</h3>
        <p class="text-[var(--text-secondary)] text-sm">A large green candle → a small candle → a large red candle. Signals a potential top.</p>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Timeframes: Which One to Use?</h2>
    <ul class="list-disc pl-6 space-y-2">
      <li><strong>1m / 5m</strong>: Noise. Mostly useless for beginners.</li>
      <li><strong>15m / 1h</strong>: Short-term trading. High stress, high fees.</li>
      <li><strong>4h / 1D</strong>: The sweet spot for most traders. Clear signals, less noise.</li>
      <li><strong>1W</strong>: Long-term trend identification.</li>
    </ul>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Volume: The Confirmation Signal</h2>
    <p>A candle pattern with <strong>high volume</strong> is much more reliable than one with low volume. If a bullish engulfing candle appears on low volume, it could be a fake-out.</p>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">Best Free Tool for Learning</h2>
    <p><a href="https://www.tradingview.com/" class="text-primary hover:underline" target="_blank" rel="sponsored noopener">TradingView</a> is the best free charting tool. You can practice identifying candlestick patterns on historical data without risking real money.</p>
    <a href="https://www.tradingview.com/pricing/?share_your_love=dongbw03" class="inline-block mt-3 px-4 py-2 bg-primary text-white rounded-lg text-sm font-medium hover:opacity-90 transition-opacity" target="_blank" rel="sponsored noopener">Try TradingView Free →</a>

    <h2 class="text-2xl font-bold text-[var(--text-primary)] mt-10 mb-4">The Bottom Line</h2>
    <p>Candlestick patterns are not crystal balls. They show <em>probability</em>, not certainty. Always combine them with support/resistance levels, volume, and trend direction. And never, ever trade based on a single candle pattern alone.</p>
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
