# Django, DRF, and PostgreSQL Interview Q&A

---

## Django

### What is the purpose of Django's middleware?
- **Answer:** To process requests and responses globally.

### What is the effect of setting `queryset = None` in a ViewSet?
- **Answer:** It requires overriding `get_queryset`.

### How does Django handle circular imports in models?
- **Answer:** It uses lazy loading via `apps.get_model`.

### Which method is called when a serializer is saved?
- **Answer:** `save()`

### Which tool is used for profiling and optimizing Django queries?
- **Answer:** Django Debug Toolbar

---

## Django REST Framework (DRF)

### Which method in Django REST Framework is used to customize object-level permissions?
- **Answer:** `has_object_permission`

### What does the `Meta` class inside a serializer define?
- **Answer:** The fields to be serialized.

### Which renderer class allows API responses to be viewed in a web browser?
- **Answer:** `BrowsableAPIRenderer`

### What is the role of 'throttling' in DRF?
- **Answer:** To restrict API usage rate.

### Which DRF class is used to define custom pagination?
- **Answer:**
  - `PageNumberPagination`
  - `LimitOffsetPagination`
  - `CursorPagination`

### What does `allow_null=True` do in a serializer field?
- **Answer:** Allows `None` values.

### Which authentication method is stateless and suitable for APIs?
- **Answer:** Token-based

---

## API Tools & Best Practices

### What is the purpose of Swagger/OpenAPI in API development?
- **Answer:** To document and test APIs.

### What is the role of an API Gateway in microservices?
- **Answer:** To route requests and aggregate responses.

### What is the best practice for versioning REST APIs?
- **Answer:** Use URL path (e.g., `/api/v1/`)

---

## PostgreSQL

### What is the purpose of `EXPLAIN` in PostgreSQL?
- **Answer:** To analyze and show the execution plan of a query.

### Which PostgreSQL feature allows full-text search?
- **Answer:** `tsvector`

### What is the purpose of a PostgreSQL trigger?
- **Answer:** To automate actions on data changes.

### What is the safest way to execute raw SQL in Django?
- **Answer:** Using parameterized queries with `cursor.execute()`.

### Which PostgreSQL data type is best for storing structured JSON data?
- **Answer:** `JSONB`

---

## Django ORM

### What is the effect of using `exists()` on a queryset?
- **Answer:** Returns a boolean.

### Which ORM method is used to defer loading of specific fields?
- **Answer:** `defer()`

### Which ORM method is best for bulk updates?
- **Answer:** `bulk_update()`

### Which ORM method is used to annotate each object with a calculated field?
- **Answer:** `annotate()`

### What is the difference between `values()` and `values_list()` in Django ORM?
- **Answer:**
  - `values()` returns dictionaries.
  - `values_list()` returns tuples.

# Django Interview Questions and Answers

## Basic Django Questions

### 1. What is Django?

Django is a high-level Python web framework that follows the Model-View-Template (MVT) architectural pattern. It was created by Adrian Holovaty and Simon Willison in 2003 and released publicly in 2005. Django emphasizes rapid development, clean design, and the DRY (Don't Repeat Yourself) principle.

**Key Features:**
- Object-Relational Mapping (ORM)
- Automatic admin interface
- URL routing
- Template system
- Form handling
- Authentication system
- Internationalization support
- Security features built-in

### 2. What is the difference between Flask, FastAPI and Django?

| Feature | Django | Flask | FastAPI |
|---------|--------|-------|---------|
| **Type** | Full-stack framework | Micro framework | Modern API framework |
| **Philosophy** | Batteries included | Minimalist, flexible | High performance, type hints |
| **Learning Curve** | Steeper | Gentle | Moderate |
| **Built-in Features** | ORM, Admin, Auth, etc. | Basic routing, templating | Automatic API docs, validation |
| **Performance** | Good | Good | Excellent |
| **Use Case** | Full web applications | Small to medium apps | APIs and microservices |
| **Documentation** | Automatic API docs | Manual | Automatic (OpenAPI/Swagger) |

### 3. What is the difference between a Project and an App?

**Django Project:**
- A collection of configuration and apps for a particular website
- Contains settings, URL configuration, and deployment files
- One project can contain multiple apps
- Created using `django-admin startproject projectname`

**Django App:**
- A web application that does something specific
- Reusable and pluggable
- Contains models, views, templates, and URLs
- Created using `python manage.py startapp appname`

**Example Structure:**
```
myproject/          # Project
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── blog/           # App
│   ├── models.py
│   ├── views.py
│   └── urls.py
└── shop/           # App
    ├── models.py
    ├── views.py
    └── urls.py
```

### 4. Explain Django's architecture.

Django follows the **MVT (Model-View-Template)** pattern:

**Model:**
- Represents data structure
- Defines database schema
- Handles data logic and database operations

**View:**
- Contains business logic
- Processes requests and returns responses
- Acts as a controller between Model and Template

**Template:**
- Handles presentation layer
- Contains HTML with Django template language
- Separates design from logic

**Request-Response Flow:**
1. User sends request to Django server
2. URL dispatcher maps URL to appropriate view
3. View processes request, interacts with model if needed
4. View renders template with context data
5. Response sent back to user

### 5. What are the Features of using Django?

**1. Rapid Development:**
- Built-in admin interface
- Automatic database handling
- Ready-to-use components

**2. Security:**
- Protection against CSRF, XSS, SQL injection
- User authentication and authorization
- Secure password hashing

**3. Scalability:**
- Can handle high traffic
- Caching framework
- Database optimization tools

**4. Versatility:**
- Suitable for any web application
- REST API development
- Content management systems

**5. Python Ecosystem:**
- Extensive third-party packages
- Large community support
- Clean, readable code

### 6. How do you create a Django project and app? and start server

**Creating a Project:**
```bash
# Install Django
pip install django

# Create project
django-admin startproject myproject

# Navigate to project directory
cd myproject
```

**Creating an App:**
```bash
# Create app
python manage.py startapp myapp

# Add app to INSTALLED_APPS in settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # ... other apps
    'myapp',
]
```

**Starting Development Server:**
```bash
# Run migrations
python manage.py migrate

# Start server
python manage.py runserver

# Start server on specific port
python manage.py runserver 8080

# Start server on specific IP and port
python manage.py runserver 0.0.0.0:8000
```

### 7. Give a brief about the Django admin interface.

Django admin is an automatic admin interface for Django models. It reads metadata from models and provides a production-ready interface for managing content.

**Features:**
- Automatic CRUD operations
- User authentication and permissions
- Content filtering and searching
- Bulk actions
- Customizable interface

**Setup:**
```python
# models.py
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = models.Manager()  # Default manager
    published = PublishedManager()  # Custom manager

# Usage
all_articles = Article.objects.all()  # All articles
published_articles = Article.published.all()  # Only published articles
```

**Manager with Custom Methods:**
```python
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(is_published=True)
    
    def by_author(self, author):
        return self.filter(author=author)
    
    def recent(self, days=7):
        from datetime import timedelta
        cutoff = timezone.now() - timedelta(days=days)
        return self.filter(created_at__gte=cutoff)
    
    def popular(self, min_views=100):
        return self.filter(views__gte=min_views)
    
    def with_comments(self):
        return self.annotate(
            comment_count=Count('comments')
        ).filter(comment_count__gt=0)

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = ArticleManager()

# Usage
recent_published = Article.objects.published().recent(days=30)
popular_articles = Article.objects.popular(min_views=500)
author_articles = Article.objects.by_author(user).published()
```

**Custom QuerySet with Manager:**
```python
class ArticleQuerySet(models.QuerySet):
    def published(self):
        return self.filter(is_published=True)
    
    def by_category(self, category):
        return self.filter(category=category)
    
    def search(self, query):
        return self.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    
    def with_stats(self):
        return self.annotate(
            comment_count=Count('comments'),
            avg_rating=Avg('ratings__score')
        )

class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)
    
    def published(self):
        return self.get_queryset().published()
    
    def by_category(self, category):
        return self.get_queryset().by_category(category)

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    
    objects = ArticleManager()

# Chaining custom methods
articles = Article.objects.published().by_category(tech_category).search('Django')
```

**Manager for Soft Deletes:**
```python
class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class AllObjectsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    objects = SoftDeleteManager()  # Default: only non-deleted
    all_objects = AllObjectsManager()  # All objects including deleted
    
    def delete(self, hard=False):
        if hard:
            super().delete()
        else:
            self.is_deleted = True
            self.deleted_at = timezone.now()
            self.save()
    
    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()
    
    class Meta:
        abstract = True

class Article(SoftDeleteModel):
    title = models.CharField(max_length=200)
    content = models.TextField()

# Usage
Article.objects.all()  # Only non-deleted articles
Article.all_objects.all()  # All articles including deleted
```

**Tree Structure Manager:**
```python
class TreeManager(models.Manager):
    def roots(self):
        return self.filter(parent=None)
    
    def descendants_of(self, node):
        return self.filter(path__startswith=node.path)
    
    def ancestors_of(self, node):
        paths = [node.path[:i] for i in range(1, len(node.path), 4)]
        return self.filter(path__in=paths)

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    path = models.CharField(max_length=255)  # Materialized path
    
    objects = TreeManager()
    
    def save(self, *args, **kwargs):
        if self.parent:
            self.path = f"{self.parent.path}{self.pk:04d}"
        else:
            self.path = f"{self.pk:04d}"
        super().save(*args, **kwargs)
```

**When to Use Custom Managers:**

1. **Default Filtering**: When you frequently need to filter by certain conditions
2. **Complex Queries**: When you have complex query logic that's used multiple places
3. **Business Logic**: When you want to encapsulate business rules in the data layer
4. **Performance**: When you want to optimize queries with select_related/prefetch_related
5. **API Consistency**: When you want consistent query interfaces across your application

### 43. How does Django handle database transactions?

Django provides several ways to handle database transactions to ensure data consistency.

**Automatic Transaction Management:**
```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        # ... other settings
        'ATOMIC_REQUESTS': True,  # Wrap each view in transaction
    }
}
```

**Manual Transaction Control:**
```python
from django.db import transaction

# Decorator for entire function
@transaction.atomic
def create_article_with_tags(title, content, tag_names):
    article = Article.objects.create(title=title, content=content)
    
    for tag_name in tag_names:
        tag, created = Tag.objects.get_or_create(name=tag_name)
        article.tags.add(tag)
    
    return article

# Context manager
def transfer_funds(from_account, to_account, amount):
    with transaction.atomic():
        from_account.balance -= amount
        from_account.save()
        
        to_account.balance += amount
        to_account.save()
        
        # Create transaction record
        Transaction.objects.create(
            from_account=from_account,
            to_account=to_account,
            amount=amount
        )
```

**Nested Transactions (Savepoints):**
```python
def complex_operation():
    with transaction.atomic():  # Outer transaction
        article = Article.objects.create(title="Test Article")
        
        try:
            with transaction.atomic():  # Inner transaction (savepoint)
                # This might fail
                process_risky_operation(article)
        except Exception:
            # Inner transaction rolled back, outer continues
            logger.error("Risky operation failed")
        
        # This will still be saved
        article.status = 'processed'
        article.save()
```

**Transaction Hooks:**
```python
def send_notification_after_commit():
    # This will only run if transaction commits successfully
    send_email_notification()

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        # Schedule function to run after transaction commits
        transaction.on_commit(send_notification_after_commit)

post_save.connect(create_user_profile, sender=User)
```

**Rolling Back Transactions:**
```python
def create_article_with_validation():
    with transaction.atomic():
        article = Article.objects.create(title="Test")
        
        # Custom validation
        if not validate_article_content(article):
            transaction.set_rollback(True)
            raise ValidationError("Article content is invalid")
        
        return article

# Or raise exception to rollback
def create_article_strict():
    with transaction.atomic():
        article = Article.objects.create(title="Test")
        
        if not article.is_valid():
            raise ValidationError("Invalid article")  # Rolls back automatically
        
        return article
```

**Database-level Locking:**
```python
def update_counter_safe():
    with transaction.atomic():
        # SELECT ... FOR UPDATE
        counter = Counter.objects.select_for_update().get(name='page_views')
        counter.value += 1
        counter.save()

def bulk_update_with_lock():
    with transaction.atomic():
        # Lock multiple objects
        articles = Article.objects.select_for_update().filter(
            is_published=False
        )
        
        for article in articles:
            article.is_published = True
            article.save()
```

**Custom Transaction Handling:**
```python
from django.db import connections

def raw_transaction_example():
    connection = connections['default']
    
    try:
        with connection.cursor() as cursor:
            cursor.execute("BEGIN")
            
            cursor.execute(
                "INSERT INTO blog_article (title, content) VALUES (%s, %s)",
                ["Title", "Content"]
            )
            
            cursor.execute(
                "UPDATE blog_article SET views = views + 1 WHERE id = %s",
                [1]
            )
            
            cursor.execute("COMMIT")
    except Exception:
        cursor.execute("ROLLBACK")
        raise
```

**Testing Transactions:**
```python
from django.test import TransactionTestCase
from django.db import transaction

class TransactionTest(TransactionTestCase):
    def test_atomic_transaction(self):
        initial_count = Article.objects.count()
        
        try:
            with transaction.atomic():
                Article.objects.create(title="Test 1")
                Article.objects.create(title="Test 2")
                raise Exception("Simulated error")
        except Exception:
            pass
        
        # Both articles should be rolled back
        self.assertEqual(Article.objects.count(), initial_count)
```

### 44. How do you override a save method in a model, and what are the caveats?

**Basic save() Override:**
```python
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        # Generate slug from title if not provided
        if not self.slug:
            from django.utils.text import slugify
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            
            # Ensure unique slug
            while Article.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            
            self.slug = slug
        
        # Always call the parent save method
        super().save(*args, **kwargs)
```

**Advanced save() Override with Validation:**
```python
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
    def clean(self):
        # Model-level validation
        if self.birth_date and self.birth_date > timezone.now().date():
            raise ValidationError("Birth date cannot be in the future")
    
    def save(self, *args, **kwargs):
        # Run full_clean before saving
        self.full_clean()
        
        # Custom logic before save
        if self.avatar:
            self._resize_avatar()
        
        # Track if this is a new instance
        is_new = self._state.adding
        
        # Call parent save
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    def __str__(self):
        return self.title

# admin.py
from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'content']
```

**Creating Superuser:**
```bash
python manage.py createsuperuser
```

### 8. What are the sessions?

Sessions are a way to store information about a user across multiple requests. Django provides a session framework that stores session data on the server side and sends only a session ID to the client via cookies.

**Session Configuration:**
```python
# settings.py
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Database-backed sessions
SESSION_COOKIE_AGE = 1209600  # 2 weeks
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
```

**Using Sessions:**
```python
# views.py
def login_view(request):
    # Set session data
    request.session['user_id'] = user.id
    request.session['username'] = user.username

def profile_view(request):
    # Get session data
    user_id = request.session.get('user_id')
    username = request.session.get('username', 'Guest')
    
def logout_view(request):
    # Clear session
    request.session.flush()
```

### 9. Difference between MVC and MVT design patterns?

| Aspect | MVC (Model-View-Controller) | MVT (Model-View-Template) |
|--------|----------------------------|---------------------------|
| **Components** | Model, View, Controller | Model, View, Template |
| **Controller** | Handles user input and logic | Django framework acts as controller |
| **View** | Presents data to user | Contains business logic |
| **Template** | Not present | Handles presentation |
| **Framework Control** | Developer manages controller | Django manages URL routing |
| **Examples** | Laravel, Ruby on Rails | Django |

**MVT Flow:**
1. URL dispatcher (built-in controller) receives request
2. Maps URL to appropriate View
3. View processes request and interacts with Model
4. View renders Template with context
5. Template returns HTML response

### 10. What is Superuser?

A superuser is a user account with all permissions in Django admin. They have unrestricted access to the admin interface and can perform all operations.

**Creating Superuser:**
```bash
python manage.py createsuperuser
```

**Superuser Properties:**
- `is_staff = True` (can access admin)
- `is_superuser = True` (has all permissions)
- `is_active = True` (account is active)

**Programmatically Creating Superuser:**
```python
from django.contrib.auth.models import User

User.objects.create_superuser(
    username='admin',
    email='admin@example.com',
    password='securepassword'
)
```

### 11. What do you mean by the csrf_token?

CSRF (Cross-Site Request Forgery) token is a security measure that protects against CSRF attacks. It ensures that forms are submitted from the same site and not from malicious third-party sites.

**How it works:**
1. Django generates a unique token for each session
2. Token is included in forms as a hidden field
3. When form is submitted, Django verifies the token
4. If token is invalid, request is rejected

**Usage:**
```html
<!-- In template -->
<form method="post">
    {% csrf_token %}
    <input type="text" name="username">
    <button type="submit">Submit</button>
</form>
```

**In AJAX:**
```javascript
// Get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Use in AJAX request
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});
```

### 12. What is Media Root?

MEDIA_ROOT is the absolute filesystem path to the directory that holds user-uploaded files. It's where Django stores files uploaded through FileField and ImageField.

**Configuration:**
```python
# settings.py
import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

**URL Configuration:**
```python
# urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # your url patterns
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

**Model Example:**
```python
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/')
    resume = models.FileField(upload_to='documents/')
```

### 13. How you can include and inherit files in your application?

**Template Inheritance:**
```html
<!-- base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <div id="content">
        {% block content %}{% endblock %}
    </div>
</body>
</html>

<!-- child.html -->
{% extends "base.html" %}

{% block title %}Page Title{% endblock %}

{% block content %}
    <h1>Welcome to my page</h1>
{% endblock %}
```

**Including Templates:**
```html
<!-- header.html -->
<header>
    <nav>Navigation here</nav>
</header>

<!-- main.html -->
{% include "header.html" %}
<main>
    Content here
</main>
{% include "footer.html" %}
```

**Including with Variables:**
```html
{% include "snippet.html" with value="hello" %}
```

### 14. How do you connect your Django Project to the database?

**Database Configuration:**
```python
# settings.py

# SQLite (Default)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

**Required Packages:**
```bash
# PostgreSQL
pip install psycopg2-binary

# MySQL
pip install mysqlclient
```

**Migration Commands:**
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Check migration status
python manage.py showmigrations
```

### 15. Give the exception classes present in Django.

**Common Django Exceptions:**

**1. Model Exceptions:**
```python
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

try:
    user = User.objects.get(username='john')
except User.DoesNotExist:
    # Handle case when user doesn't exist
    pass
except MultipleObjectsReturned:
    # Handle case when multiple users found
    pass
```

**2. Validation Exceptions:**
```python
from django.core.exceptions import ValidationError

def clean_email(self):
    email = self.cleaned_data['email']
    if not email.endswith('@company.com'):
        raise ValidationError('Email must be company email')
    return email
```

**3. HTTP Exceptions:**
```python
from django.http import Http404
from django.core.exceptions import PermissionDenied, SuspiciousOperation

def my_view(request):
    if not request.user.is_authenticated:
        raise PermissionDenied
    
    try:
        obj = MyModel.objects.get(pk=1)
    except MyModel.DoesNotExist:
        raise Http404("Object not found")
```

**4. Form Exceptions:**
```python
from django.forms import ValidationError

class MyForm(forms.Form):
    def clean_field(self):
        data = self.cleaned_data['field']
        if len(data) < 5:
            raise ValidationError('Field must be at least 5 characters')
        return data
```

### 16. How do filter items in the Model?

**Basic Filtering:**
```python
# Get all published articles
articles = Article.objects.filter(is_published=True)

# Get articles by specific author
articles = Article.objects.filter(author__username='john')

# Get articles created today
from datetime import date
articles = Article.objects.filter(created_at__date=date.today())
```

**Field Lookups:**
```python
# Exact match
Article.objects.filter(title__exact='Django Tutorial')

# Case-insensitive match
Article.objects.filter(title__iexact='django tutorial')

# Contains
Article.objects.filter(title__contains='Django')

# Starts with / ends with
Article.objects.filter(title__startswith='How to')
Article.objects.filter(title__endswith='Tutorial')

# Greater than / less than
Article.objects.filter(views__gt=100)
Article.objects.filter(views__gte=100)
Article.objects.filter(views__lt=1000)

# Date filtering
Article.objects.filter(created_at__year=2023)
Article.objects.filter(created_at__month=12)
Article.objects.filter(created_at__day=25)

# In list
Article.objects.filter(category__in=['tech', 'science'])

# Range
Article.objects.filter(views__range=(100, 1000))

# Null values
Article.objects.filter(description__isnull=True)
```

**Complex Filtering:**
```python
from django.db.models import Q

# OR conditions
articles = Article.objects.filter(
    Q(category='tech') | Q(category='science')
)

# AND conditions (default)
articles = Article.objects.filter(
    category='tech',
    is_published=True
)

# NOT conditions
articles = Article.objects.filter(~Q(category='tech'))

# Complex combinations
articles = Article.objects.filter(
    Q(category='tech') & (Q(views__gt=100) | Q(is_featured=True))
)
```

### 17. What is the difference between CharField and TextField in Django

| Aspect | CharField | TextField |
|--------|-----------|-----------|
| **Max Length** | Required (max_length parameter) | No limit (optional max_length) |
| **Database Type** | VARCHAR | TEXT |
| **Use Case** | Short strings (names, titles) | Long text (descriptions, content) |
| **Form Widget** | TextInput (single line) | Textarea (multi-line) |
| **Indexing** | Better for indexing | Less efficient for indexing |

**Examples:**
```python
class Article(models.Model):
    title = models.CharField(max_length=200)  # Short, limited text
    slug = models.CharField(max_length=200, unique=True)
    content = models.TextField()  # Long, unlimited text
    summary = models.TextField(max_length=500)  # Limited long text
```

### 18. What are Django cookies?

Cookies are small pieces of data stored in the user's browser. Django provides methods to set, get, and delete cookies.

**Setting Cookies:**
```python
def set_cookie_view(request):
    response = HttpResponse("Cookie set")
    response.set_cookie('username', 'john', max_age=3600)  # 1 hour
    return response

# With additional parameters
response.set_cookie(
    'user_preference',
    'dark_theme',
    max_age=365*24*60*60,  # 1 year
    secure=True,  # Only over HTTPS
    httponly=True,  # Not accessible via JavaScript
    samesite='Strict'  # CSRF protection
)
```

**Getting Cookies:**
```python
def get_cookie_view(request):
    username = request.COOKIES.get('username', 'Guest')
    return HttpResponse(f"Hello {username}")
```

**Deleting Cookies:**
```python
def delete_cookie_view(request):
    response = HttpResponse("Cookie deleted")
    response.delete_cookie('username')
    return response
```

### 19. How to check the version of Django installed on your system?

**Method 1: Command Line**
```bash
python -m django --version
# or
django-admin --version
```

**Method 2: Python Code**
```python
import django
print(django.get_version())
# or
print(django.VERSION)
```

**Method 3: pip**
```bash
pip show django
pip freeze | grep Django
```

### 20. Why is Django called a loosely coupled framework?

Django is called loosely coupled because its components are independent and can be modified without affecting other parts of the system.

**Examples of Loose Coupling:**

**1. Apps are Independent:**
```python
# Each app can function independently
# blog app doesn't depend on shop app
INSTALLED_APPS = [
    'blog',
    'shop',
    'users',
]
```

**2. Model-View-Template Separation:**
```python
# Models don't know about views
class Article(models.Model):
    title = models.CharField(max_length=200)

# Views don't know about template internals
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/list.html', {'articles': articles})
```

**3. URL Configuration:**
```python
# URLs are separate from views
urlpatterns = [
    path('articles/', views.article_list, name='article_list'),
    path('articles/<int:pk>/', views.article_detail, name='article_detail'),
]
```

**4. Database Independence:**
```python
# Can switch databases without changing models
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Can change to MySQL
        # ... other settings
    }
}
```

### 21. Explain user authentication in Django

Django provides a robust authentication system with built-in user management, permissions, and groups.

**User Model:**
```python
from django.contrib.auth.models import User

# Create user
user = User.objects.create_user(
    username='john',
    email='john@example.com',
    password='securepassword'
)

# Create superuser
user = User.objects.create_superuser(
    username='admin',
    email='admin@example.com',
    password='adminpassword'
)
```

**Login/Logout Views:**
```python
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
```

**Permission Decorators:**
```python
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def profile_view(request):
    return render(request, 'profile.html')

@permission_required('blog.add_article')
def create_article(request):
    # Only users with add_article permission can access
    pass
```

**Custom User Model:**
```python
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True, blank=True)

# settings.py
AUTH_USER_MODEL = 'accounts.CustomUser'
```

### 22. What is the "Django.shortcuts.render" function?

The `render()` function is a shortcut for rendering templates with context data. It combines template loading, context creation, and HTTP response generation.

**Syntax:**
```python
render(request, template_name, context=None, content_type=None, status=None, using=None)
```

**Basic Usage:**
```python
from django.shortcuts import render

def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
        'title': 'All Articles'
    }
    return render(request, 'blog/article_list.html', context)
```

**What it does internally:**
```python
# render() is equivalent to:
from django.template import loader
from django.http import HttpResponse

def article_list(request):
    articles = Article.objects.all()
    template = loader.get_template('blog/article_list.html')
    context = {
        'articles': articles,
        'title': 'All Articles'
    }
    return HttpResponse(template.render(context, request))
```

**Additional Parameters:**
```python
# Custom content type
return render(request, 'template.xml', context, content_type='application/xml')

# Custom status code
return render(request, 'error.html', context, status=404)
```

### 23. What is serialization in Django?

Serialization is the process of converting Django model instances into other formats like JSON, XML, or YAML for data exchange or storage.

**Django Built-in Serialization:**
```python
from django.core import serializers

# Serialize to JSON
data = serializers.serialize('json', Article.objects.all())

# Serialize specific fields
data = serializers.serialize('json', Article.objects.all(), 
                           fields=('title', 'content', 'created_at'))

# Deserialize
for obj in serializers.deserialize('json', data):
    obj.save()
```

**Manual JSON Serialization:**
```python
import json
from django.http import JsonResponse

def article_api(request):
    articles = Article.objects.all()
    data = []
    for article in articles:
        data.append({
            'id': article.id,
            'title': article.title,
            'content': article.content,
            'created_at': article.created_at.isoformat()
        })
    return JsonResponse(data, safe=False)
```

**Using model_to_dict:**
```python
from django.forms.models import model_to_dict

def article_detail_api(request, pk):
    article = get_object_or_404(Article, pk=pk)
    data = model_to_dict(article)
    return JsonResponse(data)
```

## Intermediate Django Questions

### 24. What is Django URLs

Django URLs are patterns that define how URLs in your web application map to views. They act as the routing system for your Django project.

**URL Configuration:**
```python
# urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    # Basic URL pattern
    path('', views.home, name='home'),
    
    # URL with parameters
    path('article/<int:id>/', views.article_detail, name='article_detail'),
    
    # URL with string parameter
    path('category/<str:name>/', views.category_view, name='category'),
    
    # URL with slug
    path('article/<slug:slug>/', views.article_by_slug, name='article_slug'),
    
    # Including app URLs
    path('blog/', include('blog.urls')),
    
    # Regular expressions
    path('year/<int:year>/', views.year_archive, name='year_archive'),
]
```

**URL Converters:**
- `str` - Matches any non-empty string (default)
- `int` - Matches zero or positive integers
- `slug` - Matches ASCII letters, numbers, hyphens, underscores
- `uuid` - Matches UUID strings
- `path` - Matches any non-empty string including path separator

**Named URLs and Reverse:**
```python
# In views
from django.urls import reverse
from django.shortcuts import redirect

def my_view(request):
    return redirect(reverse('article_detail', args=[1]))

# In templates
# <a href="{% url 'article_detail' article.id %}">View Article</a>
```

### 25. Explain Django project directory

**Project Structure:**
```
myproject/                  # Project root directory
├── manage.py              # Command-line utility
├── myproject/             # Project package
│   ├── __init__.py       # Python package marker
│   ├── settings.py       # Project settings
│   ├── urls.py           # Root URL configuration
│   ├── wsgi.py           # WSGI deployment
│   └── asgi.py           # ASGI deployment (Django 3.0+)
├── myapp/                # Django app
│   ├── __init__.py
│   ├── admin.py          # Admin configuration
│   ├── apps.py           # App configuration
│   ├── models.py         # Data models
│   ├── views.py          # View functions/classes
│   ├── urls.py           # App URL patterns
│   ├── tests.py          # Unit tests
│   ├── migrations/       # Database migrations
│   │   └── __init__.py
│   ├── templates/        # HTML templates
│   │   └── myapp/
│   └── static/           # Static files (CSS, JS, images)
│       └── myapp/
├── static/               # Collected static files
├── media/                # User uploaded files
├── templates/            # Global templates
└── requirements.txt      # Project dependencies
```

**Key Files Explained:**
- **manage.py**: Command-line utility for administrative tasks
- **settings.py**: All project settings and configuration
- **urls.py**: URL routing configuration
- **wsgi.py**: Web Server Gateway Interface for deployment
- **models.py**: Database models definition
- **views.py**: Business logic and request handling
- **admin.py**: Django admin interface configuration

### 26. What are models in django

Models in Django are Python classes that define the structure and behavior of your database tables. Each model class represents a database table, and each attribute represents a database field.

**Basic Model:**
```python
from django.db import models
from django.contrib.auth.models import User

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

**Common Field Types:**
```python
class ExampleModel(models.Model):
    # Text fields
    char_field = models.CharField(max_length=100)
    text_field = models.TextField()
    email_field = models.EmailField()
    url_field = models.URLField()
    slug_field = models.SlugField()
    
    # Numeric fields
    integer_field = models.IntegerField()
    float_field = models.FloatField()
    decimal_field = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Date/Time fields
    date_field = models.DateField()
    datetime_field = models.DateTimeField()
    time_field = models.TimeField()
    
    # Boolean field
    boolean_field = models.BooleanField()
    
    # File fields
    image_field = models.ImageField(upload_to='images/')
    file_field = models.FileField(upload_to='documents/')
    
    # Choice field
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
```

**Model Relationships:**
```python
# One-to-Many (ForeignKey)
class Category(models.Model):
    name = models.CharField(max_length=100)

class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

# Many-to-Many
class Tag(models.Model):
    name = models.CharField(max_length=50)

class Article(models.Model):
    tags = models.ManyToManyField(Tag, blank=True)

# One-to-One
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
```

### 27. What are templates in Django or Django template language?

Django templates are text files that define the structure and layout of your web pages. They use Django Template Language (DTL) to dynamically generate HTML.

**Template Syntax:**

**Variables:**
```html
<!-- Basic variable -->
<h1>{{ article.title }}</h1>
<p>{{ article.content }}</p>

<!-- Accessing attributes -->
<p>Author: {{ article.author.username }}</p>
<p>Created: {{ article.created_at|date:"Y-m-d" }}</p>
```

**Template Tags:**
```html
<!-- Control structures -->
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}

<!-- Loops -->
{% for article in articles %}
    <div>
        <h3>{{ article.title }}</h3>
        <p>{{ article.content|truncatewords:20 }}</p>
    </div>
{% empty %}
    <p>No articles found.</p>
{% endfor %}

<!-- URL generation -->
<a href="{% url 'article_detail' article.id %}">Read More</a>

<!-- Static files -->
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

**Template Filters:**
```html
<!-- String filters -->
{{ article.title|upper }}
{{ article.content|lower }}
{{ article.content|truncatewords:10 }}
{{ article.title|capfirst }}

<!-- Date filters -->
{{ article.created_at|date:"F d, Y" }}
{{ article.created_at|timesince }}

<!-- Number filters -->
{{ price|floatformat:2 }}
{{ number|add:5 }}

<!-- List filters -->
{{ articles|length }}
{{ articles|first }}
{{ articles|last }}

<!-- Default values -->
{{ article.description|default:"No description available" }}
```

**Template Inheritance:**
```html
<!-- base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
    {% block extra_css %}{% endblock %}
</head>
<body>
    <header>
        {% block header %}
            <h1>My Website</h1>
        {% endblock %}
    </header>
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    <footer>
        {% block footer %}
            <p>&copy; 2023 My Website</p>
        {% endblock %}
    </footer>
    
    {% block extra_js %}{% endblock %}
</body>
</html>

<!-- article_detail.html -->
{% extends "base.html" %}

{% block title %}{{ article.title }} - {{ block.super }}{% endblock %}

{% block content %}
    <article>
        <h1>{{ article.title }}</h1>
        <p class="meta">By {{ article.author }} on {{ article.created_at|date:"F d, Y" }}</p>
        <div class="content">
            {{ article.content|linebreaks }}
        </div>
    </article>
{% endblock %}
```

### 28. What are views in Django? Its different types. pros and cons

Views in Django are Python functions or classes that handle HTTP requests and return HTTP responses. They contain the business logic of your application.

**Function-Based Views (FBVs):**
```python
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

def article_list(request):
    articles = Article.objects.filter(is_published=True)
    return render(request, 'blog/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk, is_published=True)
    return render(request, 'blog/article_detail.html', {'article': article})

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

**Class-Based Views (CBVs):**
```python
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'
    queryset = Article.objects.filter(is_published=True)
    paginate_by = 10

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/create_article.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
```

**Generic Views:**
```python
# Built-in generic views
from django.views.generic import (
    ListView, DetailView, CreateView, 
    UpdateView, DeleteView, TemplateView
)

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'content', 'is_published']
    template_name = 'blog/update_article.html'

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'blog/delete_article.html'
    success_url = reverse_lazy('article_list')
```

**Comparison:**

| Aspect | Function-Based Views | Class-Based Views |
|--------|---------------------|-------------------|
| **Simplicity** | Simple and straightforward | More complex, steeper learning curve |
| **Reusability** | Limited reusability | Highly reusable through inheritance |
| **Customization** | Easy to customize | Requires understanding of methods |
| **Code Organization** | Can become repetitive | Better code organization |
| **Learning Curve** | Easier for beginners | Requires OOP knowledge |
| **Debugging** | Easier to debug | Can be harder to trace execution |

**Pros of FBVs:**
- Simple and explicit
- Easy to understand and debug
- Full control over request handling
- Good for simple views

**Cons of FBVs:**
- Code repetition
- Limited reusability
- Can become lengthy for complex operations

**Pros of CBVs:**
- Code reusability through inheritance
- Built-in functionality for common patterns
- Clean separation of concerns
- Less boilerplate code

**Cons of CBVs:**
- Steeper learning curve
- Can be over-engineered for simple views
- Harder to debug and understand flow

### 29. What is Django ORM?

Django ORM (Object-Relational Mapping) is a programming technique that allows you to interact with databases using Python objects instead of writing raw SQL queries.

**Basic ORM Operations:**

**Creating Objects:**
```python
# Method 1: Create and save
article = Article(title="My Article", content="Article content")
article.save()

# Method 2: Create directly
article = Article.objects.create(
    title="My Article",
    content="Article content",
    author=request.user
)

# Method 3: get_or_create
article, created = Article.objects.get_or_create(
    title="My Article",
    defaults={'content': 'Article content', 'author': request.user}
)
```

**Reading/Querying Objects:**
```python
# Get all objects
articles = Article.objects.all()

# Filter objects
published_articles = Article.objects.filter(is_published=True)

# Get single object
article = Article.objects.get(pk=1)

# Get or return 404
article = get_object_or_404(Article, pk=1)

# Check if exists
exists = Article.objects.filter(title="My Article").exists()

# Count objects
count = Article.objects.filter(is_published=True).count()

# Order objects
articles = Article.objects.order_by('-created_at', 'title')

# Limit results
recent_articles = Article.objects.all()[:5]

# Exclude objects
articles = Article.objects.exclude(is_published=False)
```

**Complex Queries:**
```python
from django.db.models import Q, F, Count, Sum, Avg

# Q objects for complex conditions
articles = Article.objects.filter(
    Q(title__contains='Django') | Q(content__contains='Python')
)

# F objects for field comparisons
articles = Article.objects.filter(views__gt=F('likes') * 2)

# Annotations
articles = Article.objects.annotate(
    comment_count=Count('comments'),
    avg_rating=Avg('ratings__score')
)

# Aggregations
stats = Article.objects.aggregate(
    total_articles=Count('id'),
    avg_views=Avg('views'),
    total_views=Sum('views')
)
```

**Updating Objects:**
```python
# Update single object
article = Article.objects.get(pk=1)
article.title = "Updated Title"
article.save()

# Update multiple objects
Article.objects.filter(is_published=False).update(is_published=True)

# Update with F expressions
Article.objects.filter(pk=1).update(views=F('views') + 1)
```

**Deleting Objects:**
```python
# Delete single object
article = Article.objects.get(pk=1)
article.delete()

# Delete multiple objects
Article.objects.filter(is_published=False).delete()

# Soft delete (custom implementation)
Article.objects.filter(pk=1).update(is_deleted=True)
```

### 30. Define static files and explain their uses?

Static files are assets like CSS, JavaScript, images, and fonts that don't change dynamically. Django provides a robust system for managing static files.

**Configuration:**
```python
# settings.py
import os

# URL prefix for static files
STATIC_URL = '/static/'

# Directory where collectstatic will collect static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Additional directories to search for static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'assets'),
]

# Static file finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
```

**Directory Structure:**
```
myproject/
├── static/                    # Global static files
│   ├── css/
│   │   └── main.css
│   ├── js/
│   │   └── main.js
│   └── images/
│       └── logo.png
├── myapp/
│   └── static/               # App-specific static files
│       └── myapp/
│           ├── css/
│           │   └── app.css
│           ├── js/
│           │   └── app.js
│           └── images/
│               └── icon.png
└── staticfiles/              # Collected static files (production)
```

**Using Static Files in Templates:**
```html
{% load static %}

<!DOCTYPE html>
<html>
<head>
    <title>My Site</title>
    <!-- CSS files -->
    <link rel="stylesheet" href="{% static 'css/main.css' %}">
    <link rel="stylesheet" href="{% static 'myapp/css/app.css' %}">
</head>
<body>
    <!-- Images -->
    <img src="{% static 'images/logo.png' %}" alt="Logo">
    <img src="{% static 'myapp/images/icon.png' %}" alt="Icon">
    
    <!-- JavaScript files -->
    <script src="{% static 'js/main.js' %}"></script>
    <script src="{% static 'myapp/js/app.js' %}"></script>
</body>
</html>
```

**URL Configuration for Development:**
```python
# urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # your url patterns
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

**Management Commands:**
```bash
# Collect all static files to STATIC_ROOT
python manage.py collectstatic

# Find static files
python manage.py findstatic css/main.css

# Run development server with static files
python manage.py runserver
```

**Production Setup:**
```python
# settings.py for production
STATIC_ROOT = '/var/www/mysite/static/'

# Use whitenoise for serving static files
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this
    # ... other middleware
]

# Whitenoise settings
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### 31. What is Django Rest Framework(DRF)?

Django REST Framework is a powerful toolkit for building Web APIs in Django. It provides serialization, authentication, permissions, and browsable API features.

**Installation:**
```bash
pip install djangorestframework
```

**Configuration:**
```python
# settings.py
INSTALLED_APPS = [
    # ... other apps
    'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}
```

**Serializers:**
```python
# serializers.py
from rest_framework import serializers
from .models import Article, Category

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
        fields = ['id', 'title', 'content', 'author', 'category', 
                 'category_id', 'created_at', 'is_published']
        read_only_fields = ['created_at']
    
    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long")
        return value
```

**API Views:**
```python
# views.py
from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

# Function-based API view
@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Class-based API views
class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]
```

**ViewSets and Routers:**
```python
# views.py
from rest_framework import viewsets
from rest_framework.decorators import action

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        article = self.get_object()
        article.is_published = True
        article.save()
        return Response({'status': 'article published'})
    
    @action(detail=False)
    def published(self, request):
        published_articles = Article.objects.filter(is_published=True)
        serializer = self.get_serializer(published_articles, many=True)
        return Response(serializer.data)

# urls.py
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'articles', views.ArticleViewSet)
urlpatterns = router.urls
```

**Authentication and Permissions:**
```python
# Custom permission
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only to the owner
        return obj.author == request.user

# Using in views
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
```

### 32. What is django-admin and manage.py and explain its commands?

**django-admin** is Django's command-line utility for administrative tasks, while **manage.py** is a project-specific wrapper around django-admin.

**Common Commands:**

**Project Management:**
```bash
# Create new project
django-admin startproject myproject

# Create new app
python manage.py startapp myapp

# Run development server
python manage.py runserver
python manage.py runserver 8080
python manage.py runserver 0.0.0.0:8000
```

**Database Commands:**
```bash
# Create migrations
python manage.py makemigrations
python manage.py makemigrations myapp

# Apply migrations
python manage.py migrate
python manage.py migrate myapp

# Show migrations
python manage.py showmigrations

# Create empty migration
python manage.py makemigrations --empty myapp

# Reverse migration
python manage.py migrate myapp 0001

# Show SQL for migration
python manage.py sqlmigrate myapp 0001
```

**User Management:**
```bash
# Create superuser
python manage.py createsuperuser

# Change user password
python manage.py changepassword username
```

**Data Management:**
```bash
# Load data from fixtures
python manage.py loaddata fixture_name

# Dump data to fixtures
python manage.py dumpdata > data.json
python manage.py dumpdata myapp.MyModel > model_data.json

# Flush database
python manage.py flush
```

**Static Files:**
```bash
# Collect static files
python manage.py collectstatic

# Find static files
python manage.py findstatic css/main.css
```

**Development Tools:**
```bash
# Django shell
python manage.py shell

# Database shell
python manage.py dbshell

# Check for problems
python manage.py check

# Show installed apps
python manage.py diffsettings

# Test runner
python manage.py test
python manage.py test myapp
python manage.py test myapp.tests.TestMyModel
```

**Custom Management Commands:**
```python
# myapp/management/commands/my_command.py
from django.core.management.base import BaseCommand
from myapp.models import Article

class Command(BaseCommand):
    help = 'Updates article statistics'
    
    def add_arguments(self, parser):
        parser.add_argument('--days', type=int, default=30)
        parser.add_argument('--verbose', action='store_true')
    
    def handle(self, *args, **options):
        days = options['days']
        verbose = options['verbose']
        
        # Your command logic here
        articles = Article.objects.filter(created_at__gte=timezone.now() - timedelta(days=days))
        
        if verbose:
            self.stdout.write(f"Processing {articles.count()} articles")
        
        for article in articles:
            # Update statistics
            pass
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully updated {articles.count()} articles')
        )

# Usage: python manage.py my_command --days=7 --verbose
```

### 33. What is Jinja templating?

Jinja2 is a modern templating engine for Python that can be used with Django as an alternative to Django's built-in template system.

**Installation and Setup:**
```bash
pip install Jinja2
```

```python
# settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(BASE_DIR, 'jinja2')],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'myproject.jinja2.environment',
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

**Jinja2 Environment Setup:**
```python
# myproject/jinja2.py
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment

def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    return env
```

**Template Syntax Comparison:**

| Feature | Django Templates | Jinja2 |
|---------|-----------------|--------|
| **Variables** | `{{ variable }}` | `{{ variable }}` |
| **Filters** | `{{ variable\|filter }}` | `{{ variable\|filter }}` |
| **If Statement** | `{% if condition %}` | `{% if condition %}` |
| **For Loop** | `{% for item in items %}` | `{% for item in items %}` |
| **Comments** | `{# comment #}` | `{# comment #}` |
| **Template Inheritance** | `{% extends "base.html" %}` | `{% extends "base.html" %}` |

**Jinja2 Template Example:**
```html
<!-- article_list.html -->
{% extends "base.html" %}

{% block title %}Articles{% endblock %}

{% block content %}
    <h1>Article List</h1>
    
    {% if articles %}
        {% for article in articles %}
            <div class="article">
                <h2>{{ article.title }}</h2>
                <p>{{ article.content[:100] }}...</p>
                <p>By {{ article.author.username }} on {{ article.created_at.strftime('%Y-%m-%d') }}</p>
                
                {# Jinja2 allows more Python-like expressions #}
                {% if loop.index % 2 == 0 %}
                    <p class="even-article">Even article</p>
                {% endif %}
            </div>
        {% endfor %}
    {% else %}
        <p>No articles found.</p>
    {% endif %}
{% endblock %}
```

**Jinja2 Advantages:**
- More Python-like syntax
- Better performance
- More powerful expressions
- Rich set of built-in filters and functions
- Better error messages

**Django Template Advantages:**
- Integrated with Django ecosystem
- Automatic escaping
- Built-in Django-specific tags
- Better integration with forms and CSRF

### 34. Explain Django Architecture?

Django follows the **MVT (Model-View-Template)** architectural pattern, which is a variation of the traditional MVC pattern.

**Architecture Components:**

**1. Models (Data Layer):**
```python
# models.py
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
```

**2. Views (Logic Layer):**
```python
# views.py
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/list.html', {'articles': articles})
```

**3. Templates (Presentation Layer):**
```html
<!-- templates/articles/list.html -->
<h1>Articles</h1>
{% for article in articles %}
    <div>
        <h2>{{ article.title }}</h2>
        <p>{{ article.content }}</p>
    </div>
{% endfor %}
```

**4. URLs (Routing Layer):**
```python
# urls.py
urlpatterns = [
    path('articles/', views.article_list, name='article_list'),
]
```

**Request-Response Flow:**

```
1. User Request
   ↓
2. URL Dispatcher (urls.py)
   ↓
3. View Function/Class (views.py)
   ↓
4. Model Interaction (models.py) ← → Database
   ↓
5. Template Rendering (templates/)
   ↓
6. HTTP Response
   ↓
7. User Browser
```

**Detailed Flow:**
1. **HTTP Request**: User sends request to Django application
2. **URL Resolution**: Django's URL dispatcher matches the URL to a view
3. **Middleware Processing**: Request passes through middleware layers
4. **View Execution**: View function/class is executed
5. **Model Interaction**: View interacts with models to get/set data
6. **Database Operations**: ORM translates to SQL queries
7. **Template Rendering**: View renders template with context data
8. **Middleware Processing**: Response passes through middleware
9. **HTTP Response**: Final response sent to user

**Django's Layered Architecture:**

```
┌─────────────────────────────────────────┐
│            Web Server (nginx/Apache)    │
├─────────────────────────────────────────┤
│            WSGI Server (gunicorn)       │
├─────────────────────────────────────────┤
│                Django                   │
│  ┌─────────────────────────────────┐   │
│  │         Middleware              │   │
│  ├─────────────────────────────────┤   │
│  │         URL Dispatcher          │   │
│  ├─────────────────────────────────┤   │
│  │            Views                │   │
│  ├─────────────────────────────────┤   │
│  │           Models                │   │
│  ├─────────────────────────────────┤   │
│  │          Templates              │   │
│  └─────────────────────────────────┘   │
├─────────────────────────────────────────┤
│              Database                   │
└─────────────────────────────────────────┘
```

### 35. What are different model inheritance styles in the Django?

Django provides three types of model inheritance:

**1. Abstract Base Classes:**
Used when you want to put common information into multiple models but don't want the base class to be a database table.

```python
# Abstract base class
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True  # This makes it abstract

# Inheriting models
class Article(BaseModel):
    title = models.CharField(max_length=200)
    content = models.TextField()

class Product(BaseModel):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

# No BaseModel table is created
# Article and Product tables include all BaseModel fields
```

**2. Multi-table Inheritance:**
Each model has its own database table, with automatic OneToOne links.

```python
# Base model (creates a table)
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

# Inherited models (each creates its own table)
class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

class Gas_Station(Place):
    number_of_pumps = models.IntegerField()

# Usage
place = Place.objects.create(name="Joe's Cafe", address="123 Main St")
restaurant = Restaurant.objects.create(
    name="Joe's Restaurant", 
    address="123 Main St",
    serves_pizza=True
)

# Accessing parent from child
print(restaurant.name)  # "Joe's Restaurant"

# Accessing child from parent
print(place.restaurant.serves_pizza)  # True (if place is a restaurant)
```

**3. Proxy Models:**
Used when you want to change the Python behavior of a model without changing the database schema.

```python
# Original model
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()

# Proxy model (same table, different behavior)
class Student(Person):
    class Meta:
        proxy = True
        ordering = ['last_name']
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def is_adult(self):
        from datetime import date
        today = date.today()
        return today.year - self.birth_date.year >= 18

# Another proxy model
class Teacher(Person):
    class Meta:
        proxy = True
    
    def get_title(self):
        return f"Prof. {self.last_name}"

# Usage - all use the same database table
person = Person.objects.create(first_name="John", last_name="Doe", birth_date="1990-01-01")
student = Student.objects.get(pk=person.pk)
teacher = Teacher.objects.get(pk=person.pk)

print(student.get_full_name())  # "John Doe"
print(teacher.get_title())      # "Prof. Doe"
```

**Comparison:**

| Type | Database Tables | Use Case | Parent Access |
|------|----------------|----------|---------------|
| **Abstract** | Child tables only | Share common fields | No |
| **Multi-table** | Parent + Child tables | Each model needs table | Yes |
| **Proxy** | Original table only | Different behavior | Yes |

**When to Use:**
- **Abstract**: When you need common fields across models
- **Multi-table**: When you need to query both parent and child
- **Proxy**: When you need different managers or methods

### 36. What's the use of Middleware in Django?

Middleware is a framework of hooks into Django's request/response processing. It's a light, low-level plugin system for globally altering Django's input or output.

**Middleware Order:**
```python
# settings.py
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

**Built-in Middleware:**

**1. SecurityMiddleware:**
```python
# Provides several security enhancements
# - HTTPS redirect
# - Security headers (HSTS, etc.)
# - Content type sniffing protection
```

**2. SessionMiddleware:**
```python
# Enables session support
# Must be before AuthenticationMiddleware
```

**3. AuthenticationMiddleware:**
```python
# Adds user attribute to request
# request.user is available in views
```

**4. CsrfViewMiddleware:**
```python
# Protects against Cross Site Request Forgeries
# Validates CSRF tokens on POST requests
```

**Custom Middleware:**
```python
# middleware.py
import time
from django.utils.deprecation import MiddlewareMixin

class TimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        
        response = self.get_response(request)
        
        duration = time.time() - start_time
        response['X-Response-Time'] = str(duration)
        
        return response

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code executed before view
        print(f"Request: {request.method} {request.path}")
        
        response = self.get_response(request)
        
        # Code executed after view
        print(f"Response: {response.status_code}")
        
        return response

    def process_exception(self, request, exception):
        # Called when view raises exception
        print(f"Exception: {exception}")
        return None

# Old-style middleware (still supported)
class OldStyleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Called before view
        pass
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        # Called before view execution
        pass
    
    def process_response(self, request, response):
        # Called after view
        return response
    
    def process_exception(self, request, exception):
        # Called when view raises exception
        pass
```

**Middleware Hooks:**
- `process_request()`: Called before view
- `process_view()`: Called before view execution
- `process_response()`: Called after view
- `process_exception()`: Called when view raises exception

**Adding Custom Middleware:**
```python
# settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'myapp.middleware.TimingMiddleware',
    'myapp.middleware.RequestLoggingMiddleware',
    # ... other middleware
]
```

### 37. What is context in the Django?

Context in Django refers to the data passed from views to templates. It's a dictionary-like object that contains variables accessible in templates.

**Basic Context:**
```python
# views.py
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    
    # Context dictionary
    context = {
        'article': article,
        'title': article.title,
        'comments': article.comments.all()[:5],
        'current_time': timezone.now(),
    }
    
    return render(request, 'blog/article_detail.html', context)
```

**Template Usage:**
```html
<!-- article_detail.html -->
<h1>{{ title }}</h1>
<article>
    <h2>{{ article.title }}</h2>
    <p>{{ article.content }}</p>
    <p>Published: {{ article.created_at }}</p>
    <p>Current time: {{ current_time }}</p>
</article>

<div class="comments">
    {% for comment in comments %}
        <p>{{ comment.content }}</p>
    {% endfor %}
</div>
```

**Context Processors:**
Context processors are functions that add variables to every template context automatically.

```python
# context_processors.py
from django.conf import settings

def site_settings(request):
    return {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_URL': settings.SITE_URL,
        'DEBUG': settings.DEBUG,
    }

def user_data(request):
    if request.user.is_authenticated:
        return {
            'user_profile': request.user.profile,
            'unread_messages': request.user.messages.filter(is_read=False).count(),
        }
    return {}
```

**Register Context Processors:**
```python
# settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'myapp.context_processors.site_settings',  # Custom
                'myapp.context_processors.user_data',      # Custom
            ],
        },
    },
]
```

**Built-in Context Processors:**
- `django.template.context_processors.debug`: Adds `debug` and `sql_queries`
- `django.template.context_processors.request`: Adds `request` object
- `django.contrib.auth.context_processors.auth`: Adds `user` and `perms`
- `django.contrib.messages.context_processors.messages`: Adds `messages`

**RequestContext:**
```python
from django.template import RequestContext
from django.template.loader import get_template

def my_view(request):
    template = get_template('my_template.html')
    context = RequestContext(request, {
        'my_variable': 'my_value',
    })
    return HttpResponse(template.render(context))
```

**Context in Class-Based Views:**
```python
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()[:5]
        context['related_articles'] = Article.objects.filter(
            category=self.object.category
        ).exclude(pk=self.object.pk)[:3]
        return context
```

### 38. What's the significance of the settings.py file?

The `settings.py` file is the central configuration file for a Django project. It contains all the settings and configuration options that control how Django behaves.

**Key Settings Categories:**

**1. Database Configuration:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

**2. Installed Apps:**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'rest_framework',
    'django_extensions',
    
    # Local apps
    'blog',
    'users',
    'shop',
]
```

**3. Middleware:**
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

**4. Templates:**
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

**5. Static and Media Files:**
```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

**6. Security Settings:**
```python
SECRET_KEY = 'your-secret-key-here'
DEBUG = False  # Set to False in production
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Security enhancements
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

**7. Internationalization:**
```python
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('en', 'English'),
    ('es', 'Spanish'),
    ('fr', 'French'),
]
```

**8. Authentication:**
```python
AUTH_USER_MODEL = 'users.CustomUser'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
```

**Environment-Specific Settings:**
```python
# settings/base.py - Common settings
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRET_KEY = os.environ.get('SECRET_KEY')

# settings/development.py
from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# settings/production.py
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']

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
```

**Custom Settings:**
```python
# Custom application settings
SITE_NAME = "My Awesome Site"
SITE_URL = "https://mysite.com"
CONTACT_EMAIL = "admin@mysite.com"

# Third-party app settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-password'
```

### 39. What's the use of a session framework?

Django's session framework allows you to store and retrieve data on a per-site-visitor basis. It stores data on the server side and abstracts the sending and receiving of cookies.

**Session Configuration:**
```python
# settings.py
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Default
SESSION_COOKIE_AGE = 1209600  # 2 weeks in seconds
SESSION_COOKIE_NAME = 'sessionid'
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_SAVE_EVERY_REQUEST = False
SESSION_COOKIE_SECURE = True  # Only over HTTPS
SESSION_COOKIE_HTTPONLY = True  # Not accessible via JavaScript
SESSION_COOKIE_SAMESITE = 'Lax'  # CSRF protection
```

**Session Backends:**
```python
# Database sessions (default)
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# Cache sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

# File-based sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_FILE_PATH = '/tmp/django_sessions'

# Cookie-based sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

# Cached database sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
```

**Using Sessions in Views:**
```python
# Setting session data
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user:
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            request.session['last_login'] = str(timezone.now())
            request.session.set_expiry(300)  # Expire in 5 minutes
            
            return redirect('dashboard')
    
    return render(request, 'login.html')

# Getting session data
def dashboard_view(request):
    user_id = request.session.get('user_id')
    username = request.session.get('username', 'Guest')
    last_login = request.session.get('last_login')
    
    if not user_id:
        return redirect('login')
    
    context = {
        'username': username,
        'last_login': last_login,
    }
    return render(request, 'dashboard.html', context)

# Shopping cart example
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    
    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1
    
    request.session['cart'] = cart
    request.session.modified = True
    
    return JsonResponse({'success': True, 'cart_count': sum(cart.values())})

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': product.price * quantity
        })
    
    return render(request, 'cart.html', {'cart_items': cart_items})

# Session manipulation
def session_management(request):
    # Check if key exists
    if 'key' in request.session:
        value = request.session['key']
    
    # Get with default
    value = request.session.get('key', 'default_value')
    
    # Set session data
    request.session['key'] = 'value'
    
    # Delete session key
    del request.session['key']
    
    # Clear all session data
    request.session.flush()
    
    # Set session expiry
    request.session.set_expiry(300)  # 5 minutes
    request.session.set_expiry(0)    # Expire at browser close
    
    # Cycle session key (security)
    request.session.cycle_key()
    
    # Get session key
    session_key = request.session.session_key
    
    # Check if session is empty
    if request.session.is_empty():
        pass
```

**Session in Templates:**
```html
<!-- Templates have access to session -->
{% if request.session.username %}
    <p>Welcome, {{ request.session.username }}!</p>
{% endif %}

<!-- Shopping cart count -->
<span class="cart-count">{{ request.session.cart|length }}</span>
```

**Custom Session Data:**
```python
class SessionMixin:
    def get_session_data(self, key, default=None):
        return self.request.session.get(key, default)
    
    def set_session_data(self, key, value):
        self.request.session[key] = value
        self.request.session.modified = True
    
    def clear_session_data(self, key):
        if key in self.request.session:
            del self.request.session[key]
            self.request.session.modified = True

class ShoppingCartView(SessionMixin, View):
    def post(self, request):
        cart = self.get_session_data('cart', {})
        product_id = request.POST.get('product_id')
        
        cart[product_id] = cart.get(product_id, 0) + 1
        self.set_session_data('cart', cart)
        
        return JsonResponse({'success': True})
```

**Session Security:**
```python
# Middleware to track session changes
class SessionSecurityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Check for suspicious activity
        if 'last_ip' in request.session:
            if request.session['last_ip'] != request.META.get('REMOTE_ADDR'):
                # IP changed, possible session hijacking
                request.session.flush()
        
        request.session['last_ip'] = request.META.get('REMOTE_ADDR')
        
        response = self.get_response(request)
        return response
```

### 40. What are Django Signals?

Django signals are a dispatch mechanism that allows decoupled applications to get notified when certain actions occur. They implement the observer pattern.

**Built-in Signals:**

**Model Signals:**
```python
from django.db.models.signals import (
    pre_save, post_save, pre_delete, post_delete,
    m2m_changed, pre_migrate, post_migrate
)
from django.dispatch import receiver
from django.contrib.auth.models import User

# post_save signal
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()

# pre_delete signal
@receiver(pre_delete, sender=Article)
def backup_article(sender, instance, **kwargs):
    # Backup article before deletion
    ArticleBackup.objects.create(
        title=instance.title,
        content=instance.content,
        original_id=instance.id
    )

# m2m_changed signal
@receiver(m2m_changed, sender=Article.tags.through)
def article_tags_changed(sender, instance, action, pk_set, **kwargs):
    if action == 'post_add':
        # Tags were added
        for tag_id in pk_set:
            tag = Tag.objects.get(pk=tag_id)
            print(f"Tag '{tag.name}' added to article '{instance.title}'")
    elif action == 'post_remove':
        # Tags were removed
        print(f"Tags removed from article '{instance.title}'")
```

**Request/Response Signals:**
```python
from django.core.signals import request_started, request_finished
from django.contrib.auth.signals import user_logged_in, user_logged_out

@receiver(request_started)
def request_started_handler(sender, environ, **kwargs):
    print("Request started")

@receiver(request_finished)
def request_finished_handler(sender, **kwargs):
    print("Request finished")

@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    # Log user login
    LoginLog.objects.create(
        user=user,
        ip_address=request.META.get('REMOTE_ADDR'),
        user_agent=request.META.get('HTTP_USER_AGENT')
    )

@receiver(user_logged_out)
def user_logged_out_handler(sender, request, user, **kwargs):
    # Log user logout
    if user:
        LogoutLog.objects.create(
            user=user,
            ip_address=request.META.get('REMOTE_ADDR')
        )
```

**Custom Signals:**
```python
# signals.py
import django.dispatch

# Define custom signals
article_published = django.dispatch.Signal()
user_upgraded = django.dispatch.Signal()

# models.py
class Article(models.Model):
    title = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)
    
    def publish(self):
        self.is_published = True
        self.save()
        
        # Send custom signal
        article_published.send(
            sender=self.__class__,
            article=self,
            published_by=self.author
        )

# handlers.py
@receiver(article_published)
def notify_subscribers(sender, article, published_by, **kwargs):
    # Send notifications to subscribers
    subscribers = Subscription.objects.filter(category=article.category)
    for subscription in subscribers:
        send_notification_email(subscription.user, article)

@receiver(article_published)
def update_search_index(sender, article, **kwargs):
    # Update search index
    search_index.add_document(article)

@receiver(article_published)
def social_media_post(sender, article, **kwargs):
    # Post to social media
    post_to_twitter(article)
    post_to_facebook(article)
```

**Signal Registration:**
```python
# Method 1: Using decorator
@receiver(post_save, sender=User)
def my_handler(sender, **kwargs):
    pass

# Method 2: Using connect method
def my_handler(sender, **kwargs):
    pass

post_save.connect(my_handler, sender=User)

# Method 3: In apps.py
class MyAppConfig(AppConfig):
    name = 'myapp'
    
    def ready(self):
        import myapp.signals  # Import signal handlers
```

**Signal Best Practices:**
```python
# Use weak references to prevent memory leaks
@receiver(post_save, sender=User, weak=False)  # Keep strong reference
def my_handler(sender, **kwargs):
    pass

# Handle exceptions in signal handlers
@receiver(post_save, sender=Article)
def send_notification(sender, instance, created, **kwargs):
    if created:
        try:
            send_email_notification(instance)
        except Exception as e:
            logger.error(f"Failed to send notification: {e}")

# Use dispatch_uid to prevent duplicate connections
@receiver(post_save, sender=User, dispatch_uid="create_user_profile")
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# Conditional signal handling
@receiver(post_save, sender=Article)
def handle_article_save(sender, instance, created, **kwargs):
    if created and instance.is_published:
        # Only handle published articles
        notify_subscribers(instance)
```

**Disconnecting Signals:**
```python
# Disconnect signal
post_save.disconnect(my_handler, sender=User)

# Temporarily disconnect in tests
class MyTestCase(TestCase):
    def setUp(self):
        post_save.disconnect(my_handler, sender=User)
    
    def tearDown(self):
        post_save.connect(my_handler, sender=User)
```

**Real-world Example - E-commerce Order Processing:**
```python
# signals.py
order_placed = django.dispatch.Signal()
payment_completed = django.dispatch.Signal()

# models.py
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ]
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    def mark_as_paid(self):
        self.status = 'paid'
        self.save()
        
        payment_completed.send(
            sender=self.__class__,
            order=self
        )

# handlers.py
@receiver(payment_completed)
def send_confirmation_email(sender, order, **kwargs):
    send_email(
        subject=f'Order #{order.id} Confirmed',
        message=f'Thank you for your order!',
        recipient_list=[order.user.email]
    )

@receiver(payment_completed)
def update_inventory(sender, order, **kwargs):
    for item in order.items.all():
        item.product.quantity -= item.quantity
        item.product.save()

@receiver(payment_completed)
def create_shipping_label(sender, order, **kwargs):
    ShippingLabel.objects.create(
        order=order,
        address=order.shipping_address
    )
```

## Advanced Django Questions

### 41. How can you improve the performance of Django ORM queries?

**1. Use select_related() for ForeignKey relationships:**
```python
# Bad - N+1 queries
articles = Article.objects.all()
for article in articles:
    print(article.author.username)  # Each iteration hits DB

# Good - Single query with JOIN
articles = Article.objects.select_related('author')
for article in articles:
    print(article.author.username)  # No additional DB hits
```

**2. Use prefetch_related() for ManyToMany and reverse ForeignKey:**
```python
# Bad - N+1 queries
articles = Article.objects.all()
for article in articles:
    print(article.tags.all())  # Each iteration hits DB

# Good - Two queries total
articles = Article.objects.prefetch_related('tags')
for article in articles:
    print(article.tags.all())  # Uses prefetched data

# Advanced prefetch
from django.db.models import Prefetch

articles = Article.objects.prefetch_related(
    Prefetch('comments', queryset=Comment.objects.select_related('author'))
)
```

**3. Use only() and defer() to limit fields:**
```python
# Only fetch specific fields
articles = Article.objects.only('title', 'slug', 'created_at')

# Defer heavy fields
articles = Article.objects.defer('content', 'description')

# For related fields
articles = Article.objects.select_related('author').only(
    'title', 'author__username', 'author__email'
)
```

**4. Use values() and values_list() for simple data:**
```python
# Instead of full objects
article_titles = Article.objects.values_list('title', flat=True)

# Multiple fields
article_data = Article.objects.values('id', 'title', 'author__username')

# Dictionary format
for data in article_data:
    print(f"{data['title']} by {data['author__username']}")
```

**5. Database Indexing:**
```python
class Article(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True)  # Automatically indexed
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['created_at', 'is_published']),
            models.Index(fields=['author', '-created_at']),
        ]
```

**6. Use exists() instead of len() or count():**
```python
# Bad
if len(Article.objects.filter(author=user)) > 0:
    pass

# Good
if Article.objects.filter(author=user).exists():
    pass
```

**7. Bulk Operations:**
```python
# Bulk create
articles = [
    Article(title=f'Article {i}', content=f'Content {i}')
    for i in range(1000)
]
Article.objects.bulk_create(articles, batch_size=100)

# Bulk update
Article.objects.filter(is_published=False).update(is_published=True)

# Bulk delete
Article.objects.filter(created_at__lt=old_date).delete()
```

**8. Use Raw SQL when necessary:**
```python
# Complex aggregations
articles = Article.objects.raw("""
    SELECT a.*, COUNT(c.id) as comment_count
    FROM blog_article a
    LEFT JOIN blog_comment c ON a.id = c.article_id
    GROUP BY a.id
    ORDER BY comment_count DESC
""")

# Use extra() for complex WHERE clauses
articles = Article.objects.extra(
    where=["created_at > %s"],
    params=[last_week]
)
```

**9. Query Optimization with annotations:**
```python
from django.db.models import Count, Avg, F, Q

# Annotate with related data
articles = Article.objects.annotate(
    comment_count=Count('comments'),
    avg_rating=Avg('ratings__score'),
    is_popular=Q(views__gt=1000)
).select_related('author')
```

**10. Connection Pooling:**
```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'CONN_MAX_AGE': 600,  # Connection pooling
        'OPTIONS': {
            'MAX_CONNS': 20,
            'MIN_CONNS': 5,
        }
    }
}
```

### 42. What are custom model managers and when would you use them?

Custom model managers allow you to add custom query methods and modify the default QuerySet for a model.

**Basic Custom Manager:**
```python
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)

class Article(models.Model):


# Django Advanced Concepts - Complete Guide

## 42. What are custom model managers and when would you use them?

**Custom Model Managers** are Python classes that define the interface through which database query operations are provided to Django models. Every model gets at least one manager, and by default, Django adds a manager with the name `objects` to every model class.

### When to use Custom Managers:

1. **Add extra manager methods** - Custom query logic
2. **Modify initial QuerySet** - Filter default results
3. **Encapsulate common queries** - Reusable query patterns

### Example Implementation:

```python
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')
    
    def by_author(self, author):
        return self.get_queryset().filter(author=author)

class Post(models.Model):
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    objects = models.Manager()  # Default manager
    published = PublishedManager()  # Custom manager
```

### Use Cases:
- Soft deletes (hiding deleted records)
- Multi-tenancy (filtering by tenant)
- Status-based filtering
- Complex aggregations

## 43. How does Django handle database transactions?

Django provides several mechanisms for handling database transactions, ensuring data consistency and integrity.

### Transaction Handling Mechanisms:

1. **Autocommit Mode** (Default)
   - Each database operation is immediately committed
   - Django wraps each view in a transaction by default

2. **Atomic Transactions**
   ```python
   from django.db import transaction
   
   # Decorator
   @transaction.atomic
   def my_view(request):
       # All database operations in one transaction
       pass
   
   # Context manager
   def my_function():
       with transaction.atomic():
           # Database operations here
           Model.objects.create(...)
   ```

3. **Manual Transaction Control**
   ```python
   from django.db import transaction
   
   def manual_transaction():
       sid = transaction.savepoint()
       try:
           # Database operations
           Model.objects.create(...)
       except Exception:
           transaction.savepoint_rollback(sid)
       else:
           transaction.savepoint_commit(sid)
   ```

### Transaction Isolation Levels:
Django supports different isolation levels depending on the database backend, helping prevent issues like dirty reads, phantom reads, and non-repeatable reads.

## 44. How do you override a save method in a model, and what are the caveats?

Overriding the `save()` method allows custom logic during model saving, but requires careful consideration of several caveats.

### Basic Override:

```python
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    
    def save(self, *args, **kwargs):
        # Custom logic before saving
        if not self.slug:
            self.slug = slugify(self.name)
        
        # Call the parent save method
        super().save(*args, **kwargs)
        
        # Custom logic after saving
        self.send_notification()
```

### Important Caveats:

1. **Always call super().save()** - Skipping this prevents actual database saving
2. **Bulk operations bypass save()** - `bulk_create()`, `update()` don't call save()
3. **Admin interface considerations** - May not trigger your custom logic
4. **Signal implications** - Overridden save affects signal timing
5. **Performance impact** - Additional logic slows down saves
6. **Exception handling** - Wrap risky operations in try-catch blocks

### Advanced Override with Validation:

```python
def save(self, *args, **kwargs):
    # Validation
    self.full_clean()
    
    # Custom logic
    if self._state.adding:  # New instance
        self.created_at = timezone.now()
    else:  # Existing instance
        self.updated_at = timezone.now()
    
    super().save(*args, **kwargs)
```

## 45. What are database routers in Django and how are they used?

**Database Routers** determine which database to use for which model and operation when working with multiple databases in Django.

### Router Structure:

```python
class DatabaseRouter:
    def db_for_read(self, model, **hints):
        """Suggest the database to read from."""
        if model._meta.app_label == 'analytics':
            return 'analytics_db'
        return None
    
    def db_for_write(self, model, **hints):
        """Suggest the database to write to."""
        if model._meta.app_label == 'analytics':
            return 'analytics_db'
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if models are in the same app."""
        db_set = {'default', 'analytics_db'}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that certain apps' models get created on the right DB."""
        if app_label == 'analytics':
            return db == 'analytics_db'
        elif db == 'analytics_db':
            return False
        return db == 'default'
```

### Configuration:
```python
# settings.py
DATABASES = {
    'default': {...},
    'analytics_db': {...},
}

DATABASE_ROUTERS = ['path.to.routers.DatabaseRouter']
```

### Use Cases:
- Separating read/write operations
- App-specific databases
- Legacy database integration
- Geographic data distribution

## 46. What are signals pitfalls and how to avoid them?

Django signals provide decoupled notifications when certain actions occur, but they come with several pitfalls that developers should be aware of.

### Common Pitfalls:

1. **Infinite Loops**
   ```python
   # BAD - Can cause infinite recursion
   @receiver(post_save, sender=MyModel)
   def my_handler(sender, instance, **kwargs):
       instance.save()  # This triggers the signal again!
   
   # GOOD - Use update() or conditional logic
   @receiver(post_save, sender=MyModel)
   def my_handler(sender, instance, **kwargs):
       if not kwargs.get('created'):
           MyModel.objects.filter(pk=instance.pk).update(field='value')
   ```

2. **Performance Issues**
   ```python
   # BAD - Expensive operations in signals
   @receiver(post_save, sender=User)
   def send_welcome_email(sender, instance, created, **kwargs):
       if created:
           send_mail(...)  # Blocking operation
   
   # GOOD - Use background tasks
   @receiver(post_save, sender=User)
   def send_welcome_email(sender, instance, created, **kwargs):
       if created:
           send_welcome_email_task.delay(instance.id)
   ```

3. **Transaction Issues**
   ```python
   # BAD - Signal fires before transaction commit
   @receiver(post_save, sender=Order)
   def process_payment(sender, instance, **kwargs):
       payment_gateway.charge(instance.amount)  # May fail if transaction rolls back
   
   # GOOD - Use on_commit
   @receiver(post_save, sender=Order)
   def process_payment(sender, instance, **kwargs):
       transaction.on_commit(lambda: payment_gateway.charge(instance.amount))
   ```

### Best Practices:
- Keep signal handlers lightweight
- Use `transaction.on_commit()` for external services
- Avoid database operations that might cause loops
- Consider using background tasks for heavy operations
- Test signal behavior thoroughly

## 47. How does Django handle file uploads under the hood?

Django's file upload system involves multiple components working together to securely and efficiently handle file data.

### Upload Process Flow:

1. **HTTP Request Parsing**
   - Django's request handler parses multipart/form-data
   - Files are temporarily stored in memory or on disk

2. **UploadHandler Classes**
   ```python
   # Django uses different handlers based on file size
   FILE_UPLOAD_HANDLERS = [
       'django.core.files.uploadhandler.MemoryFileUploadHandler',
       'django.core.files.uploadhandler.TemporaryFileUploadHandler',
   ]
   ```

3. **File Object Creation**
   ```python
   class MyModel(models.Model):
       file = models.FileField(upload_to='uploads/')
   
   # In view
   def upload_view(request):
       uploaded_file = request.FILES['file']
       # uploaded_file is a UploadedFile instance
   ```

### Storage Backends:

Django abstracts file storage through storage backends:

```python
from django.core.files.storage import default_storage

# Default file system storage
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

# Custom storage (e.g., S3)
class S3Storage(Storage):
    def _save(self, name, content):
        # Save to S3
        pass
    
    def url(self, name):
        # Return S3 URL
        pass
```

### Security Measures:
- File type validation
- Size limits
- Path traversal protection
- Virus scanning integration points

### Configuration Options:
```python
# settings.py
FILE_UPLOAD_MAX_MEMORY_SIZE = 2.5 * 1024 * 1024  # 2.5 MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 2.5 * 1024 * 1024
FILE_UPLOAD_TEMP_DIR = '/tmp'
MEDIA_ROOT = '/path/to/media'
MEDIA_URL = '/media/'
```

## 48. Explain the working of the ContentType framework in Django

The **ContentTypes framework** provides a high-level, generic interface for working with models in your Django application. It allows you to create relationships to "any" model.

### Core Components:

1. **ContentType Model**
   ```python
   from django.contrib.contenttypes.models import ContentType
   
   # Get ContentType for a model
   content_type = ContentType.objects.get_for_model(MyModel)
   
   # Get the model class back
   model_class = content_type.model_class()
   ```

2. **Generic Foreign Keys**
   ```python
   from django.contrib.contenttypes.fields import GenericForeignKey
   from django.contrib.contenttypes.models import ContentType
   
   class Comment(models.Model):
       content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
       object_id = models.PositiveIntegerField()
       content_object = GenericForeignKey('content_type', 'object_id')
       text = models.TextField()
   
   # Usage
   blog_post = BlogPost.objects.get(pk=1)
   comment = Comment.objects.create(
       content_object=blog_post,
       text="Great post!"
   )
   ```

3. **Generic Relations**
   ```python
   from django.contrib.contenttypes.fields import GenericRelation
   
   class BlogPost(models.Model):
       title = models.CharField(max_length=200)
       comments = GenericRelation(Comment)
   
   # Usage
   post = BlogPost.objects.get(pk=1)
   comments = post.comments.all()
   ```

### Use Cases:
- Comments system for multiple models
- Tagging system
- Activity logs
- Permissions framework
- Polymorphic relationships

### Limitations:
- Cannot use foreign key constraints
- Queries can be less efficient
- No referential integrity at database level

## 49. What are some security vulnerabilities Django protects against by default?

Django includes numerous built-in security features that protect against common web vulnerabilities.

### 1. Cross-Site Scripting (XSS)
```python
# Django automatically escapes variables in templates
{{ user_input }}  # Automatically escaped

# Manual escaping when needed
from django.utils.html import escape
safe_content = escape(user_input)
```

### 2. Cross-Site Request Forgery (CSRF)
```python
# CSRF middleware enabled by default
MIDDLEWARE = [
    'django.middleware.csrf.CsrfViewMiddleware',
    # ...
]

# In templates
<form method="post">
    {% csrf_token %}
    <!-- form fields -->
</form>
```

### 3. SQL Injection
```python
# Django ORM automatically parameterizes queries
User.objects.filter(name=user_input)  # Safe

# Raw queries with parameters
User.objects.raw("SELECT * FROM users WHERE name = %s", [user_input])
```

### 4. Clickjacking
```python
# X-Frame-Options middleware
MIDDLEWARE = [
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

X_FRAME_OPTIONS = 'DENY'  # or 'SAMEORIGIN'
```

### 5. Security Headers
```python
# settings.py
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

### 6. Password Security
- Password hashing with PBKDF2 by default
- Password validators
- Session security

### 7. Host Header Validation
```python
ALLOWED_HOSTS = ['example.com', 'www.example.com']
```

## 50. How to implement soft deletes in Django models?

**Soft deletes** mark records as deleted without actually removing them from the database, allowing for data recovery and audit trails.

### Implementation with Custom Manager:

```python
from django.db import models
from django.utils import timezone

class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    objects = SoftDeleteManager()
    all_objects = models.Manager()  # Access to all records including deleted
    
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

# Usage
class Post(SoftDeleteModel):
    title = models.CharField(max_length=200)
    content = models.TextField()

# Using the model
post = Post.objects.create(title="Test")
post.delete()  # Soft delete
Post.objects.all()  # Won't include deleted post
Post.all_objects.all()  # Includes deleted post
post.restore()  # Restore the post
```

### Advanced Implementation with QuerySet:

```python
class SoftDeleteQuerySet(models.QuerySet):
    def delete(self):
        return self.update(deleted_at=timezone.now())
    
    def hard_delete(self):
        return super().delete()
    
    def alive(self):
        return self.filter(deleted_at=None)
    
    def dead(self):
        return self.exclude(deleted_at=None)

class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, using=self._db).alive()
    
    def all_with_deleted(self):
        return SoftDeleteQuerySet(self.model, using=self._db)
    
    def deleted_only(self):
        return SoftDeleteQuerySet(self.model, using=self._db).dead()
```

## 51. How does ModelForm validation work internally?

Django's **ModelForm** validation follows a multi-step process that combines form validation with model validation.

### Validation Flow:

1. **Field Validation** - Individual field cleaning
2. **Form Validation** - Cross-field validation
3. **Model Validation** - Model-level constraints
4. **Database Validation** - Database constraints

### Internal Process:

```python
class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['field1', 'field2']
    
    def clean_field1(self):
        # Individual field validation
        data = self.cleaned_data['field1']
        if some_condition:
            raise forms.ValidationError("Invalid field1")
        return data
    
    def clean(self):
        # Cross-field validation
        cleaned_data = super().clean()
        field1 = cleaned_data.get('field1')
        field2 = cleaned_data.get('field2')
        
        if field1 and field2 and some_condition:
            raise forms.ValidationError("Field1 and Field2 conflict")
        
        return cleaned_data
```

### Validation Steps Internally:

1. **full_clean() method**:
   ```python
   def full_clean(self):
       """
       Clean all of self.data and populate self._errors and self.cleaned_data.
       """
       self._errors = ErrorDict()
       if not self.is_bound:
           return
       
       self.cleaned_data = {}
       self._clean_fields()      # Step 1: Field validation
       self._clean_form()        # Step 2: Form validation
       self._post_clean()        # Step 3: Model validation
   ```

2. **Model Instance Validation**:
   ```python
   def _post_clean(self):
       # Create model instance
       instance = self.instance
       
       # Set field values
       for field_name in self.fields:
           if field_name in self.cleaned_data:
               setattr(instance, field_name, self.cleaned_data[field_name])
       
       # Call model's full_clean()
       try:
           instance.full_clean()
       except ValidationError as e:
           self._update_errors(e)
   ```

### Custom Model Validation:

```python
class MyModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    
    def clean(self):
        # Model-level validation
        if self.field1 == 'invalid' and self.field2 < 10:
            raise ValidationError("Invalid combination of field1 and field2")
    
    def clean_fields(self, exclude=None):
        # Individual field validation at model level
        super().clean_fields(exclude)
        if self.field1 and len(self.field1) < 3:
            raise ValidationError({'field1': 'Too short'})
```

## 52. How can you implement a throttling mechanism in Django (or DRF)?

Throttling prevents abuse by limiting the rate of requests from clients. Both Django and Django REST Framework provide mechanisms for implementing throttling.

### DRF Built-in Throttling:

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/hour',
        'user': '1000/hour',
        'login': '5/min',
    }
}

# In views
from rest_framework.throttling import UserRateThrottle

class MyAPIView(APIView):
    throttle_classes = [UserRateThrottle]
    throttle_scope = 'user'
    
    def get(self, request):
        return Response({'message': 'Hello'})
```

### Custom Throttle Class:

```python
from rest_framework.throttling import BaseThrottle
from django.core.cache import cache
from django.utils import timezone

class CustomThrottle(BaseThrottle):
    def allow_request(self, request, view):
        # Get client identifier
        ident = self.get_ident(request)
        
        # Check cache for request count
        key = f'throttle_{ident}'
        request_count = cache.get(key, 0)
        
        if request_count >= 100:  # Max 100 requests
            return False
        
        # Increment counter
        cache.set(key, request_count + 1, timeout=3600)  # 1 hour
        return True
    
    def wait(self):
        return 3600  # Wait time in seconds
```

### Django Middleware Throttling:

```python
class ThrottleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        client_ip = self.get_client_ip(request)
        key = f'throttle_{client_ip}'
        
        request_count = cache.get(key, 0)
        if request_count >= 100:
            return HttpResponse('Rate limit exceeded', status=429)
        
        cache.set(key, request_count + 1, timeout=3600)
        return self.get_response(request)
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
```

### Advanced Rate Limiting with Redis:

```python
import redis
import time

class RedisThrottle(BaseThrottle):
    def __init__(self):
        self.redis_client = redis.Redis(host='localhost', port=6379, db=0)
    
    def allow_request(self, request, view):
        ident = self.get_ident(request)
        key = f'throttle:{ident}'
        
        # Sliding window approach
        now = time.time()
        window = 3600  # 1 hour window
        
        # Remove old entries
        self.redis_client.zremrangebyscore(key, 0, now - window)
        
        # Count current requests
        current_requests = self.redis_client.zcard(key)
        
        if current_requests >= 100:  # Limit
            return False
        
        # Add current request
        self.redis_client.zadd(key, {str(now): now})
        self.redis_client.expire(key, window)
        
        return True
```

## 53. Explain how DRF's ViewSet and Router work together

**ViewSets** and **Routers** in Django REST Framework work together to provide a powerful and conventional way to organize API views and URL patterns.

### ViewSet Basics:

```python
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Custom action
    @action(detail=True, methods=['post'])
    def set_favorite(self, request, pk=None):
        book = self.get_object()
        # Logic to set favorite
        return Response({'status': 'favorite set'})
    
    @action(detail=False)
    def recent_books(self, request):
        recent = Book.objects.filter(created_at__gte=timezone.now() - timedelta(days=7))
        serializer = self.get_serializer(recent, many=True)
        return Response(serializer.data)
```

### Router Configuration:

```python
from rest_framework.routers import DefaultRouter
from django.urls import path, include

# Create router
router = DefaultRouter()
router.register(r'books', BookViewSet)

# URL patterns
urlpatterns = [
    path('api/', include(router.urls)),
]
```

### Generated URL Patterns:

The router automatically generates these URL patterns:
- `GET /api/books/` - List books
- `POST /api/books/` - Create book
- `GET /api/books/{id}/` - Retrieve book
- `PUT /api/books/{id}/` - Update book
- `PATCH /api/books/{id}/` - Partial update
- `DELETE /api/books/{id}/` - Delete book
- `POST /api/books/{id}/set_favorite/` - Custom action
- `GET /api/books/recent_books/` - Custom list action

### ViewSet Types:

1. **ModelViewSet** - Full CRUD operations
2. **ReadOnlyModelViewSet** - Only read operations
3. **ViewSet** - Custom viewset with manual action methods

```python
class CustomViewSet(viewsets.ViewSet):
    def list(self, request):
        # Custom list logic
        return Response([])
    
    def create(self, request):
        # Custom create logic
        return Response({})
    
    def retrieve(self, request, pk=None):
        # Custom retrieve logic
        return Response({})
```

### Custom Router:

```python
class CustomRouter(DefaultRouter):
    def get_urls(self):
        urls = super().get_urls()
        # Add custom URL patterns
        custom_urls = [
            # Custom patterns
        ]
        return urls + custom_urls
```

### Advanced Usage:

```python
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get_serializer_class(self):
        # Different serializers for different actions
        if self.action == 'create':
            return BookCreateSerializer
        elif self.action == 'list':
            return BookListSerializer
        return BookDetailSerializer
    
    def get_permissions(self):
        # Different permissions for different actions
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
```

## 54. How do you write a custom pagination class in Django REST Framework?

Custom pagination classes in DRF allow you to control how large datasets are divided into discrete pages and how pagination metadata is presented.

### Basic Custom Pagination:

```python
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100
    
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'page_size': self.page_size,
            'results': data
        })
```

### Cursor-Based Pagination:

```python
from rest_framework.pagination import CursorPagination

class CustomCursorPagination(CursorPagination):
    page_size = 20
    ordering = '-created_at'
    cursor_query_param = 'cursor'
    page_size_query_param = 'page_size'
    
    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })
```

### Custom Pagination from Scratch:

```python
from rest_framework.pagination import BasePagination
from rest_framework.response import Response
from django.core.paginator import Paginator
from collections import OrderedDict

class CustomPagination(BasePagination):
    page_size = 25
    
    def paginate_queryset(self, queryset, request, view=None):
        page_size = self.get_page_size(request)
        if not page_size:
            return None
        
        paginator = Paginator(queryset, page_size)
        page_number = request.query_params.get('page', 1)
        
        try:
            page_number = int(page_number)
        except ValueError:
            page_number = 1
        
        try:
            self.page = paginator.page(page_number)
        except:
            self.page = paginator.page(1)
        
        return list(self.page)
    
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('page_info', {
                'current_page': self.page.number,
                'total_pages': self.page.paginator.num_pages,
                'has_next': self.page.has_next(),
                'has_previous': self.page.has_previous(),
                'start_index': self.page.start_index(),
                'end_index': self.page.end_index(),
            }),
            ('results', data)
        ]))
    
    def get_page_size(self, request):
        if hasattr(self, 'page_size_query_param'):
            try:
                return int(request.query_params[self.page_size_query_param])
            except (KeyError, ValueError):
                pass
        return self.page_size
```

### Offset-Based Pagination:

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

### Usage in Views:

```python
class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = CustomPageNumberPagination

# Or globally in settings
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'myapp.pagination.CustomPageNumberPagination',
    'PAGE_SIZE': 20
}
```

## 55. What is the difference between APIView and GenericAPIView in DRF?

**APIView** and **GenericAPIView** are base classes in Django REST Framework that provide different levels of functionality for building API views.

### APIView - Basic Foundation:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BookAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            # Get single book
            try:
                book = Book.objects.get(pk=pk)
                serializer = BookSerializer(book)
                return Response(serializer.data)
            except Book.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            # Get all books
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
```

### GenericAPIView - Enhanced with Common Patterns:

```python
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

class BookGenericAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```

### Key Differences:

| Feature | APIView | GenericAPIView |
|---------|---------|----------------|
| **Queryset** | Manual handling | Built-in `get_queryset()` method |
| **Serializer** | Manual instantiation | Built-in `get_serializer()` method |
| **Object Retrieval** | Manual `get()` calls | Built-in `get_object()` method |
| **Permissions** | Manual implementation | Built-in permission handling |
| **Filtering** | Manual implementation | Built-in filter backends |
| **Pagination** | Manual implementation | Built-in pagination support |

### GenericAPIView Advanced Features:

```python
class BookGenericAPIView(GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'  # Instead of 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'author']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'title']
    
    def get_queryset(self):
        """Override to customize queryset based on user"""
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(is_published=True)
        return queryset
    
    def get_serializer_class(self):
        """Different serializers for different actions"""
        if self.request.method == 'POST':
            return BookCreateSerializer
        return BookSerializer
    
    def get_object(self):
        """Custom object retrieval with additional checks"""
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj
```

### Using Built-in Generic Views:

```python
from rest_framework.generics import (
    ListCreateAPIView, 
    RetrieveUpdateDestroyAPIView
)

# List and Create in one view
class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Retrieve, Update, Delete in one view
class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

## 56. How do you implement permissions per object in DRF?

Object-level permissions in DRF allow you to control access to individual model instances based on custom logic.

### Custom Object Permission:

```python
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    
    def has_object_permission(self, request, view, obj):
        # Read permissions for any request (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions only for owner
        return obj.owner == request.user

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Permission for blog posts - only author can edit
    """
    
    def has_permission(self, request, view):
        # View-level permission check
        return request.user.is_authenticated or request.method in permissions.SAFE_METHODS
    
    def has_object_permission(self, request, view, obj):
        # Object-level permission check
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
```

### Using Object Permissions in Views:

```python
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]

class CommentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
```

### Complex Object Permissions:

```python
class ProjectPermission(permissions.BasePermission):
    """
    Complex permission system for project management
    """
    
    def has_object_permission(self, request, view, obj):
        # Project owner has full access
        if obj.owner == request.user:
            return True
        
        # Check team membership
        try:
            membership = obj.team_members.get(user=request.user)
        except ProjectMember.DoesNotExist:
            return False
        
        # Different permissions based on role
        if request.method in permissions.SAFE_METHODS:
            # All team members can read
            return True
        elif request.method in ['PUT', 'PATCH']:
            # Only editors and admins can update
            return membership.role in ['editor', 'admin']
        elif request.method == 'DELETE':
            # Only admins can delete
            return membership.role == 'admin'
        
        return False

class ConditionalPermission(permissions.BasePermission):
    """
    Permission that changes based on object state
    """
    
    def has_object_permission(self, request, view, obj):
        # Published articles are read-only for non-owners
        if obj.status == 'published':
            if request.method in permissions.SAFE_METHODS:
                return True
            return obj.author == request.user
        
        # Draft articles only accessible by author
        return obj.author == request.user
```

### Permission with External Services:

```python
class SubscriptionPermission(permissions.BasePermission):
    """
    Permission based on user subscription status
    """
    
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        # Check subscription status
        return request.user.subscription.is_active
    
    def has_object_permission(self, request, view, obj):
        # Premium content requires premium subscription
        if obj.is_premium:
            return request.user.subscription.tier == 'premium'
        return True
```

### Dynamic Permissions:

```python
class DynamicPermission(permissions.BasePermission):
    """
    Permission that can be configured per view
    """
    
    def __init__(self, allowed_roles=None):
        self.allowed_roles = allowed_roles or []
    
    def has_object_permission(self, request, view, obj):
        if not hasattr(obj, 'get_user_role'):
            return False
        
        user_role = obj.get_user_role(request.user)
        return user_role in self.allowed_roles

# Usage in view
class DocumentView(RetrieveUpdateAPIView):
    permission_classes = [DynamicPermission(['owner', 'editor'])]
```

### Permissions with Caching:

```python
from django.core.cache import cache

class CachedPermission(permissions.BasePermission):
    """
    Permission with caching for expensive checks
    """
    
    def has_object_permission(self, request, view, obj):
        cache_key = f'permission_{request.user.id}_{obj.id}_{request.method}'
        
        # Check cache first
        cached_result = cache.get(cache_key)
        if cached_result is not None:
            return cached_result
        
        # Expensive permission check
        result = self._check_permission(request, obj)
        
        # Cache for 5 minutes
        cache.set(cache_key, result, 300)
        return result
    
    def _check_permission(self, request, obj):
        # Complex permission logic here
        return True
```

## 57. What is the difference between authentication and authorization in Django?

**Authentication** and **Authorization** are two distinct but related security concepts in Django that work together to secure your application.

### Authentication - "Who are you?"

Authentication verifies the identity of a user. It answers the question "Who is this user?"

```python
# Authentication backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default
    'myapp.backends.EmailBackend',  # Custom
]

# Custom authentication backend
class EmailBackend:
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
```

### DRF Authentication Classes:

```python
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication,
    BasicAuthentication
)

class CustomTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'  # Use 'Bearer' instead of 'Token'
    
    def authenticate_credentials(self, key):
        # Custom token validation logic
        user, token = super().authenticate_credentials(key)
        
        # Additional checks
        if not user.is_active:
            raise AuthenticationFailed('User inactive')
        
        return (user, token)

# JWT Authentication
from rest_framework_simplejwt.authentication import JWTAuthentication

class CustomJWTAuthentication(JWTAuthentication):
    def get_validated_token(self, raw_token):
        # Custom JWT validation
        validated_token = super().get_validated_token(raw_token)
        
        # Additional token checks
        if validated_token.payload.get('custom_claim') != 'expected_value':
            raise InvalidToken('Invalid custom claim')
        
        return validated_token
```

### Authorization - "What can you do?"

Authorization determines what an authenticated user is allowed to do. It answers "What permissions does this user have?"

### Django Permissions System:

```python
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# Built-in permissions (automatically created)
# - add_<modelname>
# - change_<modelname>
# - delete_<modelname>
# - view_<modelname>

# Custom permissions in model
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    class Meta:
        permissions = [
            ("can_publish", "Can publish article"),
            ("can_feature", "Can feature article"),
        ]

# Checking permissions
from django.contrib.auth.decorators import permission_required

@permission_required('myapp.can_publish')
def publish_article(request, article_id):
    # Only users with 'can_publish' permission can access
    pass

# In views
def my_view(request):
    if request.user.has_perm('myapp.can_publish'):
        # User has permission
        pass
```

### DRF Authorization (Permissions):

```python
from rest_framework.permissions import BasePermission

class CanPublishPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('myapp.can_publish')
    
    def has_object_permission(self, request, view, obj):
        # Object-level permission check
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

# Group-based permissions
class EditorPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='editors').exists()

# Role-based permissions
class RoleBasedPermission(BasePermission):
    required_roles = []
    
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        user_roles = request.user.profile.roles.values_list('name', flat=True)
        return any(role in self.required_roles for role in user_roles)
```

### Complete Authentication + Authorization Flow:

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

# View with both authentication and authorization
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, CanPublishPermission]
    
    def get_permissions(self):
        """Different permissions for different actions"""
        if self.action == 'create':
            permission_classes = [IsAuthenticated, CanPublishPermission]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        else:
            permission_classes = [AllowAny]
        
        return [permission() for permission in permission_classes]
```

### Custom User Model with Roles:

```python
class CustomUser(AbstractUser):
    role = models.CharField(max_length=20, choices=[
        ('admin', 'Admin'),
        ('editor', 'Editor'),
        ('viewer', 'Viewer'),
    ])
    
    def has_role(self, role):
        return self.role == role
    
    def can_edit_article(self, article):
        if self.role == 'admin':
            return True
        elif self.role == 'editor':
            return article.author == self
        return False

# Usage in views
class ArticleUpdateView(UpdateAPIView):
    def get_object(self):
        article = super().get_object()
        if not self.request.user.can_edit_article(article):
            raise PermissionDenied("You don't have permission to edit this article")
        return article
```

### Key Differences Summary:

| Aspect | Authentication | Authorization |
|--------|----------------|---------------|
| **Purpose** | Verify identity | Control access |
| **Question** | "Who are you?" | "What can you do?" |
| **Process** | Login/Token validation | Permission checking |
| **Timing** | Before authorization | After authentication |
| **Failure** | 401 Unauthorized | 403 Forbidden |
| **Django Classes** | Authentication backends | Permission classes |
| **DRF Classes** | Authentication classes | Permission classes |

## 58. How can you handle nested serializers in DRF?

Nested serializers in DRF allow you to represent related objects within a single serialized response and handle complex data structures.

### Basic Nested Serializers:

```python
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)  # Nested serializer
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_date']

# This produces:
# {
#     "id": 1,
#     "title": "Django Book",
#     "author": {
#         "id": 1,
#         "name": "John Doe",
#         "email": "john@example.com"
#     },
#     "publication_date": "2023-01-01"
# }
```

### Writable Nested Serializers:

```python
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_date']
    
    def create(self, validated_data):
        author_data = validated_data.pop('author')
        
        # Create or get author
        author, created = Author.objects.get_or_create(
            email=author_data['email'],
            defaults=author_data
        )
        
        # Create book with author
        book = Book.objects.create(author=author, **validated_data)
        return book
    
    def update(self, instance, validated_data):
        author_data = validated_data.pop('author', None)
        
        # Update book fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        # Update author if provided
        if author_data:
            for attr, value in author_data.items():
                setattr(instance.author, attr, value)
            instance.author.save()
        
        instance.save()
        return instance
```

### Nested Serializers with Many-to-Many:

```python
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    tags = TagSerializer(many=True)
    category = CategorySerializer()
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'tags', 'category']
    
    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        category_data = validated_data.pop('category')
        
        # Create category
        category, _ = Category.objects.get_or_create(**category_data)
        
        # Create post
        post = Post.objects.create(category=category, **validated_data)
        
        # Handle tags
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(**tag_data)
            post.tags.add(tag)
        
        return post
```

### Deep Nested Serializers:

```python
class CommentSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'comments', 'tags']
```

### Selective Nested Fields:

```python
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PostListSerializer(serializers.ModelSerializer):
    # Minimal author info for list view
    author = serializers.StringRelatedField()
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'created_at']

class PostDetailSerializer(serializers.ModelSerializer):
    # Full author info for detail view
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'comments', 'created_at']
```

### Dynamic Nested Serializers:

```python
class DynamicFieldsMixin:
    """
    Mixin to dynamically include/exclude fields
    """
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)
        
        super().__init__(*args, **kwargs)
        
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
        
        if exclude is not None:
            for field_name in exclude:
                self.fields.pop(field_name, None)

class PostSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = '__all__'

# Usage
# Include only specific fields
serializer = PostSerializer(post, fields=['title', 'author'])

# Exclude specific fields
serializer = PostSerializer(post, exclude=['comments'])
```

### Nested Serializers with Validation:

```python
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'city', 'country', 'postal_code']
    
    def validate_postal_code(self, value):
        if len(value) != 5:
            raise serializers.ValidationError("Postal code must be 5 digits")
        return value

class UserProfileSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'address']
    
    def validate(self, data):
        # Cross-field validation
        address_data = data.get('address', {})
        if address_data.get('country') == 'US' and len(address_data.get('postal_code', '')) != 5:
            raise serializers.ValidationError("US postal codes must be 5 digits")
        return data
    
    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        profile = UserProfile.objects.create(address=address, **validated_data)
        return profile
```

### Optimizing Nested Serializers:

```python
class OptimizedPostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'category', 'tags']

# In the view, use select_related and prefetch_related
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = OptimizedPostSerializer
    
    def get_queryset(self):
        return Post.objects.select_related('author', 'category')\
                          .prefetch_related('tags')
```

## 59. How do you implement background tasks in Django?

Background tasks in Django allow you to execute time-consuming operations asynchronously, improving user experience and application performance.

### Using Celery (Most Popular):

```python
# celery.py
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# settings.py
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
```

### Celery Tasks:

```python
# tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
import time

@shared_task
def send_welcome_email(user_id):
    """Send welcome email to new user"""
    try:
        user = User.objects.get(id=user_id)
        send_mail(
            'Welcome!',
            f'Welcome {user.username}!',
            'from@example.com',
            [user.email],
        )
        return f"Email sent to {user.email}"
    except User.DoesNotExist:
        return "User not found"

@shared_task
def process_image(image_path):
    """Process uploaded image"""
    from PIL import Image
    
    # Simulate processing
    time.sleep(10)
    
    # Resize image
    with Image.open(image_path) as img:
        img.thumbnail((800, 600))
        img.save(image_path)
    
    return f"Processed {image_path}"

@shared_task
def generate_report(report_id):
    """Generate heavy report"""
    report = Report.objects.get(id=report_id)
    
    # Complex calculations
    data = perform_complex_calculations()
    
    # Generate PDF
    pdf_path = generate_pdf(data)
    
    # Update report
    report.status = 'completed'
    report.file_path = pdf_path
    report.save()
    
    return f"Report {report_id} generated"
```

### Using Tasks in Views:

```python
from django.shortcuts import render
from django.http import JsonResponse
from .tasks import send_welcome_email, process_image

def register_user(request):
    # Create user
    user = User.objects.create_user(...)
    
    # Send welcome email asynchronously
    send_welcome_email.delay(user.id)
    
    return JsonResponse({'status': 'User created, email queued'})

def upload_image(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['image']
        
        # Save file
        file_path = save_uploaded_file(uploaded_file)
        
        # Process asynchronously
        task = process_image.delay(file_path)
        
        return JsonResponse({
            'status': 'Image uploaded, processing started',
            'task_id': task.id
        })
```

### Periodic Tasks with Celery Beat:

```python
# settings.py
from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'send-daily-report': {
        'task': 'myapp.tasks.send_daily_report',
        'schedule': crontab(hour=9, minute=0),  # Every day at 9 AM
    },
    'cleanup-old-files': {
        'task': 'myapp.tasks.cleanup_old_files',
        'schedule': crontab(hour=2, minute=0, day_of_week=1),  # Every Monday at 2 AM
    },
    'heartbeat': {
        'task': 'myapp.tasks.heartbeat',
        'schedule': 30.0,  # Every 30 seconds
    },
}

# tasks.py
@shared_task
def send_daily_report():
    """Send daily report to admin"""
    # Generate and send report
    pass

@shared_task
def cleanup_old_files():
    """Clean up files older than 30 days"""
    from datetime import datetime, timedelta
    
    cutoff_date = datetime.now() - timedelta(days=30)
    old_files = File.objects.filter(created_at__lt=cutoff_date)
    
    for file in old_files:
        file.delete()
    
    return f"Cleaned up {old_files.count()} files"
```

### Using Django-RQ (Redis Queue):

```python
# settings.py
RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
        'PASSWORD': '',
        'DEFAULT_TIMEOUT': 360,
    },
    'high': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
    },
    'low': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
    }
}

# jobs.py
def send_email_job(user_id):
    user = User.objects.get(id=user_id)
    send_mail(
        'Subject',
        'Message',
        'from@example.com',
        [user.email],
    )

# views.py
import django_rq

def my_view(request):
    queue = django_rq.get_queue('high')
    queue.enqueue(send_email_job, user_id=request.user.id)
    return HttpResponse("Job queued!")
```

### Using Django-Q:

```python
# settings.py
Q_CLUSTER = {
    'name': 'myproject',
    'workers': 8,
    'recycle': 500,
    'timeout': 60,
    'compress': True,
    'save_limit': 250,
    'queue_limit': 500,
    'cpu_affinity': 1,
    'label': 'Django Q',
    'redis': {
        'host': '127.0.0.1',
        'port': 6379,
        'db': 0,
    }
}

# Usage
from django_q.tasks import async_task, schedule

# Async task
async_task('myapp.tasks.send_email', user_id)

# Scheduled task
schedule('myapp.tasks.cleanup',
         schedule_type=Schedule.DAILY,
         hour=2,
         minute=0)
```

### Custom Background Task System:

```python
# Simple background task using threading
import threading
from django.core.management.base import BaseCommand

class TaskWorker:
    def __init__(self):
        self.tasks = []
        self.running = False
    
    def add_task(self, func, *args, **kwargs):
        self.tasks.append((func, args, kwargs))
    
    def start(self):
        self.running = True
        thread = threading.Thread(target=self._worker)
        thread.daemon = True
        thread.start()
    
    def _worker(self):
        while self.running:
            if self.tasks:
                func, args, kwargs = self.tasks.pop(0)
                try:
                    func(*args, **kwargs)
                except Exception as e:
                    print(f"Task failed: {e}")
            time.sleep(1)

# Global task worker
task_worker = TaskWorker()

# Start worker when Django starts
def ready(self):
    task_worker.start()
```

### Task Monitoring and Error Handling:

```python
# Celery task with retry logic
@shared_task(bind=True, max_retries=3)
def process_payment(self, payment_id):
    try:
        payment = Payment.objects.get(id=payment_id)
        # Process payment
        result = payment_gateway.charge(payment.amount)
        payment.status = 'completed'
        payment.save()
        return result
    except PaymentGatewayError as exc:
        # Retry after 60 seconds
        raise self.retry(exc=exc, countdown=60)
    except Exception as exc:
        # Log error and don't retry
        logger.error(f"Payment processing failed: {exc}")
        payment.status = 'failed'
        payment.save()
        raise

# Task with progress tracking
@shared_task(bind=True)
def bulk_import_data(self, file_path):
    total_records = count_records(file_path)
    processed = 0
    
    for record in read_records(file_path):
        # Process record
        process_record(record)
        processed += 1
        
        # Update progress
        self.update_state(
            state='PROGRESS',
            meta={'current': processed, 'total': total_records}
        )
    
    return {'status': 'completed', 'processed': processed}
```

## 60. What are database schema migrations and how does Django handle them?

**Database schema migrations** are version-controlled changes to your database structure. Django's migration system automatically generates and applies these changes based on model modifications.

### Migration Workflow:

```python
# 1. Make changes to models
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # Adding new field
    created_at = models.DateTimeField(auto_now_add=True)

# 2. Create migration
# python manage.py makemigrations

# 3. Apply migration
# python manage.py migrate
```

### Migration File Structure:

```python
# migrations/0002_add_created_at.py
from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):
    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
```

### Custom Migration Operations:

```python
# Data migration
from django.db import migrations

def populate_slug_field(apps, schema_editor):
    """Populate slug field for existing posts"""
    Post = apps.get_model('myapp', 'Post')
    for post in Post.objects.all():
        post.slug = post.title.lower().replace(' ', '-')
        post.save()

def reverse_populate_slug_field(apps, schema_editor):
    """Reverse operation - clear slug field"""
    Post = apps.get_model('myapp', 'Post')
    Post.objects.all().update(slug='')

class Migration(migrations.Migration):
    dependencies = [
        ('myapp', '0002_add_slug_field'),
    ]

    operations = [
        migrations.RunPython(
            populate_slug_field,
            reverse_populate_slug_field
        ),
    ]
```

### Complex Migration Scenarios:

```python
# Renaming fields with data preservation
class Migration(migrations.Migration):
    operations = [
        # Step 1: Add new field
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=200, null=True),
        ),
        # Step 2: Copy data
        migrations.RunPython(
            lambda apps, schema_editor: copy_name_data(apps, schema_editor),
            migrations.RunPython.noop
        ),
        # Step 3: Remove old field
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]

def copy_name_data(apps, schema_editor):
    User = apps.get_model('myapp', 'User')
    for user in User.objects.all():
        user.full_name = user.name
        user.save()
```

### Migration Dependencies and Conflicts:

```python
# migrations/0003_complex_changes.py
class Migration(migrations.Migration):
    dependencies = [
        ('myapp', '0002_add_created_at'),
        ('anotherapp', '0001_initial'),  # Cross-app dependency
    ]

    operations = [
        # Operations here
    ]
```

### Squashing Migrations:

```bash
# Combine multiple migrations into one
python manage.py squashmigrations myapp 0002 0005

# This creates a new migration file that replaces migrations 0002-0005
```

### Custom Migration Commands:

```python
# management/commands/migrate_custom.py
from django.core.management.base import BaseCommand
from django.db import migrations, transaction

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Custom migration logic
        with transaction.atomic():
            # Perform complex data transformation
            self.migrate_user_data()
            self.cleanup_orphaned_records()
    
    def migrate_user_data(self):
        # Complex data migration logic
        pass
```

## 61. How to connect 2 databases in Django?

Django supports multiple databases through its database routing system, allowing you to distribute your data across different database servers.

### Database Configuration:

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'main_db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'users_db': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'users_database',
        'USER': 'mysql_user',
        'PASSWORD': 'mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    },
    'analytics': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'analytics.sqlite3',
    }
}
```

### Database Router:

```python
# db_router.py
class DatabaseRouter:
    """
    Route specific models to specific databases
    """
    
    route_app_labels = {
        'users': 'users_db',
        'analytics': 'analytics',
        'main': 'default'
    }

    def db_for_read(self, model, **hints):
        """Suggest the database that should be used for reads"""
        if model._meta.app_label in self.route_app_labels:
            return self.route_app_labels[model._meta.app_label]
        return None

    def db_for_write(self, model, **hints):
        """Suggest the database that should be used for writes"""
        if model._meta.app_label in self.route_app_labels:
            return self.route_app_labels[model._meta.app_label]
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if a model in the same app is involved"""
        db_set = {'default', 'users_db', 'analytics'}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that the app's models get created on the right database"""
        if app_label in self.route_app_labels:
            return db == self.route_app_labels[app_label]
        elif db in self.route_app_labels.values():
            return False
        return db == 'default'

# settings.py
DATABASE_ROUTERS = ['myproject.db_router.DatabaseRouter']
```

### Using Multiple Databases in Code:

```python
# Manual database selection
from django.db import connections

# Get specific database connection
users_db = connections['users_db']
analytics_db = connections['analytics']

# Query specific database
users = User.objects.using('users_db').all()
analytics_data = AnalyticsEvent.objects.using('analytics').all()

# Save to specific database
user = User(name='John')
user.save(using='users_db')

# Raw SQL on specific database
with connections['analytics'].cursor() as cursor:
    cursor.execute("SELECT * FROM analytics_event WHERE date > %s", [date])
    results = cursor.fetchall()
```

### Cross-Database Queries (Limited):

```python
# Note: Cross-database JOINs are not supported
# You need to query separately and combine in Python

def get_user_with_analytics(user_id):
    # Get user from users database
    user = User.objects.using('users_db').get(id=user_id)
    
    # Get analytics from analytics database
    analytics = AnalyticsEvent.objects.using('analytics').filter(
        user_id=user_id
    )
    
    return {
        'user': user,
        'analytics': list(analytics)
    }
```

### Master-Slave Database Setup:

```python
class PrimaryReplicaRouter:
    """
    Route reads to replica database and writes to primary
    """
    
    def db_for_read(self, model, **hints):
        """Reading from the replica."""
        return 'replica'

    def db_for_write(self, model, **hints):
        """Writing to the primary."""
        return 'primary'

    def allow_relation(self, obj1, obj2, **hints):
        """Relations between objects are allowed."""
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """All migrations go to primary."""
        return db == 'primary'

# settings.py
DATABASES = {
    'primary': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'primary_db',
        'HOST': 'primary-server.com',
        # ... other settings
    },
    'replica': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'primary_db',  # Same database name
        'HOST': 'replica-server.com',
        # ... other settings
    }
}
```

### Database-Specific Models:

```python
# users/models.py
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    
    class Meta:
        app_label = 'users'  # This will use 'users_db'

# analytics/models.py
class AnalyticsEvent(models.Model):
    event_type = models.CharField(max_length=50)
    user_id = models.IntegerField()  # Foreign key to users database
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        app_label = 'analytics'  # This will use 'analytics' database
```

### Migrations with Multiple Databases:

```bash
# Migrate specific database
python manage.py migrate --database=users_db
python manage.py migrate --database=analytics

# Migrate specific app to specific database
python manage.py migrate --database=users_db users
```

## 62. How to apply previous migration in Django?

Rolling back migrations in Django allows you to revert database changes to a previous state, which is useful for fixing issues or undoing problematic changes.

### Basic Migration Rollback:

```bash
# Show migration status
python manage.py showmigrations

# Rollback to specific migration
python manage.py migrate myapp 0002

# Rollback to before first migration (unapply all)
python manage.py migrate myapp zero

# Rollback all apps to specific point
python manage.py migrate 0001
```

### Migration Status Check:

```bash
# Show all migrations and their status
python manage.py showmigrations

# Output example:
# myapp
#  [X] 0001_initial
#  [X] 0002_add_created_at
#  [X] 0003_add_slug_field
#  [ ] 0004_add_status_field  # Not applied

# Show migrations for specific app
python manage.py showmigrations myapp
```

### Handling Rollback Issues:

```python
# migrations/0003_reversible_changes.py
from django.db import migrations, models

def populate_data(apps, schema_editor):
    """Forward data migration"""
    MyModel = apps.get_model('myapp', 'MyModel')
    for obj in MyModel.objects.all():
        obj.new_field = calculate_value(obj)
        obj.save()

def remove_data(apps, schema_editor):
    """Reverse data migration"""
    MyModel = apps.get_model('myapp', 'MyModel')
    MyModel.objects.all().update(new_field=None)

class Migration(migrations.Migration):
    dependencies = [
        ('myapp', '0002_add_new_field'),
    ]

    operations = [
        migrations.RunPython(
            populate_data,
            remove_data  # Reverse operation
        ),
    ]
```

### Non-Reversible Operations:

```python
# Some operations cannot be automatically reversed
class Migration(migrations.Migration):
    operations = [
        # This operation is not reversible
        migrations.RunSQL(
            "UPDATE myapp_mymodel SET field = 'value';",
            reverse_sql="UPDATE myapp_mymodel SET field = NULL;"  # Provide reverse
        ),
        
        # Irreversible operation
        migrations.RunPython(
            forward_func,
            reverse_code=migrations.RunPython.noop  # Cannot be reversed
        ),
    ]
```

### Safe Rollback Strategies:

```python
# Create backup before major changes
class Migration(migrations.Migration):
    operations = [
        migrations.RunSQL(
            # Create backup table
            "CREATE TABLE myapp_mymodel_backup AS SELECT * FROM myapp_mymodel;",
            reverse_sql="DROP TABLE myapp_mymodel_backup;"
        ),
        
        # Make changes
        migrations.AlterField(
            model_name='mymodel',
            name='important_field',
            field=models.CharField(max_length=200),
        ),
    ]
```

### Custom Rollback Command:

```python
# management/commands/safe_rollback.py
from django.core.management.base import BaseCommand
from django.db import transaction, connection

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('app_label', type=str)
        parser.add_argument('migration_name', type=str)
    
    def handle(self, *args, **options):
        app_label = options['app_label']
        migration_name = options['migration_name']
        
        # Create database backup
        self.create_backup()
        
        try:
            with transaction.atomic():
                # Perform rollback
                self.rollback_migration(app_label, migration_name)
                
                # Verify data integrity
                if not self.verify_data_integrity():
                    raise Exception("Data integrity check failed")
                    
        except Exception as e:
            self.stdout.write(f"Rollback failed: {e}")
            self.restore_backup()
    
    def create_backup(self):
        # Database backup logic
        pass
    
    def rollback_migration(self, app_label, migration_name):
        # Migration rollback logic
        pass
```

## 63. How Django knows which files will be migrated with migrate command?

Django's migration system uses a sophisticated tracking mechanism to determine which migrations to apply based on the current database state and available migration files.

### Migration State Tracking:

```python
# Django creates a table: django_migrations
# Structure:
# id | app | name | applied
# 1  | myapp | 0001_initial | 2023-01-01 10:00:00
# 2  | myapp | 0002_add_field | 2023-01-02 11:00:00
```

### Migration Discovery Process:

```python
# Django scans for migration files in each app's migrations directory
# myapp/migrations/
#   __init__.py
#   0001_initial.py
#   0002_add_created_at.py
#   0003_add_slug_field.py

# Migration file structure
class Migration(migrations.Migration):
    dependencies = [
        ('myapp', '0001_initial'),  # This migration depends on 0001_initial
    ]
    
    operations = [
        # Migration operations
    ]
```

### Migration Dependency Graph:

```python
# Django builds a dependency graph to determine execution order
def get_migration_graph():
    """
    Django's internal process (simplified)
    """
    graph = {}
    
    # 1. Discover all migration files
    for app in settings.INSTALLED_APPS:
        migration_files = find_migration_files(app)
        
        for migration_file in migration_files:
            migration = import_migration(migration_file)
            
            # 2. Build dependency relationships
            graph[migration.name] = {
                'dependencies': migration.dependencies,
                'operations': migration.operations,
                'applied': is_migration_applied(app, migration.name)
            }
    
    return graph

def calculate_migrations_to_apply(target_migration=None):
    """
    Determine which migrations need to be applied
    """
    graph = get_migration_graph()
    applied_migrations = get_applied_migrations()
    
    # Find unapplied migrations
    unapplied = []
    for migration_name, migration_data in graph.items():
        if migration_name not in applied_migrations:
            # Check if all dependencies are satisfied
            if all_dependencies_applied(migration_data['dependencies']):
                unapplied.append(migration_name)
    
    return sort_by_dependencies(unapplied)
```

### Migration Executor Process:

```python
# Simplified version of Django's migration executor
class MigrationExecutor:
    def migrate(self, targets):
        """
        Execute migrations to reach target state
        """
        # 1. Get current migration state
        current_state = self.get_current_state()
        
        # 2. Calculate plan
        plan = self.migration_plan(targets)
        
        # 3. Execute migrations in order
        for migration, backwards in plan:
            if backwards:
                self.unapply_migration(migration)
            else:
                self.apply_migration(migration)
    
    def migration_plan(self, targets):
        """
        Create execution plan to reach targets
        """
        # Build dependency graph
        graph = self.build_graph()
        
        # Find path from current state to target
        plan = []
        for app_label, migration_name in targets:
            path = graph.find_path_to(app_label, migration_name)
            plan.extend(path)
        
        return plan
    
    def apply_migration(self, migration):
        """
        Apply a single migration
        """
        # 1. Execute migration operations
        for operation in migration.operations:
            operation.database_forwards(
                migration.app_label,
                self.connection.schema_editor(),
                migration.from_state,
                migration.to_state
            )
        
        # 2. Record migration as applied
        self.record_migration(migration)
```

### Custom Migration Loader:

```python
# How Django loads and validates migrations
class MigrationLoader:
    def load_disk(self):
        """Load migrations from disk"""
        self.disk_migrations = {}
        
        for app_config in apps.get_app_configs():
            # Look for migrations directory
            migration_directory = os.path.join(app_config.path, 'migrations')
            
            if os.path.isdir(migration_directory):
                # Load migration files
                for filename in os.listdir(migration_directory):
                    if filename.endswith('.py') and not filename.startswith('__'):
                        migration_name = filename[:-3]  # Remove .py
                        
                        # Import migration module
                        module = import_module(f'{app_config.name}.migrations.{migration_name}')
                        migration = module.Migration
                        
                        # Store migration
                        self.disk_migrations[app_config.label, migration_name] = migration
    
    def check_consistent_history(self):
        """Ensure migration history is consistent"""
        # Check for conflicts, missing dependencies, etc.
        for (app_label, migration_name), migration in self.disk_migrations.items():
            for dep_app, dep_migration in migration.dependencies:
                if (dep_app, dep_migration) not in self.disk_migrations:
                    raise InconsistentMigrationHistory(
                        f"Migration {app_label}.{migration_name} depends on "
                        f"{dep_app}.{dep_migration} which doesn't exist"
                    )
```

### Migration State Detection:

```python
def get_migration_state():
    """
    Determine current migration state
    """
    # Query django_migrations table
    applied_migrations = MigrationRecorder.Migration.objects.all()
    
    state = {}
    for migration in applied_migrations:
        state[migration.app, migration.name] = migration.applied
    
    return state

def find_unapplied_migrations():
    """
    Find migrations that haven't been applied
    """
    disk_migrations = load_migrations_from_disk()
    applied_migrations = get_migration_state()
    
    unapplied = []
    for (app_label, migration_name), migration in disk_migrations.items():
        if (app_label, migration_name) not in applied_migrations:
            unapplied.append((app_label, migration_name, migration))
    
    return unapplied
```

### showmigrations Command Implementation:

```python
# Simplified version of showmigrations command
class Command(BaseCommand):
    def handle(self, *args, **options):
        # Load migration loader
        loader = MigrationLoader(connection)
        
        # Get applied migrations
        applied = set(
            (migration.app, migration.name)
            for migration in MigrationRecorder.Migration.objects.all()
        )
        
        # Show migration status for each app
        for app_label in loader.migrated_apps:
            self.stdout.write(f"{app_label}")
            
            # Get migrations for this app
            migrations = loader.disk_migrations
            app_migrations = [
                (name, migration) for (app, name), migration in migrations.items()
                if app == app_label
            ]
            
            # Sort by name (which includes ordering)
            app_migrations.sort()
            
            for migration_name, migration in app_migrations:
                # Check if applied
                if (app_label, migration_name) in applied:
                    self.stdout.write(f" [X] {migration_name}")
                else:
                    self.stdout.write(f" [ ] {migration_name}")
```

## 64. What is the flow of requests in Django files?

Django follows a well-defined request-response cycle that involves multiple components working together to process HTTP requests and generate responses.

### Request Flow Overview:

```
1. Web Server (nginx/Apache) → 2. WSGI Server (Gunicorn/uWSGI) → 
3. Django Application → 4. Middleware → 5. URL Resolver → 
6. View → 7. Model (if needed) → 8. Template → 9. Response
```

### Detailed Request Flow:

```python
# 1. WSGI Application Entry Point
# wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
application = get_wsgi_application()

# 2. Django's WSGI Handler
class WSGIHandler:
    def __call__(self, environ, start_response):
        # Convert WSGI environ to Django HttpRequest
        request = self.request_class(environ)
        
        # Get response from Django
        response = self.get_response(request)
        
        # Convert Django HttpResponse to WSGI response
        return response(environ, start_response)
```

### Middleware Processing:

```python
# 3. Middleware Chain Processing
class MiddlewareHandler:
    def __init__(self):
        # Load middleware classes from settings
        self.middleware_classes = [
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
        ]
    
    def get_response(self, request):
        # Process request through middleware
        for middleware_class in self.middleware_classes:
            middleware = middleware_class()
            
            # Call process_request if it exists
            if hasattr(middleware, 'process_request'):
                response = middleware.process_request(request)
                if response:
                    return response  # Short-circuit if middleware returns response
        
        # Get response from URL resolver and view
        response = self.resolve_and_call_view(request)
        
        # Process response through middleware (in reverse order)
        for middleware_class in reversed(self.middleware_classes):
            middleware = middleware_class()
            
            # Call process_response if it exists
            if hasattr(middleware, 'process_response'):
                response = middleware.process_response(request, response)
        
        return response
```

### URL Resolution:

```python
# 4. URL Resolution Process
# urls.py (root URLconf)
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
    path('blog/', include('blog.urls')),
    path('', views.home, name='home'),
]

# myapp/urls.py
urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/create/', views.PostCreateView.as_view(), name='post-create'),
]

# URL Resolver Implementation (simplified)
class URLResolver:
    def resolve(self, path):
        """
        Resolve URL path to view function and arguments
        """
        # Try each URL pattern
        for pattern in self.url_patterns:
            match = pattern.resolve(path)
            if match:
                return ResolverMatch(
                    func=match.func,
                    args=match.args,
                    kwargs=match.kwargs,
                    url_name=match.url_name,
                    app_names=match.app_names,
                )
        
        # No match found
        raise Http404("URL not found")
```

### View Processing:

```python
# 5. View Execution
# views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView

def post_detail(request, pk):
    """
    Function-based view
    """
    # Get data from model
    post = get_object_or_404(Post, pk=pk)
    
    # Process request data
    if request.method == 'POST':
        # Handle form submission
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    
    # Prepare context data
    context = {
        'post': post,
        'comments': post.comments.all(),
        'form': CommentForm(),
    }
    
    # Render template with context
    return render(request, 'blog/post_detail.html', context)

class PostListView(ListView):
    """
    Class-based view
    """
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        # Customize queryset
        return Post.objects.filter(published=True).select_related('author')
    
    def get_context_data(self, **kwargs):
        # Add extra context
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
```

### Model Layer Interaction:

```python
# 6. Model and Database Interaction
# models.py
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

# ORM Query Processing
def get_posts():
    """
    Django ORM generates SQL queries
    """
    # This Django ORM query:
    posts = Post.objects.filter(published=True).select_related('author')
    
    # Generates SQL like:
    # SELECT post.*, author.* FROM blog_post post
    # INNER JOIN auth_user author ON post.author_id = author.id
    # WHERE post.published = true;
    
    return posts
```

### Template Rendering:

```python
# 7. Template Processing
# Template: blog/post_detail.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>{{ post.title }}</title>
</head>
<body>
    <h1>{{ post.title }}</h1>
    <p>By {{ post.author.username }} on {{ post.created_at|date:"F d, Y" }}</p>
    
    <div class="content">
        {{ post.content|linebreaks }}
    </div>
    
    <h3>Comments</h3>
    {% for comment in comments %}
        <div class="comment">
            <strong>{{ comment.author }}</strong>: {{ comment.content }}
        </div>
    {% empty %}
        <p>No comments yet.</p>
    {% endfor %}
</body>
</html>
"""

# Template Engine Processing
class TemplateRenderer:
    def render(self, template_name, context, request=None):
        # 1. Load template
        template = self.get_template(template_name)
        
        # 2. Create context
        context_instance = Context(context, request=request)
        
        # 3. Render template with context
        rendered_content = template.render(context_instance)
        
        return rendered_content
```

### Response Generation:

```python
# 8. Response Creation and Return
from django.http import HttpResponse, JsonResponse

def create_response(content, request):
    """
    Create appropriate HTTP response
    """
    if request.content_type == 'application/json':
        return JsonResponse(content)
    else:
        return HttpResponse(content, content_type='text/html')

# Response flows back through middleware chain in reverse order
def process_response_middleware(request, response):
    """
    Response processing through middleware
    """
    # Content compression
    if 'gzip' in request.META.get('HTTP_ACCEPT_ENCODING', ''):
        response = compress_response(response)
    
    # Security headers
    response['X-Content-Type-Options'] = 'nosniff'
    response['X-Frame-Options'] = 'DENY'
    
    return response
```

### Complete Request Flow Example:

```python
# Complete flow for a blog post request
"""
1. Browser requests: GET /blog/posts/1/

2. Web server (nginx) forwards to WSGI server (Gunicorn)

3. Gunicorn calls Django's WSGI application

4. Django processes through middleware:
   - SecurityMiddleware: Adds security headers
   - SessionMiddleware: Loads session data
   - AuthenticationMiddleware: Identifies user
   - CsrfMiddleware: Validates CSRF token (for POST)

5. URLResolver matches /blog/posts/1/ to:
   path('posts/<int:pk>/', views.PostDetailView.as_view())

6. PostDetailView.as_view() is called:
   - dispatch() method determines HTTP method
   - get() method is called for GET request
   - get_object() retrieves Post with pk=1
   - get_context_data() prepares template context

7. Model layer:
   - Post.objects.get(pk=1) generates SQL query
   - Database returns post data
   - Related objects (author, comments) loaded if needed

8. Template rendering:
   - blog/post_detail.html template loaded
   - Context variables replaced with actual data
   - Template tags and filters processed
   - Final HTML generated

9. Response creation:
   - HttpResponse object created with rendered HTML
   - Response flows back through middleware (reverse order)
   - Headers added, content compressed, etc.

10. WSGI server sends response back to web server

11. Web server returns response to browser
"""
```

### Error Handling in Request Flow:

```python
# Exception handling middleware
class ExceptionHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        try:
            response = self.get_response(request)
        except Http404:
            # Handle 404 errors
            return self.handle_404(request)
        except PermissionDenied:
            # Handle 403 errors
            return self.handle_403(request)
        except Exception as e:
            # Handle 500 errors
            return self.handle_500(request, e)
        
        return response
    
    def handle_404(self, request):
        return render(request, '404.html', status=404)
    
    def handle_500(self, request, exception):
        # Log error
        logger.error(f"Server error: {exception}")
        return render(request, '500.html', status=500)
```

## 65. What is the use of Celery?

**Celery** is a distributed task queue system that allows you to execute tasks asynchronously, improving application performance and user experience by offloading time-consuming operations.

### Core Concepts:

```python
# Celery Architecture Components:
"""
1. Celery Client - Sends tasks to queue
2. Message Broker - Stores task messages (Redis/RabbitMQ)
3. Celery Workers - Execute tasks
4. Result Backend - Stores task results
"""

# celery.py
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
```

### Common Use Cases:

```python
# 1. Email Processing
@shared_task
def send_bulk_emails(user_ids, email_template):
    """Send emails to multiple users asynchronously"""
    for user_id in user_ids:
        user = User.objects.get(id=user_id)
        send_mail(
            subject=email_template['subject'],
            message=email_template['body'],
            from_email='noreply@example.com',
            recipient_list=[user.email],
        )
    return f"Sent emails to {len(user_ids)} users"

# 2. Image Processing
@shared_task
def process_uploaded_image(image_path):
    """Process uploaded images (resize, watermark, etc.)"""
    from PIL import Image
    
    with Image.open(image_path) as img:
        # Create thumbnail
        img.thumbnail((800, 600), Image.Resampling.LANCZOS)
        
        # Add watermark
        watermark = Image.open('watermark.png')
        img.paste(watermark, (img.width - watermark.width, img.height - watermark.height))
        
        # Save processed image
        processed_path = image_path.replace('.jpg', '_processed.jpg')
        img.save(processed_path)
    
    return processed_path

# 3. Data Export
@shared_task
def generate_csv_export(queryset_params, user_id):
    """Generate large CSV exports"""
    import csv
    from io import StringIO
    
    # Reconstruct queryset
    objects = MyModel.objects.filter(**queryset_params)
    
    # Generate CSV
    output = StringIO()
    writer = csv.writer(output)
    
    # Write header
    writer.writerow(['ID', 'Name', 'Email', 'Created'])
    
    # Write data
    for obj in objects:
        writer.writerow([obj.id, obj.name, obj.email, obj.created_at])
    
    # Save file and notify user
    file_path = f'exports/export_{user_id}_{timezone.now().timestamp()}.csv'
    with open(file_path, 'w') as f:
        f.write(output.getvalue())
    
    # Send notification
    send_export_ready_email.delay(user_id, file_path)
    
    return file_path
```

### Advanced Task Features:

```python
# Task with retry logic
@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def process_payment(self, payment_id):
    """Process payment with retry on failure"""
    try:
        payment = Payment.objects.get(id=payment_id)
        
        # Call payment gateway
        result = payment_gateway.charge(
            amount=payment.amount,
            card_token=payment.card_token
        )
        
        # Update payment status
        payment.status = 'completed'
        payment.transaction_id = result['transaction_id']
        payment.save()
        
        return f"Payment {payment_id} processed successfully"
        
    except PaymentGatewayError as exc:
        # Retry on gateway errors
        logger.warning(f"Payment gateway error for payment {payment_id}: {exc}")
        raise self.retry(exc=exc, countdown=60 * (self.request.retries + 1))
        
    except Exception as exc:
        # Don't retry on other errors
        logger.error(f"Payment processing failed for payment {payment_id}: {exc}")
        payment.status = 'failed'
        payment.save()
        raise

# Task with progress tracking
@shared_task(bind=True)
def bulk_data_import(self, file_path):
    """Import large dataset with progress tracking"""
    total_rows = count_csv_rows(file_path)
    processed_rows = 0
    
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            # Process each row
            MyModel.objects.create(
                name=row['name'],
                email=row['email'],
                # ... other fields
            )
            
            processed_rows += 1
            
            # Update progress
            self.update_state(
                state='PROGRESS',
                meta={
                    'current': processed_rows,
                    'total': total_rows,
                    'percentage': int((processed_rows / total_rows) * 100)
                }
            )
    
    return {
        'status': 'completed',
        'processed_rows': processed_rows,
        'total_rows': total_rows
    }
```

### Periodic Tasks with Celery Beat:

```python
# settings.py
from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    # Run every day at 2:30 AM
    'cleanup-expired-sessions': {
        'task': 'myapp.tasks.cleanup_expired_sessions',
        'schedule': crontab(hour=2, minute=30),
    },
    
    # Run every Monday at 9:00 AM
    'weekly-report': {
        'task': 'myapp.tasks.generate_weekly_report',
        'schedule': crontab(hour=9, minute=0, day_of_week=1),
    },
    
    # Run every 5 minutes
    'health-check': {
        'task': 'myapp.tasks.system_health_check',
        'schedule': 300.0,  # 5 minutes in seconds
    },
    
    # Run on the first day of every month
    'monthly-billing': {
        'task': 'billing.tasks.process_monthly_billing',
        'schedule': crontab(hour=0, minute=0, day_of_month=1),
    },
}

# Periodic task examples
@shared_task
def cleanup_expired_sessions():
    """Clean up expired user sessions"""
    from django.contrib.sessions.models import Session
    from django.utils import timezone
    
    expired_sessions = Session.objects.filter(expire_date__lt=timezone.now())
    count = expired_sessions.count()
    expired_sessions.delete()
    
    return f"Cleaned up {count} expired sessions"

@shared_task
def generate_weekly_report():
    """Generate and email weekly report"""
    # Calculate weekly stats
    start_date = timezone.now() - timedelta(days=7)
    
    stats = {
        'new_users': User.objects.filter(date_joined__gte=start_date).count(),
        'new_orders': Order.objects.filter(created_at__gte=start_date).count(),
        'revenue': Order.objects.filter(
            created_at__gte=start_date,
            status='completed'
        ).aggregate(total=Sum('amount'))['total'] or 0
    }
    
    # Generate report
    report_html = render_to_string('reports/weekly_report.html', stats)
    
    # Email to administrators
    send_mail(
        subject=f'Weekly Report - {timezone.now().strftime("%Y-%m-%d")}',
        message='',
        html_message=report_html,
        from_email='reports@example.com',
        recipient_list=['admin@example.com'],
    )
    
    return f"Weekly report sent with stats: {stats}"
```

### Task Monitoring and Management:

```python
# Monitor task progress
def check_task_progress(task_id):
    """Check the progress of a running task"""
    from celery.result import AsyncResult
    
    result = AsyncResult(task_id)
    
    if result.state == 'PENDING':
        response = {
            'state': result.state,
            'progress': 0,
            'status': 'Task is waiting to be processed...'
        }
    elif result.state == 'PROGRESS':
        response = {
            'state': result.state,
            'progress': result.info.get('current', 0),
            'total': result.info.get('total', 1),
            'percentage': result.info.get('percentage', 0),
            'status': f"Processing... {result.info.get('current', 0)}/{result.info.get('total', 1)}"
        }
    elif result.state == 'SUCCESS':
        response = {
            'state': result.state,
            'progress': 100,
            'status': 'Task completed successfully',
            'result': result.result
        }
    else:  # FAILURE
        response = {
            'state': result.state,
            'progress': 100,
            'status': str(result.info),  # Error message
        }
    
    return response

# Task management views
def start_bulk_import(request):
    """Start bulk import task"""
    if request.method == 'POST':
        uploaded_file = request.FILES['csv_file']
        
        # Save uploaded file
        file_path = save_uploaded_file(uploaded_file)
        
        # Start task
        task = bulk_data_import.delay(file_path)
        
        return JsonResponse({
            'task_id': task.id,
            'status': 'Task started'
        })

def task_progress(request, task_id):
    """Get task progress"""
    progress = check_task_progress(task_id)
    return JsonResponse(progress)
```

### Task Routing and Queues:

```python
# settings.py
CELERY_TASK_ROUTES = {
    'myapp.tasks.send_email': {'queue': 'emails'},
    'myapp.tasks.process_image': {'queue': 'images'},
    'myapp.tasks.generate_report': {'queue': 'reports'},
    'myapp.tasks.high_priority_task': {'queue': 'priority'},
}

# Different worker configurations
"""
# Start workers for different queues
celery -A myproject worker -Q emails --concurrency=4
celery -A myproject worker -Q images --concurrency=2
celery -A myproject worker -Q reports --concurrency=1
celery -A myproject worker -Q priority --concurrency=8
"""

# Route tasks to specific queues
@shared_task
def send_email_task(email_data):
    # This will go to 'emails' queue
    pass

# Manual queue specification
send_email_task.apply_async(args=[email_data], queue='emails')
```

### Error Handling and Logging:

```python
import logging
from celery.signals import task_failure, task_success

logger = logging.getLogger(__name__)

@task_failure.connect
def task_failure_handler(sender=None, task_id=None, exception=None, traceback=None, einfo=None):
    """Handle task failures"""
    logger.error(f'Task {task_id} failed: {exception}')
    
    # Send alert to administrators
    send_admin_alert.delay(
        subject=f'Task Failure: {sender}',
        message=f'Task {task_id} failed with error: {exception}'
    )

@task_success.connect
def task_success_handler(sender=None, result=None, **kwargs):
    """Handle successful task completion"""
    logger.info(f'Task {sender} completed successfully')

# Custom error handling in tasks
@shared_task(bind=True)
def robust_task(self, data):
    try:
        # Task logic here
        result = process_data(data)
        return result
        
    except RetryableError as exc:
        # Retry on specific errors
        logger.warning(f"Retryable error in task {self.request.id}: {exc}")
        raise self.retry(exc=exc, countdown=60, max_retries=3)
        
    except CriticalError as exc:
        # Don't retry, but log and alert
        logger.error(f"Critical error in task {self.request.id}: {exc}")
        send_admin_alert.delay(
            subject='Critical Task Error',
            message=f'Task failed with critical error: {exc}'
        )
        raise
        
    except Exception as exc:
        # Unexpected error
        logger.exception(f"Unexpected error in task {self.request.id}")
        raise
```

### Benefits of Using Celery:

1. **Improved User Experience** - Long-running tasks don't block web requests
2. **Scalability** - Distribute work across multiple workers/servers
3. **Reliability** - Task retry mechanisms and failure handling
4. **Flexibility** - Schedule tasks, route to different queues
5. **Monitoring** - Built-in monitoring and management tools
6. **Performance** - Parallel processing of tasks

## 66. How database concurrency is handled in Django?

Django provides several mechanisms to handle database concurrency issues that arise when multiple users or processes access and modify the same data simultaneously.

### Database Locking Mechanisms:

```python
# 1. Select for Update - Row-level locking
from django.db import transaction

def transfer_money(from_account_id, to_account_id, amount):
    """Transfer money between accounts with row locking"""
    with transaction.atomic():
        # Lock the accounts for update
        from_account = Account.objects.select_for_update().get(id=from_account_id)
        to_account = Account.objects.select_for_update().get(id=to_account_id)
        
        # Check sufficient balance
        if from_account.balance < amount:
            raise InsufficientFundsError("Not enough money")
        
        # Perform transfer
        from_account.balance -= amount
        to_account.balance += amount
        
        # Save changes (locks released when transaction ends)
        from_account.save()
        to_account.save()

# 2. Select for Update with timeout and skip_locked
def process_pending_orders():
    """Process orders with locking to prevent concurrent processing"""
    with transaction.atomic():
        # Get orders that aren't locked by other processes
        orders = Order.objects.select_for_update(
            skip_locked=True  # Skip locked rows
        ).filter(status='pending')[:10]
        
        for order in orders:
            # Process order (other processes can't access this order)
            order.status = 'processing'
            order.save()
            
            # Time-consuming processing
            process_order_items(order)
            
            order.status = 'completed'
            order.save()
```

### Optimistic Concurrency Control:

```python
# Using version fields for optimistic locking
class Document(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    version = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.pk:  # Updating existing record
            # Increment version
            self.version += 1
            
            # Check for concurrent updates
            updated_rows = Document.objects.filter(
                pk=self.pk,
                version=self.version - 1  # Expected previous version
            ).update(
                title=self.title,
                content=self.content,
                version=self.version,
                updated_at=timezone.now()
            )
            
            if updated_rows == 0:
                raise ConcurrentUpdateError(
                    "Document was modified by another user"
                )
        else:
            # New record
            super().save(*args, **kwargs)

# Usage in views
def update_document(request, doc_id):
    document = get_object_or_404(Document, id=doc_id)
    
    if request.method == 'POST':
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Document updated successfully')
            except ConcurrentUpdateError:
                messages.error(request, 'Document was modified by another user. Please refresh and try again.')
        
    return render(request, 'edit_document.html', {'form': form})
```

### Database Constraints for Data Integrity:

```python
# Using database constraints to prevent race conditions
class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    reserved = models.IntegerField(default=0)
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(quantity__gte=0),
                name='quantity_non_negative'
            ),
            models.CheckConstraint(
                check=models.Q(reserved__gte=0),
                name='reserved_non_negative'
            ),
            models.CheckConstraint(
                check=models.Q(reserved__lte=models.F('quantity')),
                name='reserved_not_exceed_quantity'
            )
        ]

def reserve_inventory(product_id, quantity):
    """Reserve inventory with database constraints"""
    try:
        with transaction.atomic():
            inventory = Inventory.objects.select_for_update().get(
                product_id=product_id
            )
            
            # Check availability
            available = inventory.quantity - inventory.reserved
            if available < quantity:
                raise InsufficientInventoryError()
            
            # Reserve items (constraint ensures we don't over-reserve)
            inventory.reserved += quantity
            inventory.save()
            
    except IntegrityError:
        # Database constraint violation
        raise InsufficientInventoryError("Not enough inventory available")
```

### Atomic Transactions:

```python
# Atomic decorators and context managers
@transaction.atomic
def create_order_with_items(customer_id, items):
    """Create order with items atomically"""
    # Create order
    order = Order.objects.create(
        customer_id=customer_id,
        status='pending',
        total_amount=0
    )
    
    total_amount = 0
    
    # Create order items
    for item_data in items:
        # Check inventory
        inventory = Inventory.objects.select_for_update().get(
            product_id=item_data['product_id']
        )
        
        if inventory.quantity < item_data['quantity']:
            raise InsufficientInventoryError(
                f"Not enough {inventory.product.name} in stock"
            )
        
        # Create order item
        order_item = OrderItem.objects.create(
            order=order,
            product_id=item_data['product_id'],
            quantity=item_data['quantity'],
            price=item_data['price']
        )
        
        # Update inventory
        inventory.quantity -= item_data['quantity']
        inventory.save()
        
        total_amount += order_item.quantity * order_item.price
    
    # Update order total
    order.total_amount = total_amount
    order.save()
    
    return order

# Nested atomic transactions
def complex_business_operation():
    """Complex operation with nested transactions"""
    with transaction.atomic():  # Outer transaction
        # Main operation
        main_record = MainModel.objects.create(...)
        
        try:
            with transaction.atomic():  # Inner transaction (savepoint)
                # Risky operation
                risky_operation()
                
        except SomeException:
            # Inner transaction rolled back, outer continues
            log_error("Risky operation failed, continuing with main operation")
        
        # Complete main operation
        complete_main_operation(main_record)
```

### Race Condition Prevention:

```python
# Preventing duplicate record creation
def get_or_create_unique_slug(title):
    """Create unique slug preventing race conditions"""
    base_slug = slugify(title)
    slug = base_slug
    counter = 1
    
    while True:
        try:
            # Try to create with current slug
            with transaction.atomic():
                return Article.objects.create(
                    title=title,
                    slug=slug
                )
        except IntegrityError:
            # Slug already exists, try with counter
            slug = f"{base_slug}-{counter}"
            counter += 1
            
            if counter > 100:  # Prevent infinite loop
                raise ValueError("Unable to create unique slug")

# Using get_or_create safely
def safe_get_or_create_category(name):
    """Safely get or create category"""
    try:
        with transaction.atomic():
            category, created = Category.objects.get_or_create(
                name=name,
                defaults={'slug': slugify(name)}
            )
            return category
    except IntegrityError:
        # Another process created it between our check and create
        # Just get the existing one
        return Category.objects.get(name=name)
```

### Cache-Based Concurrency Control:

```python
from django.core.cache import cache
import time

def distributed_lock_operation(lock_key, timeout=30):
    """Perform operation with distributed lock using cache"""
    lock_id = f"lock:{lock_key}"
    
    # Try to acquire lock
    if cache.add(lock_id, "locked", timeout=timeout):
        try:
            # Perform protected operation
            return perform_critical_operation()
        finally:
            # Always release lock
            cache.delete(lock_id)
    else:
        raise ConcurrentOperationError("Operation already in progress")

# Usage
def process_user_data(user_id):
    """Process user data with distributed locking"""
    lock_key = f"user_processing_{user_id}"
    
    try:
        result = distributed_lock_operation(lock_key, timeout=300)  # 5 minutes
        return result
    except ConcurrentOperationError:
        raise ValueError("User data is already being processed")
```

### Database-Specific Concurrency Features:

```python
# PostgreSQL specific features
from django.db import connection

def update_with_returning(model_class, filter_kwargs, update_kwargs):
    """Update with RETURNING clause (PostgreSQL)"""
    with connection.cursor() as cursor:
        # Build dynamic query
        table_name = model_class._meta.db_table
        set_clause = ', '.join([f"{k} = %s" for k in update_kwargs.keys()])
        where_clause = ' AND '.join([f"{k} = %s" for k in filter_kwargs.keys()])
        
        query = f"""
            UPDATE {table_name} 
            SET {set_clause}
            WHERE {where_clause}
            RETURNING *
        """
        
        cursor.execute(query, list(update_kwargs.values()) + list(filter_kwargs.values()))
        return cursor.fetchall()

# Using advisory locks (PostgreSQL)
def with_advisory_lock(lock_id):
    """Context manager for PostgreSQL advisory locks"""
    class AdvisoryLock:
        def __enter__(self):
            with connection.cursor() as cursor:
                cursor.execute("SELECT pg_advisory_lock(%s)", [lock_id])
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            with connection.cursor() as cursor:
                cursor.execute("SELECT pg_advisory_unlock(%s)", [lock_id])
    
    return AdvisoryLock()

# Usage
def critical_section_with_advisory_lock():
    with with_advisory_lock(12345):
        # Only one process can execute this at a time
        perform_critical_operation()
```

### Monitoring and Debugging Concurrency:

```python
import logging
from django.db import transaction

logger = logging.getLogger(__name__)

def log_transaction_info(func):
    """Decorator to log transaction information"""
    def wrapper(*args, **kwargs):
        logger.info(f"Starting transaction for {func.__name__}")
        
        try:
            with transaction.atomic():
                result = func(*args, **kwargs)
                logger.info(f"Transaction {func.__name__} completed successfully")
                return result
        except Exception as e:
            logger.error(f"Transaction {func.__name__} failed: {e}")
            raise
    
    return wrapper

# Deadlock detection and retry
def retry_on_deadlock(max_retries=3):
    """Decorator to retry operations on deadlock"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except OperationalError as e:
                    if 'deadlock' in str(e).lower() and attempt < max_retries - 1:
                        logger.warning(f"Deadlock detected in {func.__name__}, retrying...")
                        time.sleep(0.1 * (2 ** attempt))  # Exponential backoff
                        continue
                    raise
        return wrapper
    return decorator
```

## 67. How atomic transactions happen in Django?

**Atomic transactions** in Django ensure that a group of database operations either all succeed or all fail, maintaining data consistency and integrity.

### Understanding Atomicity:

```python
# ACID Properties:
# Atomicity - All operations succeed or all fail
# Consistency - Database remains in valid state
# Isolation - Transactions don't interfere with each other
# Durability - Committed changes are permanent

# Without atomicity (BAD):
def transfer_money_unsafe(from_account, to_account, amount):
    from_account.balance -= amount
    from_account.save()  # If this succeeds but next fails...
    
    # If error occurs here, money disappears!
    if to_account.is_frozen:
        raise AccountFrozenError()
    
    to_account.balance += amount
    to_account.save()  # This might never execute

# With atomicity (GOOD):
@transaction.atomic
def transfer_money_safe(from_account, to_account, amount):
    from_account.balance -= amount
    from_account.save()
    
    if to_account.is_frozen:
        raise AccountFrozenError()  # Entire transaction rolls back
    
    to_account.balance += amount
    to_account.save()
```

### Different Ways to Use Atomic Transactions:

```python
from django.db import transaction

# 1. Decorator approach
@transaction.atomic
def create_blog_post_with_tags(title, content, tag_names):
    # All operations in this function are atomic
    post = BlogPost.objects.create(title=title, content=content)
    
    for tag_name in tag_names:
        tag, created = Tag.objects.get_or_create(name=tag_name)
        post.tags.add(tag)
    
    # Send notification
    notify_subscribers.delay(post.id)
    
    return post

# 2. Context manager approach
def update_user_profile(user_id, profile_data, address_data):
    with transaction.atomic():
        user = User.objects.get(id=user_id)
        
        # Update user fields
        for field, value in profile_data.items():
            setattr(user, field, value)
        user.save()
        
        # Update or create address
        address, created = Address.objects.update_or_create(
            user=user,
            defaults=address_data
        )
        
        # Log the change
        UserActivityLog.objects.create(
            user=user,
            action='profile_updated',
            details=f"Profile and address updated"
        )

# 3. Manual transaction control
def complex_data_migration():
    # Start transaction# Django Advanced Concepts - Complete Guide

## 42. What are custom model managers and when would you use them?

**Custom Model Managers** are Python classes that define the interface through which database query operations are provided to Django models. Every model gets at least one manager, and by default, Django adds a manager with the name `objects` to every model class.

### When to use Custom Managers:

1. **Add extra manager methods** - Custom query logic
2. **Modify initial QuerySet** - Filter default results
3. **Encapsulate common queries** - Reusable query patterns

### Example Implementation:

```python
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')
    
    def by_author(self, author):
        return self.get_queryset().filter(author=author)

class Post(models.Model):
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    objects = models.Manager()  # Default manager
    published = PublishedManager()  # Custom manager
```

### Use Cases:
- Soft deletes (hiding deleted records)
- Multi-tenancy (filtering by tenant)
- Status-based filtering
- Complex aggregations

## 43. How does Django handle database transactions?

Django provides several mechanisms for handling database transactions, ensuring data consistency and integrity.

### Transaction Handling Mechanisms:

1. **Autocommit Mode** (Default)
   - Each database operation is immediately committed
   - Django wraps each view in a transaction by default

2. **Atomic Transactions**
   ```python
   from django.db import transaction
   
   # Decorator
   @transaction.atomic
   def my_view(request):
       # All database operations in one transaction
       pass
   
   # Context manager
   def my_function():
       with transaction.atomic():
           # Database operations here
           Model.objects.create(...)
   ```

3. **Manual Transaction Control**
   ```python
   from django.db import transaction
   
   def manual_transaction():
       sid = transaction.savepoint()
       try:
           # Database operations
           Model.objects.create(...)
       except Exception:
           transaction.savepoint_rollback(sid)
       else:
           transaction.savepoint_commit(sid)
   ```

### Transaction Isolation Levels:
Django supports different isolation levels depending on the database backend, helping prevent issues like dirty reads, phantom reads, and non-repeatable reads.

## 44. How do you override a save method in a model, and what are the caveats?

Overriding the `save()` method allows custom logic during model saving, but requires careful consideration of several caveats.

### Basic Override:

```python
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    
    def save(self, *args, **kwargs):
        # Custom logic before saving
        if not self.slug:
            self.slug = slugify(self.name)
        
        # Call the parent save method
        super().save(*args, **kwargs)
        
        # Custom logic after saving
        self.send_notification()
```

### Important Caveats:

1. **Always call super().save()** - Skipping this prevents actual database saving
2. **Bulk operations bypass save()** - `bulk_create()`, `update()` don't call save()
3. **Admin interface considerations** - May not trigger your custom logic
4. **Signal implications** - Overridden save affects signal timing
5. **Performance impact** - Additional logic slows down saves
6. **Exception handling** - Wrap risky operations in try-catch blocks

### Advanced Override with Validation:

```python
def save(self, *args, **kwargs):
    # Validation
    self.full_clean()
    
    # Custom logic
    if self._state.adding:  # New instance
        self.created_at = timezone.now()
    else:  # Existing instance
        self.updated_at = timezone.now()
    
    super().save(*args, **kwargs)
```

## 45. What are database routers in Django and how are they used?

**Database Routers** determine which database to use for which model and operation when working with multiple databases in Django.

### Router Structure:

```python
class DatabaseRouter:
    def db_for_read(self, model, **hints):
        """Suggest the database to read from."""
        if model._meta.app_label == 'analytics':
            return 'analytics_db'
        return None
    
    def db_for_write(self, model, **hints):
        """Suggest the database to write to."""
        if model._meta.app_label == 'analytics':
            return 'analytics_db'
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if models are in the same app."""
        db_set = {'default', 'analytics_db'}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that certain apps' models get created on the right DB."""
        if app_label == 'analytics':
            return db == 'analytics_db'
        elif db == 'analytics_db':
            return False
        return db == 'default'
```

### Configuration:
```python
# settings.py
DATABASES = {
    'default': {...},
    'analytics_db': {...},
}

DATABASE_ROUTERS = ['path.to.routers.DatabaseRouter']
```

### Use Cases:
- Separating read/write operations
- App-specific databases
- Legacy database integration
- Geographic data distribution

## 46. What are signals pitfalls and how to avoid them?

Django signals provide decoupled notifications when certain actions occur, but they come with several pitfalls that developers should be aware of.

### Common Pitfalls:

1. **Infinite Loops**
   ```python
   # BAD - Can cause infinite recursion
   @receiver(post_save, sender=MyModel)
   def my_handler(sender, instance, **kwargs):
       instance.save()  # This triggers the signal again!
   
   # GOOD - Use update() or conditional logic
   @receiver(post_save, sender=MyModel)
   def my_handler(sender, instance, **kwargs):
       if not kwargs.get('created'):
           MyModel.objects.filter(pk=instance.pk).update(field='value')
   ```

2. **Performance Issues**
   ```python
   # BAD - Expensive operations in signals
   @receiver(post_save, sender=User)
   def send_welcome_email(sender, instance, created, **kwargs):
       if created:
           send_mail(...)  # Blocking operation
   
   # GOOD - Use background tasks
   @receiver(post_save, sender=User)
   def send_welcome_email(sender, instance, created, **kwargs):
       if created:
           send_welcome_email_task.delay(instance.id)
   ```

3. **Transaction Issues**
   ```python
   # BAD - Signal fires before transaction commit
   @receiver(post_save, sender=Order)
   def process_payment(sender, instance, **kwargs):
       payment_gateway.charge(instance.amount)  # May fail if transaction rolls back
   
   # GOOD - Use on_commit
   @receiver(post_save, sender=Order)
   def process_payment(sender, instance, **kwargs):
       transaction.on_commit(lambda: payment_gateway.charge(instance.amount))
   ```

### Best Practices:
- Keep signal handlers lightweight
- Use `transaction.on_commit()` for external services
- Avoid database operations that might cause loops
- Consider using background tasks for heavy operations
- Test signal behavior thoroughly

## 47. How does Django handle file uploads under the hood?

Django's file upload system involves multiple components working together to securely and efficiently handle file data.

### Upload Process Flow:

1. **HTTP Request Parsing**
   - Django's request handler parses multipart/form-data
   - Files are temporarily stored in memory or on disk

2. **UploadHandler Classes**
   ```python
   # Django uses different handlers based on file size
   FILE_UPLOAD_HANDLERS = [
       'django.core.files.uploadhandler.MemoryFileUploadHandler',
       'django.core.files.uploadhandler.TemporaryFileUploadHandler',
   ]
   ```

3. **File Object Creation**
   ```python
   class MyModel(models.Model):
       file = models.FileField(upload_to='uploads/')
   
   # In view
   def upload_view(request):
       uploaded_file = request.FILES['file']
       # uploaded_file is a UploadedFile instance
   ```

### Storage Backends:

Django abstracts file storage through storage backends:

```python
from django.core.files.storage import default_storage

# Default file system storage
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

# Custom storage (e.g., S3)
class S3Storage(Storage):
    def _save(self, name, content):
        # Save to S3
        pass
    
    def url(self, name):
        # Return S3 URL
        pass
```

### Security Measures:
- File type validation
- Size limits
- Path traversal protection
- Virus scanning integration points

### Configuration Options:
```python
# settings.py
FILE_UPLOAD_MAX_MEMORY_SIZE = 2.5 * 1024 * 1024  # 2.5 MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 2.5 * 1024 * 1024
FILE_UPLOAD_TEMP_DIR = '/tmp'
MEDIA_ROOT = '/path/to/media'
MEDIA_URL = '/media/'
```

## 48. Explain the working of the ContentType framework in Django

The **ContentTypes framework** provides a high-level, generic interface for working with models in your Django application. It allows you to create relationships to "any" model.

### Core Components:

1. **ContentType Model**
   ```python
   from django.contrib.contenttypes.models import ContentType
   
   # Get ContentType for a model
   content_type = ContentType.objects.get_for_model(MyModel)
   
   # Get the model class back
   model_class = content_type.model_class()
   ```

2. **Generic Foreign Keys**
   ```python
   from django.contrib.contenttypes.fields import GenericForeignKey
   from django.contrib.contenttypes.models import ContentType
   
   class Comment(models.Model):
       content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
       object_id = models.PositiveIntegerField()
       content_object = GenericForeignKey('content_type', 'object_id')
       text = models.TextField()
   
   # Usage
   blog_post = BlogPost.objects.get(pk=1)
   comment = Comment.objects.create(
       content_object=blog_post,
       text="Great post!"
   )
   ```

3. **Generic Relations**
   ```python
   from django.contrib.contenttypes.fields import GenericRelation
   
   class BlogPost(models.Model):
       title = models.CharField(max_length=200)
       comments = GenericRelation(Comment)
   
   # Usage
   post = BlogPost.objects.get(pk=1)
   comments = post.comments.all()
   ```

### Use Cases:
- Comments system for multiple models
- Tagging system
- Activity logs
- Permissions framework
- Polymorphic relationships

### Limitations:
- Cannot use foreign key constraints
- Queries can be less efficient
- No referential integrity at database level

## 49. What are some security vulnerabilities Django protects against by default?

Django includes numerous built-in security features that protect against common web vulnerabilities.

### 1. Cross-Site Scripting (XSS)
```python
# Django automatically escapes variables in templates
{{ user_input }}  # Automatically escaped

# Manual escaping when needed
from django.utils.html import escape
safe_content = escape(user_input)
```

### 2. Cross-Site Request Forgery (CSRF)
```python
# CSRF middleware enabled by default
MIDDLEWARE = [
    'django.middleware.csrf.CsrfViewMiddleware',
    # ...
]

# In templates
<form method="post">
    {% csrf_token %}
    <!-- form fields -->
</form>
```

### 3. SQL Injection
```python
# Django ORM automatically parameterizes queries
User.objects.filter(name=user_input)  # Safe

# Raw queries with parameters
User.objects.raw("SELECT * FROM users WHERE name = %s", [user_input])
```

### 4. Clickjacking
```python
# X-Frame-Options middleware
MIDDLEWARE = [
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

X_FRAME_OPTIONS = 'DENY'  # or 'SAMEORIGIN'
```

### 5. Security Headers
```python
# settings.py
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

### 6. Password Security
- Password hashing with PBKDF2 by default
- Password validators
- Session security

### 7. Host Header Validation
```python
ALLOWED_HOSTS = ['example.com', 'www.example.com']
```

## 50. How to implement soft deletes in Django models?

**Soft deletes** mark records as deleted without actually removing them from the database, allowing for data recovery and audit trails.

### Implementation with Custom Manager:

```python
from django.db import models
from django.utils import timezone

class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    objects = SoftDeleteManager()
    all_objects = models.Manager()  # Access to all records including deleted
    
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

# Usage
class Post(SoftDeleteModel):
    title = models.CharField(max_length=200)
    content = models.TextField()

# Using the model
post = Post.objects.create(title="Test")
post.delete()  # Soft delete
Post.objects.all()  # Won't include deleted post
Post.all_objects.all()  # Includes deleted post
post.restore()  # Restore the post
```

### Advanced Implementation with QuerySet:

```python
class SoftDeleteQuerySet(models.QuerySet):
    def delete(self):
        return self.update(deleted_at=timezone.now())
    
    def hard_delete(self):
        return super().delete()
    
    def alive(self):
        return self.filter(deleted_at=None)
    
    def dead(self):
        return self.exclude(deleted_at=None)

class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, using=self._db).alive()
    
    def all_with_deleted(self):
        return SoftDeleteQuerySet(self.model, using=self._db)
    
    def deleted_only(self):
        return SoftDeleteQuerySet(self.model, using=self._db).dead()
```

## 51. How does ModelForm validation work internally?

Django's **ModelForm** validation follows a multi-step process that combines form validation with model validation.

### Validation Flow:

1. **Field Validation** - Individual field cleaning
2. **Form Validation** - Cross-field validation
3. **Model Validation** - Model-level constraints
4. **Database Validation** - Database constraints

### Internal Process:

```python
class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['field1', 'field2']
    
    def clean_field1(self):
        # Individual field validation
        data = self.cleaned_data['field1']
        if some_condition:
            raise forms.ValidationError("Invalid field1")
        return data
    
    def clean(self):
        # Cross-field validation
        cleaned_data = super().clean()
        field1 = cleaned_data.get('field1')
        field2 = cleaned_data.get('field2')
        
        if field1 and field2 and some_condition:
            raise forms.ValidationError("Field1 and Field2 conflict")
        
        return cleaned_data
```

### Validation Steps Internally:

1. **full_clean() method**:
   ```python
   def full_clean(self):
       """
       Clean all of self.data and populate self._errors and self.cleaned_data.
       """
       self._errors = ErrorDict()
       if not self.is_bound:
           return
       
       self.cleaned_data = {}
       self._clean_fields()      # Step 1: Field validation
       self._clean_form()        # Step 2: Form validation
       self._post_clean()        # Step 3: Model validation
   ```

2. **Model Instance Validation**:
   ```python
   def _post_clean(self):
       # Create model instance
       instance = self.instance
       
       # Set field values
       for field_name in self.fields:
           if field_name in self.cleaned_data:
               setattr(instance, field_name, self.cleaned_data[field_name])
       
       # Call model's full_clean()
       try:
           instance.full_clean()
       except ValidationError as e:
           self._update_errors(e)
   ```

### Custom Model Validation:

```python
class MyModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    
    def clean(self):
        # Model-level validation
        if self.field1 == 'invalid' and self.field2 < 10:
            raise ValidationError("Invalid combination of field1 and field2")
    
    def clean_fields(self, exclude=None):
        # Individual field validation at model level
        super().clean_fields(exclude)
        if self.field1 and len(self.field1) < 3:
            raise ValidationError({'field1': 'Too short'})
```

## 52. How can you implement a throttling mechanism in Django (or DRF)?

Throttling prevents abuse by limiting the rate of requests from clients. Both Django and Django REST Framework provide mechanisms for implementing throttling.

### DRF Built-in Throttling:

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/hour',
        'user': '1000/hour',
        'login': '5/min',
    }
}

# In views
from rest_framework.throttling import UserRateThrottle

class MyAPIView(APIView):
    throttle_classes = [UserRateThrottle]
    throttle_scope = 'user'
    
    def get(self, request):
        return Response({'message': 'Hello'})
```

### Custom Throttle Class:

```python
from rest_framework.throttling import BaseThrottle
from django.core.cache import cache
from django.utils import timezone

class CustomThrottle(BaseThrottle):
    def allow_request(self, request, view):
        # Get client identifier
        ident = self.get_ident(request)
        
        # Check cache for request count
        key = f'throttle_{ident}'
        request_count = cache.get(key, 0)
        
        if request_count >= 100:  # Max 100 requests
            return False
        
        # Increment counter
        cache.set(key, request_count + 1, timeout=3600)  # 1 hour
        return True
    
    def wait(self):
        return 3600  # Wait time in seconds
```

### Django Middleware Throttling:

```python
class ThrottleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        client_ip = self.get_client_ip(request)
        key = f'throttle_{client_ip}'
        
        request_count = cache.get(key, 0)
        if request_count >= 100:
            return HttpResponse('Rate limit exceeded', status=429)
        
        cache.set(key, request_count + 1, timeout=3600)
        return self.get_response(request)
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
```

### Advanced Rate Limiting with Redis:

```python
import redis
import time

class RedisThrottle(BaseThrottle):
    def __init__(self):
        self.redis_client = redis.Redis(host='localhost', port=6379, db=0)
    
    def allow_request(self, request, view):
        ident = self.get_ident(request)
        key = f'throttle:{ident}'
        
        # Sliding window approach
        now = time.time()
        window = 3600  # 1 hour window
        
        # Remove old entries
        self.redis_client.zremrangebyscore(key, 0, now - window)
        
        # Count current requests
        current_requests = self.redis_client.zcard(key)
        
        if current_requests >= 100:  # Limit
            return False
        
        # Add current request
        self.redis_client.zadd(key, {str(now): now})
        self.redis_client.expire(key, window)
        
        return True
```

## 53. Explain how DRF's ViewSet and Router work together

**ViewSets** and **Routers** in Django REST Framework work together to provide a powerful and conventional way to organize API views and URL patterns.

### ViewSet Basics:

```python
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Custom action
    @action(detail=True, methods=['post'])
    def set_favorite(self, request, pk=None):
        book = self.get_object()
        # Logic to set favorite
        return Response({'status': 'favorite set'})
    
    @action(detail=False)
    def recent_books(self, request):
        recent = Book.objects.filter(created_at__gte=timezone.now() - timedelta(days=7))
        serializer = self.get_serializer(recent, many=True)
        return Response(serializer.data)
```

### Router Configuration:

```python
from rest_framework.routers import DefaultRouter
from django.urls import path, include

# Create router
router = DefaultRouter()
router.register(r'books', BookViewSet)

# URL patterns
urlpatterns = [
    path('api/', include(router.urls)),
]
```

### Generated URL Patterns:

The router automatically generates these URL patterns:
- `GET /api/books/` - List books
- `POST /api/books/` - Create book
- `GET /api/books/{id}/` - Retrieve book
- `PUT /api/books/{id}/` - Update book
- `PATCH /api/books/{id}/` - Partial update
- `DELETE /api/books/{id}/` - Delete book
- `POST /api/books/{id}/set_favorite/` - Custom action
- `GET /api/books/recent_books/` - Custom list action

### ViewSet Types:

1. **ModelViewSet** - Full CRUD operations
2. **ReadOnlyModelViewSet** - Only read operations
3. **ViewSet** - Custom viewset with manual action methods

```python
class CustomViewSet(viewsets.ViewSet):
    def list(self, request):
        # Custom list logic
        return Response([])
    
    def create(self, request):
        # Custom create logic
        return Response({})
    
    def retrieve(self, request, pk=None):
        # Custom retrieve logic
        return Response({})
```

### Custom Router:

```python
class CustomRouter(DefaultRouter):
    def get_urls(self):
        urls = super().get_urls()
        # Add custom URL patterns
        custom_urls = [
            # Custom patterns
        ]
        return urls + custom_urls
```

### Advanced Usage:

```python
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get_serializer_class(self):
        # Different serializers for different actions
        if self.action == 'create':
            return BookCreateSerializer
        elif self.action == 'list':
            return BookListSerializer
        return BookDetailSerializer
    
    def get_permissions(self):
        # Different permissions for different actions
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
```

## 54. How do you write a custom pagination class in Django REST Framework?

Custom pagination classes in DRF allow you to control how large datasets are divided into discrete pages and how pagination metadata is presented.

### Basic Custom Pagination:

```python
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100
    
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'page_size': self.page_size,
            'results': data
        })
```

### Cursor-Based Pagination:

```python
from rest_framework.pagination import CursorPagination

class CustomCursorPagination(CursorPagination):
    page_size = 20
    ordering = '-created_at'
    cursor_query_param = 'cursor'
    page_size_query_param = 'page_size'
    
    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })
```

### Custom Pagination from Scratch:

```python
from rest_framework.pagination import BasePagination
from rest_framework.response import Response
from django.core.paginator import Paginator
from collections import OrderedDict

class CustomPagination(BasePagination):
    page_size = 25
    
    def paginate_queryset(self, queryset, request, view=None):
        page_size = self.get_page_size(request)
        if not page_size:
            return None
        
        paginator = Paginator(queryset, page_size)
        page_number = request.query_params.get('page', 1)
        
        try:
            page_number = int(page_number)
        except ValueError:
            page_number = 1
        
        try:
            self.page = paginator.page(page_number)
        except:
            self.page = paginator.page(1)
        
        return list(self.page)
    
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('page_info', {
                'current_page': self.page.number,
                'total_pages': self.page.paginator.num_pages,
                'has_next': self.page.has_next(),
                'has_previous': self.page.has_previous(),
                'start_index': self.page.start_index(),
                'end_index': self.page.end_index(),
            }),
            ('results', data)
        ]))
    
    def get_page_size(self, request):
        if hasattr(self, 'page_size_query_param'):
            try:
                return int(request.query_params[self.page_size_query_param])
            except (KeyError, ValueError):
                pass
        return self.page_size
```

### Offset-Based Pagination:

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

### Usage in Views:

```python
class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = CustomPageNumberPagination

# Or globally in settings
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'myapp.pagination.CustomPageNumberPagination',
    'PAGE_SIZE': 20
}
```

## 55. What is the difference between APIView and GenericAPIView in DRF?

**APIView** and **GenericAPIView** are base classes in Django REST Framework that provide different levels of functionality for building API views.

### APIView - Basic Foundation:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BookAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            # Get single book
            try:
                book = Book.objects.get(pk=pk)
                serializer = BookSerializer(book)
                return Response(serializer.data)
            except Book.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            # Get all books
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
```

### GenericAPIView - Enhanced with Common Patterns:

```python
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

class BookGenericAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```

### Key Differences:

| Feature | APIView | GenericAPIView |
|---------|---------|----------------|
| **Queryset** | Manual handling | Built-in `get_queryset()` method |
| **Serializer** | Manual instantiation | Built-in `get_serializer()` method |
| **Object Retrieval** | Manual `get()` calls | Built-in `get_object()` method |
| **Permissions** | Manual implementation | Built-in permission handling |
| **Filtering** | Manual implementation | Built-in filter backends |
| **Pagination** | Manual implementation | Built-in pagination support |

### GenericAPIView Advanced Features:

```python
class BookGenericAPIView(GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'  # Instead of 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'author']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'title']
    
    def get_queryset(self):
        """Override to customize queryset based on user"""
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(is_published=True)
        return queryset
    
    def get_serializer_class(self):
        """Different serializers for different actions"""
        if self.request.method == 'POST':
            return BookCreateSerializer
        return BookSerializer
    
    def get_object(self):
        """Custom object retrieval with additional checks"""
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj
```

### Using Built-in Generic Views:

```python
from rest_framework.generics import (
    ListCreateAPIView, 
    RetrieveUpdateDestroyAPIView
)

# List and Create in one view
class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Retrieve, Update, Delete in one view
class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

## 56. How do you implement permissions per object in DRF?

Object-level permissions in DRF allow you to control access to individual model instances based on custom logic.

### Custom Object Permission:

```python
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    
    def has_object_permission(self, request, view, obj):
        # Read permissions for any request (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions only for owner
        return obj.owner == request.user

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Permission for blog posts - only author can edit
    """
    
    def has_permission(self, request, view):
        # View-level permission check
        return request.user.is_authenticated or request.method in permissions.SAFE_METHODS
    
    def has_object_permission(self, request, view, obj):
        # Object-level permission check
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
```

### Using Object Permissions in Views:

```python
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]

class CommentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
```

### Complex Object Permissions:

```python
class ProjectPermission(permissions.BasePermission):
    """
    Complex permission system for project management
    """
    
    def has_object_permission(self, request, view, obj):
        # Project owner has full access
        if obj.owner == request.user:
            return True
        
        # Check team membership
        try:
            membership = obj.team_members.get(user=request.user)
        except ProjectMember.DoesNotExist:
            return False
        
        # Different permissions based on role
        if request.method in permissions.SAFE_METHODS:
            # All team members can read
            return True
        elif request.method in ['PUT', 'PATCH']:
            # Only editors and admins can update
            return membership.role in ['editor', 'admin']
        elif request.method == 'DELETE':
            # Only admins can delete
            return membership.role == 'admin'
        
        return False

class ConditionalPermission(permissions.BasePermission):
    """
    Permission that changes based on object state
    """
    
    def has_object_permission(self, request, view, obj):
        # Published articles are read-only for non-owners
        if obj.status == 'published':
            if request.method in permissions.SAFE_METHODS:
                return True
            return obj.author == request.user
        
        # Draft articles only accessible by author
        return obj.author == request.user
```

### Permission with External Services:

```python
class SubscriptionPermission(permissions.BasePermission):
    """
    Permission based on user subscription status
    """
    
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        # Check subscription status
        return request.user.subscription.is_active
    
    def has_object_permission(self, request, view, obj):
        # Premium content requires premium subscription
        if obj.is_premium:
            return request.user.subscription.tier == 'premium'
        return True
```

### Dynamic Permissions:

```python
class DynamicPermission(permissions.BasePermission):
    """
    Permission that can be configured per view
    """
    
    def __init__(self, allowed_roles=None):
        self.allowed_roles = allowed_roles or []
    
    def has_object_permission(self, request, view, obj):
        if not hasattr(obj, 'get_user_role'):
            return False
        
        user_role = obj.get_user_role(request.user)
        return user_role in self.allowed_roles

# Usage in view
class DocumentView(RetrieveUpdateAPIView):
    permission_classes = [DynamicPermission(['owner', 'editor'])]
```

### Permissions with Caching:

```python
from django.core.cache import cache

class CachedPermission(permissions.BasePermission):
    """
    Permission with caching for expensive checks
    """
    
    def has_object_permission(self, request, view, obj):
        cache_key = f'permission_{request.user.id}_{obj.id}_{request.method}'
        
        # Check cache first
        cached_result = cache.get(cache_key)
        if cached_result is not None:
            return cached_result
        
        # Expensive permission check
        result = self._check_permission(request, obj)
        
        # Cache for 5 minutes
        cache.set(cache_key, result, 300)
        return result
    
    def _check_permission(self, request, obj):
        # Complex permission logic here
        return True
```

## 57. What is the difference between authentication and authorization in Django?

**Authentication** and **Authorization** are two distinct but related security concepts in Django that work together to secure your application.

### Authentication - "Who are you?"

Authentication verifies the identity of a user. It answers the question "Who is this user?"

```python
# Authentication backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default
    'myapp.backends.EmailBackend',  # Custom
]

# Custom authentication backend
class EmailBackend:
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
```

### DRF Authentication Classes:

```python
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication,
    BasicAuthentication
)

class CustomTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'  # Use 'Bearer' instead of 'Token'
    
    def authenticate_credentials(self, key):
        # Custom token validation logic
        user, token = super().authenticate_credentials(key)
        
        # Additional checks
        if not user.is_active:
            raise AuthenticationFailed('User inactive')
        
        return (user, token)

# JWT Authentication
from rest_framework_simplejwt.authentication import JWTAuthentication

class CustomJWTAuthentication(JWTAuthentication):
    def get_validated_token(self, raw_token):
        # Custom JWT validation
        validated_token = super().get_validated_token(raw_token)
        
        # Additional token checks
        if validated_token.payload.get('custom_claim') != 'expected_value':
            raise InvalidToken('Invalid custom claim')
        
        return validated_token
```

### Authorization - "What can you do?"

Authorization determines what an authenticated user is allowed to do. It answers "What permissions does this user have?"

### Django Permissions System:

```python
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# Built-in permissions (automatically created)
# - add_<modelname>
# - change_<modelname>
# - delete_<modelname>
# - view_<modelname>

# Custom permissions in model
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    class Meta:
        permissions = [
            ("can_publish", "Can publish article"),
            ("can_feature", "Can feature article"),
        ]

# Checking permissions
from django.contrib.auth.decorators import permission_required

@permission_required('myapp.can_publish')
def publish_article(request, article_id):
    # Only users with 'can_publish' permission can access
    pass

# In views
def my_view(request):
    if request.user.has_perm('myapp.can_publish'):
        # User has permission
        pass
```

### DRF Authorization (Permissions):

```python
from rest_framework.permissions import BasePermission

class CanPublishPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('myapp.can_publish')
    
    def has_object_permission(self, request, view, obj):
        # Object-level permission check
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

# Group-based permissions
class EditorPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='editors').exists()

# Role-based permissions
class RoleBasedPermission(BasePermission):
    required_roles = []
    
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        user_roles = request.user.profile.roles.values_list('name', flat=True)
        return any(role in self.required_roles for role in user_roles)
```

### Complete Authentication + Authorization Flow:

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

# View with both authentication and authorization
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, CanPublishPermission]
    
    def get_permissions(self):
        """Different permissions for different actions"""
        if self.action == 'create':
            permission_classes = [IsAuthenticated, CanPublishPermission]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        else:
            permission_classes = [AllowAny]
        
        return [permission() for permission in permission_classes]
```

### Custom User Model with Roles:

```python
class CustomUser(AbstractUser):
    role = models.CharField(max_length=20, choices=[
        ('admin', 'Admin'),
        ('editor', 'Editor'),
        ('viewer', 'Viewer'),
    ])
    
    def has_role(self, role):
        return self.role == role
    
    def can_edit_article(self, article):
        if self.role == 'admin':
            return True
        elif self.role == 'editor':
            return article.author == self
        return False

# Usage in views
class ArticleUpdateView(UpdateAPIView):
    def get_object(self):
        article = super().get_object()
        if not self.request.user.can_edit_article(article):
            raise PermissionDenied("You don't have permission to edit this article")
        return article
```

### Key Differences Summary:

| Aspect | Authentication | Authorization |
|--------|----------------|---------------|
| **Purpose** | Verify identity | Control access |
| **Question** | "Who are you?" | "What can you do?" |
| **Process** | Login/Token validation | Permission checking |
| **Timing** | Before authorization | After authentication |
| **Failure** | 401 Unauthorized | 403 Forbidden |
| **Django Classes** | Authentication backends | Permission classes |
| **DRF Classes** | Authentication classes | Permission classes |

## 58. How can you handle nested serializers in DRF?

Nested serializers in DRF allow you to represent related objects within a single serialized response and handle complex data structures.

### Basic Nested Serializers:

```python
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)  # Nested serializer
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_date']

# This produces:
# {
#     "id": 1,
#     "title": "Django Book",
#     "author": {
#         "id": 1,
#         "name": "John Doe",
#         "email": "john@example.com"
#     },
#     "publication_date": "2023-01-01"
# }
```

### Writable Nested Serializers:

```python
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_date']
    
    def create(self, validated_data):
        author_data = validated_data.pop('author')
        
        # Create or get author
        author, created = Author.objects.get_or_create(
            email=author_data['email'],
            defaults=author_data
        )
        
        # Create book with author
        book = Book.objects.create(author=author, **validated_data)
        return book
    
    def update(self, instance, validated_data):
        author_data = validated_data.pop('author', None)
        
        # Update book fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        # Update author if provided
        if author_data:
            for attr, value in author_data.items():
                setattr(instance.author, attr, value)
            instance.author.save()
        
        instance.save()
        return instance
```

### Nested Serializers with Many-to-Many:

```python
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    tags = TagSerializer(many=True)
    category = CategorySerializer()
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'tags', 'category']
    
    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        category_data = validated_data.pop('category')
        
        # Create category
        category, _ = Category.objects.get_or_create(**category_data)
        
        # Create post
        post = Post.objects.create(category=category, **validated_data)
        
        # Handle tags
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(**tag_data)
            post.tags.add(tag)
        
        return post
```

### Deep Nested Serializers:

```python
class CommentSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'comments', 'tags']
```

### Selective Nested Fields:

```python
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PostListSerializer(serializers.ModelSerializer):
    # Minimal author info for list view
    author = serializers.StringRelatedField()
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'created_at']

class PostDetailSerializer(serializers.ModelSerializer):
    # Full author info for detail view
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'comments', 'created_at']
```

### Dynamic Nested Serializers:

```python
class DynamicFieldsMixin:
    """
    Mixin to dynamically include/exclude fields
    """
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)
        
        super().__init__(*args, **kwargs)
        
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
        
        if exclude is not None:
            for field_name in exclude:
                self.fields.pop(field_name, None)

class PostSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = '__all__'

# Usage
# Include only specific fields
serializer = PostSerializer(post, fields=['title', 'author'])

# Exclude specific fields
serializer = PostSerializer(post, exclude=['comments'])
```

### Nested Serializers with Validation:

```python
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'city', 'country', 'postal_code']
    
    def validate_postal_code(self, value):
        if len(value) != 5:
            raise serializers.ValidationError("Postal code must be 5 digits")
        return value

class UserProfileSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'address']
    
    def validate(self, data):
        # Cross-field validation
        address_data = data.get('address', {})
        if address_data.get('country') == 'US' and len(address_data.get('postal_code', '')) != 5:
            raise serializers.ValidationError("US postal codes must be 5 digits")
        return data
    
    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        profile = UserProfile.objects.create(address=address, **validated_data)
        return profile
```

### Optimizing Nested Serializers:

```python
class OptimizedPostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'category', 'tags']

# In the view, use select_related and prefetch_related
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = OptimizedPostSerializer
    
    def get_queryset(self):
        return Post.objects.select_related('author', 'category')\
                          .prefetch_related('tags')
```

## 59. How do you implement background tasks in Django?

Background tasks in Django allow you to execute time-consuming operations asynchronously, improving user experience and application performance.

### Using Celery (Most Popular):

```python
# celery.py
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# settings.py
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
```

### Celery Tasks:

```python
# tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
import time

@shared_task
def send_welcome_email(user_id):
    """Send welcome email to new user"""
    try:
        user = User.objects.get(id=user_id)
        send_mail(
            'Welcome!',
            f'Welcome {user.username}!',
            'from@example.com',
            [user.email],
        )
        return f"Email sent to {user.email}"
    except User.DoesNotExist:
        return "User not found"

@shared_task
def process_image(image_path):
    """Process uploaded image"""
    from PIL import Image
    
    # Simulate processing
    time.sleep(10)
    
    # Resize image
    with Image.open(image_path) as img:
        img.thumbnail((800, 600))
        img.save(image_path)
    
    return f"Processed {image_path}"

@shared_task
def generate_report(report_id):
    """Generate heavy report"""
    report = Report.objects.get(id=report_id)
    
    # Complex calculations
    data = perform_complex_calculations()
    
    # Generate PDF
    pdf_path = generate_pdf(data)
    
    # Update report
    report.status = 'completed'
    report.file_path = pdf_path
    report.save()
    
    return f"Report {report_id} generated"
```

### Using Tasks in Views:

```python
from django.shortcuts import render
from django.http import JsonResponse
from .tasks import send_welcome_email, process_image

def register_user(request):
    # Create user
    user = User.objects.create_user(...)
    
    # Send welcome email asynchronously
    send_welcome_email.delay(user.id)
    
    return JsonResponse({'status': 'User created, email queued'})

def upload_image(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['image']
        
        # Save file
        file_path = save_uploaded_file(uploaded_file)
        
        # Process asynchronously
        task = process_image.delay(file_path)
        
        return JsonResponse({
            'status': 'Image uploaded, processing started',
            'task_id': task.id
        })
```

### Periodic Tasks with Celery Beat:

```python
# settings.py
from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'send-daily-report': {
        'task': 'myapp.tasks.send_daily_report',
        'schedule': crontab(hour=9, minute=0),  # Every day at 9 AM
    },
    'cleanup-old-files': {
        'task': 'myapp.tasks.cleanup_old_files',
        'schedule': crontab(hour=2, minute=0, day_of_week=1),  # Every Monday at 2 AM
    },
    'heartbeat': {
        'task': 'myapp.tasks.heartbeat',
        'schedule': 30.0,  # Every 30 seconds
    },
}

# tasks.py
@shared_task
def send_daily_report():
    """Send daily report to admin"""
    # Generate and send report
    pass

@shared_task
def cleanup_old_files():
    """Clean up files older than 30 days"""
    from datetime import datetime, timedelta
    
    cutoff_date = datetime.now() - timedelta(days=30)
    old_files = File.objects.filter(created_at__lt=cutoff_date)
    
    for file in old_files:
        file.delete()
    
    return f"Cleaned up {old_files.count()} files"
```

### Using Django-RQ (Redis Queue):

```python
# settings.py
RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
        'PASSWORD': '',
        'DEFAULT_TIMEOUT': 360,
    },
    'high': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
    },
    'low': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
    }
}

# jobs.py
def send_email_job(user_id):
    user = User.objects.get(id=user_id)
    send_mail(
        'Subject',
        'Message',
        'from@example.com',
        [user.email],
    )

# views.py
import django_rq

def my_view(request):
    queue = django_rq.get_queue('high')
    queue.enqueue(send_email_job, user_id=request.user.id)
    return HttpResponse("Job queued!")
```

### Using Django-Q:

```python
# settings.py
Q_CLUSTER = {
    'name': 'myproject',
    'workers': 8,
    'recycle': 500,
    'timeout': 60,
    'compress': True,
    'save_limit': 250,
    'queue_limit': 500,
    'cpu_affinity': 1,
    'label': 'Django Q',
    'redis': {
        'host': '127.0.0.1',
        'port': 6379,
        'db': 0,
    }
}

# Usage
from django_q.tasks import async_task, schedule

# Async task
async_task('myapp.tasks.send_email', user_id)

# Scheduled task
schedule('myapp.tasks.cleanup',
         schedule_type=Schedule.DAILY,
         hour=2,
         minute=0)
```

### Custom Background Task System:

```python
# Simple background task using threading
import threading
from django.core.management.base import BaseCommand

class TaskWorker:
    def __init__(self):
        self.tasks = []
        self.running = False
    
    def add_task(self, func, *args, **kwargs):
        self.tasks.append((func, args, kwargs))
    
    def start(self):
        self.running = True
        thread = threading.Thread(target=self._worker)
        thread.daemon = True
        thread.start()
    
    def _worker(self):
        while self.running:
            if self.tasks:
                func, args, kwargs = self.tasks.pop(0)
                try:
                    func(*args, **kwargs)
                except Exception as e:
                    print(f"Task failed: {e}")
            time.sleep(1)

# Global task worker
task_worker = TaskWorker()

# Start worker when Django starts
def ready(self):
    task_worker.start()
```

### Task Monitoring and Error Handling:

```python
# Celery task with retry logic
@shared_task(bind=True, max_retries=3)
def process_payment(self, payment_id):
    try:
        payment = Payment.objects.get(id=payment_id)
        # Process payment
        result = payment_gateway.charge(payment.amount)
        payment.status = 'completed'
        payment.save()
        return result
    except PaymentGatewayError as exc:
        # Retry after 60 seconds
        raise self.retry(exc=exc, countdown=60)
    except Exception as exc:
        # Log error and don't retry
        logger.error(f"Payment processing failed: {exc}")
        payment.status = 'failed'
        payment.save()
        raise

# Task with progress tracking
@shared_task(bind=True)
def bulk_import_data(self, file_path):
    total_records = count_records(file_path)
    processed = 0
    
    for record in read_records(file_path):
        # Process record
        process_record(record)
        processed += 1
        
        # Update progress
        self.update_state(
            state='PROGRESS',
            meta={'current': processed, 'total': total_records}
        )
    
    return {'status': 'completed', 'processed': processed}
```

## 60. What are database schema migrations and how does Django handle them?

**Database schema migrations** are version-controlled changes to your database structure. Django's migration system automatically generates and applies these changes based on model modifications.

### Migration Workflow:

```python
# 1. Make changes to models
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # Adding new field
    created_at = models.DateTimeField(auto_now_add=True)

# 2. Create migration
# python manage.py makemigrations

# 3. Apply migration
# python manage.py migrate
```

### Migration File Structure:

```python
# migrations/0002_add_created_at.py
from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):
    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
```

### Custom Migration Operations:

```python
# Data migration
from django.db import migrations

def populate_slug_field(apps, schema_editor):
    """Populate slug field for existing posts"""
    Post = apps.get_model('myapp', 'Post')
    for post in Post.objects.all():
        post.slug = post.title.lower().replace(' ', '-')
        post.save()

def reverse_populate_slug_field(apps, schema_editor):
    """Reverse operation - clear slug field"""
    Post = apps.get_model('myapp', 'Post')
    Post.objects.all().update(slug='')

class Migration(migrations.Migration):
    dependencies = [
        ('myapp', '0002_add_slug_field'),
    ]

    operations = [
        migrations.RunPython(
            populate_slug_field,
            reverse_populate_slug_field
        ),
    ]
```

### Complex Migration Scenarios:

```python
# Renaming fields with data preservation
class Migration(migrations.Migration):
    operations = [
        # Step 1: Add new field
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=200, null=True),
        ),
        # Step 2: Copy data
        migrations.RunPython(
            lambda apps, schema_editor: copy_name_data(apps, schema_editor),
            migrations.RunPython.noop
        ),
        # Step 3: Remove old field
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]

def copy_name_data(apps, schema_editor):
    User = apps.get_model('myapp', 'User')
    for user in User.objects.all():
        user.full_name = user.name
        user.save()
```

### Migration Dependencies and Conflicts:

```python
# migrations/0003_complex_changes.py
class Migration(migrations.Migration):
    dependencies = [
        ('myapp', '0002_add_created_at'),
        ('anotherapp', '0001_initial'),  # Cross-app dependency
    ]

    operations = [
        # Operations here
    ]
```

### Squashing Migrations:

```bash
# Combine multiple migrations into one
python manage.py squashmigrations myapp 0002 0005

# This creates a new migration file that replaces migrations 0002-0005
```

### Custom Migration Commands:

```python
# management/commands/migrate_custom.py
from django.core.management.base import BaseCommand
from django.db import migrations, transaction

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Custom migration logic
        with transaction.atomic():
            # Perform complex data transformation
            self.migrate_user_data()
            self.cleanup_orphaned_records()
    
    def migrate_user_data(self):
        # Complex data migration logic
        pass
```

## 61. How to connect 2 databases in Django?

Django supports multiple databases through its database routing system, allowing you to distribute your data across different database servers.

### Database Configuration:

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'main_db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'users_db': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'users_database',
        'USER': 'mysql_user',
        'PASSWORD': 'mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    },
    'analytics': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'analytics.sqlite3',
    }
}
```

### Database Router:

```python
# db_router.py
class DatabaseRouter:
    """
    Route specific models to specific databases
    """
    
    route_app_labels = {
        'users': 'users_db',
        'analytics': 'analytics',
        'main': 'default'
    }

    def db_for_read(self, model, **hints):
        """Suggest the database that should be used for reads"""
        if model._meta.app_label in self.route_app_labels:
            return self.route_app_labels[model._meta.app_label]
        return None

    def db_for_write(self, model, **hints):
        """Suggest the database that should be used for writes"""
        if model._meta.app_label in self.route_app_labels:
            return self.route_app_labels[model._meta.app_label]
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if a model in the same app is involved"""
        db_set = {'default', 'users_db', 'analytics'}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that the app's models get created on the right database"""
        if app_label in self.route_app_labels:
            return db == self.route_app_labels[app_label]
        elif db in self.route_app_labels.values():
            return False
        return db == 'default'

# settings.py
DATABASE_ROUTERS = ['myproject.db_router.DatabaseRouter']
```

### Using Multiple Databases in Code:

```python
# Manual database selection
from django.db import connections

# Get specific database connection
users_db = connections['users_db']
analytics_db = connections['analytics']

# Query specific database
users = User.objects.using('users_db').all()
analytics_data = AnalyticsEvent.objects.using('analytics').all()

# Save to specific database
user = User(name='John')
user.save(using='users_db')

# Raw SQL on specific database
with connections['analytics'].cursor() as cursor:
    cursor.execute("SELECT * FROM analytics_event WHERE date > %s", [date])
    results = cursor.fetchall()
```

### Cross-Database Queries (Limited):

```python
# Note: Cross-database JOINs are not supported
# You need to query separately and combine in Python

def get_user_with_analytics(user_id):
    # Get user from users database
    user = User.objects.using('users_db').get(id=user_id)
    
    # Get analytics from analytics database
    analytics = AnalyticsEvent.objects.using('analytics').filter(
        user_id=user_id
    )
    
    return {
        'user': user,
        'analytics': list(analytics)
    }
```

### Master-Slave Database Setup:

```python
class PrimaryReplicaRouter:
    """
    Route reads to replica database and writes to primary
    """
    
    def db_for_read(self, model, **hints):
        """Reading from the replica."""
        return 'replica'

    def db_for_write(self, model, **hints):
        """Writing to the primary."""
        return 'primary'

    def allow_relation(self, obj1, obj2, **hints):
        """Relations between objects are allowed."""
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """All migrations go to primary."""
        return db == 'primary'

# settings.py
DATABASES = {
    'primary': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'primary_db',
        'HOST': 'primary-server.com',
        # ... other settings
    },
    'replica': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'primary_db',  # Same database name
        'HOST': 'replica-server.com',
        # ... other settings
    }
}
```

### Database-Specific Models:

```python
# users/models.py
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    
    class Meta:
        app_label = 'users'  # This will use 'users_db'

# analytics/models.py
class AnalyticsEvent(models.Model):
    event_type = models.CharField(max_length=50)
    user_id = models.IntegerField()  # Foreign key to users database
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        app_label = 'analytics'  # This will use 'analytics' database
```

### Migrations with Multiple Databases:

```bash
# Migrate specific database
python manage.py migrate --database=users_db
python manage.py migrate --database=analytics

# Migrate specific app to specific database
python manage.py migrate --database=users_db users
```

## 62. How to apply previous migration in Django?

Rolling back migrations in Django allows you to revert database changes to a previous state, which is useful for fixing issues or undoing problematic changes.

### Basic Migration Rollback:

```bash
# Show migration status
python manage.py showmigrations

# Rollback to specific migration
python manage.py migrate myapp 0002

# Rollback to before first migration (unapply all)
python manage.py migrate myapp zero

# Rollback all apps to specific point
python manage.py migrate 0001
```

### Migration Status Check:

```bash
# Show all migrations and their status
python manage.py showmigrations

# Output example:
# myapp
#  [X] 0001_initial
#  [X] 0002_add_created_at
#  [X] 0003_add_slug_field
#  [ ] 0004_add_status_field  # Not applied

# Show migrations for specific app
python manage.py showmigrations myapp
```

### Handling Rollback Issues:

```python
# migrations/0003_reversible_changes.py
from django.db import migrations, models

def populate_data(apps, schema_editor):
    """Forward data migration"""
    MyModel = apps.get_model('myapp', 'MyModel')
    for obj in MyModel.objects.all():
        obj.new_field = calculate_value(obj)
        obj.save()

def remove_data(apps, schema_editor):
    """Reverse data migration"""
    MyModel = apps.get_model('myapp', 'MyModel')
    MyModel.objects.all().update(new_field=None)

class Migration(migrations.Migration):
    dependencies = [
        ('myapp', '0002_add_new_field'),
    ]

    operations = [
        migrations.RunPython(
            populate_data,
            remove_data  # Reverse operation
        ),
    ]
```

### Non-Reversible Operations:

```python
# Some operations cannot be automatically reversed
class Migration(migrations.Migration):
    operations = [
        # This operation is not reversible
        migrations.RunSQL(
            "UPDATE myapp_mymodel SET field = 'value';",
            reverse_sql="UPDATE myapp_mymodel SET field = NULL;"  # Provide reverse
        ),
        
        # Irreversible operation
        migrations.RunPython(
            forward_func,
            reverse_code=migrations.RunPython.noop  # Cannot be reversed
        ),
    ]
```

### Safe Rollback Strategies:

```python
# Create backup before major changes
class Migration(migrations.Migration):
    operations = [
        migrations.RunSQL(
            # Create backup table
            "CREATE TABLE myapp_mymodel_backup AS SELECT * FROM myapp_mymodel;",
            reverse_sql="DROP TABLE myapp_mymodel_backup;"
        ),
        
        # Make changes
        migrations.AlterField(
            model_name='mymodel',
            name='important_field',
            field=models.CharField(max_length=200),
        ),
    ]
```

### Custom Rollback Command:

```python
# management/commands/safe_rollback.py
from django.core.management.base import BaseCommand
from django.db import transaction, connection

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('app_label', type=str)
        parser.add_argument('migration_name', type=str)
    
    def handle(self, *args, **options):
        app_label = options['app_label']
        migration_name = options['migration_name']
        
        # Create database backup
        self.create_backup()
        
        try:
            with transaction.atomic():
                # Perform rollback
                self.rollback_migration(app_label, migration_name)
                
                # Verify data integrity
                if not self.verify_data_integrity():
                    raise Exception("Data integrity check failed")
                    
        except Exception as e:
            self.stdout.write(f"Rollback failed: {e}")
            self.restore_backup()
    
    def create_backup(self):
        # Database backup logic
        pass
    
    def rollback_migration(self, app_label, migration_name):
        # Migration rollback logic
        pass
```

## 63. How Django knows which files will be migrated with migrate command?

Django's migration system uses a sophisticated tracking mechanism to determine which migrations to apply based on the current database state and available migration files.

### Migration State Tracking:

```python
# Django creates a table: django_migrations
# Structure:
# id | app | name | applied
# 1  | myapp | 0001_initial | 2023-01-01 10:00:00
# 2  | myapp | 0002_add_field | 2023-01-02 11:00:00
```

### Migration Discovery Process:

```python
# Django scans for migration files in each app's migrations directory
# myapp/migrations/
#   __init__.py
#   0001_initial.py
#   0002_add_created_at.py
#   0003_add_slug_field.py

# Migration file structure
class Migration(migrations.Migration):
    dependencies = [
        ('myapp', '0001_initial'),  # This migration depends on 0001_initial
    ]
    
    operations = [
        # Migration operations
    ]
```

### Migration Dependency Graph:

```python
# Django builds a dependency graph to determine execution order
def get_migration_graph():
    """
    Django's internal process (simplified)
    """
    graph = {}
    
    # 1. Discover all migration files
    for app in settings.INSTALLED_APPS:
        migration_files = find_migration_files(app)
        
        for migration_file in migration_files:
            migration = import_migration(migration_file)
            
            # 2. Build dependency relationships
            graph[migration.name] = {
                'dependencies': migration.dependencies,
                'operations': migration.operations,
                'applied': is_migration_applied(app, migration.name)
            }
    
    return graph

def calculate_migrations_to_apply(target_migration=None):
    """
    Determine which migrations need to be applied
    """
    graph = get_migration_graph()
    applied_migrations = get_applied_migrations()
    
    # Find unapplied migrations
    unapplied = []
    for migration_name, migration_data in graph.items():
        if migration_name not in applied_migrations:
            # Check if all dependencies are satisfied
            if all_dependencies_applied(migration_data['dependencies']):
                unapplied.append(migration_name)
    
    return sort_by_dependencies(unapplied)
```

### Migration Executor Process:

```python
# Simplified version of Django's migration executor
class MigrationExecutor:
    def migrate(self, targets):
        """
        Execute migrations to reach target state
        """
        # 1. Get current migration state
        current_state = self.get_current_state()
        
        # 2. Calculate plan
        plan = self.migration_plan(targets)
        
        # 3. Execute migrations in order
        for migration, backwards in plan:
            if backwards:
                self.unapply_migration(migration)
            else:
                self.apply_migration(migration)
    
    def migration_plan(self, targets):
        """
        Create execution plan to reach targets
        """
        # Build dependency graph
        graph = self.build_graph()
        
        # Find path from current state to target
        plan = []
        for app_label, migration_name in targets:
            path = graph.find_path_to(app_label, migration_name)
            plan.extend(path)
        
        return plan
    
    def apply_migration(self, migration):
        """
        Apply a single migration
        """
        # 1. Execute migration operations
        for operation in migration.operations:
            operation.database_forwards(
                migration.app_label,
                self.connection.schema_editor(),
                migration.from_state,
                migration.to_state
            )
        
        # 2. Record migration as applied
        self.record_migration(migration)
```

### Custom Migration Loader:

```python
# How Django loads and validates migrations
class MigrationLoader:
    def load_disk(self):
        """Load migrations from disk"""
        self.disk_migrations = {}
        
        for app_config in apps.get_app_configs():
            # Look for migrations directory
            migration_directory = os.path.join(app_config.path, 'migrations')
            
            if os.path.isdir(migration_directory):
                # Load migration files
                for filename in os.listdir(migration_directory):
                    if filename.endswith('.py') and not filename.startswith('__'):
                        migration_name = filename[:-3]  # Remove .py
                        
                        # Import migration module
                        module = import_module(f'{app_config.name}.migrations.{migration_name}')
                        migration = module.Migration
                        
                        # Store migration
                        self.disk_migrations[app_config.label, migration_name] = migration
    
    def check_consistent_history(self):
        """Ensure migration history is consistent"""
        # Check for conflicts, missing dependencies, etc.
        for (app_label, migration_name), migration in self.disk_migrations.items():
            for dep_app, dep_migration in migration.dependencies:
                if (dep_app, dep_migration) not in self.disk_migrations:
                    raise InconsistentMigrationHistory(
                        f"Migration {app_label}.{migration_name} depends on "
                        f"{dep_app}.{dep_migration} which doesn't exist"
                    )
```

### Migration State Detection:

```python
def get_migration_state():
    """
    Determine current migration state
    """
    # Query django_migrations table
    applied_migrations = MigrationRecorder.Migration.objects.all()
    
    state = {}
    for migration in applied_migrations:
        state[migration.app, migration.name] = migration.applied
    
    return state

def find_unapplied_migrations():
    """
    Find migrations that haven't been applied
    """
    disk_migrations = load_migrations_from_disk()
    applied_migrations = get_migration_state()
    
    unapplied = []
    for (app_label, migration_name), migration in disk_migrations.items():
        if (app_label, migration_name) not in applied_migrations:
            unapplied.append((app_label, migration_name, migration))
    
    return unapplied
```

### showmigrations Command Implementation:

```python
# Simplified version of showmigrations command
class Command(BaseCommand):
    def handle(self, *args, **options):
        # Load migration loader
        loader = MigrationLoader(connection)
        
        # Get applied migrations
        applied = set(
            (migration.app, migration.name)
            for migration in MigrationRecorder.Migration.objects.all()
        )
        
        # Show migration status for each app
        for app_label in loader.migrated_apps:
            self.stdout.write(f"{app_label}")
            
            # Get migrations for this app
            migrations = loader.disk_migrations
            app_migrations = [
                (name, migration) for (app, name), migration in migrations.items()
                if app == app_label
            ]
            
            # Sort by name (which includes ordering)
            app_migrations.sort()
            
            for migration_name, migration in app_migrations:
                # Check if applied
                if (app_label, migration_name) in applied:
                    self.stdout.write(f" [X] {migration_name}")
                else:
                    self.stdout.write(f" [ ] {migration_name}")
```

## 64. What is the flow of requests in Django files?

Django follows a well-defined request-response cycle that involves multiple components working together to process HTTP requests and generate responses.

### Request Flow Overview:

```
1. Web Server (nginx/Apache) → 2. WSGI Server (Gunicorn/uWSGI) → 
3. Django Application → 4. Middleware → 5. URL Resolver → 
6. View → 7. Model (if needed) → 8. Template → 9. Response
```

### Detailed Request Flow:

```python
# 1. WSGI Application Entry Point
# wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
application = get_wsgi_application()

# 2. Django's WSGI Handler
class WSGIHandler:
    def __call__(self, environ, start_response):
        # Convert WSGI environ to Django HttpRequest
        request = self.request_class(environ)
        
        # Get response from Django
        response = self.get_response(request)
        
        # Convert Django HttpResponse to WSGI response
        return response(environ, start_response)
```

### Middleware Processing:

```python
# 3. Middleware Chain Processing
class MiddlewareHandler:
    def __init__(self):
        # Load middleware classes from settings
        self.middleware_classes = [
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
        ]
    
    def get_response(self, request):
        # Process request through middleware
        for middleware_class in self.middleware_classes:
            middleware = middleware_class()
            
            # Call process_request if it exists
            if hasattr(middleware, 'process_request'):
                response = middleware.process_request(request)
                if response:
                    return response  # Short-circuit if middleware returns response
        
        # Get response from URL resolver and view
        response = self.resolve_and_call_view(request)
        
        # Process response through middleware (in reverse order)
        for middleware_class in reversed(self.middleware_classes):
            middleware = middleware_class()
            
            # Call process_response if it exists
            if hasattr(middleware, 'process_response'):
                response = middleware.process_response(request, response)
        
        return response
```

### URL Resolution:

```python
# 4. URL Resolution Process
# urls.py (root URLconf)
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
    path('blog/', include('blog.urls')),
    path('', views.home, name='home'),
]

# myapp/urls.py
urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/create/', views.PostCreateView.as_view(), name='post-create'),
]

# URL Resolver Implementation (simplified)
class URLResolver:
    def resolve(self, path):
        """
        Resolve URL path to view function and arguments
        """
        # Try each URL pattern
        for pattern in self.url_patterns:
            match = pattern.resolve(path)
            if match:
                return ResolverMatch(
                    func=match.func,
                    args=match.args,
                    kwargs=match.kwargs,
                    url_name=match.url_name,
                    app_names=match.app_names,
                )
        
        # No match found
        raise Http404("URL not found")
```

### View Processing:

```python
# 5. View Execution
# views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView

def post_detail(request, pk):
    """
    Function-based view
    """
    # Get data from model
    post = get_object_or_404(Post, pk=pk)
    
    # Process request data
    if request.method == 'POST':
        # Handle form submission
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    
    # Prepare context data
    context = {
        'post': post,
        'comments': post.comments.all(),
        'form': CommentForm(),
    }
    
    # Render template with context
    return render(request, 'blog/post_detail.html', context)

class PostListView(ListView):
    """
    Class-based view
    """
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        # Customize queryset
        return Post.objects.filter(published=True).select_related('author')
    
    def get_context_data(self, **kwargs):
        # Add extra context
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
```

### Model Layer Interaction:

```python
# 6. Model and Database Interaction
# models.py
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

# ORM Query Processing
def get_posts():
    """
    Django ORM generates SQL queries
    """
    # This Django ORM query:
    posts = Post.objects.filter(published=True).select_related('author')
    
    # Generates SQL like:
    # SELECT post.*, author.* FROM blog_post post
    # INNER JOIN auth_user author ON post.author_id = author.id
    # WHERE post.published = true;
    
    return posts
```

### Template Rendering:

```python
# 7. Template Processing
# Template: blog/post_detail.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>{{ post.title }}</title>
</head>
<body>
    <h1>{{ post.title }}</h1>
    <p>By {{ post.author.username }} on {{ post.created_at|date:"F d, Y" }}</p>
    
    <div class="content">
        {{ post.content|linebreaks }}
    </div>
    
    <h3>Comments</h3>
    {% for comment in comments %}
        <div class="comment">
            <strong>{{ comment.author }}</strong>: {{ comment.content }}
        </div>
    {% empty %}
        <p>No comments yet.</p>
    {% endfor %}
</body>
</html>
"""

# Template Engine Processing
class TemplateRenderer:
    def render(self, template_name, context, request=None):
        # 1. Load template
        template = self.get_template(template_name)
        
        # 2. Create context
        context_instance = Context(context, request=request)
        
        # 3. Render template with context
        rendered_content = template.render(context_instance)
        
        return rendered_content
```

### Response Generation:

```python
# 8. Response Creation and Return
from django.http import HttpResponse, JsonResponse

def create_response(content, request):
    """
    Create appropriate HTTP response
    """
    if request.content_type == 'application/json':
        return JsonResponse(content)
    else:
        return HttpResponse(content, content_type='text/html')

# Response flows back through middleware chain in reverse order
def process_response_middleware(request, response):
    """
    Response processing through middleware
    """
    # Content compression
    if 'gzip' in request.META.get('HTTP_ACCEPT_ENCODING', ''):
        response = compress_response(response)
    
    # Security headers
    response['X-Content-Type-Options'] = 'nosniff'
    response['X-Frame-Options'] = 'DENY'
    
    return response
```

### Complete Request Flow Example:

```python
# Complete flow for a blog post request
"""
1. Browser requests: GET /blog/posts/1/

2. Web server (nginx) forwards to WSGI server (Gunicorn)

3. Gunicorn calls Django's WSGI application

4. Django processes through middleware:
   - SecurityMiddleware: Adds security headers
   - SessionMiddleware: Loads session data
   - AuthenticationMiddleware: Identifies user
   - CsrfMiddleware: Validates CSRF token (for POST)

5. URLResolver matches /blog/posts/1/ to:
   path('posts/<int:pk>/', views.PostDetailView.as_view())

6. PostDetailView.as_view() is called:
   - dispatch() method determines HTTP method
   - get() method is called for GET request
   - get_object() retrieves Post with pk=1
   - get_context_data() prepares template context

7. Model layer:
   - Post.objects.get(pk=1) generates SQL query
   - Database returns post data
   - Related objects (author, comments) loaded if needed

8. Template rendering:
   - blog/post_detail.html template loaded
   - Context variables replaced with actual data
   - Template tags and filters processed
   - Final HTML generated

9. Response creation:
   - HttpResponse object created with rendered HTML
   - Response flows back through middleware (reverse order)
   - Headers added, content compressed, etc.

10. WSGI server sends response back to web server

11. Web server returns response to browser
"""
```

### Error Handling in Request Flow:

```python
# Exception handling middleware
class ExceptionHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        try:
            response = self.get_response(request)
        except Http404:
            # Handle 404 errors
            return self.handle_404(request)
        except PermissionDenied:
            # Handle 403 errors
            return self.handle_403(request)
        except Exception as e:
            # Handle 500 errors
            return self.handle_500(request, e)
        
        return response
    
    def handle_404(self, request):
        return render(request, '404.html', status=404)
    
    def handle_500(self, request, exception):
        # Log error
        logger.error(f"Server error: {exception}")
        return render(request, '500.html', status=500)
```

## 65. What is the use of Celery?

**Celery** is a distributed task queue system that allows you to execute tasks asynchronously, improving application performance and user experience by offloading time-consuming operations.

### Core Concepts:

```python
# Celery Architecture Components:
"""
1. Celery Client - Sends tasks to queue
2. Message Broker - Stores task messages (Redis/RabbitMQ)
3. Celery Workers - Execute tasks
4. Result Backend - Stores task results
"""

# celery.py
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
```

### Common Use Cases:

```python
# 1. Email Processing
@shared_task
def send_bulk_emails(user_ids, email_template):
    """Send emails to multiple users asynchronously"""
    for user_id in user_ids:
        user = User.objects.get(id=user_id)
        send_mail(
            subject=email_template['subject'],
            message=email_template['body'],
            from_email='noreply@example.com',
            recipient_list=[user.email],
        )
    return f"Sent emails to {len(user_ids)} users"

# 2. Image Processing
@shared_task
def process_uploaded_image(image_path):
    """Process uploaded images (resize, watermark, etc.)"""
    from PIL import Image
    
    with Image.open(image_path) as img:
        # Create thumbnail
        img.thumbnail((800, 600), Image.Resampling.LANCZOS)
        
        # Add watermark
        watermark = Image.open('watermark.png')
        img.paste(watermark, (img.width - watermark.width, img.height - watermark.height))
        
        # Save processed image
        processed_path = image_path.replace('.jpg', '_processed.jpg')
        img.save(processed_path)
    
    return processed_path

# 3. Data Export
@shared_task
def generate_csv_export(queryset_params, user_id):
    """Generate large CSV exports"""
    import csv
    from io import StringIO
    
    # Reconstruct queryset
    objects = MyModel.objects.filter(**queryset_params)
    
    # Generate CSV
    output = StringIO()
    writer = csv.writer(output)
    
    # Write header
    writer.writerow(['ID', 'Name', 'Email', 'Created'])
    
    # Write data
    for obj in objects:
        writer.writerow([obj.id, obj.name, obj.email, obj.created_at])
    
    # Save file and notify user
    file_path = f'exports/export_{user_id}_{timezone.now().timestamp()}.csv'
    with open(file_path, 'w') as f:
        f.write(output.getvalue())
    
    # Send notification
    send_export_ready_email.delay(user_id, file_path)
    
    return file_path
```

### Advanced Task Features:

```python
# Task with retry logic
@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def process_payment(self, payment_id):
    """Process payment with retry on failure"""
    try:
        payment = Payment.objects.get(id=payment_id)
        
        # Call payment gateway
        result = payment_gateway.charge(
            amount=payment.amount,
            card_token=payment.card_token
        )
        
        # Update payment status
        payment.status = 'completed'
        payment.transaction_id = result['transaction_id']
        payment.save()
        
        return f"Payment {payment_id} processed successfully"
        
    except PaymentGatewayError as exc:
        # Retry on gateway errors
        logger.warning(f"Payment gateway error for payment {payment_id}: {exc}")
        raise self.retry(exc=exc, countdown=60 * (self.request.retries + 1))
        
    except Exception as exc:
        # Don't retry on other errors
        logger.error(f"Payment processing failed for payment {payment_id}: {exc}")
        payment.status = 'failed'
        payment.save()
        raise

# Task with progress tracking
@shared_task(bind=True)
def bulk_data_import(self, file_path):
    """Import large dataset with progress tracking"""
    total_rows = count_csv_rows(file_path)
    processed_rows = 0
    
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            # Process each row
            MyModel.objects.create(
                name=row['name'],
                email=row['email'],
                # ... other fields
            )
            
            processed_rows += 1
            
            # Update progress
            self.update_state(
                state='PROGRESS',
                meta={
                    'current': processed_rows,
                    'total': total_rows,
                    'percentage': int((processed_rows / total_rows) * 100)
                }
            )
    
    return {
        'status': 'completed',
        'processed_rows': processed_rows,
        'total_rows': total_rows
    }
```

### Periodic Tasks with Celery Beat:

```python
# settings.py
from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    # Run every day at 2:30 AM
    'cleanup-expired-sessions': {
        'task': 'myapp.tasks.cleanup_expired_sessions',
        'schedule': crontab(hour=2, minute=30),
    },
    
    # Run every Monday at 9:00 AM
    'weekly-report': {
        'task': 'myapp.tasks.generate_weekly_report',
        'schedule': crontab(hour=9, minute=0, day_of_week=1),
    },
    
    # Run every 5 minutes
    'health-check': {
        'task': 'myapp.tasks.system_health_check',
        'schedule': 300.0,  # 5 minutes in seconds
    },
    
    # Run on the first day of every month
    'monthly-billing': {
        'task': 'billing.tasks.process_monthly_billing',
        'schedule': crontab(hour=0, minute=0, day_of_month=1),
    },
}

# Periodic task examples
@shared_task
def cleanup_expired_sessions():
    """Clean up expired user sessions"""
    from django.contrib.sessions.models import Session
    from django.utils import timezone
    
    expired_sessions = Session.objects.filter(expire_date__lt=timezone.now())
    count = expired_sessions.count()
    expired_sessions.delete()
    
    return f"Cleaned up {count} expired sessions"

@shared_task
def generate_weekly_report():
    """Generate and email weekly report"""
    # Calculate weekly stats
    start_date = timezone.now() - timedelta(days=7)
    
    stats = {
        'new_users': User.objects.filter(date_joined__gte=start_date).count(),
        'new_orders': Order.objects.filter(created_at__gte=start_date).count(),
        'revenue': Order.objects.filter(
            created_at__gte=start_date,
            status='completed'
        ).aggregate(total=Sum('amount'))['total'] or 0
    }
    
    # Generate report
    report_html = render_to_string('reports/weekly_report.html', stats)
    
    # Email to administrators
    send_mail(
        subject=f'Weekly Report - {timezone.now().strftime("%Y-%m-%d")}',
        message='',
        html_message=report_html,
        from_email='reports@example.com',
        recipient_list=['admin@example.com'],
    )
    
    return f"Weekly report sent with stats: {stats}"
```

### Task Monitoring and Management:

```python
# Monitor task progress
def check_task_progress(task_id):
    """Check the progress of a running task"""
    from celery.result import AsyncResult
    
    result = AsyncResult(task_id)
    
    if result.state == 'PENDING':
        response = {
            'state': result.state,
            'progress': 0,
            'status': 'Task is waiting to be processed...'
        }
    elif result.state == 'PROGRESS':
        response = {
            'state': result.state,
            'progress': result.info.get('current', 0),
            'total': result.info.get('total', 1),
            'percentage': result.info.get('percentage', 0),
            'status': f"Processing... {result.info.get('current', 0)}/{result.info.get('total', 1)}"
        }
    elif result.state == 'SUCCESS':
        response = {
            'state': result.state,
            'progress': 100,
            'status': 'Task completed successfully',
            'result': result.result
        }
    else:  # FAILURE
        response = {
            'state': result.state,
            'progress': 100,
            'status': str(result.info),  # Error message
        }
    
    return response

# Task management views
def start_bulk_import(request):
    """Start bulk import task"""
    if request.method == 'POST':
        uploaded_file = request.FILES['csv_file']
        
        # Save uploaded file
        file_path = save_uploaded_file(uploaded_file)
        
        # Start task
        task = bulk_data_import.delay(file_path)
        
        return JsonResponse({
            'task_id': task.id,
            'status': 'Task started'
        })

def task_progress(request, task_id):
    """Get task progress"""
    progress = check_task_progress(task_id)
    return JsonResponse(progress)
```

### Task Routing and Queues:

```python
# settings.py
CELERY_TASK_ROUTES = {
    'myapp.tasks.send_email': {'queue': 'emails'},
    'myapp.tasks.process_image': {'queue': 'images'},
    'myapp.tasks.generate_report': {'queue': 'reports'},
    'myapp.tasks.high_priority_task': {'queue': 'priority'},
}

# Different worker configurations
"""
# Start workers for different queues
celery -A myproject worker -Q emails --concurrency=4
celery -A myproject worker -Q images --concurrency=2
celery -A myproject worker -Q reports --concurrency=1
celery -A myproject worker -Q priority --concurrency=8
"""

# Route tasks to specific queues
@shared_task
def send_email_task(email_data):
    # This will go to 'emails' queue
    pass

# Manual queue specification
send_email_task.apply_async(args=[email_data], queue='emails')
```

### Error Handling and Logging:

```python
import logging
from celery.signals import task_failure, task_success

logger = logging.getLogger(__name__)

@task_failure.connect
def task_failure_handler(sender=None, task_id=None, exception=None, traceback=None, einfo=None):
    """Handle task failures"""
    logger.error(f'Task {task_id} failed: {exception}')
    
    # Send alert to administrators
    send_admin_alert.delay(
        subject=f'Task Failure: {sender}',
        message=f'Task {task_id} failed with error: {exception}'
    )

@task_success.connect
def task_success_handler(sender=None, result=None, **kwargs):
    """Handle successful task completion"""
    logger.info(f'Task {sender} completed successfully')

# Custom error handling in tasks
@shared_task(bind=True)
def robust_task(self, data):
    try:
        # Task logic here
        result = process_data(data)
        return result
        
    except RetryableError as exc:
        # Retry on specific errors
        logger.warning(f"Retryable error in task {self.request.id}: {exc}")
        raise self.retry(exc=exc, countdown=60, max_retries=3)
        
    except CriticalError as exc:
        # Don't retry, but log and alert
        logger.error(f"Critical error in task {self.request.id}: {exc}")
        send_admin_alert.delay(
            subject='Critical Task Error',
            message=f'Task failed with critical error: {exc}'
        )
        raise
        
    except Exception as exc:
        # Unexpected error
        logger.exception(f"Unexpected error in task {self.request.id}")
        raise
```

### Benefits of Using Celery:

1. **Improved User Experience** - Long-running tasks don't block web requests
2. **Scalability** - Distribute work across multiple workers/servers
3. **Reliability** - Task retry mechanisms and failure handling
4. **Flexibility** - Schedule tasks, route to different queues
5. **Monitoring** - Built-in monitoring and management tools
6. **Performance** - Parallel processing of tasks

## 66. How database concurrency is handled in Django?

Django provides several mechanisms to handle database concurrency issues that arise when multiple users or processes access and modify the same data simultaneously.

### Database Locking Mechanisms:

```python
# 1. Select for Update - Row-level locking
from django.db import transaction

def transfer_money(from_account_id, to_account_id, amount):
    """Transfer money between accounts with row locking"""
    with transaction.atomic():
        # Lock the accounts for update
        from_account = Account.objects.select_for_update().get(id=from_account_id)
        to_account = Account.objects.select_for_update().get(id=to_account_id)
        
        # Check sufficient balance
        if from_account.balance < amount:
            raise InsufficientFundsError("Not enough money")
        
        # Perform transfer
        from_account.balance -= amount
        to_account.balance += amount
        
        # Save changes (locks released when transaction ends)
        from_account.save()
        to_account.save()

# 2. Select for Update with timeout and skip_locked
def process_pending_orders():
    """Process orders with locking to prevent concurrent processing"""
    with transaction.atomic():
        # Get orders that aren't locked by other processes
        orders = Order.objects.select_for_update(
            skip_locked=True  # Skip locked rows
        ).filter(status='pending')[:10]
        
        for order in orders:
            # Process order (other processes can't access this order)
            order.status = 'processing'
            order.save()
            
            # Time-consuming processing
            process_order_items(order)
            
            order.status = 'completed'
            order.save()
```

### Optimistic Concurrency Control:

```python
# Using version fields for optimistic locking
class Document(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    version = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.pk:  # Updating existing record
            # Increment version
            self.version += 1
            
            # Check for concurrent updates
            updated_rows = Document.objects.filter(
                pk=self.pk,
                version=self.version - 1  # Expected previous version
            ).update(
                title=self.title,
                content=self.content,
                version=self.version,
                updated_at=timezone.now()
            )
            
            if updated_rows == 0:
                raise ConcurrentUpdateError(
                    "Document was modified by another user"
                )
        else:
            # New record
            super().save(*args, **kwargs)

# Usage in views
def update_document(request, doc_id):
    document = get_object_or_404(Document, id=doc_id)
    
    if request.method == 'POST':
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Document updated successfully')
            except ConcurrentUpdateError:
                messages.error(request, 'Document was modified by another user. Please refresh and try again.')
        
    return render(request, 'edit_document.html', {'form': form})
```

### Database Constraints for Data Integrity:

```python
# Using database constraints to prevent race conditions
class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    reserved = models.IntegerField(default=0)
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(quantity__gte=0),
                name='quantity_non_negative'
            ),
            models.CheckConstraint(
                check=models.Q(reserved__gte=0),
                name='reserved_non_negative'
            ),
            models.CheckConstraint(
                check=models.Q(reserved__lte=models.F('quantity')),
                name='reserved_not_exceed_quantity'
            )
        ]

def reserve_inventory(product_id, quantity):
    """Reserve inventory with database constraints"""
    try:
        with transaction.atomic():
            inventory = Inventory.objects.select_for_update().get(
                product_id=product_id
            )
            
            # Check availability
            available = inventory.quantity - inventory.reserved
            if available < quantity:
                raise InsufficientInventoryError()
            
            # Reserve items (constraint ensures we don't over-reserve)
            inventory.reserved += quantity
            inventory.save()
            
    except IntegrityError:
        # Database constraint violation
        raise InsufficientInventoryError("Not enough inventory available")
```

### Atomic Transactions:

```python
# Atomic decorators and context managers
@transaction.atomic
def create_order_with_items(customer_id, items):
    """Create order with items atomically"""
    # Create order
    order = Order.objects.create(
        customer_id=customer_id,
        status='pending',
        total_amount=0
    )
    
    total_amount = 0
    
    # Create order items
    for item_data in items:
        # Check inventory
        inventory = Inventory.objects.select_for_update().get(
            product_id=item_data['product_id']
        )
        
        if inventory.quantity < item_data['quantity']:
            raise InsufficientInventoryError(
                f"Not enough {inventory.product.name} in stock"
            )
        
        # Create order item
        order_item = OrderItem.objects.create(
            order=order,
            product_id=item_data['product_id'],
            quantity=item_data['quantity'],
            price=item_data['price']
        )
        
        # Update inventory
        inventory.quantity -= item_data['quantity']
        inventory.save()
        
        total_amount += order_item.quantity * order_item.price
    
    # Update order total
    order.total_amount = total_amount
    order.save()
    
    return order

# Nested atomic transactions
def complex_business_operation():
    """Complex operation with nested transactions"""
    with transaction.atomic():  # Outer transaction
        # Main operation
        main_record = MainModel.objects.create(...)
        
        try:
            with transaction.atomic():  # Inner transaction (savepoint)
                # Risky operation
                risky_operation()
                
        except SomeException:
            # Inner transaction rolled back, outer continues
            log_error("Risky operation failed, continuing with main operation")
        
        # Complete main operation
        complete_main_operation(main_record)
```

### Race Condition Prevention:

```python
# Preventing duplicate record creation
def get_or_create_unique_slug(title):
    """Create unique slug preventing race conditions"""
    base_slug = slugify(title)
    slug = base_slug
    counter = 1
    
    while True:
        try:
            # Try to create with current slug
            with transaction.atomic():
                return Article.objects.create(
                    title=title,
                    slug=slug
                )
        except IntegrityError:
            # Slug already exists, try with counter
            slug = f"{base_slug}-{counter}"
            counter += 1
            
            if counter > 100:  # Prevent infinite loop
                raise ValueError("Unable to create unique slug")

# Using get_or_create safely
def safe_get_or_create_category(name):
    """Safely get or create category"""
    try:
        with transaction.atomic():
            category, created = Category.objects.get_or_create(
                name=name,
                defaults={'slug': slugify(name)}
            )
            return category
    except IntegrityError:
        # Another process created it between our check and create
        # Just get the existing one
        return Category.objects.get(name=name)
```

### Cache-Based Concurrency Control:

```python
from django.core.cache import cache
import time

def distributed_lock_operation(lock_key, timeout=30):
    """Perform operation with distributed lock using cache"""
    lock_id = f"lock:{lock_key}"
    
    # Try to acquire lock
    if cache.add(lock_id, "locked", timeout=timeout):
        try:
            # Perform protected operation
            return perform_critical_operation()
        finally:
            # Always release lock
            cache.delete(lock_id)
    else:
        raise ConcurrentOperationError("Operation already in progress")

# Usage
def process_user_data(user_id):
    """Process user data with distributed locking"""
    lock_key = f"user_processing_{user_id}"
    
    try:
        result = distributed_lock_operation(lock_key, timeout=300)  # 5 minutes
        return result
    except ConcurrentOperationError:
        raise ValueError("User data is already being processed")
```

### Database-Specific Concurrency Features:

```python
# PostgreSQL specific features
from django.db import connection

def update_with_returning(model_class, filter_kwargs, update_kwargs):
    """Update with RETURNING clause (PostgreSQL)"""
    with connection.cursor() as cursor:
        # Build dynamic query
        table_name = model_class._meta.db_table
        set_clause = ', '.join([f"{k} = %s" for k in update_kwargs.keys()])
        where_clause = ' AND '.join([f"{k} = %s" for k in filter_kwargs.keys()])
        
        query = f"""
            UPDATE {table_name} 
            SET {set_clause}
            WHERE {where_clause}
            RETURNING *
        """
        
        cursor.execute(query, list(update_kwargs.values()) + list(filter_kwargs.values()))
        return cursor.fetchall()

# Using advisory locks (PostgreSQL)
def with_advisory_lock(lock_id):
    """Context manager for PostgreSQL advisory locks"""
    class AdvisoryLock:
        def __enter__(self):
            with connection.cursor() as cursor:
                cursor.execute("SELECT pg_advisory_lock(%s)", [lock_id])
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            with connection.cursor() as cursor:
                cursor.execute("SELECT pg_advisory_unlock(%s)", [lock_id])
    
    return AdvisoryLock()

# Usage
def critical_section_with_advisory_lock():
    with with_advisory_lock(12345):
        # Only one process can execute this at a time
        perform_critical_operation()
```

### Monitoring and Debugging Concurrency:

```python
import logging
from django.db import transaction

logger = logging.getLogger(__name__)

def log_transaction_info(func):
    """Decorator to log transaction information"""
    def wrapper(*args, **kwargs):
        logger.info(f"Starting transaction for {func.__name__}")
        
        try:
            with transaction.atomic():
                result = func(*args, **kwargs)
                logger.info(f"Transaction {func.__name__} completed successfully")
                return result
        except Exception as e:
            logger.error(f"Transaction {func.__name__} failed: {e}")
            raise
    
    return wrapper

# Deadlock detection and retry
def retry_on_deadlock(max_retries=3):
    """Decorator to retry operations on deadlock"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except OperationalError as e:
                    if 'deadlock' in str(e).lower() and attempt < max_retries - 1:
                        logger.warning(f"Deadlock detected in {func.__name__}, retrying...")
                        time.sleep(0.1 * (2 ** attempt))  # Exponential backoff
                        continue
                    raise
        return wrapper
    return decorator
```


## Question 67: How Atomic Transactions Happen in Django

### What are Atomic Transactions?

Atomic transactions in Django ensure that a series of database operations either all succeed or all fail together. This follows the ACID (Atomicity, Consistency, Isolation, Durability) principles of database transactions. If any operation within a transaction fails, all changes are rolled back, maintaining data consistency.

### How Django Implements Atomic Transactions

#### 1. Database-Level Support
Django relies on the underlying database's transaction support. Most databases (PostgreSQL, MySQL, SQLite, Oracle) support transactions natively.

#### 2. Django's Transaction Management
Django provides several ways to handle atomic transactions:

**a) Automatic Transaction Management**
- By default, Django wraps each HTTP request in a transaction
- If the view completes successfully, the transaction is committed
- If an exception occurs, the transaction is rolled back

**b) Manual Transaction Control**
Django provides decorators and context managers for explicit transaction control.

### Methods to Implement Atomic Transactions

#### 1. Using `@transaction.atomic` Decorator

```python
from django.db import transaction
from django.http import JsonResponse
from .models import Account

@transaction.atomic
def transfer_money(request):
    from_account_id = request.POST.get('from_account')
    to_account_id = request.POST.get('to_account')
    amount = float(request.POST.get('amount'))
    
    from_account = Account.objects.get(id=from_account_id)
    to_account = Account.objects.get(id=to_account_id)
    
    # These operations will be atomic
    from_account.balance -= amount
    from_account.save()
    
    to_account.balance += amount
    to_account.save()
    
    return JsonResponse({'status': 'success'})
```

#### 2. Using `transaction.atomic()` Context Manager

```python
from django.db import transaction

def process_order(request):
    try:
        with transaction.atomic():
            # Create order
            order = Order.objects.create(
                user=request.user,
                total_amount=100.00
            )
            
            # Update inventory
            product = Product.objects.get(id=1)
            if product.quantity < 1:
                raise ValueError("Insufficient stock")
            
            product.quantity -= 1
            product.save()
            
            # Create order item
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=1
            )
            
    except Exception as e:
        return JsonResponse({'error': str(e)})
    
    return JsonResponse({'status': 'success'})
```

#### 3. Nested Transactions with Savepoints

```python
from django.db import transaction

@transaction.atomic
def complex_operation():
    # Outer transaction
    user = User.objects.create(username='newuser')
    
    try:
        with transaction.atomic():  # Inner transaction (savepoint)
            profile = Profile.objects.create(user=user, bio='Test bio')
            # Some operation that might fail
            risky_operation()
    except Exception:
        # Inner transaction rolled back, but outer continues
        # User is still created, but profile is not
        pass
    
    # This will still be committed
    user.is_active = True
    user.save()
```

### Transaction Isolation Levels

Django allows setting transaction isolation levels:

```python
from django.db import transaction

# Set isolation level
with transaction.atomic():
    # Set specific isolation level
    with connection.cursor() as cursor:
        cursor.execute("SET TRANSACTION ISOLATION LEVEL READ COMMITTED")
        # Your database operations here
```

### Best Practices for Atomic Transactions

1. **Keep transactions small and fast** - Long transactions can cause performance issues
2. **Handle exceptions properly** - Always wrap risky operations in try-catch blocks
3. **Use savepoints for nested operations** - When you need partial rollback capability
4. **Avoid external API calls within transactions** - Keep only database operations inside transactions
5. **Be careful with signals** - Django signals fired within transactions are also rolled back

### Common Pitfalls

1. **Long-running transactions** - Can cause database locks and performance issues
2. **Mixing transactional and non-transactional operations** - File operations, external API calls
3. **Not handling exceptions** - Unhandled exceptions can leave transactions in inconsistent states

---

## Question 68: Steps in Deployment of Django Application

### Pre-Deployment Preparation

#### 1. Environment Setup
- Separate development, staging, and production environments
- Use environment variables for configuration
- Create requirements.txt file
- Set up version control (Git)

#### 2. Django Settings Configuration

**Production Settings (settings/production.py):**
```python
import os
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Database configuration
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

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
```

### Deployment Steps

#### Step 1: Server Preparation

**1.1 Choose a Server**
- Cloud providers: AWS, Google Cloud, DigitalOcean, Heroku
- VPS providers: Linode, Vultr
- Platform-as-a-Service: Heroku, PythonAnywhere

**1.2 Server Setup (Ubuntu/Linux)**
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install python3 python3-pip python3-venv

# Install database (PostgreSQL example)
sudo apt install postgresql postgresql-contrib

# Install web server (Nginx)
sudo apt install nginx

# Install process manager (Supervisor)
sudo apt install supervisor
```

#### Step 2: Application Setup

**2.1 Clone Repository**
```bash
cd /var/www/
sudo git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

**2.2 Create Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**2.3 Environment Variables**
```bash
# Create .env file
sudo nano .env

# Add environment variables
SECRET_KEY=your-secret-key
DEBUG=False
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

#### Step 3: Database Setup

**3.1 Create Database**
```bash
sudo -u postgres psql
CREATE DATABASE your_db_name;
CREATE USER your_db_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE your_db_name TO your_db_user;
\q
```

**3.2 Run Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

#### Step 4: Web Server Configuration

**4.1 Gunicorn Setup**
```bash
pip install gunicorn
```

**Create Gunicorn configuration (gunicorn_config.py):**
```python
bind = "127.0.0.1:8000"
workers = 3
worker_class = "sync"
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 100
timeout = 30
keepalive = 2
preload_app = True
```

**4.2 Supervisor Configuration**
```bash
sudo nano /etc/supervisor/conf.d/yourproject.conf
```

```ini
[program:yourproject]
command=/var/www/yourproject/venv/bin/gunicorn --config gunicorn_config.py yourproject.wsgi:application
directory=/var/www/yourproject
user=www-data
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/yourproject.log
```

**4.3 Nginx Configuration**
```bash
sudo nano /etc/nginx/sites-available/yourproject
```

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    
    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /var/www/yourproject;
    }
    
    location /media/ {
        root /var/www/yourproject;
    }
    
    location / {
        include proxy_params;
        proxy_pass http://127.0.0.1:8000;
    }
}
```

**Enable site:**
```bash
sudo ln -s /etc/nginx/sites-available/yourproject /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### Step 5: SSL Certificate Setup

**5.1 Install Certbot**
```bash
sudo apt install certbot python3-certbot-nginx
```

**5.2 Obtain SSL Certificate**
```bash
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

#### Step 6: Start Services

```bash
# Start Supervisor
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start yourproject

# Start Nginx
sudo systemctl start nginx
sudo systemctl enable nginx
```

### Alternative Deployment Methods

#### 1. Docker Deployment

**Dockerfile:**
```dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "yourproject.wsgi:application"]
```

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
    depends_on:
      - db
      
  db:
    image: postgres:13
    environment:
      POSTGRES_DB: yourdb
      POSTGRES_USER: youruser
      POSTGRES_PASSWORD: yourpassword
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

#### 2. Platform-as-a-Service (Heroku)

**Procfile:**
```
web: gunicorn yourproject.wsgi:application
```

**runtime.txt:**
```
python-3.9.7
```

**Deploy commands:**
```bash
heroku create yourapp
heroku addons:create heroku-postgresql:hobby-dev
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### Post-Deployment Tasks

#### 1. Monitoring and Logging
- Set up application monitoring (New Relic, DataDog)
- Configure log rotation
- Set up error tracking (Sentry)

#### 2. Backup Strategy
- Database backups
- Media files backup
- Code repository backup

#### 3. Performance Optimization
- Enable caching (Redis, Memcached)
- Optimize database queries
- Use CDN for static files
- Enable gzip compression

#### 4. Security Measures
- Regular security updates
- Firewall configuration
- Rate limiting
- SQL injection protection
- XSS protection

### Continuous Integration/Continuous Deployment (CI/CD)

**GitHub Actions Example (.github/workflows/deploy.yml):**
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
    
    - name: Setup Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        python manage.py test
    
    - name: Deploy to server
      run: |
        # Add deployment script here
```

### Common Deployment Issues and Solutions

1. **Static Files Not Loading**
   - Run `python manage.py collectstatic`
   - Check STATIC_ROOT and STATIC_URL settings
   - Verify Nginx configuration

2. **Database Connection Errors**
   - Check database credentials
   - Verify database server is running
   - Check firewall settings

3. **Permission Errors**
   - Set correct file permissions
   - Use appropriate user (www-data)
   - Check directory ownership

4. **Memory Issues**
   - Optimize Gunicorn worker count
   - Monitor memory usage
   - Consider upgrading server resources

This comprehensive guide covers both atomic transactions in Django and the complete deployment process, providing practical examples and best practices for production deployment.