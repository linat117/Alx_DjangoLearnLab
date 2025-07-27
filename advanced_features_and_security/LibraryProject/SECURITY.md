# HTTPS and Security Settings

## Django Settings

- **SECURE_SSL_REDIRECT**: Redirect all HTTP requests to HTTPS.
- **HSTS**: Instruct browsers to use HTTPS only for 1 year, including subdomains.
- **Secure Cookies**: Session and CSRF cookies marked secure.
- **Security Headers**: Added to prevent clickjacking, MIME sniffing, and enable browser XSS filter.
- **SECURE_PROXY_SSL_HEADER**: Configured for deployments behind a proxy/load balancer.

## Deployment Setup

- Web server (Nginx/Apache) configured with SSL certificates.
- HTTP port 80 redirects all requests to HTTPS port 443.
- Security headers reinforced at web server level for defense in depth.

## Testing

- Verify redirect by accessing http://yourdomain.com and confirming HTTPS redirect.
- Use security scanning tools like [Mozilla Observatory](https://observatory.mozilla.org/) or [SSL Labs](https://www.ssllabs.com/ssltest/) to verify headers and SSL config.

## Notes

- Remember to set `DEBUG = False` in production.
- Ensure `ALLOWED_HOSTS` is correctly set.
