Django’s views have three requirements:

- They are callable. A view can be either function or a class-based view. CBVs inherit the method as_view() which uses a dispatch() method to call the appropriate method depending on the HTTP verb (get, post, etc)
- They must accept an HttpRequest object as its first positional argument
- They must return an HttpResponse object or raise an exception.

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

# Pros
- Simple to implement
- Easy to read
- Explicit code flow
- Straightforward usage of decorators
- good for one-off or specialized functionality
# Cons
- Hard to extend and reuse the code
- Handling of HTTP methods via conditional branching

---
This function is very easy to implement and it’s very useful but the main disadvantage is that on a large Django project, usually a lot of similar functions in the views . If all objects of a Django project usually have CRUD operations so this code is repeated again and again unnecessarily and this was one of the reasons that the class-based views and generic views were created for solving that problem.

---

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
---
# Pros
- Code reuseability — In CBV, a view class can be inherited by another - view class and modified for a different use case.
- DRY — Using CBVs help to reduce code duplication
- Code extendability — CBV can be extended to include more functionalities using Mixins
- Code structuring — In CBVs A class based view helps you respond to different http request with different class instance methods instead of conditional branching statements inside a single function based view.
- Built-in generic class-based views
# Cons
- Harder to read
- Implicit code flow
- Use of view decorators require extra import, or method override
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