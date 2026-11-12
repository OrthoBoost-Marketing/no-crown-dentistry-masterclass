// Vercel Routing Middleware. Runs before the filesystem, which a vercel.json
// rewrite cannot do for "/" on a static project (index.html always wins).
// On the main domain, "/" serves the sales page; masterclass.nocrowndentistry.com
// and every other host keep "/" = the masterclass registration page.
// Note: rewrite to the clean URL "/sales" (verified over HTTPS); "/sales.html" 404s.
export const config = { matcher: '/' };

const SALES_HOSTS = new Set(['nocrowndentistry.com', 'www.nocrowndentistry.com']);

export default function middleware(request) {
  const host = (request.headers.get('host') || '').toLowerCase().split(':')[0];
  if (!SALES_HOSTS.has(host)) {
    return new Response(null, { headers: { 'x-middleware-next': '1' } });
  }
  return new Response(null, {
    headers: { 'x-middleware-rewrite': new URL('/sales', request.url).toString() },
  });
}
