// Cloudflare Pages Function - 价格 API 代理
// 避免 CORS 问题，同时隐藏 API 调用细节

interface PriceData {
  btc: {
    price: number | null;
    change24h: number | null;
    vol24h: number | null;
    mcap: number | null;
    updatedAt: number | null;
  };
  eth: {
    price: number | null;
    change24h: number | null;
    vol24h: number | null;
    mcap: number | null;
    updatedAt: number | null;
  };
  fearGreed?: {
    value: number | null;
    classification: string;
    timestamp: number | null;
  };
  fetchedAt: number;
}

async function fetchFearGreed(): Promise<PriceData['fearGreed']> {
  try {
    const url = "https://api.alternative.me/fng/?limit=1";
    const resp = await fetch(url, {
      headers: { "User-Agent": "1hcrypto/1.0" },
    });
    if (!resp.ok) return undefined;
    const data = await resp.json();
    const item = data?.data?.[0];
    if (!item) return undefined;
    return {
      value: parseInt(item.value) || null,
      classification: item.value_classification || "Unknown",
      timestamp: parseInt(item.timestamp) || null,
    };
  } catch {
    return undefined;
  }
}

export const onRequest: PagesFunction = async (context) => {
  const { request } = context;
  
  // CORS 头
  const corsHeaders = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Content-Type": "application/json",
  };

  // 处理 OPTIONS 预检请求
  if (request.method === "OPTIONS") {
    return new Response(null, { headers: corsHeaders });
  }

  try {
    // 并行获取：CoinGecko 价格 + Fear & Greed 指数
    const [priceRes, fgRes] = await Promise.all([
      fetch(
        "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd&include_24hr_change=true&include_24hr_vol=true&include_market_cap=true&include_last_updated_at=true",
        { headers: { "User-Agent": "1hcrypto/1.0", "Accept": "application/json" } }
      ),
      fetchFearGreed(),
    ]);

    if (!priceRes.ok) {
      throw new Error(`CoinGecko API error: ${priceRes.status}`);
    }

    const data = await priceRes.json();

    // 格式化为前端友好结构
    const result: PriceData = {
      btc: {
        price: data.bitcoin?.usd ?? null,
        change24h: data.bitcoin?.usd_24h_change ?? null,
        vol24h: data.bitcoin?.usd_24h_vol ?? null,
        mcap: data.bitcoin?.usd_market_cap ?? null,
        updatedAt: data.bitcoin?.last_updated_at ?? null,
      },
      eth: {
        price: data.ethereum?.usd ?? null,
        change24h: data.ethereum?.usd_24h_change ?? null,
        vol24h: data.ethereum?.usd_24h_vol ?? null,
        mcap: data.ethereum?.usd_market_cap ?? null,
        updatedAt: data.ethereum?.last_updated_at ?? null,
      },
      fetchedAt: Date.now(),
    };

    if (fgRes) {
      result.fearGreed = fgRes;
    }

    return new Response(JSON.stringify(result), { headers: corsHeaders });
  } catch (err) {
    return new Response(
      JSON.stringify({ error: "Failed to fetch price", message: String(err) }),
      { status: 500, headers: corsHeaders }
    );
  }
};
