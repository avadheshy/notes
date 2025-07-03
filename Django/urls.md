# 1. path(), re_path(), and include()
🔹 path()
Introduced in Django 2.0.

Uses simpler syntax and converters like <int:id>, <slug:slug>.

```
from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:id>/', views.product_detail, name='product-detail'),
    path('blog/<slug:slug>/', views.blog_post, name='blog-post'),
]
```
🔹 re_path()
Uses regular expressions.

More flexible but harder to read.

```
from django.urls import re_path

urlpatterns = [
    re_path(r'^article/(?P<year>[0-9]{4})/$', views.year_archive),
]
```
🔹 include()
Lets you include other URLconfs to modularize your app.

```
from django.urls import include, path

urlpatterns = [
    path('blog/', include('blog.urls')),  # routes to blog/urls.py
]
```
# 2. Named URLs and URL Reversing
Naming your URLs makes your project more maintainable.

🔹 Named URLs
```
path('product/<int:id>/', views.product_detail, name='product-detail')
```
🔹 Reverse in Python
```
from django.urls import reverse

url = reverse('product-detail', kwargs={'id': 5})
```
# Result: /product/5/
🔹 {% url %} in Templates
```
<a href="{% url 'product-detail' id=5 %}">View Product</a>
```
✅ 3. Dynamic URL Patterns with Slugs and IDs
Django supports converters in path():

```
| Converter | Matches                               | Example           |
| --------- | ------------------------------------- | ----------------- |
| `str`     | any non-empty string excluding `/`    | `<str:name>/`     |
| `int`     | integer                               | `<int:id>/`       |
| `slug`    | letters, numbers, dashes, underscores | `<slug:slug>/`    |
| `uuid`    | UUID strings                          | `<uuid:uuid>/`    |
| `path`    | string including `/`                  | `<path:subpath>/` |

```
# Example:
```
path('blog/<slug:slug>/', views.blog_detail, name='blog-detail')
```
```
def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog_detail.html', {'blog': blog})
```
✅ Summary Table
```
| Feature                | Function/Tag              | Description                      |
| ---------------------- | ------------------------- | -------------------------------- |
| Basic routing          | `path()`                  | Clean and readable routing       |
| Regex routing          | `re_path()`               | Advanced matching using regex    |
| Nested routes          | `include()`               | Include routes from other apps   |
| Named route            | `name='...'`              | Assign a name to a route         |
| URL reverse (view)     | `reverse()`               | Get URL path from view name      |
| URL reverse (template) | `{% url %}`               | Get URL in templates dynamically |
| Dynamic segments       | `<int:id>`, `<slug:slug>` | Dynamic URL parts                |

```
# Types of URL Routing
- Function-Based Views with urlpatterns
- Basic URL Configurations with Class-Based API Views
- Viewsets and Routers
- Nested Routers
- Custom Routers

# 1. Types of URL Routing in Django & DRF
```
Type	                       Use Case
path() / re_path()	           Basic Django routing
include()	                   Modular apps
Function-Based Views (FBV)	   Simple views with custom logic
Class-Based Views (CBV)	       Reusable and extensible logic
DRF Viewsets + Routers	       Automatic URL generation for CRUD APIs
Nested Routers	               For nested relationships (e.g., /user/1/posts/)
Custom Routers	              Fine-grained control over DRF routes
```

#  2. Function-Based Views (FBVs) with urlpatterns
```
# views.py
from django.http import JsonResponse

def product_list(request):
    return JsonResponse({'message': 'List of products'})

# urls.py
from django.urls import path
from .views import product_list

urlpatterns = [
    path('products/', product_list, name='product-list'),
]
```
# 3. Class-Based API Views with path()
```
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response

class ProductListView(APIView):
    def get(self, request):
        return Response({'message': 'List of products'})

# urls.py
from django.urls import path
from .views import ProductListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
]
```
# 4. DRF ViewSets and Routers
🔹 ViewSet
```
# views.py
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```
🔹 Router
```
# urls.py
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = router.urls
```
DRF will automatically create:

GET /products/ → list

GET /products/1/ → retrieve

POST /products/ → create

PUT /products/1/ → update

DELETE /products/1/ → destroy

# 5. Nested Routers (using drf-nested-routers)
pip install drf-nested-routers
```
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from .views import UserViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

nested_router = NestedDefaultRouter(router, r'users', lookup='user')
nested_router.register(r'orders', OrderViewSet, basename='user-orders')

urlpatterns = router.urls + nested_router.urls
```
Routes generated:

/users/

/users/1/orders/

/users/1/orders/5/

# 6. Custom Routers
If you need more control over URL structure:

```
from rest_framework.routers import SimpleRouter

class CustomRouter(SimpleRouter):
    routes = [
        # define custom routes here
    ]
```
You can override the .get_routes() method for fully custom behavior.

# Summary Table
```
| Routing Type         | Used With            | Description                                   |
| -------------------- | -------------------- | --------------------------------------------- |
| `path()`/`re_path()` | All views            | Basic Django routing                          |
| FBV                  | Django, DRF          | Quick and easy for simple logic               |
| CBV                  | Django, DRF          | Reusable logic via classes                    |
| ViewSet + Router     | DRF                  | Auto-routing for CRUD operations              |
| Nested Router        | `drf-nested-routers` | For nested resources (parent-child relations) |
| Custom Router        | DRF                  | For fine-grained routing control              |

```
