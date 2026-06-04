# Django & DRF Interview Preparation
> **Target:** 4 Years Experience | Python Backend Developer

---

## Table of Contents

1. [Django Core](#1-django-core)
2. [Django ORM](#2-django-orm)
3. [Django Middleware](#3-django-middleware)
4. [Django Signals](#4-django-signals)
5. [Django Caching](#5-django-caching)
6. [Django Security](#6-django-security)
7. [Django REST Framework (DRF)](#7-django-rest-framework-drf)
8. [DRF Authentication & Permissions](#8-drf-authentication--permissions)
9. [DRF Serializers](#9-drf-serializers)
10. [DRF ViewSets & Routers](#10-drf-viewsets--routers)
11. [Performance & Optimization](#11-performance--optimization)
12. [Testing](#12-testing)
13. [Deployment & Production](#13-deployment--production)
14. [Advanced Topics](#14-advanced-topics)

---

## 1. Django Core

### Q1. What is Django's request-response lifecycle?

```
Browser → WSGI/ASGI Server → Django → URL Dispatcher
→ Middleware (process_request) → View → Middleware (process_response) → Response
```

**Detailed flow:**
1. WSGI/ASGI server receives HTTP request
2. `process_request()` of each middleware runs (top-down)
3. URL resolver matches pattern → calls view
4. View interacts with models/DB if needed, renders template
5. View returns `HttpResponse`
6. `process_response()` runs (bottom-up through middleware)
7. Response sent to client

---

### Q2. Django's MVT Architecture

| Component | Role |
|-----------|------|
| **Model** | Data layer — defines DB schema, ORM queries |
| **View** | Business logic — processes request, returns response |
| **Template** | Presentation layer — renders HTML |

Unlike MVC, Django's "Controller" is the URL dispatcher + framework itself.

**Request flow:**
```
URL Dispatcher → View → Model ↔ DB → Template → HttpResponse
```

---

### Q3. Django Project vs App

- A **Django project** = entire web application (settings, root URLs, config)
- A **Django app** = modular, reusable component (e.g., `users`, `products`, `orders`)
- Apps promote separation of concerns and reusability across projects

```bash
django-admin startproject myproject
python manage.py startapp users
```

**Project structure:**
```
myproject/
├── manage.py
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/          # App
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
│   ├── admin.py
│   └── migrations/
└── products/       # App
```

---

### Q4. Django's `settings.py` — Multi-environment Setup

```
settings/
  __init__.py
  base.py       # Common settings
  local.py      # Dev overrides
  production.py # Prod overrides
```

```python
# base.py
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRET_KEY = os.environ['SECRET_KEY']

# local.py
from .base import *
DEBUG = True
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'db.sqlite3'}}

# production.py
from .base import *
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
DATABASES = {'default': dj_database_url.config(conn_max_age=600)}
```

Run with: `python manage.py runserver --settings=settings.local`

---

### Q5. Common `manage.py` Commands

```bash
python manage.py runserver           # Start dev server
python manage.py makemigrations      # Generate migration files
python manage.py migrate             # Apply migrations
python manage.py showmigrations      # List migration status
python manage.py sqlmigrate app 0001 # Show raw SQL for migration
python manage.py migrate app 0002    # Rollback to specific migration
python manage.py migrate app zero    # Unapply all migrations for app
python manage.py createsuperuser     # Create admin user
python manage.py shell               # Django interactive shell
python manage.py collectstatic       # Gather static files
python manage.py dbshell             # DB CLI
python manage.py test                # Run tests
python manage.py check --deploy      # Production readiness check
```

---

### Q6. URL Dispatcher — `path()` vs `re_path()`

```python
from django.urls import path, re_path, include

urlpatterns = [
    path('users/<int:pk>/', views.user_detail),           # Type-safe converter
    path('users/<str:username>/', views.user_by_name),
    path('articles/<slug:slug>/', views.article_detail),
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.archive),  # Full regex
    path('api/', include('api.urls')),                    # Nested URLs
]
```

`path()` — simpler, built-in converters: `int`, `str`, `slug`, `uuid`, `path`
`re_path()` — full regex control, more verbose

---

### Q7. Django Sessions

Sessions store server-side data per visitor; only a session ID is sent to the client via cookie.

```python
# settings.py
SESSION_ENGINE = 'django.contrib.sessions.backends.db'   # Default
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # Redis-backed
SESSION_COOKIE_AGE = 1209600      # 2 weeks
SESSION_COOKIE_SECURE = True      # HTTPS only
SESSION_COOKIE_HTTPONLY = True    # No JS access

# views.py
def login_view(request):
    request.session['user_id'] = user.id
    request.session.set_expiry(300)   # 5 minutes

def logout_view(request):
    request.session.flush()   # Clear all session data
```

---

### Q8. Django Admin

```python
# models.py
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

# admin.py
from django.contrib import admin

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published', 'created_at']
    list_filter = ['is_published', 'created_at']
    search_fields = ['title', 'content']
    list_editable = ['is_published']
    ordering = ['-created_at']
```

```bash
python manage.py createsuperuser
```

---

### Q9. Django Signals — Built-in List

| Signal | When fired |
|--------|-----------|
| `pre_save` | Before model `save()` |
| `post_save` | After model `save()` |
| `pre_delete` | Before model `delete()` |
| `post_delete` | After model `delete()` |
| `m2m_changed` | ManyToMany relationship changes |
| `request_started` | HTTP request begins |
| `request_finished` | HTTP request ends |
| `user_logged_in` | User login |
| `user_logged_out` | User logout |

---

### Q10. Model Inheritance Styles

| Type | DB Tables | Use Case |
|------|-----------|---------|
| **Abstract** | Child tables only (no parent table) | Share common fields across models |
| **Multi-table** | Parent + Child tables | Each model needs its own table |
| **Proxy** | Original table only | Different Python behavior, same DB schema |

```python
# Abstract base class
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Article(BaseModel):
    title = models.CharField(max_length=200)

# Proxy model
class PublishedArticle(Article):
    class Meta:
        proxy = True
        ordering = ['-created_at']

    def publish(self):
        self.is_published = True
        self.save()
```

---

### Q11. How to Override `save()` — and Caveats

```python
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        # Custom logic before save
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.title)

        # Always call super — skipping prevents DB write
        super().save(*args, **kwargs)

        # Custom logic after save
```

**Key caveats:**
- Always call `super().save()` — skipping prevents actual DB save
- `bulk_create()` and `update()` bypass `save()` entirely
- Overriding `save()` also bypasses it for admin actions
- Wrap risky logic in try/except to avoid silent failures
- Use `self._state.adding` to detect new vs existing instance

---

### Q12. Database Transactions

```python
from django.db import transaction

# Decorator
@transaction.atomic
def transfer_funds(from_account, to_account, amount):
    from_account.balance -= amount
    from_account.save()
    to_account.balance += amount
    to_account.save()   # If this fails, both saves rollback

# Context manager
def place_order(user, cart):
    with transaction.atomic():
        order = Order.objects.create(user=user)
        for item in cart.items.all():
            OrderItem.objects.create(order=order, product=item.product)
            item.product.stock = F('stock') - item.quantity
            item.product.save()
        cart.delete()

# Nested transactions (savepoints)
def complex_operation():
    with transaction.atomic():           # Outer transaction
        obj = MainModel.objects.create(name='Main')
        try:
            with transaction.atomic():   # Inner savepoint
                risky_operation()
        except SomeException:
            pass   # Savepoint rolled back, outer continues

# on_commit — run after successful transaction
@receiver(post_save, sender=Order)
def notify_payment(sender, instance, **kwargs):
    transaction.on_commit(
        lambda: payment_gateway.charge(instance.amount)
    )
```

---

### Q13. Database Routers (Multiple DBs)

```python
# db_router.py
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
        return db == 'default'

# settings.py
DATABASE_ROUTERS = ['myproject.db_router.DatabaseRouter']

# Manual override in queries
users = User.objects.using('users_db').all()
user.save(using='users_db')
```

---

### Q14. Soft Deletes

```python
from django.utils import timezone

class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

class SoftDeleteMixin(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True, db_index=True)

    objects = SoftDeleteManager()       # Default — excludes deleted
    all_objects = models.Manager()      # Includes deleted

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save(update_fields=['deleted_at'])

    def restore(self):
        self.deleted_at = None
        self.save(update_fields=['deleted_at'])

    def hard_delete(self):
        super().delete()

    class Meta:
        abstract = True

class Product(SoftDeleteMixin):
    name = models.CharField(max_length=200)

# Product.objects.all()          — excludes deleted
# Product.all_objects.all()      — includes deleted
```

---

### Q15. Custom Model Managers

```python
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

    def by_author(self, author):
        return self.get_queryset().filter(author=author)

    def recent(self, days=7):
        cutoff = timezone.now() - timedelta(days=days)
        return self.get_queryset().filter(created_at__gte=cutoff)

class Article(models.Model):
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = models.Manager()           # Default
    published = PublishedManager()       # Custom

# Usage
Article.published.by_author(user).recent(days=30)
```

**When to use:** soft deletes, multi-tenancy filtering, status-based filtering, encapsulating complex queries.

---

### Q16. ContentTypes Framework

Enables generic relationships — a "Comment" that can attach to any model.

```python
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    text = models.TextField()

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    comments = GenericRelation(Comment)

# Usage
post = BlogPost.objects.get(pk=1)
Comment.objects.create(content_object=post, text="Great post!")
post.comments.all()
```

**Limitations:** No DB-level FK constraints, less efficient queries, no referential integrity.

---

## 2. Django ORM

### Q17. `select_related` vs `prefetch_related`

| | `select_related` | `prefetch_related` |
|--|------------------|--------------------|
| **Relationship** | ForeignKey, OneToOne | ManyToMany, reverse FK |
| **SQL** | Single query with JOIN | 2 separate queries |
| **Use when** | Following a single FK | Fetching many related objects |

```python
# select_related — SQL JOIN
orders = Order.objects.select_related('customer', 'customer__address').all()

# prefetch_related — 2 queries total
products = Product.objects.prefetch_related('categories', 'tags').all()

# Combine both
orders = Order.objects.select_related('customer').prefetch_related('items__product')

# Prefetch with custom queryset
from django.db.models import Prefetch
articles = Article.objects.prefetch_related(
    Prefetch('comments', queryset=Comment.objects.select_related('author'))
)
```

---

### Q18. `only()` vs `defer()`

```python
# only() — fetch ONLY specified fields (defers the rest)
users = User.objects.only('id', 'email', 'name')

# defer() — fetch everything EXCEPT specified fields
users = User.objects.defer('bio', 'avatar', 'last_login')
```

Accessing a deferred field triggers an additional DB query. Use for wide tables where you don't need all columns.

---

### Q19. Lazy vs Eager QuerySet Evaluation

**Lazy** (no DB hit): `filter()`, `exclude()`, `order_by()`, `annotate()`, `values()`

**Eager** (hits DB): iteration (`for`), `list()`, `len()`, slicing, `bool()`, `repr()`

```python
qs = Product.objects.filter(active=True).order_by('-created_at')  # No DB yet

products = list(qs)       # DB query executes HERE

qs.count()    # SELECT COUNT(*) — use over len()
qs.exists()   # SELECT 1 LIMIT 1 — faster than count() > 0
qs.first()    # LIMIT 1
```

---

### Q20. `annotate()` vs `aggregate()`

```python
from django.db.models import Count, Sum, Avg, Max

# annotate() — adds computed field per row
categories = Category.objects.annotate(product_count=Count('products'))
# Each object gets .product_count

# aggregate() — single summary value for entire queryset
result = Product.objects.aggregate(
    total=Sum('price'),
    avg_price=Avg('price'),
    max_price=Max('price')
)
# Returns: {'total': 9999.99, 'avg_price': 49.99, 'max_price': 199.99}
```

---

### Q21. `F()` and `Q()` Expressions

```python
from django.db.models import F, Q

# F() — reference a field value atomically (avoids race conditions)
Product.objects.update(stock=F('stock') - 1)         # Atomic decrement
Product.objects.filter(sale_price__lt=F('price'))    # Compare two fields

# Q() — complex lookups with AND / OR / NOT
Product.objects.filter(
    Q(category='electronics') | Q(price__lt=100),
    ~Q(stock=0)   # NOT out of stock
)
```

**Why `F()` over Python math?** `F()` executes in the DB atomically — no race condition if two threads read the same value simultaneously.

---

### Q22. Field Lookups

```python
Article.objects.filter(title__exact='Django Tutorial')
Article.objects.filter(title__icontains='django')     # Case-insensitive
Article.objects.filter(title__startswith='How')
Article.objects.filter(views__gt=100)                 # Greater than
Article.objects.filter(views__range=(100, 1000))
Article.objects.filter(created_at__year=2024)
Article.objects.filter(category__in=['tech', 'science'])
Article.objects.filter(description__isnull=True)
```

---

### Q23. `values()` vs `values_list()`

```python
# values() — returns list of dicts
User.objects.values('id', 'email')
# [{'id': 1, 'email': 'a@b.com'}, ...]

# values_list() — returns list of tuples
User.objects.values_list('id', 'email')
# [(1, 'a@b.com'), ...]

# flat=True — single field, flat list
User.objects.values_list('email', flat=True)
# ['a@b.com', 'b@c.com', ...]
```

Much faster than fetching full model instances when you only need specific fields.

---

### Q24. Bulk Operations

```python
# bulk_create — single INSERT for many rows
products = [Product(name=f'Product {i}', price=10*i) for i in range(1000)]
Product.objects.bulk_create(products, batch_size=500)
# Note: skips signals, custom save(), and model validation

# bulk_update — single UPDATE for many rows
for p in products:
    p.price = p.price * 1.1
Product.objects.bulk_update(products, ['price'], batch_size=500)

# update() — most efficient for uniform updates (no objects loaded)
Product.objects.filter(category='books').update(discount=10)
```

---

### Q25. `get_or_create()` and `update_or_create()`

```python
# get_or_create — returns (instance, created_bool)
user, created = User.objects.get_or_create(
    email='john@example.com',
    defaults={'name': 'John', 'role': 'user'}
)

# update_or_create — updates if exists, creates if not
profile, created = UserProfile.objects.update_or_create(
    user=user,
    defaults={'bio': 'Updated bio', 'avatar': 'new.jpg'}
)
```

Both are thread-safe — handle `IntegrityError` internally.

---

### Q26. Django Migrations — How They Work

- **`makemigrations`** — detects model changes, generates migration files
- **`migrate`** — applies pending migrations; tracks state in `django_migrations` table

```bash
python manage.py makemigrations users
python manage.py sqlmigrate users 0001    # Preview SQL without applying
python manage.py migrate
python manage.py migrate users 0002       # Rollback to specific migration
python manage.py migrate users zero       # Unapply all
python manage.py squashmigrations myapp 0002 0005  # Squash range
```

**Data migration example:**
```python
from django.db import migrations

def populate_slug(apps, schema_editor):
    Article = apps.get_model('blog', 'Article')
    for article in Article.objects.all():
        article.slug = article.title.lower().replace(' ', '-')
        article.save()

class Migration(migrations.Migration):
    dependencies = [('blog', '0003_article_slug')]
    operations = [
        migrations.RunPython(populate_slug, migrations.RunPython.noop)
    ]
```

**How Django knows what to apply:** Django builds a dependency graph from `dependencies` in each migration file, then checks which are recorded in `django_migrations` table to find unapplied ones.

---

### Q27. `CharField` vs `TextField`

| Aspect | CharField | TextField |
|--------|-----------|-----------|
| **Max Length** | Required (`max_length=`) | No hard limit |
| **DB Type** | VARCHAR | TEXT |
| **Use Case** | Short strings (name, title) | Long content |
| **Form Widget** | TextInput (single line) | Textarea (multi-line) |
| **Indexing** | Better for indexing | Less efficient |

---

### Q28. Database Concurrency — `select_for_update()`

```python
from django.db import transaction

def transfer_money(from_id, to_id, amount):
    with transaction.atomic():
        # Lock rows for update (released when transaction ends)
        from_acc = Account.objects.select_for_update().get(id=from_id)
        to_acc = Account.objects.select_for_update().get(id=to_id)

        if from_acc.balance < amount:
            raise ValueError("Insufficient funds")

        from_acc.balance -= amount
        to_acc.balance += amount
        from_acc.save()
        to_acc.save()

# skip_locked — skip rows locked by other processes (job queue pattern)
def process_pending_jobs():
    with transaction.atomic():
        jobs = Job.objects.select_for_update(skip_locked=True).filter(
            status='pending'
        )[:10]
        for job in jobs:
            job.status = 'processing'
            job.save()
```

---

## 3. Django Middleware

### Q29. What is Middleware?

Middleware is a framework of hooks into Django's request/response processing. Order matters — runs top-down on request, bottom-up on response.

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',    # First — HTTPS redirect
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

---

### Q30. Writing Custom Middleware

```python
# myapp/middleware.py
import time
import logging

logger = logging.getLogger(__name__)

class RequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response   # Called once on startup

    def __call__(self, request):
        # Code before view
        start = time.time()

        response = self.get_response(request)  # Call view + downstream middleware

        # Code after view
        duration = time.time() - start
        logger.info(f"{request.method} {request.path} — {duration:.3f}s")
        response['X-Response-Time'] = f"{duration:.3f}s"
        return response

    def process_exception(self, request, exception):
        # Only runs if view raises an exception
        logger.error(f"Exception on {request.path}: {exception}")
        return None   # re-raises; return HttpResponse to suppress
```

```python
# settings.py — add to MIDDLEWARE list
MIDDLEWARE = [
    'myapp.middleware.RequestTimingMiddleware',
    ...
]
```

**Old-style hooks** (still valid):
- `process_request(request)` — before URL resolution
- `process_view(request, view_func, args, kwargs)` — before view execution
- `process_response(request, response)` — always runs
- `process_exception(request, exception)` — only on view exception

---

## 4. Django Signals

### Q31. Signals — What, When, and How

```python
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()

@receiver(pre_delete, sender=Article)
def backup_before_delete(sender, instance, **kwargs):
    ArticleBackup.objects.create(
        title=instance.title,
        content=instance.content
    )
```

**Register in `AppConfig.ready()`:**
```python
# apps.py
class UsersConfig(AppConfig):
    name = 'users'
    def ready(self):
        import users.signals   # noqa
```

---

### Q32. Custom Signals

```python
# signals.py
import django.dispatch

article_published = django.dispatch.Signal()

# models.py
class Article(models.Model):
    def publish(self):
        self.is_published = True
        self.save()
        article_published.send(sender=self.__class__, article=self)

# handlers.py
@receiver(article_published)
def notify_subscribers(sender, article, **kwargs):
    subscribers = Subscription.objects.filter(category=article.category)
    for sub in subscribers:
        send_notification_email(sub.user, article)
```

---

### Q33. Signal Pitfalls

1. **Infinite loops** — signal handler calls `save()`, which triggers the signal again
   ```python
   # BAD
   @receiver(post_save, sender=MyModel)
   def handler(sender, instance, **kwargs):
       instance.save()   # Infinite recursion!

   # GOOD — use update() to bypass save() signals
   @receiver(post_save, sender=MyModel)
   def handler(sender, instance, **kwargs):
       MyModel.objects.filter(pk=instance.pk).update(field='value')
   ```

2. **Transaction issues** — signal fires before transaction commits; external service call may fail if transaction rolls back → use `transaction.on_commit()`

3. **Performance** — heavy work in signals blocks the request → use background tasks (Celery)

4. **Hard to trace/debug** — prefer direct function calls when the relationship is tight

---

## 5. Django Caching

### Q34. Caching Backends

| Backend | Use case |
|---------|---------|
| `LocMemCache` | Per-process, dev only |
| `FileBasedCache` | Simple, no extra services |
| `MemcachedCache` | High-performance, distributed |
| `RedisCache` | Most popular in production |
| `DatabaseCache` | Rare — cache in DB |

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'TIMEOUT': 300,
    }
}
```

---

### Q35. Cache API Levels

```python
# 1. Per-view caching
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)   # 15 minutes
def product_list(request): ...

# 2. Template fragment caching
{% load cache %}
{% cache 600 product_detail product.id %}
    <div>{{ product.description }}</div>
{% endcache %}

# 3. Low-level cache API
from django.core.cache import cache

cache.set('user_123', user_data, timeout=3600)
data = cache.get('user_123')           # None if not found
cache.delete('user_123')

# Get-or-set pattern
def get_user_profile(user_id):
    key = f'user_{user_id}_profile'
    data = cache.get(key)
    if data is None:
        data = UserProfile.objects.get(user_id=user_id)
        cache.set(key, data, 3600)
    return data

cache.set_many({'a': 1, 'b': 2})
cache.get_many(['a', 'b'])
cache.delete_many(['a', 'b'])
```

---

## 6. Django Security

### Q36. Built-in Security Protections

| Threat | Django Protection |
|--------|------------------|
| **CSRF** | `CsrfViewMiddleware`, `{% csrf_token %}` |
| **XSS** | Auto-escaping in templates |
| **SQL Injection** | ORM parameterized queries |
| **Clickjacking** | `X-Frame-Options` header |
| **Host header attacks** | `ALLOWED_HOSTS` |
| **Session hijacking** | `SESSION_COOKIE_SECURE`, `SESSION_COOKIE_HTTPONLY` |

```python
# Production security settings
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
```

---

### Q37. CSRF — How It Works

CSRF (Cross-Site Request Forgery) tricks a user's browser into making unintended requests.

Django uses a **double-submit cookie pattern**:
1. Sets `csrftoken` cookie on first visit
2. Requires matching `csrfmiddlewaretoken` in POST form body
3. For AJAX: send `X-CSRFToken` header

```python
# Exempt a view (e.g., webhook with own auth)
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def webhook(request): ...
```

DRF: session auth requires CSRF; token/JWT auth does not.

---

## 7. Django REST Framework (DRF)

### Q38. Core DRF Components

| Component | Purpose |
|-----------|---------|
| `Serializer` | Data validation + serialization/deserialization |
| `APIView` / `ViewSet` | HTTP method handling |
| `Router` | Auto URL generation for ViewSets |
| `Permission` | Access control |
| `Authentication` | Identity verification |
| `Throttle` | Rate limiting |
| `Pagination` | Large result sets |
| `Filter` | QuerySet filtering |
| `Renderer` | Output format (JSON, Browsable API) |
| `Parser` | Input parsing (JSON, form, multipart) |

---

### Q39. `APIView` vs `GenericAPIView` vs `ViewSet`

```python
# APIView — most control, most manual code
class ProductAPIView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return Response(ProductSerializer(product).data)

    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

# GenericAPIView + Mixins — less boilerplate
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# ViewSet — most DRY, auto-routed
from rest_framework.viewsets import ModelViewSet

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

**Key difference:** `GenericAPIView` adds `get_queryset()`, `get_serializer()`, `get_object()`, pagination, filtering. `ViewSet` adds action-based dispatch and router integration.

---

### Q40. All DRF Generic Views

| Class | HTTP Methods |
|-------|-------------|
| `ListAPIView` | GET (collection) |
| `CreateAPIView` | POST |
| `RetrieveAPIView` | GET (single) |
| `UpdateAPIView` | PUT, PATCH |
| `DestroyAPIView` | DELETE |
| `ListCreateAPIView` | GET, POST |
| `RetrieveUpdateAPIView` | GET, PUT, PATCH |
| `RetrieveDestroyAPIView` | GET, DELETE |
| `RetrieveUpdateDestroyAPIView` | GET, PUT, PATCH, DELETE |

---

### Q41. DRF Global Configuration

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day',
    },
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}
```

---

## 8. DRF Authentication & Permissions

### Q42. Authentication Classes

| Class | How it works |
|-------|-------------|
| `SessionAuthentication` | Django session cookie (browser clients) |
| `BasicAuthentication` | Base64 `username:password` in header (dev only) |
| `TokenAuthentication` | `Token <token>` in `Authorization` header |
| `JWTAuthentication` | JWT via `djangorestframework-simplejwt` |
| `RemoteUserAuthentication` | Proxy-auth via `REMOTE_USER` |

```python
# Per-view override
class PublicProductList(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
```

---

### Q43. JWT Auth with SimpleJWT

```python
# settings.py
from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}

# urls.py
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
```

```bash
# Get token
POST /api/token/      {"username": "admin", "password": "pass"}
# Returns: {"access": "eyJ...", "refresh": "eyJ..."}

# Use token
GET /api/products/    Authorization: Bearer eyJ...

# Refresh
POST /api/token/refresh/    {"refresh": "eyJ..."}
```

---

### Q44. Permission Classes

| Class | Who can access |
|-------|---------------|
| `AllowAny` | Everyone |
| `IsAuthenticated` | Logged-in users |
| `IsAdminUser` | Staff users (`is_staff=True`) |
| `IsAuthenticatedOrReadOnly` | Auth for write, anyone for read |
| `DjangoModelPermissions` | Django model-level permissions |
| `DjangoObjectPermissions` | Object-level permissions |

```python
# Custom permission
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    message = 'You must be the owner to edit this.'

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user

# Apply per-view
class ProductView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
```

**`has_permission`** — view-level check (runs first)
**`has_object_permission`** — object-level check (runs after `get_object()`)

---

### Q45. Throttling

```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day',
        'login': '5/hour',
    }
}

# Custom Redis sliding window throttle
import redis, time
from rest_framework.throttling import BaseThrottle

class RedisSlidingWindowThrottle(BaseThrottle):
    r = redis.Redis()

    def allow_request(self, request, view):
        key = f"throttle:{request.user.id}"
        limit, window = 100, 60

        pipe = self.r.pipeline()
        now = time.time()
        pipe.zremrangebyscore(key, 0, now - window)
        pipe.zadd(key, {str(now): now})
        pipe.zcard(key)
        pipe.expire(key, window)
        _, _, count, _ = pipe.execute()
        return count <= limit

    def wait(self):
        return 60
```

---

### Q46. Authentication vs Authorization

| Aspect | Authentication | Authorization |
|--------|----------------|---------------|
| **Question** | "Who are you?" | "What can you do?" |
| **Process** | Login / token validation | Permission checking |
| **Timing** | First | After auth |
| **Failure** | 401 Unauthorized | 403 Forbidden |
| **Django** | Auth backends | Permission classes |
| **DRF** | Authentication classes | Permission classes |

---

## 9. DRF Serializers

### Q47. `Serializer` vs `ModelSerializer`

```python
# Serializer — manual field definition
class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

# ModelSerializer — auto-generates fields from model
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['id', 'name', 'price']
        # exclude = ['created_at']
        read_only_fields = ['id', 'created_at']
        extra_kwargs = {'password': {'write_only': True}}
```

---

### Q48. Nested Serializers

```python
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)             # Nested read
    category_id = serializers.PrimaryKeyRelatedField(         # Write via FK
        queryset=Category.objects.all(), source='category', write_only=True
    )
    discount_price = serializers.SerializerMethodField()      # Computed field
    tags = serializers.StringRelatedField(many=True)          # String repr

    def get_discount_price(self, obj):
        return obj.price * 0.9 if obj.on_sale else obj.price

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'discount_price', 'category', 'category_id', 'tags']
```

**Writable nested serializers** — must override `create()` and `update()`:
```python
def create(self, validated_data):
    tags_data = validated_data.pop('tags', [])
    category_data = validated_data.pop('category')
    category, _ = Category.objects.get_or_create(**category_data)
    product = Product.objects.create(category=category, **validated_data)
    for tag_data in tags_data:
        tag, _ = Tag.objects.get_or_create(**tag_data)
        product.tags.add(tag)
    return product
```

**Optimization:** Always use `select_related` / `prefetch_related` in the view's `get_queryset()` when using nested serializers.

---

### Q49. Serializer Validation

```python
class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}

    # Field-level validation
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already in use.")
        return value.lower()

    # Object-level validation (cross-field)
    def validate(self, data):
        if data['password'] != data.pop('confirm_password'):
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
```

**Validation order:** `to_internal_value()` → `validate_<field>()` → `validate()` → `save()`

---

### Q50. `to_representation()` and `to_internal_value()`

```python
class ProductSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        # Customize output (serialization → outgoing data)
        data = super().to_representation(instance)
        data['price'] = f"₹{data['price']}"
        if not self.context['request'].user.is_staff:
            data.pop('cost_price', None)    # Hide sensitive field
        return data

    def to_internal_value(self, data):
        # Customize input (deserialization → incoming data)
        if 'price' in data and isinstance(data['price'], str):
            data['price'] = data['price'].replace('₹', '').strip()
        return super().to_internal_value(data)
```

---

### Q51. Serializer Context

```python
# Pass context from view
serializer = ProductSerializer(
    product,
    context={'request': request, 'user': request.user}
)

# Access in serializer
class ProductSerializer(serializers.ModelSerializer):
    is_liked = serializers.SerializerMethodField()

    def get_is_liked(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            return obj.likes.filter(user=user).exists()
        return False
```

---

### Q52. ModelForm Validation (Internal Flow)

**Steps:** `full_clean()` → `_clean_fields()` → `_clean_form()` → `_post_clean()` (model validation)

```python
class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['field1', 'field2']

    def clean_field1(self):
        data = self.cleaned_data['field1']
        if len(data) < 3:
            raise forms.ValidationError("Too short")
        return data

    def clean(self):
        cleaned_data = super().clean()
        f1 = cleaned_data.get('field1')
        f2 = cleaned_data.get('field2')
        if f1 and f2 and some_conflict(f1, f2):
            raise forms.ValidationError("Fields conflict")
        return cleaned_data
```

---

## 10. DRF ViewSets & Routers

### Q53. ViewSets and Routers

```python
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.routers import DefaultRouter

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Custom detail action
    @action(detail=True, methods=['post'], url_path='toggle-featured')
    def toggle_featured(self, request, pk=None):
        product = self.get_object()
        product.featured = not product.featured
        product.save()
        return Response({'featured': product.featured})

    # Custom list action
    @action(detail=False, methods=['get'])
    def featured(self, request):
        featured = Product.objects.filter(featured=True)
        return Response(self.get_serializer(featured, many=True).data)

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [path('api/', include(router.urls))]
```

**Generated URLs:**
```
GET    /api/products/                   → list
POST   /api/products/                   → create
GET    /api/products/{pk}/              → retrieve
PUT    /api/products/{pk}/              → update
PATCH  /api/products/{pk}/              → partial_update
DELETE /api/products/{pk}/              → destroy
POST   /api/products/{pk}/toggle-featured/  → custom action
GET    /api/products/featured/          → custom list action
```

---

### Q54. Different Serializers Per Action

```python
class ProductViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer       # Minimal fields
        elif self.action == 'create':
            return ProductCreateSerializer     # Writable fields
        return ProductDetailSerializer         # Full detail

    def get_queryset(self):
        qs = Product.objects.all()
        if self.action == 'list':
            return qs.only('id', 'name', 'price')
        return qs.select_related('category').prefetch_related('tags')

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return [AllowAny()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
```

---

### Q55. Pagination

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}

# Custom paginator
from rest_framework.pagination import PageNumberPagination, CursorPagination

class StandardPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })

# Cursor pagination — for large datasets, no offset performance issues
class TimestampCursorPagination(CursorPagination):
    page_size = 20
    ordering = '-created_at'   # Must be unique + indexed
```

---

### Q56. Filtering

```python
# pip install django-filter

class ProductViewSet(ModelViewSet):
    filterset_fields = ['category', 'active']           # Exact match
    search_fields = ['name', 'description', 'sku']      # ?search=
    ordering_fields = ['price', 'created_at', 'name']   # ?ordering=-price

# Custom FilterSet
import django_filters

class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    category_name = django_filters.CharFilter(
        field_name='category__name', lookup_expr='icontains'
    )

    class Meta:
        model = Product
        fields = ['category', 'min_price', 'max_price', 'category_name']

class ProductViewSet(ModelViewSet):
    filterset_class = ProductFilter
```

---

### Q57. API Versioning

```python
# URL versioning
REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_VERSION': 'v1',
    'ALLOWED_VERSIONS': ['v1', 'v2'],
}

# urls.py
urlpatterns = [
    path('api/v1/', include('api.v1.urls')),
    path('api/v2/', include('api.v2.urls')),
]

# Conditional logic in view
class ProductViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return ProductV2Serializer
        return ProductV1Serializer
```

---

### Q58. Custom Pagination Class

```python
from rest_framework.pagination import LimitOffsetPagination

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 100

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.count,
            'limit': self.limit,
            'offset': self.offset,
            'results': data
        })
```

---

## 11. Performance & Optimization

### Q59. N+1 Query Problem

```python
# BAD — N+1 queries
orders = Order.objects.all()
for order in orders:
    print(order.customer.name)   # Extra query each iteration!

# GOOD — 1 query with JOIN
orders = Order.objects.select_related('customer').all()

# BAD for M2M
products = Product.objects.all()
for p in products:
    print(p.tags.all())   # Extra query per product

# GOOD
products = Product.objects.prefetch_related('tags').all()
```

---

### Q60. QuerySet Performance Tips

```python
# Use iterator() for large QuerySets (avoids loading everything into memory)
for product in Product.objects.filter(active=True).iterator(chunk_size=2000):
    process(product)

# exists() vs count()
if Product.objects.filter(active=True).exists():   # SELECT 1 LIMIT 1
    pass

# exists() is faster than count() > 0 or len() > 0

# values() / values_list() instead of full model instances
emails = User.objects.values_list('email', flat=True)

# Defer heavy fields
articles = Article.objects.defer('content', 'full_text')

# Bulk operations
Product.objects.filter(category='books').update(discount=10)  # No objects loaded
```

---

### Q61. Database Indexing

```python
class Product(models.Model):
    sku = models.CharField(max_length=50, db_index=True)      # Single index
    slug = models.SlugField(unique=True)                       # Auto-indexed
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['category', 'active']),           # Composite
            models.Index(fields=['-created_at']),                   # Descending
            models.Index(fields=['name'], name='product_name_idx'),
        ]
```

---

### Q62. Debugging Slow Queries

```python
# Django Debug Toolbar — install and enable in dev
# pip install django-debug-toolbar

# Manual query inspection
from django.db import connection, reset_queries

reset_queries()
# ... your code ...
print(len(connection.queries))
for q in connection.queries:
    print(q['time'], q['sql'])

# In Django shell
qs = Product.objects.filter(active=True).select_related('category')
print(qs.query)     # View raw SQL
qs.explain()        # EXPLAIN output (PostgreSQL)

# Logging
LOGGING = {
    'loggers': {
        'django.db.backends': {'level': 'DEBUG', 'handlers': ['console']}
    }
}
```

**Tools:** Django Debug Toolbar, `EXPLAIN ANALYZE` in PostgreSQL, Silk profiling middleware.

---

### Q63. Celery — Async Background Tasks

```python
# celery.py
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
app = Celery('myproject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# settings.py
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_TASK_SERIALIZER = 'json'

# tasks.py
from celery import shared_task

@shared_task(bind=True, max_retries=3)
def send_welcome_email(self, user_id):
    try:
        user = User.objects.get(id=user_id)
        send_mail('Welcome!', f'Hi {user.username}!', 'from@example.com', [user.email])
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)

# Call from view
send_welcome_email.delay(user.id)
send_welcome_email.apply_async(args=[user.id], countdown=300)
```

**Periodic tasks with Celery Beat:**
```python
from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'cleanup-expired-sessions': {
        'task': 'myapp.tasks.cleanup_expired_sessions',
        'schedule': crontab(hour=2, minute=30),   # Every day at 2:30 AM
    },
    'weekly-report': {
        'task': 'myapp.tasks.generate_weekly_report',
        'schedule': crontab(hour=9, minute=0, day_of_week=1),  # Monday 9 AM
    },
    'health-check': {
        'task': 'myapp.tasks.system_health_check',
        'schedule': 300.0,  # Every 5 minutes
    },
}
```

---

## 12. Testing

### Q64. Unit Tests in Django

```python
from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics')
        self.product = Product.objects.create(
            name='Laptop', price=999.99, category=self.category
        )

    def test_product_str(self):
        self.assertEqual(str(self.product), 'Laptop')

    def test_discount_price(self):
        self.product.on_sale = True
        self.assertAlmostEqual(self.product.discount_price, 899.99, places=2)


class ProductAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test', password='pass')
        self.client.force_authenticate(user=self.user)
        self.url = reverse('product-list')

    def test_list_products(self):
        Product.objects.create(name='Laptop', price=999)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_create_product_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.post(self.url, {'name': 'Phone', 'price': 499})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
```

---

### Q65. `factory_boy` and `pytest-django`

```python
# factories.py
import factory

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user_{n}')
    email = factory.LazyAttribute(lambda o: f'{o.username}@example.com')
    password = factory.PostGenerationMethodCall('set_password', 'testpass123')

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('word')
    price = factory.Faker('pydecimal', left_digits=3, right_digits=2, positive=True)
    category = factory.SubFactory(CategoryFactory)

# pytest test
import pytest

@pytest.mark.django_db
def test_product_api(api_client):
    user = UserFactory()
    api_client.force_authenticate(user=user)
    product = ProductFactory(name='Test Product')
    response = api_client.get(f'/api/products/{product.id}/')
    assert response.status_code == 200
    assert response.data['name'] == 'Test Product'
```

---

## 13. Deployment & Production

### Q66. Production Stack

```
Nginx (reverse proxy + static files)
  └── Gunicorn (WSGI server, multiple workers)
        └── Django application
              └── PostgreSQL + Redis + Celery
```

```bash
# Gunicorn
gunicorn myproject.wsgi:application \
    --workers 4 \
    --worker-class gthread \
    --threads 2 \
    --bind 0.0.0.0:8000 \
    --timeout 120 \
    --access-logfile /var/log/gunicorn/access.log
```

```nginx
# nginx.conf snippet
location / {
    proxy_pass http://127.0.0.1:8000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}

location /static/ {
    alias /var/www/myapp/staticfiles/;
    expires 1y;
    add_header Cache-Control "public, immutable";
}

location /media/ {
    alias /var/www/myapp/media/;
}
```

---

### Q67. Production Checklist

```python
# settings/production.py
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
SECRET_KEY = os.environ['SECRET_KEY']   # Never hardcode

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

LOGGING = {
    'version': 1,
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/app.log',
        }
    },
    'root': {'handlers': ['file'], 'level': 'WARNING'},
}
```

```bash
# Before each deploy
python manage.py check --deploy
python manage.py collectstatic --noinput
python manage.py migrate
```

---

### Q68. Docker Deployment

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
```

```yaml
# docker-compose.yml
version: '3.8'
services:
  web:
    build: .
    ports: ["8000:8000"]
    env_file: .env
    depends_on: [db, redis]

  db:
    image: postgres:15
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypass
    volumes: [postgres_data:/var/lib/postgresql/data]

  redis:
    image: redis:7-alpine

  celery:
    build: .
    command: celery -A myproject worker -l info

  celery-beat:
    build: .
    command: celery -A myproject beat -l info

volumes:
  postgres_data:
```

---

### Q69. WSGI vs ASGI

| | WSGI | ASGI |
|--|------|------|
| **Stands for** | Web Server Gateway Interface | Async Server Gateway Interface |
| **Django support** | Since v1.0 | Since v3.0 |
| **Concurrency** | Synchronous, thread-based | Async, supports many concurrent connections |
| **Protocols** | HTTP only | HTTP, WebSocket, long-polling |
| **Servers** | Gunicorn, uWSGI | Uvicorn, Daphne, Hypercorn |
| **Use when** | Standard REST APIs | Real-time features, WebSockets, streaming |

---

## 14. Advanced Topics

### Q70. API Gateway Role in Microservices

An API Gateway sits in front of all microservices and handles:
- **Routing** — forwards requests to the correct service
- **Authentication** — validates tokens centrally
- **Rate limiting** — prevents abuse
- **Load balancing** — distributes traffic
- **Aggregation** — combines responses from multiple services
- **SSL termination** — handles HTTPS at the edge

---

### Q71. File Uploads in DRF

```python
# models.py
class Document(models.Model):
    file = models.FileField(upload_to='documents/%Y/%m/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

# serializer
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'file', 'uploaded_by']
        read_only_fields = ['uploaded_by']

    def validate_file(self, value):
        max_size = 10 * 1024 * 1024   # 10 MB
        if value.size > max_size:
            raise serializers.ValidationError("File too large (max 10MB).")
        allowed = ['application/pdf', 'image/jpeg', 'image/png']
        if value.content_type not in allowed:
            raise serializers.ValidationError("Unsupported file type.")
        return value

# view
from rest_framework.parsers import MultiPartParser, FormParser

class DocumentUploadView(CreateAPIView):
    serializer_class = DocumentSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)
```

---

### Q72. Django Channels (WebSockets)

```python
# pip install channels channels-redis

# asgi.py
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns))
})

# consumer.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group = f"chat_{self.room_name}"
        await self.channel_layer.group_add(self.room_group, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.room_group,
            {'type': 'chat_message', 'message': data['message']}
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({'message': event['message']}))
```

---

### Q73. Django Security Vulnerabilities — Full List

1. **XSS** — Django auto-escapes template variables; use `mark_safe()` carefully
2. **CSRF** — `CsrfViewMiddleware` + `{% csrf_token %}`
3. **SQL Injection** — ORM uses parameterized queries; raw SQL → always use `%s` placeholders
4. **Clickjacking** — `X-Frame-Options: DENY` via `XFrameOptionsMiddleware`
5. **Sensitive Data Exposure** — `DEBUG=False`, secure cookies, `SECRET_KEY` in env vars
6. **Host Header Injection** — `ALLOWED_HOSTS` validation
7. **HTTPS** — `SECURE_SSL_REDIRECT`, HSTS headers
8. **Password storage** — PBKDF2 hashing by default; password validators enforced

---

### Q74. PostgreSQL Features Used with Django

| Feature | Use case |
|---------|---------|
| `JSONB` | Storing structured JSON data efficiently |
| `tsvector` | Full-text search |
| `EXPLAIN ANALYZE` | Query performance analysis |
| Triggers | Automate actions on data changes |
| `SELECT FOR UPDATE` | Row-level locking |
| Advisory locks | Application-level distributed locks |
| Connection pooling (`CONN_MAX_AGE`) | Reuse DB connections |

```python
# Full-text search example
from django.contrib.postgres.search import SearchVector, SearchQuery

Article.objects.annotate(
    search=SearchVector('title', 'content')
).filter(search=SearchQuery('django orm'))
```

---

### Q75. Swagger / OpenAPI Documentation

```python
# pip install drf-spectacular
# settings.py
INSTALLED_APPS = ['drf_spectacular']

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# urls.py
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
```

---

## Quick Reference

### Model Field Options

| Option | Description |
|--------|-------------|
| `null=True` | DB NULL allowed |
| `blank=True` | Form/validation allows empty |
| `db_index=True` | Create DB index |
| `unique=True` | Unique constraint + auto-indexed |
| `default=` | Default value |
| `choices=` | Restricted set of values |

### `on_delete` Options (ForeignKey)

| Option | Behavior |
|--------|---------|
| `CASCADE` | Delete child when parent deleted |
| `SET_NULL` | Set FK to NULL (requires `null=True`) |
| `PROTECT` | Prevent parent deletion if children exist |
| `SET_DEFAULT` | Set FK to `default` value |
| `DO_NOTHING` | No action (may cause DB integrity error) |

### ORM Cheat Sheet

| Method | Description |
|--------|-------------|
| `.filter()` | WHERE clause |
| `.exclude()` | WHERE NOT |
| `.order_by('-field')` | ORDER BY DESC |
| `.distinct()` | SELECT DISTINCT |
| `.count()` | SELECT COUNT(*) |
| `.exists()` | SELECT 1 LIMIT 1 |
| `.first()` / `.last()` | LIMIT 1 with ordering |
| `.get()` | Single object (raises if 0 or 2+) |
| `.values()` | Dict queryset |
| `.values_list()` | Tuple queryset |
| `.only()` | Fetch specified fields |
| `.defer()` | Skip specified fields |
| `.select_related()` | JOIN for FK/OneToOne |
| `.prefetch_related()` | Separate query for M2M/reverse FK |
| `.annotate()` | Add computed field per row |
| `.aggregate()` | Summary value for queryset |
| `.update()` | Bulk UPDATE (no signals) |
| `.bulk_create()` | Bulk INSERT (no signals) |
| `.iterator()` | Memory-efficient iteration |

### DRF Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK |
| 201 | Created |
| 204 | No Content (DELETE) |
| 400 | Bad Request (validation error) |
| 401 | Unauthorized (not authenticated) |
| 403 | Forbidden (no permission) |
| 404 | Not Found |
| 429 | Too Many Requests (throttled) |
| 500 | Server Error |

---

*Good luck with your interviews! 🚀*