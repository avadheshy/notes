Here’s a complete guide on serving static and media files in Django, including STATICFILES_DIRS, MEDIA_ROOT, MEDIA_URL, and handling file uploads via FileField and ImageField.

# 1. Serving Static Files (STATICFILES_DIRS)
🔹 What are Static Files?
Assets like CSS, JS, fonts, and icons that don’t change dynamically.

🔹 Configuration in settings.py:
```
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",  # or os.path.join(BASE_DIR, 'static')
]
```
🔹 In Development:
Ensure django.contrib.staticfiles is in INSTALLED_APPS.

🔹 In Templates:
```
{% load static %}
<link href="{% static 'css/style.css' %}" rel="stylesheet">
```
🔹 In Production:
Run:

```
python manage.py collectstatic
```
Django will gather all static files into STATIC_ROOT.

# 2. Uploading and Accessing Media Files
🔹 Configuration in settings.py:
```
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # or os.path.join(BASE_DIR, 'media')
```
🔹 In urls.py (development only):
```
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
# 3. Using FileField and ImageField
🔹 models.py:
```
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/')
    document = models.FileField(upload_to='product_docs/', null=True, blank=True)
```
The upload_to path is relative to MEDIA_ROOT.

# 4. Accessing Uploaded Files in Templates
```
<img src="{{ product.image.url }}" alt="Product Image">
<a href="{{ product.document.url }}">Download</a>
```
# 5. File Upload in Forms
🔹 In forms.py:
```
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'document']
```
🔹 In Template:
```
<form method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Upload</button>
</form>
```
enctype="multipart/form-data" is required for file uploads.

# Summary Table
```
Purpose	                    Setting / Feature	                Notes
Static files	            STATICFILES_DIRS, {% static %}	    CSS/JS/images used by templates
Media files             	MEDIA_ROOT, MEDIA_URL	            User-uploaded files like images
File upload fields	        FileField, ImageField	            Saved to /media/upload_to/ path
File serving	            static() in urls.py (dev only)	    Use Nginx or S3 in production
```

