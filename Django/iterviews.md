# Django, DRF & PostgreSQL — Complete Interview Reference

*4 YOE Python backend prep — Weavr (Django/DRF/MySQL/Redis), GA4 integration (FastAPI/MongoDB/Elasticsearch), TaskFlow (personal project), Search Engine (Mountblue, FastAPI/MongoDB/Lambda)*

## Table of Contents

1. **Django Fundamentals & Architecture** — MVT, project/app structure, admin, sessions, auth, URLs, models, templates, views (FBV/CBV), static files, model inheritance, middleware, context, settings.py, signals
2. **Django ORM, Transactions, Migrations & Database Concurrency** — QuerySet API, custom managers, soft deletes, `save()` overrides, `transaction.atomic`, database routers, migrations internals, locking/concurrency patterns, N+1 diagnosis, ContentType framework
3. **Django REST Framework (DRF)** — serializers (incl. nested/writable), APIView vs GenericAPIView vs ViewSet, request lifecycle internals, authentication vs authorization, pagination, throttling
4. **Async Django, Celery & Background Tasks** — async views, WSGI vs ASGI, Celery setup/retries/Beat/routing, file upload internals, ModelForm validation internals
5. **Testing** — TestCase vs TransactionTestCase, testing DRF views, mocking external services, factory_boy vs fixtures, query-count regression tests
6. **Security** — XSS/CSRF/SQLi/clickjacking defaults, PCI/SOC2/SOX-relevant PII handling, object-permission pitfalls
7. **Caching Strategy with Redis** — cache-aside/write-through/write-behind, invalidation, cache stampede prevention, Redis as cache vs primary store
8. **Request Flow & DRF Internals Recap**
9. **PostgreSQL** — EXPLAIN, JSONB, triggers, indexing strategy, MySQL vs PostgreSQL
10. **System Design Framing** — rate limiter design, idempotency, cross-timezone batch processing
11. **Quick-Fire Conceptual Table**
12. **Project Narrative — Behavioral/Technical Crossover Questions**
13. **Deployment Checklist (condensed)**
14. **Full Deployment Walkthrough** — Nginx/Gunicorn/Supervisor/Docker/Heroku/CI-CD reference

---

## Part 1: Django Fundamentals & Architecture

### 1.1 What is Django?

Django is a high-level Python web framework following the **Model-View-Template (MVT)** pattern, created by Adrian Holovaty and Simon Willison, released publicly in 2005. Built around rapid development, clean design, and DRY.

**Core built-in features:** ORM, automatic admin interface, URL routing, template system, form handling, authentication, internationalization, and security defaults (CSRF, XSS, SQL injection protection).

### 1.2 Django vs Flask vs FastAPI

| Feature | Django | Flask | FastAPI |
|---|---|---|---|
| Type | Full-stack framework | Micro framework | Modern API framework |
| Philosophy | Batteries included | Minimalist, flexible | High performance, type hints |
| Learning curve | Steeper | Gentle | Moderate |
| Built-in features | ORM, Admin, Auth, etc. | Basic routing, templating | Validation, auto docs |
| Performance | Good | Good | Excellent (async-native) |
| Use case | Full web applications | Small/medium apps | APIs, microservices |
| API docs | Manual (DRF adds this) | Manual | Automatic (OpenAPI/Swagger) |

**Interview-ready framing for your stack:** Weavr (Django/DRF/MySQL/Redis) is a structured backend service with well-defined CRUD and admin-heavy workflows — Django's batteries-included approach reduces boilerplate there. The GA4 integration (FastAPI/MongoDB/Elasticsearch) is an I/O-bound analytics ingestion pipeline pulling from GA4's API, writing to Mongo, indexing into Elasticsearch — FastAPI's native async and Pydantic validation fit that better, and you don't need Django's admin/ORM overhead for a service that's mostly ingestion and querying. Same logic applies to the Mountblue Search Engine project (FastAPI/MongoDB/AWS Lambda) — lightweight, deployable as Lambda functions, no need for a full framework's surface area.

### 1.3 Project vs App

**Project:** collection of configuration and apps for a site. Contains settings, root URL config, deployment files. `django-admin startproject projectname`.

**App:** a self-contained, reusable module (models, views, templates, URLs). `python manage.py startapp appname`.

```
myproject/
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py / asgi.py
├── blog/        # app
│   ├── models.py
│   ├── views.py
│   └── urls.py
└── shop/        # app
```

### 1.4 Django Architecture — MVT vs MVC

| Aspect | MVC | MVT (Django) |
|---|---|---|
| Components | Model, View, Controller | Model, View, Template |
| Controller | Developer-managed | Django framework (URL dispatcher) |
| View role | Presents data | Contains business logic |
| Template | Not present | Handles presentation |
| Examples | Laravel, Rails | Django |

**Request flow (high level):**
```
User Request → URL Dispatcher → View → Model (if needed) ↔ Database
                                  ↓
                              Template Rendering → HTTP Response → User
```

**Layered architecture:**
```
Web Server (nginx/Apache)
  → WSGI/ASGI Server (gunicorn/uvicorn)
    → Django
        Middleware → URL Dispatcher → Views → Models → Templates
  → Database
```

### 1.5 Creating a project, app, and running the server

```bash
pip install django
django-admin startproject myproject
cd myproject
python manage.py startapp myapp
# add 'myapp' to INSTALLED_APPS

python manage.py migrate
python manage.py runserver
python manage.py runserver 8080
python manage.py runserver 0.0.0.0:8000
```

### 1.6 Django Admin Interface

Auto-generated CRUD interface from model metadata.

```python
# models.py
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

# admin.py
from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'content']
```

```bash
python manage.py createsuperuser
```

### 1.7 Sessions (overview — see also section 9 for deep dive)

Sessions store per-user state server-side, with only a session ID sent to the client via cookie.

```python
# settings.py
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 1209600  # 2 weeks
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
```

```python
def login_view(request):
    request.session['user_id'] = user.id
    request.session['username'] = user.username

def profile_view(request):
    username = request.session.get('username', 'Guest')

def logout_view(request):
    request.session.flush()
```

### 1.8 Superuser

A user with `is_staff=True`, `is_superuser=True`, `is_active=True` — full admin access.

```bash
python manage.py createsuperuser
```

```python
from django.contrib.auth.models import User
User.objects.create_superuser(username='admin', email='admin@example.com', password='securepassword')
```

### 1.9 CSRF Token

Protects against Cross-Site Request Forgery. Django generates a per-session token; forms must include it; Django validates it on POST.

```html
<form method="post">
    {% csrf_token %}
    <input type="text" name="username">
</form>
```

```javascript
// AJAX usage
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie) {
        const cookies = document.cookie.split(';');
        for (let c of cookies) {
            c = c.trim();
            if (c.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(c.substring(name.length + 1));
            }
        }
    }
    return cookieValue;
}
$.ajaxSetup({
    beforeSend: (xhr) => xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'))
});
```

### 1.10 MEDIA_ROOT

Filesystem path holding user-uploaded files (via `FileField`/`ImageField`).

```python
# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# urls.py
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 1.11 Template Inheritance & Includes

```html
<!-- base.html -->
<html>
<head><title>{% block title %}My Site{% endblock %}</title></head>
<body>{% block content %}{% endblock %}</body>
</html>

<!-- child.html -->
{% extends "base.html" %}
{% block title %}Page Title{% endblock %}
{% block content %}<h1>Welcome</h1>{% endblock %}
```

```html
{% include "header.html" %}
{% include "snippet.html" with value="hello" %}
```

### 1.12 Connecting to a Database

```python
# PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase', 'USER': 'mydatabaseuser', 'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1', 'PORT': '5432',
    }
}
# MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase', 'USER': 'mydatabaseuser', 'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1', 'PORT': '3306',
    }
}
```

```bash
pip install psycopg2-binary   # PostgreSQL
pip install mysqlclient       # MySQL

python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations
```

### 1.13 Django Exception Classes

```python
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned, ValidationError, PermissionDenied, SuspiciousOperation
from django.http import Http404

try:
    user = User.objects.get(username='john')
except User.DoesNotExist:
    pass
except MultipleObjectsReturned:
    pass

def my_view(request):
    if not request.user.is_authenticated:
        raise PermissionDenied
    try:
        obj = MyModel.objects.get(pk=1)
    except MyModel.DoesNotExist:
        raise Http404("Object not found")
```

### 1.14 Filtering in Models (Field Lookups)

```python
Article.objects.filter(is_published=True)
Article.objects.filter(title__exact='Django Tutorial')
Article.objects.filter(title__iexact='django tutorial')
Article.objects.filter(title__contains='Django')
Article.objects.filter(title__startswith='How to')
Article.objects.filter(views__gt=100)
Article.objects.filter(views__gte=100)
Article.objects.filter(created_at__year=2023)
Article.objects.filter(category__in=['tech', 'science'])
Article.objects.filter(views__range=(100, 1000))
Article.objects.filter(description__isnull=True)
```

```python
from django.db.models import Q
Article.objects.filter(Q(category='tech') | Q(category='science'))
Article.objects.filter(~Q(category='tech'))
Article.objects.filter(Q(category='tech') & (Q(views__gt=100) | Q(is_featured=True)))
```

### 1.15 CharField vs TextField

| Aspect | CharField | TextField |
|---|---|---|
| Max length | Required | Optional |
| DB type | VARCHAR | TEXT |
| Use case | Short strings | Long text |
| Widget | Single-line input | Textarea |
| Indexing | Better | Less efficient |

### 1.16 Cookies

```python
def set_cookie_view(request):
    response = HttpResponse("Cookie set")
    response.set_cookie('username', 'john', max_age=3600)
    response.set_cookie('user_preference', 'dark_theme', max_age=365*24*60*60,
                         secure=True, httponly=True, samesite='Strict')
    return response

def get_cookie_view(request):
    return HttpResponse(request.COOKIES.get('username', 'Guest'))

def delete_cookie_view(request):
    response = HttpResponse("Deleted")
    response.delete_cookie('username')
    return response
```

### 1.17 Checking Django Version

```bash
python -m django --version
pip show django
```
```python
import django
print(django.VERSION)
```

### 1.18 Why Django is "loosely coupled"

Apps are independent (blog doesn't depend on shop), models/views/templates are separated, URLs are decoupled from views, and the database backend can change without touching models.

### 1.19 User Authentication

```python
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required

user = User.objects.create_user(username='john', email='john@example.com', password='securepassword')

def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    return render(request, 'profile.html')

@permission_required('blog.add_article')
def create_article(request):
    pass
```

```python
# Custom user model
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True, blank=True)

# settings.py
AUTH_USER_MODEL = 'accounts.CustomUser'
```

### 1.20 `render()` shortcut

```python
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {'articles': articles, 'title': 'All Articles'})

# Internally equivalent to:
from django.template import loader
def article_list(request):
    template = loader.get_template('blog/article_list.html')
    return HttpResponse(template.render({'articles': Article.objects.all()}, request))
```

### 1.21 Serialization

```python
from django.core import serializers
data = serializers.serialize('json', Article.objects.all())
data = serializers.serialize('json', Article.objects.all(), fields=('title', 'content'))
for obj in serializers.deserialize('json', data):
    obj.save()
```

```python
from django.forms.models import model_to_dict
def article_detail_api(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return JsonResponse(model_to_dict(article))
```

### 1.22 URL Routing

```python
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:id>/', views.article_detail, name='article_detail'),
    path('category/<str:name>/', views.category_view, name='category'),
    path('article/<slug:slug>/', views.article_by_slug, name='article_slug'),
    path('blog/', include('blog.urls')),
]
```

**URL converters:** `str` (default), `int`, `slug`, `uuid`, `path` (includes `/`).

```python
from django.urls import reverse
from django.shortcuts import redirect
return redirect(reverse('article_detail', args=[1]))
```
```html
<a href="{% url 'article_detail' article.id %}">View</a>
```

### 1.23 Project Directory Layout

```
myproject/
├── manage.py
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── myapp/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── tests.py
│   ├── migrations/
│   ├── templates/myapp/
│   └── static/myapp/
├── static/
├── media/
└── requirements.txt
```

### 1.24 Models — Fields & Relationships

```python
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.id])
```

**Common field types:** `CharField`, `TextField`, `EmailField`, `URLField`, `SlugField`, `IntegerField`, `FloatField`, `DecimalField`, `DateField`, `DateTimeField`, `TimeField`, `BooleanField`, `ImageField`, `FileField`.

**Relationships:**
```python
class Category(models.Model):
    name = models.CharField(max_length=100)

class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)       # one-to-many
    tags = models.ManyToManyField(Tag, blank=True)                        # many-to-many

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)            # one-to-one
```

### 1.25 Templates / Django Template Language

```html
<h1>{{ article.title }}</h1>
<p>Author: {{ article.author.username }}</p>
<p>{{ article.created_at|date:"Y-m-d" }}</p>

{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}

{% for article in articles %}
    <h3>{{ article.title }}</h3>
{% empty %}
    <p>No articles found.</p>
{% endfor %}

{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

**Common filters:** `upper`, `lower`, `truncatewords:10`, `capfirst`, `date:"F d, Y"`, `timesince`, `floatformat:2`, `add:5`, `length`, `first`, `last`, `default:"fallback"`.

```html
<!-- Inheritance -->
{% extends "base.html" %}
{% block title %}{{ article.title }} - {{ block.super }}{% endblock %}
{% block content %}{{ article.content|linebreaks }}{% endblock %}
```

### 1.26 Views — FBV vs CBV

```python
# Function-Based View
def article_list(request):
    articles = Article.objects.filter(is_published=True)
    return render(request, 'blog/article_list.html', {'articles': articles})

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'blog/create_article.html', {'form': form})
```

```python
# Class-Based View
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'
    queryset = Article.objects.filter(is_published=True)
    paginate_by = 10

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/create_article.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
```

| Aspect | FBV | CBV |
|---|---|---|
| Simplicity | Simple, explicit | Steeper curve |
| Reusability | Limited | High (inheritance) |
| Code organization | Can repeat | Cleaner |
| Debugging | Easier to trace | Harder to trace flow |

### 1.27 Static Files

```python
# settings.py
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

```bash
python manage.py collectstatic
python manage.py findstatic css/main.css
```

```python
# Production with whitenoise
MIDDLEWARE = ['django.middleware.security.SecurityMiddleware', 'whitenoise.middleware.WhiteNoiseMiddleware', ...]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### 1.28 django-admin vs manage.py

`django-admin` is the global CLI; `manage.py` is the project-specific wrapper that sets `DJANGO_SETTINGS_MODULE` automatically.

```bash
django-admin startproject myproject
python manage.py startapp myapp
python manage.py makemigrations / migrate / showmigrations
python manage.py createsuperuser / changepassword
python manage.py loaddata / dumpdata
python manage.py collectstatic
python manage.py shell / dbshell / check / test
```

**Custom management command:**
```python
# myapp/management/commands/my_command.py
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Updates article statistics'

    def add_arguments(self, parser):
        parser.add_argument('--days', type=int, default=30)

    def handle(self, *args, **options):
        articles = Article.objects.filter(created_at__gte=timezone.now() - timedelta(days=options['days']))
        self.stdout.write(self.style.SUCCESS(f'Updated {articles.count()} articles'))
```

### 1.29 Jinja2 vs Django Templates

```python
TEMPLATES = [
    {'BACKEND': 'django.template.backends.jinja2.Jinja2', 'DIRS': [...], 'OPTIONS': {'environment': 'myproject.jinja2.environment'}},
    {'BACKEND': 'django.template.backends.django.DjangoTemplates', 'DIRS': [...]},
]
```

| Feature | Django Templates | Jinja2 |
|---|---|---|
| Syntax | `{{ var }}`, `{% if %}` | Same surface syntax |
| Python-like expressions | Limited | More powerful |
| Performance | Good | Generally faster |
| Auto-escaping | Yes, integrated | Configurable |
| Django integration | Native (forms, CSRF) | Requires custom environment setup |

### 1.30 Model Inheritance Styles

**Abstract base classes** — share fields, no separate table:
```python
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Article(BaseModel):
    title = models.CharField(max_length=200)
```

**Multi-table inheritance** — each model gets its own table, linked via implicit OneToOne:
```python
class Place(models.Model):
    name = models.CharField(max_length=50)

class Restaurant(Place):
    serves_pizza = models.BooleanField(default=False)

# place.restaurant.serves_pizza accesses child from parent
```

**Proxy models** — same table, different Python behavior:
```python
class Student(Person):
    class Meta:
        proxy = True
        ordering = ['last_name']
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
```

| Type | Tables | Use case |
|---|---|---|
| Abstract | Child only | Share common fields |
| Multi-table | Parent + child | Need to query both |
| Proxy | Original only | Different behavior, same data |

### 1.31 Middleware

Hooks into Django's request/response cycle for global processing.

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

```python
class TimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        response['X-Response-Time'] = str(time.time() - start)
        return response

    def process_exception(self, request, exception):
        print(f"Exception: {exception}")
        return None
```

**Hooks:** `process_request()`, `process_view()`, `process_response()`, `process_exception()`.

### 1.32 Context & Context Processors

```python
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {'article': article, 'comments': article.comments.all()[:5]}
    return render(request, 'blog/article_detail.html', context)
```

```python
# context_processors.py
def site_settings(request):
    return {'SITE_NAME': settings.SITE_NAME}

# settings.py TEMPLATES OPTIONS
'context_processors': [
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'myapp.context_processors.site_settings',
]
```

```python
class ArticleDetailView(DetailView):
    model = Article
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()[:5]
        return context
```

### 1.33 settings.py — Key Sections

```python
DATABASES = {...}
INSTALLED_APPS = [...]
MIDDLEWARE = [...]
TEMPLATES = [...]
STATIC_URL / STATIC_ROOT / STATICFILES_DIRS
MEDIA_URL / MEDIA_ROOT

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 3600
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_TZ = True

AUTH_USER_MODEL = 'users.CustomUser'
AUTH_PASSWORD_VALIDATORS = [...]
```

**Environment-specific settings split:**
```python
# settings/base.py, settings/development.py, settings/production.py
from .base import *
DEBUG = True  # development.py only
```

### 1.34 Session Framework (deep dive)

```python
SESSION_ENGINE = 'django.contrib.sessions.backends.db'       # default
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'    # cache-backed
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db' # cached + persisted
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
```

```python
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    request.session.modified = True
    return JsonResponse({'cart_count': sum(cart.values())})
```

```python
request.session.set_expiry(300)   # 5 minutes
request.session.set_expiry(0)     # expire at browser close
request.session.cycle_key()       # security: rotate session key (e.g., after login)
request.session.flush()           # clear everything
```

**Session hijacking mitigation example:**
```python
class SessionSecurityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        if request.session.get('last_ip') and request.session['last_ip'] != request.META.get('REMOTE_ADDR'):
            request.session.flush()
        request.session['last_ip'] = request.META.get('REMOTE_ADDR')
        return self.get_response(request)
```

### 1.35 Django Signals

```python
from django.db.models.signals import post_save, pre_delete, m2m_changed
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
```

**Custom signals:**
```python
import django.dispatch
article_published = django.dispatch.Signal()

class Article(models.Model):
    def publish(self):
        self.is_published = True
        self.save()
        article_published.send(sender=self.__class__, article=self, published_by=self.author)

@receiver(article_published)
def notify_subscribers(sender, article, published_by, **kwargs):
    ...
```

**Registration options:** decorator, `.connect()`, or in `apps.py`'s `ready()`.

**Signal pitfalls (important — see also section 8.3):**
1. **Infinite loops** — calling `instance.save()` inside its own `post_save` handler retriggers the signal. Use `.update()` on the queryset instead, or guard with `kwargs.get('created')`.
2. **Performance** — don't do blocking I/O (emails, external API calls) synchronously in a handler; dispatch to Celery instead.
3. **Transaction timing** — a signal fires when `save()` is called, which may be *before* the surrounding transaction commits. Use `transaction.on_commit(lambda: ...)` for anything that should only happen on a guaranteed-committed row (e.g., charging a payment gateway).

```python
@receiver(post_save, sender=Order)
def process_payment(sender, instance, **kwargs):
    transaction.on_commit(lambda: payment_gateway.charge(instance.amount))
```

Use `dispatch_uid` to avoid duplicate registration on app reloads:
```python
@receiver(post_save, sender=User, dispatch_uid="create_user_profile")
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
```
## Part 2: Django ORM, Transactions, Migrations & Database Concurrency

### 2.1 ORM Basics

```python
# Create
article = Article.objects.create(title="My Article", content="...", author=request.user)
article, created = Article.objects.get_or_create(title="My Article", defaults={'content': '...'})

# Read
Article.objects.all()
Article.objects.filter(is_published=True)
Article.objects.get(pk=1)
get_object_or_404(Article, pk=1)
Article.objects.filter(title="X").exists()
Article.objects.filter(is_published=True).count()
Article.objects.order_by('-created_at', 'title')
Article.objects.all()[:5]
Article.objects.exclude(is_published=False)

# Update
article.title = "Updated"
article.save()
Article.objects.filter(is_published=False).update(is_published=True)
Article.objects.filter(pk=1).update(views=F('views') + 1)

# Delete
article.delete()
Article.objects.filter(is_published=False).delete()
```

### 2.2 `exists()`, `values()` vs `values_list()`, `defer()`, `bulk_update()`, `annotate()`

```python
Article.objects.filter(author=user).exists()       # → boolean
Article.objects.values('id', 'title')               # → list of dicts
Article.objects.values_list('title', flat=True)     # → list of tuples / flat values
Article.objects.defer('content', 'description')     # exclude heavy fields from query
Article.objects.only('title', 'slug')                # opposite of defer — only fetch these
Article.objects.bulk_update(article_list, ['title', 'is_published'])

from django.db.models import Count, Avg
Article.objects.annotate(comment_count=Count('comments'), avg_rating=Avg('ratings__score'))
```

### 2.3 Complex Queries: Q, F, Aggregations

```python
from django.db.models import Q, F, Count, Sum, Avg

Article.objects.filter(Q(title__contains='Django') | Q(content__contains='Python'))
Article.objects.filter(views__gt=F('likes') * 2)   # compare two fields at the DB level

stats = Article.objects.aggregate(total=Count('id'), avg_views=Avg('views'), total_views=Sum('views'))
```

### 2.4 Custom Model Managers

Managers define the query interface for a model. Every model gets `objects` by default.

```python
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

    def by_author(self, author):
        return self.get_queryset().filter(author=author)

class Post(models.Model):
    status = models.CharField(max_length=20)
    objects = models.Manager()        # default
    published = PublishedManager()    # custom
```

**Custom QuerySet + Manager (chainable methods):**
```python
class ArticleQuerySet(models.QuerySet):
    def published(self):
        return self.filter(is_published=True)
    def search(self, query):
        return self.filter(Q(title__icontains=query) | Q(content__icontains=query))

class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)
    def published(self):
        return self.get_queryset().published()

class Article(models.Model):
    objects = ArticleManager()

# Chainable: Article.objects.published().search('Django')
```

**Use cases:** soft deletes, multi-tenancy filtering, status-based default filters, encapsulating reusable business logic in the data layer.

### 2.5 Soft Deletes

```python
class SoftDeleteQuerySet(models.QuerySet):
    def delete(self):
        return self.update(deleted_at=timezone.now())
    def hard_delete(self):
        return super().delete()
    def alive(self):
        return self.filter(deleted_at__isnull=True)
    def dead(self):
        return self.exclude(deleted_at__isnull=True)

class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, using=self._db).alive()

class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True)
    objects = SoftDeleteManager()
    all_objects = models.Manager()  # bypass the filter, see everything

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save(using=using)

    def hard_delete(self):
        super().delete()

    def restore(self):
        self.deleted_at = None
        self.save()
```

### 2.6 Overriding `save()` — Patterns & Caveats

```python
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug, counter = base_slug, 1
            while Article.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)   # always call this
```

**Caveats:**
1. **Always call `super().save()`** — skipping it means nothing is persisted.
2. **Bulk operations bypass `save()`** — `bulk_create()`, `.update()`, and `loaddata` don't trigger your overridden logic or signals.
3. **Admin may not trigger custom logic** the same way depending on `save_model()` overrides.
4. **Signal timing** is affected — your custom logic runs around the signal dispatch point.
5. **Performance** — extra logic in `save()` runs on every single save; keep it lean.
6. **Wrap risky operations** (validation, external calls) in try/except.

```python
def save(self, *args, **kwargs):
    self.full_clean()  # run validation
    if self._state.adding:
        self.created_at = timezone.now()
    else:
        self.updated_at = timezone.now()
    super().save(*args, **kwargs)
```

### 2.7 Database Transactions

**Autocommit (default):** each operation commits immediately; Django can also wrap a whole view in a transaction via `ATOMIC_REQUESTS = True`.

```python
from django.db import transaction

@transaction.atomic
def create_article_with_tags(title, content, tag_names):
    article = Article.objects.create(title=title, content=content)
    for tag_name in tag_names:
        tag, _ = Tag.objects.get_or_create(name=tag_name)
        article.tags.add(tag)
    return article

def transfer_funds(from_account, to_account, amount):
    with transaction.atomic():
        from_account.balance -= amount
        from_account.save()
        to_account.balance += amount
        to_account.save()
```

**Nested transactions (savepoints):**
```python
def complex_operation():
    with transaction.atomic():               # outer transaction
        article = Article.objects.create(title="Test")
        try:
            with transaction.atomic():        # inner = savepoint
                process_risky_operation(article)
        except Exception:
            logger.error("Risky operation failed")  # inner rolled back, outer continues
        article.status = 'processed'
        article.save()
```

**Manual savepoint control:**
```python
def manual_transaction():
    sid = transaction.savepoint()
    try:
        Model.objects.create(...)
    except Exception:
        transaction.savepoint_rollback(sid)
    else:
        transaction.savepoint_commit(sid)
```

**Transaction hooks (run only after commit):**
```python
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        transaction.on_commit(lambda: send_email_notification(instance))
```

**Forcing a rollback:**
```python
def create_article_with_validation():
    with transaction.atomic():
        article = Article.objects.create(title="Test")
        if not validate_article_content(article):
            transaction.set_rollback(True)
            raise ValidationError("Invalid content")
        return article
```

**Row-level locking:**
```python
def update_counter_safe():
    with transaction.atomic():
        counter = Counter.objects.select_for_update().get(name='page_views')
        counter.value += 1
        counter.save()
```

> `select_for_update()` outside a `transaction.atomic()` block raises `TransactionManagementError` — it only makes sense inside a transaction.

### 2.8 Database Routers (Multiple Databases)

```python
class DatabaseRouter:
    route_app_labels = {'users': 'users_db', 'analytics': 'analytics_db'}

    def db_for_read(self, model, **hints):
        return self.route_app_labels.get(model._meta.app_label)

    def db_for_write(self, model, **hints):
        return self.route_app_labels.get(model._meta.app_label)

    def allow_relation(self, obj1, obj2, **hints):
        db_set = {'default', 'users_db', 'analytics_db'}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == self.route_app_labels[app_label]
        elif db in self.route_app_labels.values():
            return False
        return db == 'default'

# settings.py
DATABASE_ROUTERS = ['myproject.db_router.DatabaseRouter']
```

**Master-replica routing:**
```python
class PrimaryReplicaRouter:
    def db_for_read(self, model, **hints):
        return 'replica'
    def db_for_write(self, model, **hints):
        return 'primary'
    def allow_relation(self, obj1, obj2, **hints):
        return True
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == 'primary'
```

**Manual database selection in code:**
```python
users = User.objects.using('users_db').all()
user.save(using='users_db')

with connections['analytics'].cursor() as cursor:
    cursor.execute("SELECT * FROM analytics_event WHERE date > %s", [date])
```

> **Cross-database JOINs are not supported.** Query each database separately and combine results in Python.

```bash
python manage.py migrate --database=users_db
python manage.py migrate --database=users_db users
```

### 2.9 Migrations

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations
python manage.py sqlmigrate myapp 0001
python manage.py makemigrations --empty myapp
```

**Migration file structure:**
```python
class Migration(migrations.Migration):
    dependencies = [('myapp', '0001_initial')]
    operations = [
        migrations.AddField(
            model_name='post', name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=timezone.now),
            preserve_default=False,
        ),
    ]
```

**Data migrations:**
```python
def populate_slug_field(apps, schema_editor):
    Post = apps.get_model('myapp', 'Post')   # historical model, not the live one
    for post in Post.objects.all():
        post.slug = post.title.lower().replace(' ', '-')
        post.save()

def reverse_populate_slug_field(apps, schema_editor):
    Post = apps.get_model('myapp', 'Post')
    Post.objects.all().update(slug='')

class Migration(migrations.Migration):
    dependencies = [('myapp', '0002_add_slug_field')]
    operations = [migrations.RunPython(populate_slug_field, reverse_populate_slug_field)]
```

**Renaming a field while preserving data (3-step pattern):**
```python
operations = [
    migrations.AddField(model_name='user', name='full_name', field=models.CharField(max_length=200, null=True)),
    migrations.RunPython(copy_name_data, migrations.RunPython.noop),
    migrations.RemoveField(model_name='user', name='name'),
]
```

**Squashing:**
```bash
python manage.py squashmigrations myapp 0002 0005
```

**Rolling back:**
```bash
python manage.py migrate myapp 0002      # to specific migration
python manage.py migrate myapp zero      # unapply everything for an app
```

**Non-reversible operations need an explicit reverse:**
```python
migrations.RunSQL(
    "UPDATE myapp_mymodel SET field = 'value';",
    reverse_sql="UPDATE myapp_mymodel SET field = NULL;"
)
```

**How Django decides what to apply:** Django maintains a `django_migrations` table (app, name, applied timestamp). On `migrate`, it scans each app's `migrations/` directory, builds a dependency graph from each file's `dependencies = [...]`, diffs that graph against what's recorded as applied, and runs the unapplied ones in dependency order. `showmigrations` just renders `[X]`/`[ ]` against that same diff.

### 2.10 Database Concurrency

**Row-level locking with `select_for_update()`:**
```python
def transfer_money(from_account_id, to_account_id, amount):
    with transaction.atomic():
        from_account = Account.objects.select_for_update().get(id=from_account_id)
        to_account = Account.objects.select_for_update().get(id=to_account_id)
        if from_account.balance < amount:
            raise InsufficientFundsError()
        from_account.balance -= amount
        to_account.balance += amount
        from_account.save()
        to_account.save()
```

```python
# Skip rows already locked by another process — useful for worker queues
orders = Order.objects.select_for_update(skip_locked=True).filter(status='pending')[:10]
```

**Optimistic concurrency control (version field):**
```python
class Document(models.Model):
    version = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.pk:
            self.version += 1
            updated = Document.objects.filter(pk=self.pk, version=self.version - 1).update(
                title=self.title, content=self.content, version=self.version
            )
            if updated == 0:
                raise ConcurrentUpdateError("Document was modified by another user")
        else:
            super().save(*args, **kwargs)
```

**Database constraints to prevent race conditions:**
```python
class Inventory(models.Model):
    quantity = models.IntegerField()
    reserved = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(quantity__gte=0), name='quantity_non_negative'),
            models.CheckConstraint(check=models.Q(reserved__lte=models.F('quantity')), name='reserved_not_exceed_quantity'),
        ]
```

**Preventing duplicate creation under race conditions:**
```python
def get_or_create_unique_slug(title):
    base_slug = slugify(title)
    slug, counter = base_slug, 1
    while True:
        try:
            with transaction.atomic():
                return Article.objects.create(title=title, slug=slug)
        except IntegrityError:
            slug = f"{base_slug}-{counter}"
            counter += 1
            if counter > 100:
                raise ValueError("Unable to create unique slug")
```

**Distributed lock via cache (Redis-backed):**
```python
def distributed_lock_operation(lock_key, timeout=30):
    lock_id = f"lock:{lock_key}"
    if cache.add(lock_id, "locked", timeout=timeout):   # atomic SETNX
        try:
            return perform_critical_operation()
        finally:
            cache.delete(lock_id)
    else:
        raise ConcurrentOperationError("Operation already in progress")
```

**PostgreSQL advisory locks:**
```python
def with_advisory_lock(lock_id):
    class AdvisoryLock:
        def __enter__(self):
            with connection.cursor() as cursor:
                cursor.execute("SELECT pg_advisory_lock(%s)", [lock_id])
        def __exit__(self, *a):
            with connection.cursor() as cursor:
                cursor.execute("SELECT pg_advisory_unlock(%s)", [lock_id])
    return AdvisoryLock()
```

**Deadlock retry pattern:**
```python
def retry_on_deadlock(max_retries=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except OperationalError as e:
                    if 'deadlock' in str(e).lower() and attempt < max_retries - 1:
                        time.sleep(0.1 * (2 ** attempt))
                        continue
                    raise
        return wrapper
    return decorator
```

### 2.11 ORM Performance Optimization

```python
# select_related — ForeignKey/OneToOne, SQL JOIN, single query
Article.objects.select_related('author')

# prefetch_related — ManyToMany / reverse FK, separate query joined in Python
Article.objects.prefetch_related('tags')

from django.db.models import Prefetch
Article.objects.prefetch_related(
    Prefetch('comments', queryset=Comment.objects.select_related('author'))
)

# only()/defer() to limit fields
Article.objects.only('title', 'slug', 'created_at')
Article.objects.select_related('author').only('title', 'author__username')

# values()/values_list() for lightweight data
Article.objects.values_list('title', flat=True)

# Indexing
class Article(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    class Meta:
        indexes = [
            models.Index(fields=['created_at', 'is_published']),
            models.Index(fields=['author', '-created_at']),
        ]

# exists() instead of len()/count() for boolean checks
if Article.objects.filter(author=user).exists(): ...

# Bulk operations
Article.objects.bulk_create([Article(title=f'A{i}') for i in range(1000)], batch_size=100)
Article.objects.filter(is_published=False).update(is_published=True)

# Connection pooling
DATABASES = {'default': {..., 'CONN_MAX_AGE': 600}}
```

**N+1 query diagnosis in practice (interview-favorite — show the process, not just the fix):**

```python
# Detect: reset and count
from django.db import connection, reset_queries

reset_queries()
articles = Article.objects.all()
for a in articles:
    print(a.author.username)   # triggers 1 query per article
print(len(connection.queries))  # if this == N+1, confirmed
```

```python
# Guard against regression in tests
from django.test.utils import CaptureQueriesContext
from django.db import connection

def test_article_list_no_n_plus_1(self):
    ArticleFactory.create_batch(10)
    with CaptureQueriesContext(connection) as ctx:
        self.client.get('/api/articles/')
    self.assertLessEqual(len(ctx.captured_queries), 3)
```

This "detect → fix with the right tool → assert query count in tests" framing is stronger than just reciting `select_related` vs `prefetch_related`, because it shows you can find and prevent the bug, not just patch it once.

### 2.12 ContentType Framework (Generic Relations)

```python
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    text = models.TextField()

class BlogPost(models.Model):
    comments = GenericRelation(Comment)

# Usage
comment = Comment.objects.create(content_object=blog_post, text="Great post!")
```

**Use cases:** universal comment systems, tagging, activity logs, polymorphic relationships.
**Limitations:** no DB-level foreign key constraint, less efficient queries, no referential integrity at the DB level.
## Part 3: Django REST Framework (DRF)

### 3.1 DRF Setup

```bash
pip install djangorestframework
```

```python
# settings.py
INSTALLED_APPS = [..., 'rest_framework']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}
```

### 3.2 Serializers

```python
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'category', 'category_id', 'created_at', 'is_published']
        read_only_fields = ['created_at']

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long")
        return value
```

**`Meta` class** defines which model fields get serialized. `save()` is the method called to persist a validated serializer. `allow_null=True` permits `None` on a field.

### 3.3 Mass Assignment Protection (security-critical)

```python
# BAD — exposes is_staff/is_superuser to client input
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# GOOD — explicit allow-list
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        read_only_fields = ['id']
```

### 3.4 Nested Serializers

**Read-only nesting:**
```python
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_date']
```

**Writable nested serializers (must implement `create`/`update`):**
```python
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Book
        fields = ['id', 'title', 'author']

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author, _ = Author.objects.get_or_create(email=author_data['email'], defaults=author_data)
        return Book.objects.create(author=author, **validated_data)

    def update(self, instance, validated_data):
        author_data = validated_data.pop('author', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if author_data:
            for attr, value in author_data.items():
                setattr(instance.author, attr, value)
            instance.author.save()
        instance.save()
        return instance
```

**Dynamic field inclusion/exclusion (useful for list vs detail views):**
```python
class DynamicFieldsMixin:
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)
        super().__init__(*args, **kwargs)
        if fields is not None:
            for f in set(self.fields) - set(fields):
                self.fields.pop(f)
        if exclude is not None:
            for f in exclude:
                self.fields.pop(f, None)

# serializer = PostSerializer(post, fields=['title', 'author'])
```

**Optimize the queryset behind nested serializers, not just the serializer:**
```python
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = OptimizedPostSerializer
    def get_queryset(self):
        return Post.objects.select_related('author', 'category').prefetch_related('tags')
```

### 3.5 Views: function-based, APIView, GenericAPIView, ViewSets

```python
# Function-based API view
@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        return Response(ArticleSerializer(Article.objects.all(), many=True).data)
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

**APIView — full manual control:**
```python
class BookAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            book = Book.objects.get(pk=pk)
            return Response(BookSerializer(book).data)
        return Response(BookSerializer(Book.objects.all(), many=True).data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

**GenericAPIView — adds `get_queryset()`, `get_serializer()`, `get_object()`, filtering, pagination:**
```python
class BookGenericAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```

| Feature | APIView | GenericAPIView |
|---|---|---|
| Queryset | Manual | Built-in `get_queryset()` |
| Serializer | Manual instantiation | Built-in `get_serializer()` |
| Object retrieval | Manual | Built-in `get_object()` |
| Filtering/pagination | Manual | Built-in support |

```python
class BookGenericAPIView(GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'author']
    search_fields = ['title', 'description']

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(is_published=True)
        return qs

    def get_serializer_class(self):
        return BookCreateSerializer if self.request.method == 'POST' else BookSerializer
```

**Built-in generics:**
```python
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

**ViewSets + Routers:**
```python
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        article = self.get_object()
        article.is_published = True
        article.save()
        return Response({'status': 'published'})

    @action(detail=False)
    def published(self, request):
        qs = Article.objects.filter(is_published=True)
        return Response(self.get_serializer(qs, many=True).data)

# urls.py
router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
urlpatterns = router.urls
```

**Auto-generated routes from a registered ViewSet:**
- `GET /articles/` — list
- `POST /articles/` — create
- `GET /articles/{id}/` — retrieve
- `PUT/PATCH /articles/{id}/` — update/partial update
- `DELETE /articles/{id}/` — delete
- `POST /articles/{id}/publish/` — custom detail action
- `GET /articles/published/` — custom list action

**ViewSet types:** `ModelViewSet` (full CRUD), `ReadOnlyModelViewSet` (list/retrieve only), plain `ViewSet` (you implement `list`/`create`/`retrieve` manually).

```python
class ArticleViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'create':
            return ArticleCreateSerializer
        elif self.action == 'list':
            return ArticleListSerializer
        return ArticleDetailSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        return [AllowAny()]
```

### 3.6 DRF Request/Response Lifecycle (internals — common "explain what happens" question)

```
1. WSGI/ASGI → Django middleware → URL resolver → DRF dispatch()
2. dispatch() wraps the request in DRF's Request object
   (content negotiation; attaches .data, .query_params)
3. perform_authentication() — tries each class in authentication_classes
   until one succeeds, or returns AnonymousUser if none required
4. check_permissions() — ALL classes in permission_classes must return True
   (403 if any fails); this is VIEW-LEVEL (has_permission())
5. check_throttles() — 429 if exceeded
6. Method routing: GET → list()/retrieve(), POST → create(), etc.
7. get_queryset() → filter_backends applied → get_serializer() →
   is_valid() → perform_create()/perform_update() → .save()
8. check_object_permissions() — OBJECT-LEVEL (has_object_permission()),
   called explicitly inside get_object(); NOT automatic for list()
9. Response serialized via negotiated renderer (JSON by default)
```

**Important trap to know:** `has_permission()` runs automatically on every request via `check_permissions()`. `has_object_permission()` only runs when your view code calls `get_object()` — meaning a `list()` action never triggers object-level checks unless you explicitly call it. This is a classic "why didn't my object permission block this list view" bug.

**Content negotiation:**
```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
}
```
DRF picks a renderer based on the `Accept` header and/or `?format=` query param, falling back to the first configured renderer.

### 3.7 Authentication

```python
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication

class CustomTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'
    def authenticate_credentials(self, key):
        user, token = super().authenticate_credentials(key)
        if not user.is_active:
            raise AuthenticationFailed('User inactive')
        return (user, token)
```

```python
# JWT
from rest_framework_simplejwt.authentication import JWTAuthentication

class CustomJWTAuthentication(JWTAuthentication):
    def get_validated_token(self, raw_token):
        token = super().get_validated_token(raw_token)
        if token.payload.get('custom_claim') != 'expected':
            raise InvalidToken('Invalid claim')
        return token
```

**Session vs JWT — when to use which:**

| | Session Auth | JWT |
|---|---|---|
| State | Stateful (server stores session) | Stateless (claims in token) |
| Revocation | Easy — delete session | Hard — needs blocklist or short expiry |
| Scaling | Needs shared store (Redis) across instances | No shared state needed |
| Best fit | Same-origin browser app | Cross-service APIs, partner integrations, mobile |

For a platform with cross-service/telephony integrations talking to internal services across timezones (no browser session to lean on), JWT or service-to-service auth (mTLS/API keys) is the more natural fit than session cookies.

### 3.8 Authorization (Permissions) — Object-Level

```python
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
```

**Role-based, multi-condition permission:**
```python
class ProjectPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        try:
            membership = obj.team_members.get(user=request.user)
        except ProjectMember.DoesNotExist:
            return False
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method in ['PUT', 'PATCH']:
            return membership.role in ['editor', 'admin']
        elif request.method == 'DELETE':
            return membership.role == 'admin'
        return False
```

**Cached permission check (for expensive checks, e.g. external subscription service):**
```python
class CachedPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        cache_key = f'permission_{request.user.id}_{obj.id}_{request.method}'
        cached = cache.get(cache_key)
        if cached is not None:
            return cached
        result = self._check_permission(request, obj)
        cache.set(cache_key, result, 300)
        return result
```

### 3.9 Authentication vs Authorization

| Aspect | Authentication | Authorization |
|---|---|---|
| Purpose | Verify identity | Control access |
| Question | "Who are you?" | "What can you do?" |
| Timing | Before authorization | After authentication |
| Failure code | 401 Unauthorized | 403 Forbidden |
| Django mechanism | Authentication backends | Permission classes |

```python
class ArticleViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, CanPublishPermission]

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), CanPublishPermission()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return [AllowAny()]
```

### 3.10 Pagination

```python
'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination'
```

- `PageNumberPagination` — `?page=2`
- `LimitOffsetPagination` — `?limit=20&offset=40`
- `CursorPagination` — opaque cursor, best for large/real-time-changing datasets (avoids page-drift)

**Custom pagination:**
```python
class CustomPageNumberPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'results': data,
        })
```

```python
class CustomCursorPagination(CursorPagination):
    page_size = 20
    ordering = '-created_at'
```

### 3.11 Throttling

```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {'anon': '100/hour', 'user': '1000/hour', 'login': '5/min'},
}
```

```python
class CustomThrottle(BaseThrottle):
    def allow_request(self, request, view):
        ident = self.get_ident(request)
        key = f'throttle_{ident}'
        count = cache.get(key, 0)
        if count >= 100:
            return False
        cache.set(key, count + 1, timeout=3600)
        return True
```

**Redis sliding-window throttle:**
```python
class RedisThrottle(BaseThrottle):
    def allow_request(self, request, view):
        ident = self.get_ident(request)
        key = f'throttle:{ident}'
        now = time.time()
        window = 3600
        self.redis_client.zremrangebyscore(key, 0, now - window)
        if self.redis_client.zcard(key) >= 100:
            return False
        self.redis_client.zadd(key, {str(now): now})
        self.redis_client.expire(key, window)
        return True
```

> See section 6.1 for full rate-limiter algorithm tradeoffs (fixed window vs sliding window vs token bucket) — that's the framing a VP-round will actually want.

### 3.12 Custom Pagination from Scratch

```python
class CustomPagination(BasePagination):
    page_size = 25

    def paginate_queryset(self, queryset, request, view=None):
        paginator = Paginator(queryset, self.get_page_size(request))
        page_number = request.query_params.get('page', 1)
        try:
            self.page = paginator.page(int(page_number))
        except Exception:
            self.page = paginator.page(1)
        return list(self.page)

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('page_info', {
                'current_page': self.page.number,
                'total_pages': self.page.paginator.num_pages,
                'has_next': self.page.has_next(),
            }),
            ('results', data),
        ]))
```

### 3.13 Renderers

`BrowsableAPIRenderer` lets API responses be viewed/tested in a browser; `JSONRenderer` is the default machine-readable output.

### 3.14 API Documentation & Versioning

**Swagger/OpenAPI** — documents and lets consumers test the API interactively (commonly `drf-spectacular` or `drf-yasg`).

**Versioning best practice:** URL path versioning — `/api/v1/`, `/api/v2/` — simplest to reason about and cache.

### 3.15 API Gateway (conceptual, microservices context)

Routes requests to the correct backend service and can aggregate responses from multiple services into one — relevant if InvoiceCloud's IVR platform sits behind a gateway routing telephony/API traffic to different internal services.
## Part 4: Async Django, Celery & Background Tasks

### 4.1 Async Views in Django

Supported since Django 3.1+. Django bridges sync/async via `asgiref`.

```python
import asyncio
from django.http import JsonResponse

async def async_view(request):
    await asyncio.sleep(1)
    return JsonResponse({"status": "done"})
```

```python
# urls.py — no special handling, Django detects coroutine functions
path('async/', views.async_view),
```

**Key gotcha — the ORM is still mostly sync.** To call it from an async view, wrap it:
```python
from asgiref.sync import sync_to_async

async def get_articles(request):
    articles = await sync_to_async(list)(Article.objects.all())
    return JsonResponse({"count": len(articles)})
```

Django 4.1+ added native async terminal methods:
```python
article = await Article.objects.aget(pk=1)
await Article.objects.acreate(title="New")
count = await Article.objects.acount()
```
(`.filter()` itself stays sync/lazy — only the terminal/executing methods got async variants.)

**When to actually use async views:**
- ✅ I/O-bound work — calling another microservice, hitting a third-party API, async drivers for Mongo/Elasticsearch.
- ❌ CPU-bound or ORM-heavy sync work — `sync_to_async` just shuffles work onto a thread pool; you gain nothing and add complexity.

**Framing for your stack:** Weavr (Django/DRF/MySQL) is mostly synchronous CRUD/admin-heavy work — Django's sync-first model is fine there. The GA4 integration went FastAPI specifically because the workload is I/O-bound — concurrent calls to Mongo and Elasticsearch for analytics aggregation — where native async is a better fit than retrofitting Django's partial async support.

### 4.2 WSGI vs ASGI Deployment

| | WSGI | ASGI |
|---|---|---|
| Protocol | Sync, one request per worker thread | Async, concurrent requests per worker |
| Servers | Gunicorn (sync workers), uWSGI | Daphne, Uvicorn, Hypercorn |
| Use case | Standard request/response | WebSockets, long-polling, async views, Channels |
| Entry point | `wsgi.py` | `asgi.py` |

```python
# asgi.py
import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
application = get_asgi_application()
```

```bash
uvicorn myproject.asgi:application --workers 4
```

### 4.3 Celery — Setup & Core Concepts

```python
# celery.py
import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
app = Celery('myproject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
```

```python
# settings.py
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
```

**Architecture:** Celery Client (sends tasks) → Message Broker (Redis/RabbitMQ, stores task messages) → Celery Workers (execute) → Result Backend (stores results).

### 4.4 Defining & Calling Tasks

```python
@shared_task
def send_welcome_email(user_id):
    user = User.objects.get(id=user_id)
    send_mail('Welcome!', f'Welcome {user.username}!', 'from@example.com', [user.email])
    return f"Email sent to {user.email}"

# Calling
def register_user(request):
    user = User.objects.create_user(...)
    send_welcome_email.delay(user.id)        # async dispatch
    return JsonResponse({'status': 'queued'})
```

### 4.5 Retry Logic & Progress Tracking

```python
@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def process_payment(self, payment_id):
    try:
        payment = Payment.objects.get(id=payment_id)
        result = payment_gateway.charge(amount=payment.amount, card_token=payment.card_token)
        payment.status = 'completed'
        payment.transaction_id = result['transaction_id']
        payment.save()
        return f"Payment {payment_id} processed"
    except PaymentGatewayError as exc:
        raise self.retry(exc=exc, countdown=60 * (self.request.retries + 1))
    except Exception:
        payment.status = 'failed'
        payment.save()
        raise
```

```python
@shared_task(bind=True)
def bulk_data_import(self, file_path):
    total = count_csv_rows(file_path)
    processed = 0
    for row in read_records(file_path):
        process_record(row)
        processed += 1
        self.update_state(state='PROGRESS', meta={'current': processed, 'total': total})
    return {'status': 'completed', 'processed': processed}
```

```python
# Checking progress from a view
def check_task_progress(task_id):
    from celery.result import AsyncResult
    result = AsyncResult(task_id)
    if result.state == 'PROGRESS':
        return {'current': result.info.get('current'), 'total': result.info.get('total')}
    elif result.state == 'SUCCESS':
        return {'status': 'done', 'result': result.result}
    return {'state': result.state}
```

### 4.6 Periodic Tasks (Celery Beat)

```python
from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'send-daily-report': {'task': 'myapp.tasks.send_daily_report', 'schedule': crontab(hour=9, minute=0)},
    'cleanup-old-files': {'task': 'myapp.tasks.cleanup_old_files', 'schedule': crontab(hour=2, day_of_week=1)},
    'heartbeat': {'task': 'myapp.tasks.heartbeat', 'schedule': 30.0},
}
```

**Cross-timezone batch processing design (relevant to invoice/billing platforms operating across regions):**
- Store all timestamps in UTC in the DB; convert only at the presentation layer.
- Use **per-region Beat entries** with `crontab(hour=X)` rather than one global "nightly" job, since "nightly" maps to different UTC hours per region.
- Partition queues by region/priority via `CELERY_TASK_ROUTES` so one region's backlog doesn't starve another.
- Make tasks **idempotent** (see section 6.2) so retries after a worker crash don't double-process invoices.

### 4.7 Task Routing & Queues

```python
CELERY_TASK_ROUTES = {
    'myapp.tasks.send_email': {'queue': 'emails'},
    'myapp.tasks.process_image': {'queue': 'images'},
    'myapp.tasks.high_priority_task': {'queue': 'priority'},
}
```
```bash
celery -A myproject worker -Q emails --concurrency=4
celery -A myproject worker -Q priority --concurrency=8
```

### 4.8 Error Handling & Signals

```python
from celery.signals import task_failure

@task_failure.connect
def task_failure_handler(sender=None, task_id=None, exception=None, **kwargs):
    logger.error(f'Task {task_id} failed: {exception}')
    send_admin_alert.delay(subject=f'Task Failure: {sender}', message=str(exception))
```

### 4.9 Alternatives to Celery

- **Django-RQ** (Redis Queue) — simpler setup, good for lighter workloads.
- **Django-Q** — built-in scheduler, ORM-based broker option, simpler ops than Celery+Beat+Flower.

```python
# django-rq
import django_rq
queue = django_rq.get_queue('high')
queue.enqueue(send_email_job, user_id=request.user.id)
```

### 4.10 Why Use Celery at All?

Improved UX (long tasks don't block requests), horizontal scalability (distribute work across workers), reliability (retries, failure handling), flexible scheduling/routing, built-in monitoring (Flower).

### 4.11 File Uploads Under the Hood

```
1. HTTP request parsing — Django parses multipart/form-data
2. UploadHandler selection based on file size:
   FILE_UPLOAD_HANDLERS = [
       'django.core.files.uploadhandler.MemoryFileUploadHandler',   # small files
       'django.core.files.uploadhandler.TemporaryFileUploadHandler', # large files, written to disk temp
   ]
3. request.FILES['file'] returns an UploadedFile instance
4. Storage backend persists it (FileSystemStorage by default, or custom e.g. S3)
```

```python
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

class S3Storage(Storage):
    def _save(self, name, content): ...   # save to S3
    def url(self, name): ...               # return S3 URL
```

```python
FILE_UPLOAD_MAX_MEMORY_SIZE = 2.5 * 1024 * 1024
DATA_UPLOAD_MAX_MEMORY_SIZE = 2.5 * 1024 * 1024
FILE_UPLOAD_TEMP_DIR = '/tmp'
```

**Security:** file type validation, size limits, path traversal protection, virus-scanning integration points.

### 4.12 ModelForm Validation Internals

```
full_clean()
  ├── _clean_fields()   — per-field cleaning (clean_<field>())
  ├── _clean_form()     — cross-field validation (clean())
  └── _post_clean()     — builds the model instance, calls instance.full_clean()
```

```python
class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['field1', 'field2']

    def clean_field1(self):
        data = self.cleaned_data['field1']
        if some_condition:
            raise forms.ValidationError("Invalid field1")
        return data

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('field1') and cleaned_data.get('field2') and conflict_condition:
            raise forms.ValidationError("Field1 and Field2 conflict")
        return cleaned_data
```

```python
class MyModel(models.Model):
    def clean(self):
        if self.field1 == 'invalid' and self.field2 < 10:
            raise ValidationError("Invalid combination")
```
## Part 5: Testing

### 5.1 TestCase vs TransactionTestCase

```python
from django.test import TestCase, TransactionTestCase

class MyTestCase(TestCase):
    """
    Wraps each test in a transaction rolled back afterward. Fast.
    Use for ~95% of tests. Cannot test transaction.on_commit() callbacks
    since the transaction never actually commits.
    """
    def test_create_article(self):
        article = Article.objects.create(title="Test")
        self.assertEqual(Article.objects.count(), 1)

class MyTransactionTestCase(TransactionTestCase):
    """
    Actually commits and truncates tables after each test (slower).
    Use for transaction.on_commit() behavior, raw SQL transaction
    semantics, or multi-threaded code needing real commits.
    """
    def test_on_commit_callback(self):
        with self.captureOnCommitCallbacks(execute=True) as callbacks:
            Article.objects.create(title="Test")
        self.assertEqual(len(callbacks), 1)
```

### 5.2 Testing DRF API Views

```python
from rest_framework.test import APITestCase
from rest_framework import status

class ArticleAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='pass123')
        self.client.force_authenticate(user=self.user)  # bypass real auth flow

    def test_create_article(self):
        response = self.client.post('/api/articles/', {'title': 'New', 'content': '...'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Article.objects.count(), 1)

    def test_unauthenticated_access_denied(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/articles/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_permission_denied_for_non_owner(self):
        other = User.objects.create_user(username='other', password='pass')
        article = Article.objects.create(title='Test', author=other)
        response = self.client.delete(f'/api/articles/{article.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
```

### 5.3 Mocking External Services (directly relevant to GA4 OAuth-style integrations)

```python
from unittest.mock import patch, MagicMock

class GA4IntegrationTests(APITestCase):
    @patch('myapp.services.ga4_client.requests.post')
    def test_ga4_oauth_token_refresh(self, mock_post):
        mock_post.return_value = MagicMock(
            status_code=200,
            json=lambda: {'access_token': 'fake_token', 'expires_in': 3600}
        )
        result = refresh_ga4_token(refresh_token='abc123')
        self.assertEqual(result['access_token'], 'fake_token')
        mock_post.assert_called_once()
```

### 5.4 Fixtures vs factory_boy

```python
# Static JSON fixture — brittle, breaks on schema changes
# fixtures/articles.json
[{"model": "blog.article", "pk": 1, "fields": {"title": "Test"}}]
```

```python
# factory_boy — preferred in most modern Django codebases
import factory
from .models import Article

class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article
    title = factory.Sequence(lambda n: f"Article {n}")
    content = factory.Faker('paragraph')
    author = factory.SubFactory('myapp.factories.UserFactory')

def test_article_list(self):
    ArticleFactory.create_batch(5)
    response = self.client.get('/api/articles/')
    self.assertEqual(len(response.data), 5)
```

**Why factories generally win:** they survive schema changes (no brittle field-renamed-but-JSON-not-updated bugs), support relationships cleanly via `SubFactory`, and let each test override only what it cares about (`ArticleFactory(is_published=False)`).

### 5.5 Asserting Query Counts (regression-proofing N+1 fixes — see also section 2.11)

```python
from django.test.utils import CaptureQueriesContext
from django.db import connection

def test_article_list_no_n_plus_1(self):
    ArticleFactory.create_batch(10)
    with CaptureQueriesContext(connection) as ctx:
        self.client.get('/api/articles/')
    self.assertLessEqual(len(ctx.captured_queries), 3)
```

---

## Part 6: Security

### 6.1 Built-in Protections

**XSS** — templates auto-escape variables by default:
```python
{{ user_input }}  # auto-escaped
from django.utils.html import escape
safe_content = escape(user_input)  # manual escaping if needed outside templates
```

**CSRF** — `CsrfViewMiddleware` + `{% csrf_token %}` in forms (see section 1.9 for full flow).

**SQL Injection** — the ORM parameterizes queries automatically:
```python
User.objects.filter(name=user_input)  # safe
User.objects.raw("SELECT * FROM users WHERE name = %s", [user_input])  # safe — always use parameterized raw SQL
```
**Safest way to run raw SQL in Django:** parameterized queries via `cursor.execute(sql, params)` or `.raw(sql, params)` — never string-format user input into SQL.

**Clickjacking:**
```python
MIDDLEWARE = ['django.middleware.clickjacking.XFrameOptionsMiddleware', ...]
X_FRAME_OPTIONS = 'DENY'  # or 'SAMEORIGIN'
```

**Security headers:**
```python
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

**Password security:** PBKDF2 hashing by default, configurable `AUTH_PASSWORD_VALIDATORS`.

**Host header validation:** `ALLOWED_HOSTS = ['example.com']`.

### 6.2 PII / Compliance-Sensitive Data (PCI-DSS / SOC2 / SOX — directly maps to roles requiring this)

- **Never store full card numbers (PAN).** Tokenize through a PCI-compliant processor; store only the token.
- **Field-level encryption** for any sensitive field you must store:
```python
from django_cryptography.fields import encrypt

class PaymentMethod(models.Model):
    last_four = models.CharField(max_length=4)         # OK to store
    token = encrypt(models.CharField(max_length=255))   # encrypted at rest
```
- **Audit logging** — who accessed/modified what, when. This is a SOX/SOC2 control, not optional polish.
- **Least-privilege DB roles** — separate read-only/reporting users from write-capable app users.
- **Secrets management** — never in `settings.py`/git; environment variables or a vault (AWS Secrets Manager, HashiCorp Vault).
```python
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']  # fail loudly if missing
DB_PASSWORD = os.environ['DB_PASSWORD']
```

### 6.3 Object-level Permission Pitfall (recap — see 3.6, 3.8)

`has_object_permission()` is not checked automatically on `list()` — only when `get_object()` is explicitly called. Don't assume an `IsOwnerOrReadOnly` permission protects a list endpoint; it doesn't unless you filter the queryset yourself.

---

## Part 7: Caching Strategy with Redis

### 7.1 Caching Strategies — Tradeoffs

| Strategy | Mechanism | Best fit |
|---|---|---|
| Cache-aside (lazy loading) | App checks cache; on miss, reads DB, populates cache | Default for read-heavy, infrequently-changing data |
| Write-through | Every write updates cache + DB together | Need immediate read-after-write consistency |
| Write-behind (write-back) | Write to cache first, DB updated async | High write throughput, eventual DB consistency acceptable |
| Read-through | Cache library itself owns DB loading | Less common in Django; usually hand-rolled as cache-aside |

```python
from django.core.cache import cache

def get_article(article_id):
    cache_key = f'article:{article_id}'
    article = cache.get(cache_key)
    if article is None:
        article = Article.objects.select_related('author').get(pk=article_id)
        cache.set(cache_key, article, timeout=300)
    return article

def update_article(article_id, **kwargs):
    Article.objects.filter(pk=article_id).update(**kwargs)
    cache.delete(f'article:{article_id}')   # invalidate, don't try to update-in-place
```

### 7.2 Invalidation via Signals

```python
@receiver([post_save, post_delete], sender=Article)
def invalidate_article_cache(sender, instance, **kwargs):
    cache.delete(f'article:{instance.pk}')
    cache.delete('article_list')
```

### 7.3 Cache Stampede Prevention

A cache stampede happens when a popular key expires and many concurrent requests all hit the DB simultaneously to repopulate it.

```python
import redis
def get_article_with_lock(article_id):
    cache_key = f'article:{article_id}'
    article = cache.get(cache_key)
    if article is not None:
        return article

    lock_key = f'lock:{cache_key}'
    r = redis.Redis()
    if r.set(lock_key, '1', nx=True, ex=10):   # only one process gets the lock
        try:
            article = Article.objects.get(pk=article_id)
            cache.set(cache_key, article, timeout=300)
        finally:
            r.delete(lock_key)
    else:
        article = Article.objects.get(pk=article_id)  # fallback: serve directly or stale
    return article
```

Other mitigations: **probabilistic early expiration** (recompute slightly before TTL with randomness) or **staggered TTLs** (`timeout=300 + random.randint(0, 30)`) so many keys don't expire at the same instant.

### 7.4 Redis as Cache vs Primary Store

**As cache:** acceptable to lose data (it's derived), so `maxmemory-policy allkeys-lru` and minimal persistence are fine.

**As primary data** (rate-limit counters, sessions, leaderboards): need **AOF persistence** (or frequent RDB snapshots) — losing this data is a real incident, not a cache miss.

### 7.5 Redis Data Types & Use Cases (quick reference)

| Type | Common use |
|---|---|
| String | Simple cache values, counters (`INCR`) |
| Hash | Object-like storage (user session fields) |
| List | Queues, recent-activity feeds |
| Set | Unique membership checks, tags |
| Sorted Set (ZSET) | Leaderboards, sliding-window rate limiting (`ZADD`/`ZREMRANGEBYSCORE`) |
| Pub/Sub | Lightweight real-time messaging |

---

## Part 8: Request Flow & DRF Internals Recap

### 8.1 Full Django Request Flow

```
1. Web Server (nginx/Apache) → WSGI/ASGI Server (Gunicorn/Uvicorn)
2. Django's WSGI/ASGI handler wraps environ into HttpRequest
3. Middleware chain — process_request() top-down
4. URL Resolver matches path → view function/class
5. View executes — interacts with Model layer (ORM → SQL → DB)
6. Template rendered with context (if HTML response)
7. HttpResponse created
8. Middleware chain — process_response() bottom-up (reverse order)
9. Response returned through WSGI/ASGI → web server → browser
```

```python
class ExceptionHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            return self.get_response(request)
        except Http404:
            return render(request, '404.html', status=404)
        except PermissionDenied:
            return render(request, '403.html', status=403)
        except Exception as e:
            logger.error(f"Server error: {e}")
            return render(request, '500.html', status=500)
```

### 8.2 DRF-specific lifecycle

See Part 3.6 for the full breakdown (authentication → permissions → throttles → method dispatch → object permissions → response).
## Part 9: PostgreSQL

### 9.1 Core PostgreSQL Concepts

| Question | Answer |
|---|---|
| Purpose of `EXPLAIN` | Shows the query execution plan — index usage, join strategy, estimated cost — used to diagnose slow queries |
| Full-text search | `tsvector` (and `tsquery` for matching) |
| Purpose of a trigger | Automate actions on data changes (e.g., maintain audit log, update derived columns) |
| Best JSON storage type | `JSONB` — binary, indexable, faster querying than plain `JSON` (which stores exact text and re-parses on each access) |

```python
# Using EXPLAIN via Django
Article.objects.filter(is_published=True).explain()
Article.objects.filter(is_published=True).explain(analyze=True)  # actually runs the query, gives real timing
```

```sql
-- Trigger example
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_article_modtime
BEFORE UPDATE ON blog_article
FOR EACH ROW EXECUTE PROCEDURE update_modified_column();
```

```python
# JSONB field in Django
class Event(models.Model):
    payload = models.JSONField()  # maps to JSONB on PostgreSQL

Event.objects.filter(payload__user_id=123)             # query into JSON keys
Event.objects.filter(payload__contains={'type': 'click'})
```

### 9.2 Indexing Strategy

- **B-tree** (default) — equality and range queries, the vast majority of cases.
- **GIN** — good for `JSONB`, array fields, full-text search (`tsvector`).
- **GiST** — geometric/range types.
- **Partial indexes** — index only a subset of rows (e.g., `WHERE is_published = true`) to keep the index small and fast for the common query pattern.

```python
class Meta:
    indexes = [
        models.Index(fields=['created_at', 'is_published']),
        models.Index(fields=['author', '-created_at']),
    ]
```

### 9.3 PostgreSQL-specific Concurrency Features

```python
# RETURNING clause via raw cursor
with connection.cursor() as cursor:
    cursor.execute("UPDATE blog_article SET views = views + 1 WHERE id = %s RETURNING *", [1])
    result = cursor.fetchone()
```

```python
# Advisory locks — app-level mutual exclusion without locking actual rows
with connection.cursor() as cursor:
    cursor.execute("SELECT pg_advisory_lock(%s)", [lock_id])
    # critical section
    cursor.execute("SELECT pg_advisory_unlock(%s)", [lock_id])
```

### 9.4 MySQL vs PostgreSQL (you've used both — Weavr is MySQL)

| | MySQL | PostgreSQL |
|---|---|---|
| JSON support | `JSON` type, less mature indexing | `JSONB` — binary, indexable, generally faster for JSON-heavy workloads |
| Full-text search | Built-in but more limited | `tsvector`/`tsquery`, more powerful |
| Concurrency model | Row-level locking (InnoDB) | MVCC (multi-version concurrency control) — readers don't block writers |
| Replication | Well-established, simple primary-replica | Logical + streaming replication, more flexible |
| Use case fit | Simpler relational workloads, very common in legacy/CMS stacks | Complex queries, JSON-heavy, analytics-adjacent workloads |

**Interview-ready framing:** Weavr uses MySQL for a structured, well-defined relational schema where MySQL's simpler operational model and InnoDB's row-level locking are sufficient. If you were designing a new service with heavier JSON/analytics needs (like the GA4 pipeline, which instead chose MongoDB/Elasticsearch directly), PostgreSQL's `JSONB` + GIN indexing would be the natural relational-DB alternative to evaluate first.

---

## Part 10: System Design Framing (VP-round style — architecture reasoning, not just syntax)

### 10.1 Designing a Rate Limiter

| Algorithm | Behavior | Tradeoff |
|---|---|---|
| Fixed window counter | Redis `INCR` + `EXPIRE` | Simple but allows ~2x burst at window boundaries |
| Sliding window log | Store every request timestamp, count within window | Accurate but memory-heavy at scale |
| Sliding window counter | Weighted average of current + previous window | Good production balance — common default |
| Token bucket | Tokens refill at fixed rate; requests consume tokens | Handles bursts gracefully; used by AWS/Stripe-style APIs |

```python
# Sliding window counter — typical "good enough" production answer
import time
from django.core.cache import cache

def is_rate_limited(user_id, limit=100, window=60):
    now = int(time.time())
    current_window = now // window
    key = f'rate:{user_id}:{current_window}'
    count = cache.get(key, 0)
    if count >= limit:
        return True
    cache.set(key, count + 1, timeout=window * 2) if count == 0 else cache.incr(key)
    return False
```

### 10.2 Idempotency for Payment/Invoice Creation

```python
class CreateInvoiceView(APIView):
    def post(self, request):
        idempotency_key = request.headers.get('Idempotency-Key')
        if not idempotency_key:
            return Response({'error': 'Idempotency-Key header required'}, status=400)

        cache_key = f'idempotency:{idempotency_key}'
        existing = cache.get(cache_key)
        if existing:
            return Response(existing, status=200)  # return prior result, don't re-process

        with transaction.atomic():
            invoice = Invoice.objects.create(**request.data)
            result = InvoiceSerializer(invoice).data
            cache.set(cache_key, result, timeout=86400)
        return Response(result, status=201)
```

**Important nuance to say out loud in an interview:** the cache/lock alone isn't sufficient for correctness — back it with a DB-level **unique constraint** on the idempotency key column too, so a cache outage can't allow a duplicate charge to slip through.

### 10.3 Cross-Timezone Batch Processing (Celery)

- Store all timestamps in UTC; convert only at the presentation layer.
- Use **per-region Celery Beat entries** (`crontab(hour=X)`), not one global "nightly" job — "nightly" means a different UTC hour per region.
- **Partition queues by region/priority** (`CELERY_TASK_ROUTES`) so one region's backlog doesn't starve another.
- Make tasks **idempotent** so retries after a crash don't double-process.

### 10.4 General System Design Talking Points to Have Ready

- **Read-heavy vs write-heavy** — drives whether you reach for read replicas + caching, or write-optimized patterns (write-behind cache, batching, queueing).
- **Consistency vs availability tradeoffs** — be ready to say "eventual consistency is fine for X (analytics counts) but not Y (account balances)."
- **Horizontal scaling of Django** — stateless app servers behind a load balancer, session state in Redis (not in-process), static/media offloaded to S3/CDN.
- **Database connection pooling** — `CONN_MAX_AGE`, or an external pooler (PgBouncer) when you have many short-lived app server connections against PostgreSQL.

---

## Part 11: Quick-Fire Conceptual Table (good warm-up round prep)

| Question | Concise Answer |
|---|---|
| `get()` vs `filter().first()` | `get()` raises `DoesNotExist`/`MultipleObjectsReturned`; `filter().first()` returns `None` or first match silently. Use `get()` when the row must exist, `filter().first()` for optional lookups. |
| `bulk_create()` caveats | Doesn't call `save()`, doesn't fire signals, doesn't set PKs on SQLite (does on Postgres via `RETURNING`), skips full_clean validation. |
| `update()` vs instance `.save()` | `update()` is a single SQL UPDATE — no signals, no overridden `save()` logic, more efficient for bulk changes. |
| `Meta.ordering` vs `.order_by()` | `Meta.ordering` is the default applied to all queries; `.order_by()` overrides it per-query and is cheaper when you don't need the model default. |
| `null=True` vs `blank=True` | `null` is DB-level (column can be NULL); `blank` is form/validation-level (field can be empty in forms/admin). For `CharField`, convention is `blank=True` only — use empty string, not NULL. |
| `related_name` | Sets the reverse accessor from the related model back to this one (`article.comments.all()` instead of the default `article.comment_set.all()`). |
| `select_for_update()` outside a transaction | Raises `TransactionManagementError` — only valid inside `transaction.atomic()`. |
| `ViewSet` vs `APIView` | `ViewSet` maps actions (`list`, `create`, `retrieve`...) to a router's auto-generated URLs; `APIView` requires you to define `get`/`post`/etc. and wire URLs manually. |
| `JSONField` vs `TextField` storing JSON manually | `JSONField` (→ `JSONB` on Postgres) supports indexing and querying into keys; storing JSON as text in a `TextField` means you lose all of that and must parse in Python every time. |
| Why avoid `fields = '__all__'` on a `ModelSerializer` for `User` | Mass assignment risk — exposes fields like `is_staff`/`is_superuser` to client-controlled input. |
| `has_permission()` vs `has_object_permission()` | View-level (always checked) vs object-level (only checked when `get_object()` is explicitly called — not automatic on `list()`). |

---

## Part 12: Project Narrative — Likely Behavioral/Technical Crossover Questions

Your resume spans Django (Weavr), FastAPI (GA4 integration, Mountblue Search Engine), and TaskFlow (personal project). Expect questions probing *why*, not just *what*.

**Q: "Your resume shows both Django and FastAPI — walk me through how you decide between them."**

- *Weavr (Django/DRF/MySQL/Redis):* structured, relational data, well-defined CRUD and admin-heavy workflows — Django's batteries-included approach (ORM, admin, auth) cuts boilerplate for a team service that needs to move fast on standard business logic.
- *GA4 integration (FastAPI/MongoDB/Elasticsearch):* schema-flexible analytics ingestion with heavy I/O — pulling from GA4's API, writing to Mongo, indexing into Elasticsearch. FastAPI's native async and Pydantic validation fit an I/O-bound pipeline better than Django's sync-first ORM, and there's no need for Django's admin/ORM surface area on a service that's mostly ingestion and querying.
- *Mountblue Search Engine (FastAPI/MongoDB/AWS Lambda):* same reasoning — lightweight, deployable as Lambda functions, no need for a full framework.

**Q: "Tell me about a time you found a bug in production. How did you trace it?"**

Use the N+1 diagnosis workflow (section 2.11) as a template if you don't have a stronger story — it demonstrates *process* (detect via query count → measure → fix with the right ORM tool → regression-guard with a test), which is what's actually being scored, not just "I know `select_related` exists."

**Q: "How do you approach documentation/handoff for other engineers?"**

You have real material: the GA4 OAuth service (`analytics_login`, Falcon-based), Quick Commerce API endpoint docs, and Zepto/Myntra scraping spider docs. Frame it as: "I write the README/runbook alongside the code, not after — especially for handoff-prone services like the scraping spiders, where the next person won't have context on the target site's quirks (rate limits, layout changes, auth flow)."

**Q: "Why did TaskFlow use FastAPI + MySQL + Redis + React rather than Django end-to-end?"**

If asked — frame as a deliberate decoupled-API choice: FastAPI for a typed, async-capable API layer; MySQL for relational task/team data with real multi-tenancy constraints; Redis for caching/session-adjacent data; React as a separate frontend consuming the API, mirroring a real production split rather than Django's monolithic templating approach. This also demonstrates you can operate outside Django when the project calls for it.

### 12.1 Honest Gap Acknowledgment (don't bluff this one)

If the role mentions **Asterisk/FAST AGI** (telephony) and you haven't touched it: don't fake depth. A defensible bridge answer: *"I haven't worked directly with Asterisk/FAST AGI, but I've built async, I/O-heavy services (the GA4 ingestion pipeline) and rate-limited/queued systems (Celery + Redis), which are the same general class of problem — handling concurrent, low-latency external I/O reliably. I'd expect the ramp-up to be learning Asterisk's specific AGI protocol, not the underlying concurrency/reliability patterns."* This is honest, shows transferable reasoning, and doesn't oversell.

---

## Part 13: Deployment Checklist (condensed — full original deployment walkthrough retained below in Part 14)

1. **Settings split** — `base.py` / `development.py` / `production.py`, `DEBUG = False` in prod, `ALLOWED_HOSTS` set.
2. **Database** — production engine configured via env vars, connection pooling (`CONN_MAX_AGE` or PgBouncer).
3. **Static/media** — `collectstatic` run, served via whitenoise/CDN/S3, not Django itself in production.
4. **Process manager** — Gunicorn/Uvicorn behind Supervisor or systemd.
5. **Reverse proxy** — Nginx in front, handling TLS termination, static file serving, and proxying to the app server.
6. **TLS** — Certbot/Let's Encrypt or managed cert.
7. **Background workers** — Celery worker + Beat running as separate supervised processes from the web process.
8. **Migrations** — run as part of deploy pipeline, before traffic is routed to new code (or with backward-compatible migration ordering for zero-downtime deploys).
9. **Monitoring** — error tracking (Sentry), APM (New Relic/Datadog), log aggregation.
10. **Secrets** — environment variables or a vault, never committed.

---

## Part 14: Full Deployment Walkthrough (Linux/Nginx/Gunicorn/Supervisor reference)

### 14.1 Production Settings

```python
# settings/production.py
import os
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
```

### 14.2 Server Preparation

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv
sudo apt install postgresql postgresql-contrib
sudo apt install nginx
sudo apt install supervisor
```

### 14.3 Application Setup

```bash
cd /var/www/
sudo git clone https://github.com/yourusername/yourproject.git
cd yourproject
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

```bash
# .env
SECRET_KEY=your-secret-key
DEBUG=False
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

### 14.4 Database Setup

```sql
sudo -u postgres psql
CREATE DATABASE your_db_name;
CREATE USER your_db_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE your_db_name TO your_db_user;
\q
```

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

### 14.5 Gunicorn + Supervisor

```python
# gunicorn_config.py
bind = "127.0.0.1:8000"
workers = 3
worker_class = "sync"
timeout = 30
preload_app = True
```

```ini
# /etc/supervisor/conf.d/yourproject.conf
[program:yourproject]
command=/var/www/yourproject/venv/bin/gunicorn --config gunicorn_config.py yourproject.wsgi:application
directory=/var/www/yourproject
user=www-data
autostart=true
autorestart=true
stdout_logfile=/var/log/yourproject.log
```

### 14.6 Nginx

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    location /static/ { root /var/www/yourproject; }
    location /media/  { root /var/www/yourproject; }

    location / {
        include proxy_params;
        proxy_pass http://127.0.0.1:8000;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/yourproject /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl restart nginx
```

### 14.7 SSL

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

### 14.8 Start Services

```bash
sudo supervisorctl reread && sudo supervisorctl update && sudo supervisorctl start yourproject
sudo systemctl start nginx && sudo systemctl enable nginx
```

### 14.9 Docker Alternative

```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "yourproject.wsgi:application"]
```

```yaml
# docker-compose.yml
version: '3.8'
services:
  web:
    build: .
    ports: ["8000:8000"]
    depends_on: [db]
  db:
    image: postgres:13
    environment:
      POSTGRES_DB: yourdb
      POSTGRES_USER: youruser
      POSTGRES_PASSWORD: yourpassword
    volumes: [postgres_data:/var/lib/postgresql/data]
volumes:
  postgres_data:
```

### 14.10 Heroku Alternative

```
# Procfile
web: gunicorn yourproject.wsgi:application
```

```bash
heroku create yourapp
heroku addons:create heroku-postgresql:hobby-dev
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### 14.11 CI/CD (GitHub Actions example)

```yaml
name: Deploy to Production
on:
  push:
    branches: [ main ]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with: { python-version: 3.9 }
      - run: pip install -r requirements.txt
      - run: python manage.py test
      - run: echo "deploy step here"
```

### 14.12 Common Deployment Issues

| Issue | Fix |
|---|---|
| Static files not loading | Run `collectstatic`; check `STATIC_ROOT`/`STATIC_URL`; verify Nginx static `location` block |
| Database connection errors | Check env var credentials; confirm DB server running; check firewall/security group |
| Permission errors | Correct file ownership (`www-data`), correct directory permissions |
| Memory issues | Tune Gunicorn worker count; monitor memory; consider upgrading instance size |