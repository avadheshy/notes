# DRF Views — Complete Reference

---

## Table of Contents

- [DRF Views — Complete Reference](#drf-views--complete-reference)
  - [Table of Contents](#table-of-contents)
  - [1. Django View Basics](#1-django-view-basics)
  - [2. Function-Based Views (FBV)](#2-function-based-views-fbv)
  - [3. APIView](#3-apiview)
  - [4. GenericAPIView](#4-genericapiview)
  - [5. Mixins](#5-mixins)
  - [6. Concrete Generic Views](#6-concrete-generic-views)
  - [7. GenericViewSet](#7-genericviewset)
  - [8. ViewSet](#8-viewset)
  - [9. ModelViewSet](#9-modelviewset)
  - [10. Custom Queries](#10-custom-queries)
    - [10.1 `get_queryset()` — filter the list](#101-get_queryset--filter-the-list)
    - [10.2 IDOR Protection](#102-idor-protection)
    - [10.3 `get_object()` — custom single-object lookup](#103-get_object--custom-single-object-lookup)
    - [10.4 `perform_create()` — inject fields before save](#104-perform_create--inject-fields-before-save)
    - [10.5 `perform_update()` — hook before update](#105-perform_update--hook-before-update)
    - [10.6 `perform_destroy()` — soft delete](#106-perform_destroy--soft-delete)
    - [10.7 `get_serializer_class()` — different serializer per action](#107-get_serializer_class--different-serializer-per-action)
    - [10.8 Annotated queryset example](#108-annotated-queryset-example)
  - [11. Custom Actions](#11-custom-actions)
  - [12. URL Routing Summary](#12-url-routing-summary)
    - [Manual URL (APIView, GenericAPIView, Concrete views)](#manual-url-apiview-genericapiview-concrete-views)
    - [Router URL (ViewSet, GenericViewSet, ModelViewSet)](#router-url-viewset-genericviewset-modelviewset)
  - [13. Override Hook Cheatsheet](#13-override-hook-cheatsheet)
  - [14. When to Use What](#14-when-to-use-what)
    - [FBV vs CBV summary](#fbv-vs-cbv-summary)
  - [Quick Reference: View Hierarchy](#quick-reference-view-hierarchy)

---

## 1. Django View Basics

Every Django view must:
- Be **callable** (function or class with `.as_view()`)
- Accept an `HttpRequest` as its first positional argument
- Return an `HttpResponse` or raise an exception

CBVs inherit `as_view()`, which calls `dispatch()` internally — this routes the request to the correct method (`get()`, `post()`, etc.) based on the HTTP verb.

---

## 2. Function-Based Views (FBV)

Simple Python functions decorated with `@api_view`.

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

**URL:**
```python
path('books/', book_list),
```

**Pros:** Simple, explicit, easy to read, good for one-off views.  
**Cons:** Repetitive for CRUD-heavy apps, harder to reuse/extend.

---

## 3. APIView

Base class for all DRF class-based views. Full manual control — no built-in queryset or serializer helpers.

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Book
from .serializers import BookSerializer

class BookListView(APIView):

    def get(self, request):
        books = Book.objects.filter(owner=request.user)  # custom query inline
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)          # inject field on save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailView(APIView):

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk, owner=request.user)  # IDOR safe
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def patch(self, request, pk):
        book = get_object_or_404(Book, pk=pk, owner=request.user)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk, owner=request.user)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

**URL:**
```python
path('books/',      BookListView.as_view()),
path('books/<int:pk>/', BookDetailView.as_view()),
```

**When to use:** Highly customised APIs, non-model responses, aggregations, proxying external services.

---

## 4. GenericAPIView

Extends `APIView` with queryset/serializer support and helper methods. **Does NOT auto-provide CRUD** — you still write every HTTP method manually, but now you use `self.get_queryset()` and `self.get_serializer()` instead of raw ORM calls.

```python
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookListView(GenericAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):                          # custom query here
        return Book.objects.filter(owner=self.request.user)

    def get(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

**Key attributes and methods:**

| Attribute / Method       | Purpose                                               |
|--------------------------|-------------------------------------------------------|
| `queryset`               | Default queryset (class-level, static)                |
| `serializer_class`       | Serializer to use                                     |
| `lookup_field`           | Field used for single-object lookup (default: `pk`)   |
| `pagination_class`       | Paginator class                                       |
| `filter_backends`        | List of filter backend classes                        |
| `get_queryset()`         | Override for dynamic queryset                         |
| `get_object()`           | Override for custom single-object lookup              |
| `get_serializer()`       | Returns serializer instance                           |
| `get_serializer_class()` | Override to switch serializer per action/user         |
| `filter_queryset(qs)`    | Applies filter backends to a queryset                 |
| `paginate_queryset(qs)`  | Paginates queryset, returns page or None              |

**URL:** Same as APIView — manage manually.

---

## 5. Mixins

Pre-built action methods that work on top of `GenericAPIView`. Each mixin adds one method you call explicitly from your HTTP handler.

```python
from rest_framework import mixins
from rest_framework.generics import GenericAPIView

class BookListCreateView(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         GenericAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```

**All 5 mixins:**

| Mixin                 | Method added   | HTTP verb | Action               |
|-----------------------|----------------|-----------|----------------------|
| `ListModelMixin`      | `list()`       | GET       | Return list          |
| `CreateModelMixin`    | `create()`     | POST      | Create instance      |
| `RetrieveModelMixin`  | `retrieve()`   | GET       | Return single object |
| `UpdateModelMixin`    | `update()` / `partial_update()` | PUT/PATCH | Update instance |
| `DestroyModelMixin`   | `destroy()`    | DELETE    | Delete instance      |

**Mixin source (what they do internally):**

```python
class CreateModelMixin:
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()                        # ← override this to inject fields


class ListModelMixin:
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class DestroyModelMixin:
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()                        # ← override for soft delete
```

**URL:** Manage manually.

---

## 6. Concrete Generic Views

Pre-built views that combine a mixin + `GenericAPIView` in one class. Most commonly used in practice.

```python
from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveAPIView,
    UpdateAPIView, DestroyAPIView,
    ListCreateAPIView, RetrieveUpdateAPIView,
    RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
)
```

**All concrete views:**

| Class                          | Mixins used                             | Methods available        |
|--------------------------------|-----------------------------------------|--------------------------|
| `ListAPIView`                  | List                                    | GET (list)               |
| `CreateAPIView`                | Create                                  | POST                     |
| `RetrieveAPIView`              | Retrieve                                | GET (detail)             |
| `UpdateAPIView`                | Update                                  | PUT, PATCH               |
| `DestroyAPIView`               | Destroy                                 | DELETE                   |
| `ListCreateAPIView`            | List + Create                           | GET, POST                |
| `RetrieveUpdateAPIView`        | Retrieve + Update                       | GET, PUT, PATCH          |
| `RetrieveDestroyAPIView`       | Retrieve + Destroy                      | GET, DELETE              |
| `RetrieveUpdateDestroyAPIView` | Retrieve + Update + Destroy             | GET, PUT, PATCH, DELETE  |

**Minimal usage:**
```python
class BookListCreateView(ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)
```

**URL:**
```python
path('books/',          BookListCreateView.as_view()),
path('books/<int:pk>/', BookDetailView.as_view()),
```

**Overriding a method to customise response:**
```python
class BookCreateView(CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data['message'] = 'Book created successfully'
        return response
```

---

## 7. GenericViewSet

`GenericAPIView` + `ViewSet` behaviour. Uses router for URL generation but does **NOT** auto-provide CRUD. You combine it with mixins to pick exactly which actions you want.

```python
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

# Read-only viewset (list + retrieve, no create/update/delete)
class BookReadOnlyViewSet(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          GenericViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)
```

```python
# LCRD viewset (no update)
class BookLCRDViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
```

**URL with router:**
```python
router = DefaultRouter()
router.register(r'books', BookReadOnlyViewSet, basename='book')
urlpatterns = [path('', include(router.urls))]
```

**When to use:** You want router-generated URLs but need to restrict which actions are available.

---

## 8. ViewSet

Bare ViewSet — flexible, not tied to a model. You write `list()`, `retrieve()`, `create()`, etc. yourself. Uses router.

```python
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class BookViewSet(ViewSet):

    def list(self, request):
        books = Book.objects.filter(owner=request.user)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk, owner=request.user)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def create(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk, owner=request.user)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def partial_update(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk, owner=request.user)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk, owner=request.user)
        book.delete()
        return Response(status=204)
```

**URL:**
```python
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
```

**When to use:** Non-model responses, aggregation endpoints, proxying another service, or when you want router URL generation without model assumptions.

---

## 9. ModelViewSet

The highest-level view. Full CRUD auto-provided. Needs only `queryset` + `serializer_class`.

```python
from rest_framework.viewsets import ModelViewSet

class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
```

**URL:**
```python
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
urlpatterns = [path('', include(router.urls))]
```

**URLs auto-generated by router:**

| URL pattern             | Method | Action          |
|-------------------------|--------|-----------------|
| `/books/`               | GET    | `list()`        |
| `/books/`               | POST   | `create()`      |
| `/books/{pk}/`          | GET    | `retrieve()`    |
| `/books/{pk}/`          | PUT    | `update()`      |
| `/books/{pk}/`          | PATCH  | `partial_update()` |
| `/books/{pk}/`          | DELETE | `destroy()`     |

**ModelViewSet internally is just:**
```python
class ModelViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,
                   DestroyModelMixin, ListModelMixin, GenericViewSet):
    pass
```

**Overridable methods:**

| Method                  | Called by              | Override reason                                  |
|-------------------------|------------------------|--------------------------------------------------|
| `get_queryset()`        | All actions            | Filter by user, query params, tenant             |
| `get_object()`          | retrieve/update/destroy| Custom lookup (slug, composite key), IDOR check  |
| `get_serializer_class()`| All actions            | Different serializer for list vs detail          |
| `perform_create()`      | `create()`             | Auto-assign fields, trigger side effects         |
| `perform_update()`      | `update()`             | Audit logs, modified_by                          |
| `perform_destroy()`     | `destroy()`            | Soft delete instead of hard delete               |
| `list()`                | GET list               | Custom response shape                            |
| `retrieve()`            | GET detail             | Custom response shape                            |
| `create()`              | POST                   | Custom response, pre-validation logic            |

---

## 10. Custom Queries

This is the most important section for real-world usage. The articles use `queryset = Model.objects.all()` only for simplicity — in production you always customise.

### 10.1 `get_queryset()` — filter the list

Override this instead of setting the static `queryset =` attribute whenever the result depends on the request.

```python
class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        # Base: scope to current user (multi-tenant / IDOR protection)
        qs = Book.objects.filter(owner=self.request.user)

        # Search: GET /books/?q=django
        q = self.request.query_params.get('q')
        if q:
            qs = qs.filter(title__icontains=q)

        # Filter: GET /books/?status=published
        status = self.request.query_params.get('status')
        if status:
            qs = qs.filter(status=status)

        # Ordering: GET /books/?ordering=-created_at
        ordering = self.request.query_params.get('ordering', '-created_at')
        qs = qs.order_by(ordering)

        return qs.select_related('author').prefetch_related('tags')
```

### 10.2 IDOR Protection

**Always scope `get_queryset()` to the current user.** If you leave `queryset = Book.objects.all()`, a logged-in user can access any other user's object by guessing the pk.

```python
# BAD — user can GET /books/999/ even if it belongs to someone else
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()           # ← exposes all records
    serializer_class = BookSerializer

# GOOD — get_queryset scopes all actions automatically
class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)
    # Now GET /books/999/ returns 404 if not the request user's book
    # This applies to retrieve, update, destroy too — get_object() calls get_queryset()
```

### 10.3 `get_object()` — custom single-object lookup

```python
class BookDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer

    def get_object(self):
        # Lookup by slug instead of pk
        obj = get_object_or_404(
            Book,
            slug=self.kwargs['slug'],
            owner=self.request.user        # IDOR protection
        )
        self.check_object_permissions(self.request, obj)   # run permission classes
        return obj
```

```python
# URL for slug-based lookup
path('books/<slug:slug>/', BookDetailView.as_view()),
```

### 10.4 `perform_create()` — inject fields before save

```python
class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def perform_create(self, serializer):
        serializer.save(
            owner=self.request.user,
            created_by_ip=self.request.META.get('REMOTE_ADDR'),
        )
```

### 10.5 `perform_update()` — hook before update

```python
    def perform_update(self, serializer):
        serializer.save(last_edited_by=self.request.user)
```

### 10.6 `perform_destroy()` — soft delete

```python
    def perform_destroy(self, instance):
        instance.is_deleted = True          # soft delete instead of .delete()
        instance.save()
```

### 10.7 `get_serializer_class()` — different serializer per action

```python
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return BookListSerializer       # lightweight for list
        return BookDetailSerializer         # full fields for detail/create/update
```

### 10.8 Annotated queryset example

```python
from django.db.models import Count, Avg

class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        return (
            Book.objects
            .filter(owner=self.request.user)
            .annotate(
                review_count=Count('reviews'),
                avg_rating=Avg('reviews__rating'),
            )
            .select_related('author', 'category')
            .prefetch_related('tags')
            .order_by('-created_at')
        )
```

---

## 11. Custom Actions

Use `@action` to add endpoints beyond standard CRUD inside a ViewSet.

```python
from rest_framework.decorators import action
from rest_framework.response import Response

class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)

    # Collection action — URL: POST /books/bulk_delete/
    @action(detail=False, methods=['post'])
    def bulk_delete(self, request):
        ids = request.data.get('ids', [])
        Book.objects.filter(pk__in=ids, owner=request.user).delete()
        return Response({'deleted': len(ids)})

    # Detail action — URL: POST /books/{pk}/mark_as_read/
    @action(detail=True, methods=['post'])
    def mark_as_read(self, request, pk=None):
        book = self.get_object()
        book.status = 'read'
        book.save()
        return Response({'status': 'book marked as read'})

    # Detail GET action — URL: GET /books/{pk}/reviews/
    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        book = self.get_object()
        reviews = book.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    # Custom serializer for an action
    @action(detail=False, methods=['get'])
    def published(self, request):
        qs = self.get_queryset().filter(status='published')
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
```

**`@action` parameters:**

| Parameter            | Values              | Meaning                                                   |
|----------------------|---------------------|-----------------------------------------------------------|
| `detail`             | `True` / `False`    | `True` = operates on single object (`/{pk}/action/`); `False` = collection (`/action/`) |
| `methods`            | list of HTTP verbs  | e.g. `['get']`, `['post']`, `['get', 'post']`             |
| `url_path`           | string              | Custom URL segment (default: method name)                 |
| `url_name`           | string              | Custom name for URL reversing                             |
| `permission_classes` | list                | Override permissions for this action only                 |

---

## 12. URL Routing Summary

### Manual URL (APIView, GenericAPIView, Concrete views)

```python
from django.urls import path
from .views import BookListCreateView, BookDetailView

urlpatterns = [
    path('books/',          BookListCreateView.as_view()),
    path('books/<int:pk>/', BookDetailView.as_view()),
]
```

### Router URL (ViewSet, GenericViewSet, ModelViewSet)

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]
```

**Which views need which URL approach:**

| View Type             | URL approach   |
|-----------------------|----------------|
| FBV                   | Manual         |
| APIView               | Manual         |
| GenericAPIView        | Manual         |
| Mixins + GenericAPIView | Manual       |
| Concrete views        | Manual         |
| GenericViewSet        | Router         |
| ViewSet               | Router         |
| ModelViewSet          | Router         |

---

## 13. Override Hook Cheatsheet

```
┌─────────────────────────────────────────────────────────────────┐
│  Hook                  │ When it runs            │ Common use   │
├─────────────────────────────────────────────────────────────────┤
│  get_queryset()        │ All list/detail actions │ Filter by    │
│                        │                         │ user, params │
├─────────────────────────────────────────────────────────────────┤
│  get_object()          │ retrieve/update/destroy │ Slug lookup, │
│                        │                         │ IDOR check   │
├─────────────────────────────────────────────────────────────────┤
│  get_serializer_class()│ Every request           │ Different    │
│                        │                         │ list/detail  │
│                        │                         │ serializers  │
├─────────────────────────────────────────────────────────────────┤
│  perform_create()      │ After POST validated    │ Auto-assign  │
│                        │                         │ owner, IP    │
├─────────────────────────────────────────────────────────────────┤
│  perform_update()      │ After PUT/PATCH valid.  │ Audit fields │
├─────────────────────────────────────────────────────────────────┤
│  perform_destroy()     │ Before DELETE           │ Soft delete  │
├─────────────────────────────────────────────────────────────────┤
│  list()                │ GET collection          │ Custom shape │
├─────────────────────────────────────────────────────────────────┤
│  create()              │ POST                    │ Custom resp. │
└─────────────────────────────────────────────────────────────────┘
```

---

## 14. When to Use What

```
┌──────────────────────────────────────────────────────────────────┐
│  Situation                           │ Recommended view          │
├──────────────────────────────────────────────────────────────────┤
│  Simple one-off logic, 1-2 methods   │ FBV or APIView            │
│  Non-model response (aggregation,    │ APIView or ViewSet        │
│  external API proxy)                 │                           │
│  Standard CRUD, full control needed  │ Concrete generic view     │
│  Standard CRUD, minimal code         │ ModelViewSet              │
│  Some CRUD actions, not all          │ GenericViewSet + mixins   │
│  Custom actions beyond CRUD          │ ModelViewSet + @action    │
│  Non-model viewset with router URLs  │ ViewSet                   │
└──────────────────────────────────────────────────────────────────┘
```

### FBV vs CBV summary

| Feature          | FBV                        | CBV                            |
|------------------|----------------------------|--------------------------------|
| Simplicity       | Very simple, explicit      | More abstraction               |
| Reusability      | Low                        | High — inheritance and mixins  |
| Best for         | Small / one-off views      | CRUD-heavy apps, DRY code      |
| Decorators       | `@api_view`, `@permission_required` | Mixins like `IsAuthenticated` |
| HTTP dispatch    | Manual `if request.method` | Auto via `dispatch()`          |

---

## Quick Reference: View Hierarchy

```
HttpRequest
    │
    ▼
FBV (@api_view)
    │
    ▼
APIView                         ← full manual control
    │
    ▼
GenericAPIView                  ← adds get_queryset(), get_serializer()
    │
    ├── + Mixin(s)              ← adds list(), create(), retrieve() etc.
    │       │
    │       └── ConcreteView    ← ListCreateAPIView, RetrieveUpdateDestroyAPIView, etc.
    │
    └── GenericViewSet          ← GenericAPIView + ViewSet routing
            │
            ├── + Mixin(s)      ← custom partial CRUD viewset
            │
            └── ModelViewSet   ← full CRUD auto-provided
```