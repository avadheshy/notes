Here's a comprehensive guide on Django security, including CSRF, XSS, SQL injection protection, key security settings, and safe file handling:

# 1. CSRF, XSS, and SQL Injection Protections
🔹 CSRF (Cross-Site Request Forgery)
Django protects POST requests using CSRF tokens.

✔️ Protection in Templates:
```
<form method="POST">
    {% csrf_token %}
    <!-- form fields -->
</form>
```
✔️ In Views:
If you're writing raw views (e.g. APIs or webhooks), use:

```
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def my_view(request):
    ...
```
⚠️ Use csrf_exempt only when absolutely necessary.

🔹 XSS (Cross-Site Scripting)
Django escapes variables by default:

```
{{ user_input }}  <!-- Safe, auto-escaped -->
```
If content is safe HTML (e.g. from an admin):
```
{{ content|safe }}  <!-- Only use when you're certain it's safe -->
```
⚠️ Never mark user input as |safe.

🔹 SQL Injection
Django ORM uses parameterized queries, making it secure by default.
```
# Safe
Product.objects.filter(name=request.GET['name'])

# NOT safe (raw query)
Product.objects.raw(f"SELECT * FROM products WHERE name = '{user_input}'")
Only use .raw() or connection.cursor() with extreme caution.
```

# 2. Important Django Security Settings
Setting	Purpose
DEBUG = False	Must be False in production
ALLOWED_HOSTS	Whitelist of allowed domains
SECURE_SSL_REDIRECT = True	Redirect all HTTP → HTTPS
SESSION_COOKIE_SECURE = True	Cookies only sent over HTTPS
CSRF_COOKIE_SECURE = True	CSRF cookie only sent over HTTPS
X_FRAME_OPTIONS = 'DENY'	Prevent clickjacking via iframe embedding
SECURE_HSTS_SECONDS	HTTP Strict Transport Security header
SECURE_CONTENT_TYPE_NOSNIFF	Prevent MIME-type sniffing
SECURE_BROWSER_XSS_FILTER	Activates browser's XSS protection

Add these in settings.py for production.

# 3. Safe File Handling and User Uploads
🔹 File Upload Field
```
from django.db import models

class Product(models.Model):
    image = models.ImageField(upload_to='product_images/')
```
🔹 Validate File Content & Extension
Use FileExtensionValidator and custom validators.

```
from django.core.validators import FileExtensionValidator

image = models.FileField(
    upload_to='uploads/',
    validators=[FileExtensionValidator(['jpg', 'png'])]
)
```
You can also validate size and type in a form or model's clean() method.

🔹 Secure Storage
Store files outside of web root or in a protected bucket.

Use secure permissions (e.g., AWS S3, Cloud Storage).

🔹 NEVER trust file name or content:
Always sanitize file names:
```
from django.utils.text import get_valid_filename

filename = get_valid_filename(user_uploaded_name)
```
# Summary
```
Topic	             Protection Method
CSRF	             {% csrf_token %}, CSRF middleware
XSS	                 Auto escaping, avoid `
SQL Injection	     Use ORM, avoid raw SQL
Secure Uploads	     Validate file type, sanitize names
Security Settings	SSL redirects, secure cookies, HSTS etc.
```