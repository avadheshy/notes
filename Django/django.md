# There are 9 classes in generics module. 
1. ListAPIView (get)
2. RetrieveAPIView (get)
3. CreateAPIView (post)
4. UpdateAPIView (put/patch)
5. DestroyAPIView (delete)
6. ListCreateAPIView (get/post)
7. RetrieveUpdateAPIView (GET/PUT/PATCH)
8. RetrieveDestroyAPIView (GET, DELETE)
9. RetrieveUpdateDestroyAPIView (GET/PUT/PATCH/DELETE)

# ✅ 1. Django Fundamentals
MTV Architecture (Model-Template-View)

Project vs App structure

manage.py, settings.py, urls.py

Virtual environments & dependency management

# ✅ 2. Models & ORM
Model fields and options (null, blank, choices, etc.)

Relationships: ForeignKey, OneToOneField, ManyToManyField

Meta options: ordering, db_table, unique_together, constraints

Custom model methods

Custom managers and QuerySets

Model validation (clean(), full_clean())

Migrations: makemigrations, migrate, and data migrations

Field lookups, F objects, Q objects

Aggregations and annotations

Indexing and performance optimization

# ✅ 3. Views
Function-based views (FBV)

Class-based views (CBV): ListView, DetailView, CreateView, UpdateView, DeleteView

Mixins and generic views

View decorators: login_required, permission_required, csrf_exempt

# ✅ 4. Templates
Template inheritance ({% extends %})

Template filters and tags

Context data and rendering

Custom template tags/filters

# ✅ 5. URLs & Routing
path(), re_path(), and include()

Named URLs and URL reversing (reverse, {% url %})

Dynamic URL patterns with slugs, IDs

# ✅ 6. Forms
forms.Form and forms.ModelForm

Form validation (clean_<field>(), clean())

Widgets and customization

Handling POST requests securely

# ✅ 7. Admin
Registering models in the admin

Customizing list views, filters, forms

Inlines and readonly fields

Overriding save_model, get_queryset, etc.

# ✅ 8. Authentication & Permissions
Django auth system (User, Group, Permission)

Login, logout, password change/reset

Custom user model (AbstractBaseUser, AbstractUser)

Permissions and @permission_required

# ✅ 9. Django REST Framework (DRF)
Serializers and ModelSerializers

API views: APIView, GenericAPIView, ViewSet

Routers and URLs

Authentication: Token, Session, JWT

Permissions: IsAuthenticated, IsAdminUser, custom permissions

Pagination, filtering, and throttling

# ✅ 10. Testing
Unit tests for models, views, and APIs

Using TestCase, Client, RequestFactory

Fixtures and factories

# ✅ 11. Middleware
How middleware works (request → response cycle)

Creating custom middleware

# ✅ 12. Security
CSRF, XSS, SQL injection protections

Django’s security settings: SECURE_SSL_REDIRECT, X_FRAME_OPTIONS, etc.

Safe file handling & user uploads

# ✅ 13. Static and Media Files
Serving static files with STATICFILES_DIRS

Uploading and accessing media via MEDIA_ROOT, MEDIA_URL

Using FileField and ImageField

# ✅ 14. Deployment
Production settings: DEBUG=False, allowed hosts, security

Using Gunicorn, uWSGI with Nginx

Static/media file handling in production

Environment variables and django-environ

Database configurations (PostgreSQL/MySQL)

# ✅ 15. Async, Caching, and Background Tasks
Django's async capabilities (3.1+)

Caching: cache.set, cache.get, @cache_page, Memcached/Redis

Celery for background tasks

Channels for WebSockets