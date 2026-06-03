# Django & DRF Interview Preparation
> **Target:** 4 Years Experience | Backend Developer

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
14. [Advanced / System Design Questions](#14-advanced--system-design-questions)

---

## 1. Django Core

### Q1. What is Django's request-response lifecycle?

```
Browser → WSGI/ASGI Server → Django → URL Dispatcher
→ Middleware (process_request) → View → Middleware (process_response) → Response
```

**Key steps:**
1. WSGI/ASGI server receives HTTP request
2. `process_request()` of each middleware runs (top-down)
3. URL resolver matches pattern → calls view
4. View returns `HttpResponse`
5. `process_response()` runs (bottom-up)
6. Response sent to client

---

### Q2. What is `settings.py`? How do you manage multiple environments?

Use `django-environ` or split settings:

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

# local.py
from .base import *
DEBUG = True
DATABASES = { 'default': { 'ENGINE': 'django.db.backends.sqlite3' } }

# production.py
from .base import *
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
```

Run with: `python manage.py runserver --settings=settings.local`

---

### Q3. Explain Django's MVT architecture.

| Component | Role |
|-----------|------|
| **Model** | Data layer — defines DB schema, ORM queries |
| **View** | Business logic — processes request, returns response |
| **Template** | Presentation layer — renders HTML |

Unlike MVC, Django's "Controller" is the URL dispatcher + framework itself.

---

### Q4. What are Django apps and why use them?

- A **Django project** = entire web application
- A **Django app** = modular, reusable component (e.g., `users`, `products`, `orders`)
- Apps promote separation of concerns and reusability across projects

```bash
python manage.py startapp users
```

---

### Q5. What is `manage.py` and common commands?

```bash
python manage.py runserver          # Start dev server
python manage.py makemigrations     # Generate migration files
python manage.py migrate            # Apply migrations
python manage.py createsuperuser    # Create admin user
python manage.py shell              # Django shell
python manage.py collectstatic      # Gather static files
python manage.py dbshell            # DB CLI
python manage.py test               # Run tests
python manage.py showmigrations     # List migrations
python manage.py sqlmigrate app 0001  # Show raw SQL
```

---

### Q6. What is Django's URL dispatcher? Explain `path()` vs `re_path()`.

```python
from django.urls import path, re_path, include

urlpatterns = [
    path('users/<int:pk>/', views.user_detail),          # Type-safe
    path('users/<str:username>/', views.user_by_name),
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),  # Regex
    path('api/', include('api.urls')),                   # Nested URLs
]
```

`path()` — simpler, built-in converters (`int`, `str`, `slug`, `uuid`, `path`)
`re_path()` — full regex control, more verbose

---

## 2. Django ORM

### Q7. Explain `select_related` vs `prefetch_related`.

| | `select_related` | `prefetch_related` |
|--|------------------|---------------------|
| **Relationship** | ForeignKey, OneToOne | ManyToMany, reverse FK |
| **SQL** | JOIN (single query) | Separate queries |
| **Use when** | Following single FK | Fetching many related objects |

```python
# select_related — SQL JOIN
orders = Order.objects.select_related('customer', 'customer__address').all()

# prefetch_related — 2 queries total
products = Product.objects.prefetch_related('categories', 'tags').all()

# Combine both
orders = Order.objects.select_related('customer').prefetch_related('items__product')
```

---

### Q8. What is `only()` vs `defer()` in QuerySets?

```python
# Only fetch specific fields (defers the rest)
users = User.objects.only('id', 'email', 'name')

# Fetch everything EXCEPT specified fields
users = User.objects.defer('bio', 'avatar', 'last_login')
```

Useful for wide tables where you don't need all columns. Accesses to deferred fields trigger additional DB queries.

---

### Q9. What are Django QuerySet methods — lazy vs eager evaluation?

**Lazy** (no DB hit): `filter()`, `exclude()`, `order_by()`, `annotate()`, `values()`

**Eager** (hits DB): iteration (`for`), `list()`, `len()`, slicing, `bool()`, `repr()`

```python
# No DB query yet
qs = Product.objects.filter(active=True).order_by('-created_at')

# DB query executes HERE
products = list(qs)

# Force evaluation
qs.count()   # SELECT COUNT(*)
qs.exists()  # SELECT 1 LIMIT 1  — faster than count()
qs.first()   # LIMIT 1
```

---

### Q10. Explain `annotate()` vs `aggregate()`.

```python
from django.db.models import Count, Sum, Avg, Max

# annotate() — adds field per row
categories = Category.objects.annotate(product_count=Count('products'))
# Each category object now has .product_count

# aggregate() — single value for entire queryset
result = Product.objects.aggregate(
    total=Sum('price'),
    avg_price=Avg('price'),
    max_price=Max('price')
)
# Returns: {'total': 9999.99, 'avg_price': 49.99, 'max_price': 199.99}
```

---

### Q11. What are `F()` and `Q()` expressions?

```python
from django.db.models import F, Q

# F() — reference field value (avoids race conditions)
Product.objects.update(stock=F('stock') - 1)     # Atomic decrement
Product.objects.filter(sale_price__lt=F('price')) # Compare two fields

# Q() — complex lookups with AND/OR/NOT
from django.db.models import Q

Product.objects.filter(
    Q(category='electronics') | Q(price__lt=100),
    ~Q(stock=0)   # NOT out of stock
)
```

**Why F() over Python math?** `F()` executes in DB atomically — no race condition if two threads read the same value simultaneously.

---

### Q12. How do Django migrations work? `makemigrations` vs `migrate`.

- **`makemigrations`** — detects model changes, generates migration files (`0001_initial.py`)
- **`migrate`** — applies pending migrations to DB

```bash
# Create migration
python manage.py makemigrations users

# Preview SQL without applying
python manage.py sqlmigrate users 0001

# Apply
python manage.py migrate

# Rollback to migration 0002
python manage.py migrate users 0002
```

**Custom migration (data migration):**
```python
from django.db import migrations

def populate_slug(apps, schema_editor):
    Article = apps.get_model('blog', 'Article')
    for article in Article.objects.all():
        article.slug = article.title.lower().replace(' ', '-')
        article.save()

class Migration(migrations.Migration):
    dependencies = [('blog', '0003_article_slug')]
    operations = [migrations.RunPython(populate_slug, migrations.RunPython.noop)]
```

---

### Q13. Explain `values()` vs `values_list()`.

```python
# values() — returns list of dicts
User.objects.values('id', 'email')
# [{'id': 1, 'email': 'a@b.com'}, ...]

# values_list() — returns list of tuples
User.objects.values_list('id', 'email')
# [(1, 'a@b.com'), ...]

# flat=True — only one field, returns flat list
User.objects.values_list('email', flat=True)
# ['a@b.com', 'b@c.com', ...]
```

Much faster than fetching full model instances when you only need specific fields.

---

### Q14. What is `bulk_create` and `bulk_update`? When to use?

```python
# bulk_create — single INSERT for many rows
products = [Product(name=f'Product {i}', price=10*i) for i in range(1000)]
Product.objects.bulk_create(products, batch_size=500)
# Skips: signals, custom save(), validation

# bulk_update — single UPDATE for many rows
for p in products:
    p.price = p.price * 1.1
Product.objects.bulk_update(products, ['price'], batch_size=500)

# update() — most efficient for uniform updates
Product.objects.filter(category='books').update(discount=10)
```

---

### Q15. What is `get_or_create()` and `update_or_create()`?

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

Thread-safe (uses `SELECT + INSERT` or handles `IntegrityError`).

---

## 3. Django Middleware

### Q16. What is Middleware? Write a custom middleware.

Middleware is a hook into request/response processing. Examples: `AuthenticationMiddleware`, `SessionMiddleware`, `CorsMiddleware`.

```python
# myapp/middleware.py
import time
import logging

logger = logging.getLogger(__name__)

class RequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response  # Called once on startup

    def __call__(self, request):
        # Code before view
        start = time.time()

        response = self.get_response(request)  # Call view

        # Code after view
        duration = time.time() - start
        logger.info(f"{request.method} {request.path} — {duration:.3f}s")
        response['X-Response-Time'] = f"{duration:.3f}s"
        return response
```

```python
# settings.py
MIDDLEWARE = [
    'myapp.middleware.RequestTimingMiddleware',
    'django.middleware.security.SecurityMiddleware',
    ...
]
```

---

### Q17. What are `process_request`, `process_view`, `process_response`, `process_exception`?

These are **old-style middleware hooks** (still valid):

```python
class OldStyleMiddleware:
    def process_request(self, request):
        # Runs before URL resolution; return None to continue or HttpResponse to short-circuit
        pass

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Runs after URL resolution, before view execution
        pass

    def process_response(self, request, response):
        # Always runs; must return response
        return response

    def process_exception(self, request, exception):
        # Only runs if view raises exception; return None to re-raise or HttpResponse
        pass
```

---

## 4. Django Signals

### Q18. What are Django Signals? Common built-in signals.

Signals allow decoupled apps to get notified when events happen.

| Signal | When fired |
|--------|-----------|
| `pre_save` | Before model `save()` |
| `post_save` | After model `save()` |
| `pre_delete` | Before model `delete()` |
| `post_delete` | After model `delete()` |
| `m2m_changed` | ManyToMany relationship changes |
| `request_started` | HTTP request begins |
| `request_finished` | HTTP request ends |

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
```

Register in `AppConfig.ready()`:
```python
# apps.py
class UsersConfig(AppConfig):
    name = 'users'
    def ready(self):
        import users.signals  # noqa
```

---

### Q19. When NOT to use signals?

- When you can call the function directly (signals are harder to trace/debug)
- For performance-critical code (signals add overhead, can't be async natively)
- When the relationship between sender/receiver is tight (defeats the purpose)

**Prefer signals for:** cross-app communication, third-party app hooks, audit logs.

---

## 5. Django Caching

### Q20. What caching backends does Django support?

| Backend | Use case |
|---------|---------|
| `LocMemCache` | Per-process, development only |
| `FileBasedCache` | Simple, no extra services |
| `MemcachedCache` | High-performance, distributed |
| `RedisCache` | Most popular in production |
| `DatabaseCache` | Cache in DB (rare) |

```python
# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
        'TIMEOUT': 300,
    }
}
```

---

### Q21. Explain per-view caching, template fragment caching, and low-level cache API.

```python
# 1. Per-view caching
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)  # 15 minutes
def product_list(request):
    ...

# 2. Template fragment caching
{% load cache %}
{% cache 600 product_detail product.id %}
    <div>{{ product.description }}</div>
{% endcache %}

# 3. Low-level cache API
from django.core.cache import cache

# Set
cache.set('user_123_profile', user_data, timeout=3600)

# Get
data = cache.get('user_123_profile')  # None if not found

# Get or set pattern
def get_user_profile(user_id):
    key = f'user_{user_id}_profile'
    data = cache.get(key)
    if data is None:
        data = UserProfile.objects.get(user_id=user_id)
        cache.set(key, data, 3600)
    return data

# Delete
cache.delete('user_123_profile')

# Many
cache.set_many({'a': 1, 'b': 2})
cache.get_many(['a', 'b'])
cache.delete_many(['a', 'b'])
```

---

## 6. Django Security

### Q22. How does Django protect against common vulnerabilities?

| Threat | Django Protection |
|--------|------------------|
| **CSRF** | `CsrfViewMiddleware`, `{% csrf_token %}` |
| **XSS** | Auto-escaping in templates |
| **SQL Injection** | ORM parameterized queries |
| **Clickjacking** | `X-Frame-Options` header |
| **Sensitive data** | `SECRET_KEY`, `DEBUG=False` in prod |
| **Host header attacks** | `ALLOWED_HOSTS` |

```python
# Production security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
```

---

### Q23. What is CSRF and how does Django handle it?

CSRF (Cross-Site Request Forgery) tricks a user's browser into making unintended requests.

Django uses a **double-submit cookie pattern**:
1. Sets `csrftoken` cookie on first visit
2. Requires matching `csrfmiddlewaretoken` in POST forms
3. For AJAX: send `X-CSRFToken` header

```python
# Exempt a view from CSRF (e.g., for APIs using token auth)
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def webhook(request):
    ...
```

DRF handles CSRF differently — session auth requires CSRF, token/JWT auth does not.

---

## 7. Django REST Framework (DRF)

### Q24. What is DRF and its core components?

Django REST Framework is a toolkit for building Web APIs on top of Django.

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
| `Renderer` | Output format (JSON, XML, HTML) |
| `Parser` | Input parsing (JSON, form, multipart) |

---

### Q25. Difference between `APIView`, `GenericAPIView`, and `ViewSet`.

```python
# APIView — most control, most manual
class ProductAPIView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid(raise_exception=True):
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

---

### Q26. List all Generic Views in DRF.

| Class | Methods | HTTP |
|-------|---------|------|
| `ListAPIView` | `list` | GET (collection) |
| `CreateAPIView` | `create` | POST |
| `RetrieveAPIView` | `retrieve` | GET (single) |
| `UpdateAPIView` | `update`, `partial_update` | PUT, PATCH |
| `DestroyAPIView` | `destroy` | DELETE |
| `ListCreateAPIView` | `list`, `create` | GET, POST |
| `RetrieveUpdateAPIView` | `retrieve`, `update` | GET, PUT, PATCH |
| `RetrieveDestroyAPIView` | `retrieve`, `destroy` | GET, DELETE |
| `RetrieveUpdateDestroyAPIView` | all of above | GET, PUT, PATCH, DELETE |

---

## 8. DRF Authentication & Permissions

### Q27. What authentication classes does DRF provide?

| Class | How it works |
|-------|-------------|
| `SessionAuthentication` | Django session cookie (browser clients) |
| `BasicAuthentication` | Base64 username:password in header (dev only) |
| `TokenAuthentication` | `Token <token>` in `Authorization` header |
| `JWTAuthentication` | JWT via `djangorestframework-simplejwt` |
| `RemoteUserAuthentication` | Proxy-auth via `REMOTE_USER` |

```python
# Global config
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# Per-view override
class PublicProductList(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
```

---

### Q28. Implement JWT Auth with SimpleJWT.

```python
# settings.py
INSTALLED_APPS = ['rest_framework_simplejwt']

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
POST /api/token/    {"username": "admin", "password": "pass"}
# Returns: {"access": "eyJ...", "refresh": "eyJ..."}

# Use token
GET /api/products/  Authorization: Bearer eyJ...

# Refresh
POST /api/token/refresh/  {"refresh": "eyJ..."}
```

---

### Q29. What permission classes does DRF have? Write a custom one.

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
from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    message = 'You must be the owner to edit this.'

    def has_permission(self, request, view):
        # View-level check
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Object-level check
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        return obj.owner == request.user

# Apply
class ProductView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
```

---

### Q30. Throttling in DRF.

```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day',
    }
}

# Custom scope throttle
class LoginRateThrottle(ScopedRateThrottle):
    scope = 'login'

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_RATES': {
        'login': '5/hour',
    }
}
```

---

## 9. DRF Serializers

### Q31. What is a Serializer? `Serializer` vs `ModelSerializer`.

**Serializer** — converts complex types (QuerySets, model instances) to Python native types → JSON, and validates incoming data.

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
```

---

### Q32. Nested Serializers and `SerializerMethodField`.

```python
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)           # Nested read
    category_id = serializers.PrimaryKeyRelatedField(       # Write via FK
        queryset=Category.objects.all(), source='category', write_only=True
    )
    discount_price = serializers.SerializerMethodField()    # Computed field
    tags = serializers.StringRelatedField(many=True)        # String repr

    def get_discount_price(self, obj):
        return obj.price * 0.9 if obj.on_sale else obj.price

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'discount_price', 'category', 'category_id', 'tags']
```

---

### Q33. How does DRF serializer validation work?

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

Validation order: `to_internal_value()` → `validate_<field>()` → `validate()` → `save()`

---

### Q34. What is `to_representation()` and `to_internal_value()`?

```python
class ProductSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        # Customize output (serialization)
        data = super().to_representation(instance)
        data['price'] = f"₹{data['price']}"   # Format price
        if not self.context['request'].user.is_staff:
            data.pop('cost_price', None)        # Hide from non-staff
        return data

    def to_internal_value(self, data):
        # Customize input (deserialization)
        if 'price' in data and isinstance(data['price'], str):
            data['price'] = data['price'].replace('₹', '').strip()
        return super().to_internal_value(data)
```

---

### Q35. What is `context` in serializers?

```python
# Pass context from view
serializer = ProductSerializer(
    product,
    context={'request': request, 'user': request.user}
)

# Access in serializer
class ProductSerializer(serializers.ModelSerializer):
    def get_is_liked(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            return obj.likes.filter(user=user).exists()
        return False
```

---

## 10. DRF ViewSets & Routers

### Q36. What are ViewSets and Routers?

```python
# ViewSet — groups related views
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Custom action
    @action(detail=True, methods=['post'], url_path='toggle-featured')
    def toggle_featured(self, request, pk=None):
        product = self.get_object()
        product.featured = not product.featured
        product.save()
        return Response({'featured': product.featured})

    @action(detail=False, methods=['get'])
    def featured(self, request):
        featured = Product.objects.filter(featured=True)
        serializer = self.get_serializer(featured, many=True)
        return Response(serializer.data)

# Router — auto URL generation
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [path('api/', include(router.urls))]
```

**Generated URLs:**
```
GET    /api/products/              → list
POST   /api/products/              → create
GET    /api/products/{pk}/         → retrieve
PUT    /api/products/{pk}/         → update
PATCH  /api/products/{pk}/         → partial_update
DELETE /api/products/{pk}/         → destroy
POST   /api/products/{pk}/toggle-featured/  → custom action
GET    /api/products/featured/     → custom list action
```

---

### Q37. How to use different serializers per action in a ViewSet?

```python
class ProductViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer      # Minimal fields
        elif self.action == 'create':
            return ProductCreateSerializer    # Writable fields
        return ProductDetailSerializer        # Full detail

    def get_queryset(self):
        qs = Product.objects.all()
        if self.action == 'list':
            return qs.only('id', 'name', 'price')
        return qs.select_related('category').prefetch_related('tags')
```

---

### Q38. Pagination in DRF.

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}

# Custom paginator
class StandardPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

# Cursor pagination (for large datasets, no offset issues)
class CursorPagination(CursorPagination):
    page_size = 20
    ordering = '-created_at'   # Must be unique + indexed

# Apply per-view
class ProductViewSet(viewsets.ModelViewSet):
    pagination_class = StandardPagination
```

---

### Q39. Filtering in DRF.

```python
# pip install django-filter

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ]
}

class ProductViewSet(viewsets.ModelViewSet):
    filterset_fields = ['category', 'active']           # Exact match
    search_fields = ['name', 'description', 'sku']      # ?search=
    ordering_fields = ['price', 'created_at', 'name']   # ?ordering=-price

# Custom FilterSet
import django_filters

class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    category_name = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['category', 'min_price', 'max_price', 'category_name']

class ProductViewSet(viewsets.ModelViewSet):
    filterset_class = ProductFilter
```

---

## 11. Performance & Optimization

### Q40. Common Django performance pitfalls.

**N+1 Query Problem:**
```python
# BAD — N+1 queries (1 + N for each order's customer)
orders = Order.objects.all()
for order in orders:
    print(order.customer.name)  # Extra query each iteration!

# GOOD — 1 query with JOIN
orders = Order.objects.select_related('customer').all()

# BAD for M2M
products = Product.objects.all()
for p in products:
    print(p.tags.all())  # Extra query per product

# GOOD
products = Product.objects.prefetch_related('tags').all()
```

**Use `iterator()` for large QuerySets:**
```python
# Avoids loading everything into memory
for product in Product.objects.filter(active=True).iterator(chunk_size=2000):
    process(product)
```

**Database indexes:**
```python
class Product(models.Model):
    sku = models.CharField(max_length=50, db_index=True)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['category', 'active']),          # Composite
            models.Index(fields=['-created_at']),                  # Descending
            models.Index(fields=['name'], name='product_name_idx'),
        ]
```

---

### Q41. How to debug slow queries in Django?

```python
# settings.py (dev only)
LOGGING = {
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    }
}

# Django Debug Toolbar (pip install django-debug-toolbar)
# Shows: queries, time, duplicates per request

# Manual query inspection
from django.db import connection, reset_queries
from django.conf import settings

settings.DEBUG = True
reset_queries()

# ... your code ...

print(len(connection.queries))
for q in connection.queries:
    print(q['sql'], q['time'])

# In shell
qs = Product.objects.filter(active=True).select_related('category')
print(qs.query)      # View raw SQL
qs.explain()         # EXPLAIN output
```

---

### Q42. Celery with Django — async tasks.

```python
# celery.py
from celery import Celery
import os

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
def send_email_task(self, user_id, subject, body):
    try:
        user = User.objects.get(id=user_id)
        send_mail(subject, body, 'from@example.com', [user.email])
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)

# Trigger from view
send_email_task.delay(user.id, 'Welcome!', 'Thanks for joining.')
send_email_task.apply_async(args=[user.id, 'Welcome!', 'Body'], countdown=300)
```

---

## 12. Testing

### Q43. How to write unit tests in Django?

```python
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

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

### Q44. What is `factory_boy` and `pytest-django`?

```python
# factories.py (factory_boy)
import factory
from .models import User, Product

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user_{n}')
    email = factory.LazyAttribute(lambda o: f'{o.username}@example.com')
    password = factory.PostGenerationMethodCall('set_password', 'testpass123')

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('product_name')
    price = factory.Faker('pydecimal', left_digits=3, right_digits=2, positive=True)
    category = factory.SubFactory(CategoryFactory)

# pytest test
import pytest

@pytest.mark.django_db
def test_product_api(api_client, user_factory):
    user = user_factory()
    api_client.force_authenticate(user=user)
    product = ProductFactory(name='Test Product')
    response = api_client.get(f'/api/products/{product.id}/')
    assert response.status_code == 200
    assert response.data['name'] == 'Test Product'
```

---

## 13. Deployment & Production

### Q45. How to deploy a Django app in production?

**Standard stack:**
```
Nginx (reverse proxy + static files)
  └── Gunicorn (WSGI server, multiple workers)
        └── Django application
              └── PostgreSQL + Redis
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

# Nginx config snippet
location / {
    proxy_pass http://127.0.0.1:8000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}

location /static/ {
    alias /var/www/myapp/static/;
}
```

---

### Q46. Production Checklist.

```python
# settings/production.py
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
SECRET_KEY = os.environ['SECRET_KEY']   # Never hardcode

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

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
# Before deploy
python manage.py check --deploy
python manage.py collectstatic --noinput
python manage.py migrate
```

---

## 14. Advanced / System Design Questions

### Q47. How would you design a rate-limited API?

```python
# Custom throttle with Redis
import redis
from rest_framework.throttling import BaseThrottle

class RedisSlidingWindowThrottle(BaseThrottle):
    r = redis.Redis()

    def allow_request(self, request, view):
        key = f"throttle:{request.user.id}"
        limit = 100
        window = 60   # 1 minute

        pipe = self.r.pipeline()
        now = time.time()
        pipe.zremrangebyscore(key, 0, now - window)
        pipe.zadd(key, {now: now})
        pipe.zcard(key)
        pipe.expire(key, window)
        _, _, count, _ = pipe.execute()
        return count <= limit
```

---

### Q48. How do you handle database transactions in Django?

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

# Savepoints
def complex_operation():
    with transaction.atomic():
        obj = Model.objects.create(name='Main')
        try:
            with transaction.atomic():  # Savepoint
                obj2 = Model.objects.create(name='Sub')
                raise ValueError("Oops")
        except ValueError:
            pass  # Savepoint rolled back, 'Main' still saved
```

---

### Q49. How to handle file uploads in DRF?

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
        max_size = 10 * 1024 * 1024  # 10MB
        if value.size > max_size:
            raise serializers.ValidationError("File too large (max 10MB).")
        allowed = ['application/pdf', 'image/jpeg', 'image/png']
        if value.content_type not in allowed:
            raise serializers.ValidationError("Unsupported file type.")
        return value

# view
class DocumentUploadView(CreateAPIView):
    serializer_class = DocumentSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)
```

---

### Q50. Explain Django Channels (WebSocket support).

```python
# pip install channels channels-redis

# asgi.py
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(ws_urlpatterns)
    )
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

### Q51. What is the difference between `WSGI` and `ASGI`?

| | WSGI | ASGI |
|--|------|------|
| **Stands for** | Web Server Gateway Interface | Async Server Gateway Interface |
| **Django support** | Since v1.0 | Since v3.0 |
| **Concurrency** | Synchronous, thread-based | Async, supports concurrent connections |
| **Protocols** | HTTP only | HTTP, WebSocket, long-polling |
| **Servers** | Gunicorn, uWSGI | Uvicorn, Daphne, Hypercorn |
| **Use when** | Standard REST APIs | Real-time, WebSockets, streaming |

---

### Q52. How would you implement soft delete?

```python
# SoftDeleteManager + Model mixin pattern
from django.db import models
from django.utils import timezone

class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

class AllObjectsManager(models.Manager):
    pass

class SoftDeleteMixin(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True, db_index=True)

    objects = SoftDeleteManager()       # Default — excludes soft-deleted
    all_objects = AllObjectsManager()   # Includes soft-deleted

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
    # Product.objects.all()         — excludes deleted
    # Product.all_objects.all()     — includes deleted
```

---

### Q53. How to version a DRF API?

```python
# 1. URL versioning
urlpatterns = [
    path('api/v1/', include('api.v1.urls')),
    path('api/v2/', include('api.v2.urls')),
]

# 2. Namespace versioning (recommended for DRF)
REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_VERSION': 'v1',
    'ALLOWED_VERSIONS': ['v1', 'v2'],
}

# 3. Conditional logic in view
class ProductViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return ProductV2Serializer
        return ProductV1Serializer
```

---

## Quick Reference — Common Django/DRF Interview Topics

| Topic | Key Points |
|-------|-----------|
| `__str__` vs `__repr__` | `__str__` for human, `__repr__` for debug |
| `null=True` vs `blank=True` | `null=True` = DB NULL, `blank=True` = form validation |
| `on_delete` options | `CASCADE`, `SET_NULL`, `PROTECT`, `SET_DEFAULT`, `DO_NOTHING` |
| `related_name` | Reverse accessor for FK/M2M (`order.items.all()`) |
| `Meta.ordering` | Default QuerySet ordering |
| `Meta.unique_together` | Composite unique constraint |
| `Meta.abstract` | Abstract base model (no DB table) |
| QuerySet `.count()` | Faster than `len()` — SELECT COUNT(*) |
| QuerySet `.exists()` | Faster than `.count() > 0` |
| `save()` vs `update()` | `save()` triggers signals; `update()` doesn't |
| DRF `raise_exception=True` | Auto-returns 400 on invalid serializer |
| DRF `many=True` | Serialize a list/queryset |
| `perform_create()` | Hook to inject extra data on save (e.g. user) |
| `get_queryset()` | Filter queryset per request/user |

---

*Good luck with your interviews! 🚀*