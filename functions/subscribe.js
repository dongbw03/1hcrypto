export async function onRequestPost(context) {
  const { request, env } = context;
  
  try {
    const formData = await request.formData();
    const email = formData.get('email') || '';
    const lang = formData.get('lang') || 'zh';

    // Basic validation
    if (!email || !email.includes('@') || !email.includes('.')) {
      return new Response(JSON.stringify({ error: 'Invalid email' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    // TODO: Integrate with email service (Mailchimp / ConvertKit / Resend)
    // For now, log to Cloudflare Analytics Engine or Workers KV
    // Store in KV: namespace = SUBSCRIBERS
    if (env.SUBSCRIBERS) {
      await env.SUBSCRIBERS.put(email, JSON.stringify({
        email,
        lang,
        subscribedAt: new Date().toISOString(),
        source: '1hcrypto-footer',
      }));
    }

    return new Response(JSON.stringify({ ok: true }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (err) {
    return new Response(JSON.stringify({ error: 'Server error' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
}
