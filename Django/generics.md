# Understanding and Implementing Views in Django Rest Framework

## What is a View?

In Django's MVT pattern, a **View** handles the logic for processing HTTP requests. It retrieves data from the Model and returns an HTTP response (HTML, JSON, redirect, 404, etc.).

Views live in `views.py` inside your Django app.

### Analogy

| Restaurant | Django |
|---|---|
| Customer makes an order | HTTP Request |
| Waiter takes the order | Django View handles the request |
| Kitchen prepares the food | Business logic (DB queries, Python processing) |
| Waiter delivers food | HTTP Response returned to client |

---

## Setup

```bash
django-admin startproject viewProject .
python manage.py startapp viewApp
```

**`settings.py`**
```python
INSTALLED_APPS = [
    ...
    "rest_framework",
    "viewApp",
]
```

**`models.py`**
```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    num_pages = models.IntegerField()

    def __str__(self):
        return self.title
```

**`serializers.py`**
```python
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'num_pages']
```

**`urls.py` (project level)**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("viewApp.urls")),
]
```

---

## Types of Views

```
Views
├── 1. Function-Based Views (FBVs)
└── 2. Class-Based Views (CBVs)
    ├── A. APIView          → rest_framework.views
    ├── B. Generic Views    → rest_framework.generics
    │   ├── GenericAPIView
    │   ├── Mixins
    │   └── Concrete Generic Views
    └── C. ViewSets         → rest_framework.viewsets
```

---

## 1. Function-Based Views (FBVs)

Simple Python functions decorated with `@api_view`.

**`views.py`**
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

**`urls.py`**
```python
from django.urls import path
from .views import book_list

urlpatterns = [
    path("view/", book_list, name="my-view"),
]
```

**Pros & Cons**

| ✅ Advantages | ❌ Disadvantages |
|---|---|
| Simple and easy to understand | Code duplication across HTTP methods |
| Fine-grained control | Less reusable as app grows |

---

## 2. Class-Based Views (CBVs)

### A. `APIView` — `rest_framework.views`

Base class for all CBVs in DRF. You define methods (`get`, `post`, `patch`, `delete`) explicitly.

**`views.py`**
```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookApiView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({"success": True, "message": "successful get", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": "successful post", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"success": False, "message": "failed post", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class BookApiInstanceView(APIView):

    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book)
            return Response({"success": True, "message": "successful get", "data": serializer.data}, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({"success": False, "message": "Pk does not exist", "data": ""}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                book.title = serializer.data['title']
                book.save()
                return Response({"success": True, "message": "successful patch", "data": serializer.data}, status=status.HTTP_201_CREATED)
        except Book.DoesNotExist:
            return Response({"success": False, "message": "Pk does not exist", "data": ""}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response({"success": True, "message": "successful delete", "data": ""}, status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response({"success": False, "message": "Pk does not exist", "data": ""}, status=status.HTTP_400_BAD_REQUEST)
```

**`urls.py`**
```python
from django.urls import path
from .views import BookApiView, BookApiInstanceView

urlpatterns = [
    path("view/", BookApiView.as_view()),
    path("view/<str:pk>", BookApiInstanceView.as_view()),
]
```

---

### B. `generics` — `rest_framework.generics`

#### i. `GenericAPIView`

Extends `APIView`. Adds `queryset` and `serializer_class` attributes, simplifying model-based views.

```python
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookGenericAPIView(GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

#### ii. Mixins

Mixins add pre-built action methods. Combined with `GenericAPIView`.

| Mixin | Action |
|---|---|
| `ListModelMixin` | `.list()` |
| `CreateModelMixin` | `.create()` |
| `RetrieveModelMixin` | `.retrieve()` |
| `UpdateModelMixin` | `.update()` |
| `DestroyModelMixin` | `.destroy()` |

```python
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .models import Book
from .serializers import BookSerializer

class BookListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```

#### iii. Concrete Generic Views

Pre-built views combining `GenericAPIView` + the appropriate mixins. Minimal code required.

| View | HTTP Methods | Use Case |
|---|---|---|
| `CreateAPIView` | POST | Create only |
| `ListAPIView` | GET | List only |
| `RetrieveAPIView` | GET | Single instance |
| `DestroyAPIView` | DELETE | Delete only |
| `UpdateAPIView` | PUT, PATCH | Update only |
| `ListCreateAPIView` | GET, POST | List + Create |
| `RetrieveUpdateAPIView` | GET, PUT, PATCH | Retrieve + Update |
| `RetrieveDestroyAPIView` | GET, DELETE | Retrieve + Delete |
| `RetrieveUpdateDestroyAPIView` | GET, PUT, PATCH, DELETE | Full instance CRUD |

```python
from rest_framework.generics import ListCreateAPIView
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

---

### C. `ViewSets` — `rest_framework.viewsets`

Groups all related CRUD actions into a single class. Use with **Routers** to auto-generate URL patterns.

**`views.py`**
```python
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

**`urls.py`**
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookModelViewSet

router = DefaultRouter()
router.register(r"view", BookModelViewSet, basename="book")

urlpatterns = [
    path("", include(router.urls)),
]
```

**Auto-generated URLs from Router:**

| URL | Method | Action |
|---|---|---|
| `/view/` | GET | list |
| `/view/` | POST | create |
| `/view/{pk}/` | GET | retrieve |
| `/view/{pk}/` | PUT/PATCH | update |
| `/view/{pk}/` | DELETE | destroy |

---

## Summary: Which View to Use?

| Scenario | Recommended View |
|---|---|
| Simple, one-off endpoint | FBV with `@api_view` |
| Full control over request/response format | `APIView` |
| Standard CRUD, some customization needed | Concrete Generic View |
| Full REST resource with minimal boilerplate | `ModelViewSet` + Router |

---

## Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Authentication & Permissions

DRF provides built-in classes to control **who** can access a view and **what** they can do.

### Authentication Classes

| Class | Description |
|---|---|
| `BasicAuthentication` | Username/password via HTTP Basic Auth |
| `SessionAuthentication` | Django session-based (browser clients) |
| `TokenAuthentication` | Token in `Authorization: Token <token>` header |
| `JWTAuthentication` | JWT tokens (requires `djangorestframework-simplejwt`) |

**Global config in `settings.py`:**
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}
```

**Per-view override:**
```python
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class BookApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        ...
```

### Permission Classes

| Class | Description |
|---|---|
| `AllowAny` | Open to everyone (default if not set) |
| `IsAuthenticated` | Must be logged in |
| `IsAdminUser` | Must be `is_staff=True` |
| `IsAuthenticatedOrReadOnly` | Read-only for anonymous, full access for authenticated |
| `DjangoModelPermissions` | Tied to Django's model-level permissions |

**Global config:**
```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

**Custom permission:**
```python
from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
```

---

## Throttling (Rate Limiting)

Controls how many requests a user can make in a given time window.

| Class | Description |
|---|---|
| `AnonRateThrottle` | Limits anonymous users by IP |
| `UserRateThrottle` | Limits authenticated users |
| `ScopedRateThrottle` | Per-view rate limits using a scope name |

**`settings.py`:**
```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/minute',
        'user': '100/minute',
    }
}
```

**Per-view override:**
```python
from rest_framework.throttling import UserRateThrottle

class BookApiView(APIView):
    throttle_classes = [UserRateThrottle]
    ...
```

---

## Pagination

Controls how list responses are split into pages.

| Class | Style |
|---|---|
| `PageNumberPagination` | `?page=2` |
| `LimitOffsetPagination` | `?limit=10&offset=20` |
| `CursorPagination` | Encrypted cursor (most efficient for large data) |

**Global config in `settings.py`:**
```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
```

**Custom pagination class:**
```python
from rest_framework.pagination import PageNumberPagination

class BookPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100
```

**Using in a view:**
```python
class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination
```

> **Note:** Pagination is only applied automatically on list views (e.g., `ListAPIView`, `ModelViewSet.list`). Manual `APIView` responses require calling `paginate_queryset()` and `get_paginated_response()` explicitly.

---

## Filtering

### Basic Filtering (manual)

```python
class BookListAPIView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        author = self.request.query_params.get('author')
        qs = Book.objects.all()
        if author:
            qs = qs.filter(author=author)
        return qs
```

### `django-filter` Integration

Install: `pip install django-filter`

```python
# settings.py
INSTALLED_APPS = [..., 'django_filters']

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}
```

```python
from django_filters.rest_framework import DjangoFilterBackend

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'num_pages']   # ?author=Tolkien&num_pages=400
```

### Search & Ordering Backends

```python
from rest_framework.filters import SearchFilter, OrderingFilter

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'author']       # ?search=tolkien
    ordering_fields = ['title', 'num_pages']  # ?ordering=-num_pages
    ordering = ['title']                       # default ordering
```

---

## Custom Actions with `@action` (ViewSets)

Use `@action` to add non-standard endpoints to a ViewSet beyond the default CRUD.

```python
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Detail action  →  GET /view/{pk}/summary/
    @action(detail=True, methods=['get'])
    def summary(self, request, pk=None):
        book = self.get_object()
        return Response({
            'title': book.title,
            'author': book.author,
            'pages': book.num_pages,
        })

    # List action  →  POST /view/bulk_create/
    @action(detail=False, methods=['post'])
    def bulk_create(self, request):
        serializer = BookSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
```

| Parameter | Description |
|---|---|
| `detail=True` | Operates on a single instance (`/{pk}/action/`) |
| `detail=False` | Operates on the collection (`/action/`) |
| `methods` | List of allowed HTTP methods |
| `url_path` | Custom URL segment (defaults to method name) |
| `permission_classes` | Override permissions for this action only |

---

## ViewSet Types

DRF ships with multiple ViewSet base classes, not just `ModelViewSet`.

| ViewSet Class | Provides |
|---|---|
| `ViewSet` | Empty base; you define every action manually |
| `GenericViewSet` | `GenericAPIView` base + router support; no actions by default |
| `ReadOnlyModelViewSet` | `list` + `retrieve` only (GET) |
| `ModelViewSet` | Full CRUD: `list`, `create`, `retrieve`, `update`, `partial_update`, `destroy` |

**`ReadOnlyModelViewSet` example:**
```python
from rest_framework import viewsets

class BookReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Exposes GET /books/ and GET /books/{pk}/ only
```

---

## Routers

| Router | Description |
|---|---|
| `SimpleRouter` | Generates standard routes, no root API view |
| `DefaultRouter` | Same as `SimpleRouter` + adds a browsable root API endpoint |

```python
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()
router.register(r'books', BookModelViewSet, basename='book')

# Generated URLs:
# GET/POST   /books/
# GET        /books/{pk}/
# PUT/PATCH  /books/{pk}/
# DELETE     /books/{pk}/
# GET        /books/{pk}/summary/      ← custom @action
# POST       /books/bulk_create/       ← custom @action
```

---

## Response & Status Codes

Always use `rest_framework.response.Response` and `rest_framework.status` constants — never raw integers.

```python
from rest_framework.response import Response
from rest_framework import status

# Common status constants
status.HTTP_200_OK            # GET success
status.HTTP_201_CREATED       # POST success
status.HTTP_204_NO_CONTENT    # DELETE success (no body)
status.HTTP_400_BAD_REQUEST   # Validation error
status.HTTP_401_UNAUTHORIZED  # Not authenticated
status.HTTP_403_FORBIDDEN     # Authenticated but no permission
status.HTTP_404_NOT_FOUND     # Object not found
```

**Consistent response envelope pattern:**
```python
return Response({
    "success": True,
    "message": "Books fetched successfully",
    "data": serializer.data
}, status=status.HTTP_200_OK)
```

---

## Exception Handling

### `get_object_or_404`

```python
from rest_framework.generics import get_object_or_404

book = get_object_or_404(Book, pk=pk)
```

### Custom Exception Handler

```python
# exceptions.py
from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data = {
            "success": False,
            "message": response.data.get('detail', 'An error occurred'),
            "data": None,
        }
    return response
```

```python
# settings.py
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'viewApp.exceptions.custom_exception_handler'
}
```

---

## Complete Feature Comparison

| Feature | FBV | APIView | GenericAPIView | Concrete Generic | ModelViewSet |
|---|:---:|:---:|:---:|:---:|:---:|
| Simplicity | ✅ | ✅ | ✅ | ✅✅ | ✅✅✅ |
| Fine-grained control | ✅✅✅ | ✅✅✅ | ✅✅ | ✅ | ✅ |
| Code reuse / DRY | ❌ | ✅ | ✅✅ | ✅✅✅ | ✅✅✅ |
| Auto URL generation | ❌ | ❌ | ❌ | ❌ | ✅ (Router) |
| Built-in pagination | ❌ | ❌ | ✅ | ✅ | ✅ |
| Built-in filtering | ❌ | ❌ | ✅ | ✅ | ✅ |
| Custom actions | ❌ | ✅ (manual) | ✅ (manual) | ✅ (manual) | ✅ (`@action`) |
| Best for | One-offs | Custom logic | Mixed CRUD | Standard CRUD | Full REST resource |

---

## Quick Reference: Import Cheatsheet

```python
# Views
from rest_framework.decorators import api_view          # FBV decorator
from rest_framework.views import APIView                 # Base CBV
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView, CreateAPIView,
    RetrieveAPIView, UpdateAPIView, DestroyAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView, RetrieveDestroyAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import viewsets                      # ViewSets

# Router
from rest_framework.routers import DefaultRouter, SimpleRouter

# Response & Status
from rest_framework.response import Response
from rest_framework import status

# Auth & Permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

# Throttling
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

# Pagination
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

# Filtering
from rest_framework.filters import SearchFilter, OrderingFilter

# Custom action
from rest_framework.decorators import action

# Mixins
from rest_framework.mixins import (
    ListModelMixin, CreateModelMixin,
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin,
)
```