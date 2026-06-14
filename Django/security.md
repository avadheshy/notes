# Django Security Reference

A consolidated reference covering the major web security vulnerabilities and how Django helps mitigate each of them.

---

## 1. SQL Injection

**Risk:** Building raw SQL queries with string formatting lets an attacker inject arbitrary SQL (e.g. escalate privileges, drop tables).

```python
# VULNERABLE
from django.db import connection
cursor = connection.cursor()
username = request.GET['username']
sql_query = "SELECT * FROM users WHERE username = '%s';" % username
cursor.execute(sql_query)
```

If `username` is set to something like `'; DROP TABLE users;'`, the attacker can execute arbitrary SQL.

**Mitigation:**
- Prefer the Django ORM over raw SQL.
- If raw SQL is unavoidable, use parameterized queries — never string-format user input into the query string.

```python
# SAFE
sql_query = "SELECT * FROM users WHERE username = %s;"
cursor.execute(sql_query, [username])
```

- The same applies to `.extra()` and `RawSQL()` — always pass parameters separately.

---

## 2. CRLF Injection

**Risk:** Carriage-return/line-feed (`\r\n`) characters separate HTTP headers from the body. If user input containing these characters reaches headers or logs unvalidated, an attacker can:

1. **Poison logs** — inject fake log lines by embedding `%0d%0a` in input that gets logged.
2. **Split/smuggle HTTP responses** — inject extra headers via unvalidated header values.

```python
# RISKY
def my_view(request):
    content_type = request.META.get("CONTENT_TYPE")
    response = HttpResponse()
    response['Content-Type'] = content_type  # unvalidated
    return response
```

**Mitigation:**
- Never write user-controlled data directly into HTTP headers — validate against an allowlist.

```python
# SAFER
def my_view(request):
    content_type = request.META.get("CONTENT_TYPE")
    response = HttpResponse()
    response['Content-Type'] = (
        content_type if content_type in ALLOWED_CONTENT_TYPES else "application/json"
    )
    return response
```

- Django already guards email headers: if `subject`, `from_email`, or `recipient_list` contain `\n`, `send_mail()` raises `BadHeaderError`.

```python
from django.core.mail import BadHeaderError, send_mail

try:
    send_mail(subject, message, from_email, to_emails)
except BadHeaderError:
    return HttpResponse('Invalid header found.')
```

General fixes: strip CR/LF before using input in headers, and encode header values.

---

## 3. Timing Attacks

**Risk:** Python's `==` comparison for strings short-circuits on the first mismatched character, so comparison time leaks information about how many leading characters are correct. An attacker can use response-time differences to brute-force a secret (API key, token, etc.) one character at a time.

```python
# VULNERABLE
def is_valid_key(api_key):
    return api_key == SECURELY_STORED_API_KEY
```

**Mitigation:** Use a constant-time comparison.

```python
from django.utils.crypto import constant_time_compare
constant_time_compare(string1, string2)
```

Equivalent manual implementation (always iterates the full length):

```python
def compare(string1, string2):
    if len(string1) != len(string2):
        return False
    result = 0
    for a, b in zip(string1, string2):
        result |= ord(a) ^ ord(b)
    return not result
```

Django itself uses `constant_time_compare` internally for password checks. See also Python's `hmac.compare_digest`.

---

## 4. Clickjacking

**Risk:** A malicious site embeds your site in an invisible `<iframe>` and tricks users into clicking elements they can't actually see.

**Mitigation:** Django's `XFrameOptionsMiddleware` sets the `X-Frame-Options` header.

```python
MIDDLEWARE = (
    ...
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ...
)
```

| Value | Meaning | Default |
|---|---|---|
| `DENY` | Page can never be framed | Default in Django ≥ 3.0 |
| `SAMEORIGIN` | Page can only be framed by same-origin pages | Default in Django < 3.0 |

Override via setting:

```python
X_FRAME_OPTIONS = 'DENY'
```

Per-view overrides via decorators:

```python
from django.views.decorators.clickjacking import (
    xframe_options_deny,
    xframe_options_exempt,
    xframe_options_sameorigin,
)

@xframe_options_exempt
def view1(request): ...

@xframe_options_deny
def view2(request): ...

@xframe_options_sameorigin
def view3(request): ...
```

**Best practice:** keep `X_FRAME_OPTIONS = 'DENY'` unless a specific view genuinely needs framing.

---

## 5. Cross-Site Scripting (XSS)

**Risk:** Attacker-controlled content (often stored in the DB) is rendered as executable script in another user's browser.

### a) Output escaping / input validation
Django templates auto-escape variables, but raw string interpolation into HTML bypasses this:

```python
# VULNERABLE
name = request.GET.get('name')
html = '<p>Hello, My name is %s</p>' % name
```

A `name` value like `<script>alert("Error")</script>` would execute. Always rely on template auto-escaping (or explicit sanitization) instead of manual string building.

### b) Browser XSS filter (legacy)
`SECURE_BROWSER_XSS_FILTER` enabled the old `X-XSS-Protection` header for older browsers; modern browsers ignore this header, so it's largely redundant now.

### c) Protect cookies from JS
`SESSION_COOKIE_HTTPONLY = True` (default) prevents JavaScript from reading the session cookie.

### d) Content-Security-Policy (CSP)
CSP restricts which scripts/styles/images the browser will load, blocking inline/unauthorized JS. Django has no built-in CSP support — use `django-csp`:

```python
MIDDLEWARE = (
    ...
    'csp.middleware.CSPMiddleware',
    ...
)

CSP_DEFAULT_SRC = ("'self'", 'cdn.example.net')
CSP_STYLE_SRC = ("'self'", 'fonts.googleapis.com')
CSP_SCRIPT_SRC = ("'self'",)
CSP_IMG_SRC = ("'self'",)
CSP_FONT_SRC = ("'self'",)
```

**Key takeaway:** no single measure fully prevents XSS — combine escaping, CSP, and cookie protections.

---

## 6. Cross-Site Request Forgery (CSRF)

**Risk:** A logged-in user is tricked (via a malicious link/form on another site) into submitting an unwanted request to your site using their authenticated session — e.g. transferring money without intending to.

**Mitigation:** CSRF tokens — unique, per-session/request tokens that must accompany state-changing requests.

Django enables `CsrfViewMiddleware` by default. In templates:

```html
<form method="post">{% csrf_token %}...</form>
```

(For Jinja2, use `csrf_input`.)

Additional cookie hardening:

```python
CSRF_COOKIE_SECURE = True    # only sent over HTTPS
CSRF_COOKIE_HTTPONLY = True  # not accessible via JS
```

---

## 7. HTTP Strict Transport Security (HSTS)

**Goal:** Always serve over HTTPS, and prevent the browser from ever attempting an HTTP connection.

Enabled via:

```python
MIDDLEWARE = (
    ...
    'django.middleware.security.SecurityMiddleware',
    ...
)
```

### a) `SECURE_SSL_REDIRECT`
Redirects all HTTP requests to HTTPS. Default `False`.

```python
SECURE_SSL_REDIRECT = True
```

Limitation: the *first* HTTP request can still be intercepted before the redirect happens.

### b) `SECURE_HSTS_SECONDS`
Tells browsers to *only ever* use HTTPS for your domain for N seconds. Default `0`.

```python
SECURE_HSTS_SECONDS = 31536000  # 1 year
```

Start with a small value (e.g. `86400` = 1 day) to avoid locking users out if HTTPS isn't fully working everywhere yet, then increase once verified.

### c) `SECURE_HSTS_INCLUDE_SUBDOMAINS`
Extends the HSTS policy to all subdomains, not just the top-level domain. Default `False`.

```python
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
```

---

## 8. Session Hijacking

Two settings to enable:

| Setting | Effect |
|---|---|
| `SESSION_COOKIE_SECURE = True` | Cookie only sent over HTTPS — prevents attackers sniffing it on plaintext connections |
| `SESSION_COOKIE_HTTPONLY = True` | Cookie not readable from client-side JS, e.g. blocks `alert(document.cookie)` |

---

## 9. Denial of Service (DoS) / Rate Limiting

Throttling and rate limiting protect against brute-force and DoS attacks, and provide side benefits:
- Prevents server/network overload from traffic spikes.
- Improves responsiveness/UX under load.
- Avoids cost overruns from resource overuse.

Example with Django REST Framework:

```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '1000/day'
    }
}
```

(`django-ratelimit` is another common option for view-level limits.)

---

## 10. General Django Security Checklist

- [ ] `DEBUG = False` in production
- [ ] Run `python manage.py check --deploy` to catch misconfigurations
- [ ] Mask sensitive data in error reports with `@sensitive_variables` / `@sensitive_post_parameters`
- [ ] Never serve static files from Django itself — use nginx/Apache/CDN
- [ ] Set up logging & monitoring to catch incidents early
- [ ] Keep dependencies updated, especially for security releases
- [ ] `SESSION_COOKIE_SECURE`, `SESSION_COOKIE_HTTPONLY`, `CSRF_COOKIE_SECURE`, `CSRF_COOKIE_HTTPONLY` all `True`
- [ ] `X_FRAME_OPTIONS = 'DENY'`
- [ ] HSTS configured (`SECURE_SSL_REDIRECT`, `SECURE_HSTS_SECONDS`, `SECURE_HSTS_INCLUDE_SUBDOMAINS`)
- [ ] CSP configured via `django-csp`
- [ ] Use ORM / parameterized queries everywhere — no raw SQL string formatting
- [ ] Use `constant_time_compare` for any secret comparison

---

## Quick Reference Table

| Vulnerability | Django Mitigation |
|---|---|
| SQL Injection | ORM / parameterized queries |
| CRLF Injection | Input validation, Django's built-in header checks |
| Timing Attack | `constant_time_compare` |
| Clickjacking | `XFrameOptionsMiddleware`, `X_FRAME_OPTIONS` |
| XSS | Template auto-escaping, CSP (`django-csp`), `SESSION_COOKIE_HTTPONLY` |
| CSRF | `CsrfViewMiddleware`, `{% csrf_token %}`, secure cookie flags |
| Insecure transport | `SecurityMiddleware`, HSTS settings |
| Session Hijacking | `SESSION_COOKIE_SECURE`, `SESSION_COOKIE_HTTPONLY` |
| DoS / brute force | DRF throttling, `django-ratelimit` |

---

*Source notes consolidated from a Django security overview article (Dec 2023).*