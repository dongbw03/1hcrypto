import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

files = [
    'src/pages/zh/learn/hardware-wallet-guide.astro',
    'src/pages/zh/learn/how-to-read-candle.astro',
    'src/pages/zh/learn/how-to-buy-crypto-p2p.astro',
    'src/pages/zh/learn/ethereum-gas-fees.astro',
    'src/pages/zh/learn/position-management-basics.astro',
    'src/pages/zh/learn/dca-strategy.astro',
]

wrong = "import BaseLayout from '../../layouts/BaseLayout.astro';"
right = "import BaseLayout from '../../../layouts/BaseLayout.astro';"

for f in files:
    if not os.path.exists(f):
        print(f"NOT FOUND: {f}")
        continue
    content = open(f, 'r', encoding='utf-8').read()
    if wrong in content:
        content = content.replace(wrong, right)
        open(f, 'w', encoding='utf-8').write(content)
        print(f"Fixed: {f}")
    elif right in content:
        print(f"Already correct: {f}")
    else:
        print(f"UNEXPECTED content in {f}")
