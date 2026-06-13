# Django REST Framework — Complete Views Reference

---

## The Big Picture (Mental Model First)

```
Django Views
│
├── FBV  (Function-Based Views)          @api_view decorator
│
└── CBV  (Class-Based Views)
    │
    ├── APIView                          raw CBV, you write everything
    │
    ├── Generic Views (generics.*)       APIView + mixins baked in
    │   ├── GenericAPIView               base class, no actions alone
    │   ├── Concrete Generic Views       GenericAPIView + 1-2 mixins
    │   │   ├── ListAPIView
    │   │   ├── CreateAPIView
    │   │   ├── RetrieveAPIView
    │   │   ├── UpdateAPIView
    │   │   ├── DestroyAPIView
    │   │   ├── ListCreateAPIView
    │   │   ├── RetrieveUpdateAPIView
    │   │   ├── RetrieveDestroyAPIView
    │   │   └── RetrieveUpdateDestroyAPIView
    │   └── Mixins (mixed in above)
    │       ├── ListModelMixin
    │       ├── CreateModelMixin
    │       ├── RetrieveModelMixin
    │       ├── UpdateModelMixin
    │       └── DestroyModelMixin
    │
    └── ViewSets (viewsets.*)            CBV + Router magic
        ├── ViewSet                      raw, you define actions
        ├── GenericViewSet               ViewSet + GenericAPIView
        ├── ModelViewSet                 full CRUD auto
        └── ReadOnlyModelViewSet         list + retrieve only
```

---

## 1. Function-Based Views (FBV)

The simplest entry point. A plain Python function decorated with `@api_view`.

### 1.1 Basic FBV

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

### 1.2 FBV with authentication/permission decorators

```python
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({'message': f'Hello {request.user.username}'})
```

### 1.3 FBV URLs

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:pk>/', views.article_detail),
]
```

**When to use FBV:** one-off endpoints, simple logic, quick prototypes, or when the view doesn't map cleanly to CRUD.

---

## 2. APIView (Raw Class-Based View)

`APIView` is the base class for all DRF CBVs. It gives you request parsing, authentication, permissions, throttling — but zero business logic. You write every HTTP method handler yourself.

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Article
from .serializers import ArticleSerializer


class ArticleListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)    # inject extra data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

```python
# urls.py
urlpatterns = [
    path('articles/', ArticleListView.as_view()),
    path('articles/<int:pk>/', ArticleDetailView.as_view()),
]
```

**When to use APIView:** non-standard logic (e.g., aggregating multiple models, custom actions), or when generic views would require more overrides than they save.

---

## 3. Generic Views

This is where DRF eliminates boilerplate. Three layers build on each other:

```
GenericAPIView          ← base: queryset, serializer_class, lookup_field hooks
    + Mixins            ← list(), create(), retrieve(), update(), destroy()
        = Concrete views ← ready-to-use classes (ListAPIView, etc.)
```

### 3.1 GenericAPIView (base, never used alone)

`GenericAPIView` extends `APIView` and adds:

| Attribute / Method | Purpose |
|---|---|
| `queryset` | default queryset |
| `serializer_class` | default serializer |
| `lookup_field` | URL kwarg for single-object lookup (default: `pk`) |
| `lookup_url_kwarg` | override the URL kwarg name |
| `filter_backends` | list of filter classes |
| `pagination_class` | pagination class |
| `get_queryset()` | override for dynamic queryset |
| `get_serializer_class()` | override for dynamic serializer |
| `get_object()` | get single object + run permissions |
| `get_serializer()` | instantiate serializer with context |
| `filter_queryset(qs)` | apply filter backends |
| `paginate_queryset(qs)` | paginate if configured |
| `get_paginated_response(data)` | wrap paginated data |

```python
# GenericAPIView alone — you still have to define handlers
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

class ArticleBase(GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request):
        qs = self.get_queryset()
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
```

That's pointless — use a mixin or concrete view instead (shown below).

---

### 3.2 Mixins

Mixins live in `rest_framework.mixins`. Each adds one action method.

| Mixin | Method added | HTTP action |
|---|---|---|
| `ListModelMixin` | `list(request)` | GET list |
| `CreateModelMixin` | `create(request)` | POST |
| `RetrieveModelMixin` | `retrieve(request, pk)` | GET detail |
| `UpdateModelMixin` | `update(request, pk)` | PUT / PATCH |
| `DestroyModelMixin` | `destroy(request, pk)` | DELETE |

**Using mixins manually with GenericAPIView:**

```python
from rest_framework import generics, mixins

class ArticleListCreateView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)     # from ListModelMixin

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)   # from CreateModelMixin


class ArticleDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)  # also from UpdateModelMixin

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
```

You almost never write mixin + GenericAPIView manually. Use concrete views instead.

---

### 3.3 Concrete Generic Views (the ones you actually use)

These are pre-combined `GenericAPIView + mixins`. Import from `rest_framework.generics`.

#### ListAPIView — GET list

```python
from rest_framework.generics import ListAPIView

class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```

#### CreateAPIView — POST

```python
from rest_framework.generics import CreateAPIView

class ArticleCreateView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```

#### RetrieveAPIView — GET single object

```python
from rest_framework.generics import RetrieveAPIView

class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # lookup_field = 'pk'  ← default; change to 'slug' etc. if needed
```

#### UpdateAPIView — PUT / PATCH

```python
from rest_framework.generics import UpdateAPIView

class ArticleUpdateView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```

#### DestroyAPIView — DELETE

```python
from rest_framework.generics import DestroyAPIView

class ArticleDeleteView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```

#### ListCreateAPIView — GET list + POST (most common list endpoint)

```python
from rest_framework.generics import ListCreateAPIView

class ArticleListCreateView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```

#### RetrieveUpdateAPIView — GET + PUT + PATCH

```python
from rest_framework.generics import RetrieveUpdateAPIView

class ArticleRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```

#### RetrieveDestroyAPIView — GET + DELETE

```python
from rest_framework.generics import RetrieveDestroyAPIView

class ArticleRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```

#### RetrieveUpdateDestroyAPIView — GET + PUT + PATCH + DELETE (most common detail endpoint)

```python
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```

#### URLs for generic views

```python
urlpatterns = [
    path('articles/', ArticleListCreateView.as_view()),
    path('articles/<int:pk>/', ArticleDetailView.as_view()),
]
```

---

### 3.4 Customizing Generic Views — The Override Hooks

This is where most real-world customization happens.

#### get_queryset() — dynamic queryset

```python
class UserArticleListView(ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        # Only return articles belonging to the logged-in user
        return Article.objects.filter(author=self.request.user)
```

```python
class ArticleByStatusView(ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        status = self.kwargs['status']           # from URL: /articles/published/
        return Article.objects.filter(status=status)
```

#### get_serializer_class() — dynamic serializer

```python
class ArticleView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()

    def get_serializer_class(self):
        if self.request.method in ('PUT', 'PATCH'):
            return ArticleWriteSerializer
        return ArticleReadSerializer
```

#### get_serializer() — inject extra context

```python
class ArticleListCreateView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        kwargs['context']['extra_data'] = {'user': self.request.user}
        return super().get_serializer(*args, **kwargs)
```

#### perform_create() — inject data on save

```python
class ArticleListCreateView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        # Automatically attach the logged-in user as author
        serializer.save(author=self.request.user)
```

#### perform_update() — hook into update

```python
class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
```

#### perform_destroy() — hook into delete

```python
class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_destroy(self, instance):
        # soft-delete instead of hard delete
        instance.is_deleted = True
        instance.save()
```

#### get_object() — custom object lookup

```python
class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'           # use slug instead of pk in URL

    def get_object(self):
        obj = super().get_object()
        # Run extra permission check
        if obj.author != self.request.user:
            raise PermissionDenied
        return obj
```

#### Overriding the response (override the method handler itself)

```python
class ArticleListCreateView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        # Wrap the default response
        return Response({
            'count': len(response.data),
            'results': response.data
        })
```

---

### 3.5 Generic Views with Filtering, Search, Ordering, Pagination

```python
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    # Filtering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'author']        # ?status=published&author=1
    search_fields = ['title', 'content']           # ?search=django
    ordering_fields = ['created_at', 'title']      # ?ordering=-created_at
    ordering = ['-created_at']                     # default ordering

    # Pagination (set globally in settings or per-view)
    # pagination_class = PageNumberPagination
```

---

## 4. ViewSets

ViewSets combine the logic for multiple related views into a single class. The Router maps HTTP methods to ViewSet actions automatically.

| ViewSet type | Based on | Provides |
|---|---|---|
| `ViewSet` | `APIView` | nothing — define actions manually |
| `GenericViewSet` | `GenericAPIView` + ViewSet | queryset/serializer hooks, no actions |
| `ModelViewSet` | GenericViewSet + all mixins | list, create, retrieve, update, destroy |
| `ReadOnlyModelViewSet` | GenericViewSet + List + Retrieve | list, retrieve |

### 4.1 ViewSet (raw)

```python
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class ArticleViewSet(ViewSet):

    def list(self, request):
        queryset = Article.objects.all()
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
```

### 4.2 GenericViewSet (base, mixed with mixins)

`GenericViewSet` is `ViewSet + GenericAPIView`. Add mixins to get actions.

```python
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

class ArticleViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet                       # note: GenericViewSet goes last
):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # Now has: list, create, retrieve — but NOT update or destroy
```

This pattern gives you precise control over which actions are available.

### 4.3 ModelViewSet (full CRUD)

```python
from rest_framework.viewsets import ModelViewSet

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
```

Provides all 5 actions: `list`, `create`, `retrieve`, `update`, `destroy`.

### 4.4 ReadOnlyModelViewSet

```python
from rest_framework.viewsets import ReadOnlyModelViewSet

class PublicArticleViewSet(ReadOnlyModelViewSet):
    queryset = Article.objects.filter(status='published')
    serializer_class = ArticleSerializer
    # Only: list, retrieve
```

### 4.5 Router — wiring ViewSets to URLs

```python
# urls.py
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')

urlpatterns = router.urls
```

**What the router generates:**

| URL | Method | Action | Name |
|---|---|---|---|
| `/articles/` | GET | `list` | `article-list` |
| `/articles/` | POST | `create` | `article-list` |
| `/articles/{pk}/` | GET | `retrieve` | `article-detail` |
| `/articles/{pk}/` | PUT | `update` | `article-detail` |
| `/articles/{pk}/` | PATCH | `partial_update` | `article-detail` |
| `/articles/{pk}/` | DELETE | `destroy` | `article-detail` |

### 4.6 @action decorator — custom actions on ViewSets

```python
from rest_framework.decorators import action
from rest_framework.response import Response

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    # detail=False → /articles/published/
    @action(detail=False, methods=['get'])
    def published(self, request):
        articles = self.get_queryset().filter(status='published')
        serializer = self.get_serializer(articles, many=True)
        return Response(serializer.data)

    # detail=True → /articles/{pk}/publish/
    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        article = self.get_object()
        article.status = 'published'
        article.save()
        return Response({'status': 'published'})

    # Different serializer on a custom action
    @action(detail=True, methods=['get'], serializer_class=ArticleSummarySerializer)
    def summary(self, request, pk=None):
        article = self.get_object()
        serializer = self.get_serializer(article)
        return Response(serializer.data)

    # Different permissions on a custom action
    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def trending(self, request):
        articles = Article.objects.order_by('-views')[:10]
        serializer = self.get_serializer(articles, many=True)
        return Response(serializer.data)
```

Router automatically adds these URLs:
- `GET /articles/published/`
- `POST /articles/{pk}/publish/`
- `GET /articles/{pk}/summary/`
- `GET /articles/trending/`

### 4.7 ViewSet with different serializers per action

```python
class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ArticleReadSerializer
        return ArticleWriteSerializer    # for create/update
```

### 4.8 ViewSet with different permissions per action

```python
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return [AllowAny()]
        if self.action == 'destroy':
            return [IsAdminUser()]
        return [IsAuthenticated()]
```

---

## 5. Comparison Table

| Feature | FBV | APIView | Generic Views | ViewSet |
|---|---|---|---|---|
| Boilerplate | high | medium | low | lowest |
| Flexibility | highest | high | medium | medium |
| Auto URL routing | ❌ | ❌ | ❌ | ✅ (Router) |
| Custom HTTP logic | ✅ | ✅ | override methods | `@action` |
| Queryset hooks | manual | manual | `get_queryset()` | `get_queryset()` |
| Filtering/Pagination | manual | manual | built-in | built-in |
| Good for | one-off | complex logic | standard CRUD | standard CRUD + REST |

---

## 6. The Confusing Part — Where Generics and ViewSets Overlap

The internet mixes these up. Here is the exact relationship:

```
generics.ListAPIView
    = generics.GenericAPIView + mixins.ListModelMixin

viewsets.ModelViewSet
    = viewsets.GenericViewSet
      + mixins.ListModelMixin
      + mixins.CreateModelMixin
      + mixins.RetrieveModelMixin
      + mixins.UpdateModelMixin
      + mixins.DestroyModelMixin

viewsets.GenericViewSet
    = viewsets.ViewSetMixin + generics.GenericAPIView
```

**Key insight:** ViewSets ARE Generic Views internally — they just add `ViewSetMixin` which handles the action → method dispatch and plugs into the Router. The `get_queryset()`, `get_serializer_class()`, `perform_create()` hooks work identically in both.

---

## 7. Quick Decision Guide

```
Need a one-off endpoint (login, password reset, health check)?
    → FBV or APIView

Standard CRUD for a model?
    → ModelViewSet

CRUD but want Router URLs?
    → ModelViewSet

CRUD but some actions disabled (e.g. no delete)?
    → GenericViewSet + only the mixins you need

Two separate URL files (list vs detail), no Router?
    → ListCreateAPIView + RetrieveUpdateDestroyAPIView

Read-only public API?
    → ReadOnlyModelViewSet

Need custom actions alongside CRUD (publish, archive, like)?
    → ModelViewSet + @action

Complex business logic that doesn't fit CRUD?
    → APIView (write everything yourself)

Need to customize queryset / serializer dynamically?
    → Any CBV: override get_queryset() or get_serializer_class()
```

---

## 8. Full Working Example — All Patterns Together

```python
# models.py
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=20, default='draft')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
```

```python
# serializers.py
from rest_framework import serializers
from .models import Article

class ArticleReadSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'status', 'author_name', 'created_at']

class ArticleWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'content', 'status']
```

```python
# views.py
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Article
from .serializers import ArticleReadSerializer, ArticleWriteSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at']

    def get_queryset(self):
        if self.action == 'list' and not self.request.user.is_staff:
            return Article.objects.filter(author=self.request.user)
        return Article.objects.all()

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve', 'published', 'trending'):
            return ArticleReadSerializer
        return ArticleWriteSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve', 'trending'):
            return [AllowAny()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        # soft delete
        instance.status = 'deleted'
        instance.save()

    @action(detail=False, methods=['get'])
    def trending(self, request):
        articles = Article.objects.filter(status='published')[:5]
        serializer = self.get_serializer(articles, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def publish(self, request, pk=None):
        article = self.get_object()
        if article.author != request.user:
            return Response({'error': 'Not your article'}, status=403)
        article.status = 'published'
        article.save()
        return Response({'status': 'published'})
```

```python
# urls.py
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')

urlpatterns = router.urls
# Generates:
# GET/POST   /articles/
# GET        /articles/trending/
# GET/PUT/PATCH/DELETE /articles/{pk}/
# POST       /articles/{pk}/publish/
```

---

## 9. Cheatsheet

```python
# --- FBV ---
@api_view(['GET', 'POST'])
def my_view(request): ...

# --- APIView ---
class MyView(APIView):
    def get(self, request): ...
    def post(self, request): ...

# --- Generic: list only ---
class MyList(ListAPIView):
    queryset = Model.objects.all()
    serializer_class = MySerializer

# --- Generic: list + create ---
class MyListCreate(ListCreateAPIView):
    queryset = Model.objects.all()
    serializer_class = MySerializer

# --- Generic: retrieve + update + delete ---
class MyDetail(RetrieveUpdateDestroyAPIView):
    queryset = Model.objects.all()
    serializer_class = MySerializer

# --- ViewSet: full CRUD ---
class MyViewSet(ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = MySerializer

# --- ViewSet: read only ---
class MyViewSet(ReadOnlyModelViewSet):
    queryset = Model.objects.all()
    serializer_class = MySerializer

# --- ViewSet: pick specific actions ---
class MyViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = Model.objects.all()
    serializer_class = MySerializer

# --- Router ---
router = DefaultRouter()
router.register(r'items', MyViewSet, basename='item')
urlpatterns = router.urls

# --- Dynamic overrides (work in generics AND viewsets) ---
def get_queryset(self): ...
def get_serializer_class(self): ...
def get_permissions(self): ...
def perform_create(self, serializer): ...
def perform_update(self, serializer): ...
def perform_destroy(self, instance): ...
def get_object(self): ...
```