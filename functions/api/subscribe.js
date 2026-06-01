/**
 * Cloudflare Pages Function - 邮件订阅 API
 * 部署到 Cloudflare Pages 后自动生效
 *
 * 使用方式：
 * 1. 绑定 D1 数据库（可选）：在 Cloudflare 控制台创建 D1 并绑定到 Pages 项目
 *    绑定名称为 "DB"，表结构会自动创建
 * 2. 配置 Webhook（可选）：设置环境变量 FORM_WEBHOOK_URL
 *    可对接 Formspree、Discord、Telegram Bot 等
 */

const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
  "Content-Type": "application/json",
};

function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

async function ensureTable(db) {
  try {
    await db.prepare(`
      CREATE TABLE IF NOT EXISTS subscribers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        lang TEXT DEFAULT 'zh',
        subscribed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        source TEXT DEFAULT 'website'
      )
    `).run();
  } catch (e) {
    console.log("Table may already exist:", e.message);
  }
}

export async function onRequestPost(context) {
  const { request, env } = context;

  try {
    const formData = await request.formData();
    const email = (formData.get("email") || "").trim().toLowerCase();
    const lang = formData.get("lang") || "zh";

    if (!email || !isValidEmail(email)) {
      return new Response(
        JSON.stringify({ ok: false, error: "Invalid email address" }),
        { status: 400, headers: CORS_HEADERS }
      );
    }

    const results = { saved: false, notified: false };

    // 1. 存储到 D1 数据库（如果绑定了）
    if (env.DB) {
      try {
        await ensureTable(env.DB);
        await env.DB.prepare(
          `INSERT OR IGNORE INTO subscribers (email, lang, source) VALUES (?, ?, ?)`
        ).bind(email, lang, "website").run();
        results.saved = true;
      } catch (e) {
        console.error("D1 save error:", e);
      }
    }

    // 2. 发送到 Webhook（如果配置了环境变量）
    if (env.FORM_WEBHOOK_URL) {
      try {
        await fetch(env.FORM_WEBHOOK_URL, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            email,
            lang,
            timestamp: new Date().toISOString(),
            source: "1hcrypto.com",
          }),
        });
        results.notified = true;
      } catch (e) {
        console.error("Webhook error:", e);
      }
    }

    // 3. 记录到日志（方便查看）
    console.log("[Subscribe]", email, lang, results);

    return new Response(
      JSON.stringify({
        ok: true,
        message: "Subscribed successfully",
        ...results,
      }),
      { status: 200, headers: CORS_HEADERS }
    );
  } catch (err) {
    console.error("Subscribe error:", err);
    return new Response(
      JSON.stringify({ ok: false, error: "Server error" }),
      { status: 500, headers: CORS_HEADERS }
    );
  }
}

export async function onRequestOptions() {
  return new Response(null, { status: 204, headers: CORS_HEADERS });
}
