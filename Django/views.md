#1. Function-Based Views (FBV)
FBVs are simple Python functions that take a request and return a HttpResponse.

🔹 Example:
```
from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products': products})
```
FBVs are:

Explicit and simple to understand

Great for small, one-off views

# 2. Class-Based Views (CBV)
CBVs provide reusable logic through classes. Django provides built-in generic CBVs for common tasks.

🔹 Common CBVs:
```
Class	    Purpose
ListView	Show a list of objects
DetailView	Show a single object
CreateView	Form to create an object
UpdateView	Form to update an object
DeleteView	Confirm + delete object
```

🔹 Example: ListView and DetailView
```
from django.views.generic import ListView, DetailView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'
```
🔹 Example: CreateView, UpdateView, DeleteView
```
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price']
    template_name = 'products/form.html'
    success_url = reverse_lazy('product-list')
```
# 3. Mixins & Generic Views
🔹 Common Mixins:
LoginRequiredMixin – restricts access to authenticated users

PermissionRequiredMixin – checks for specific permissions

```
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Product

class ProtectedProductList(LoginRequiredMixin, ListView):
    model = Product
```
🔹 Generic Views
Django provides generic views through inheritance from:

View, TemplateView, RedirectView

ListView, DetailView, etc.

# 4. View Decorators
🔹 @login_required
Only allows authenticated users.
```
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
```
🔹 @permission_required
Checks for a specific permission.

```
from django.contrib.auth.decorators import permission_required

@permission_required('products.change_product')
def edit_product(request, id):
    ...
```
🔹 @csrf_exempt
Disables CSRF protection for a view (⚠️ Use with caution).

```
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def webhook_view(request):
    ...
```
# Summary: FBV vs CBV
```
Feature	         FBV	                CBV
Simplicity	Very simple and explicit	Abstracted, more scalable
Reusability	Less reusable	            Highly reusable with mixins
Best for	Small/simple views	        Larger, CRUD-heavy apps
Decorators	@login_required, etc.	   Mixins like LoginRequiredMixin
```


#When to Use FBV vs CBV
```
Use Case	                            Recommendation
Simple logic, 1–2 methods	            FBV
Complex logic with reuse	            CBV
CRUD operations	                        CBV (generic views)
API endpoints (DRF)	                    CBV (ViewSet/APIView)
Full control over flow/response	        FBV


```