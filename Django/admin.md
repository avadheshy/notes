# 1. Registering Models in the Admin
To make a model editable via the Django admin site:

```
from django.contrib import admin
from .models import Product

admin.site.register(Product)
```
Or use a custom admin class:

```
class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
```
# 2. Customizing List Views, Filters, and Forms
🔹 list_display
Controls which fields are shown in the list view.

```
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
```
🔹 list_filter
Adds filter sidebar.

```
    list_filter = ('category', 'available')
```
🔹 search_fields
Adds a search bar.

```
    search_fields = ('name', 'description')
```
🔹 form
Use a custom form for validation or layout.

```
from django import forms

class ProductForm(forms.ModelForm):
    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price

    class Meta:
        model = Product
        fields = '__all__'

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
```
# 3. Inlines
Use TabularInline or StackedInline to edit related objects on the same page.

```
from .models import ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
```
# 4. Readonly Fields
Make some fields non-editable in the admin:

```
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
```
# 5. Overriding Admin Methods
🔹 save_model
Customize what happens when an object is saved.

```
def save_model(self, request, obj, form, change):
    if not change:
        obj.created_by = request.user
    super().save_model(request, obj, form, change)
```
🔹 get_queryset
Customize which objects are shown in admin.

```
def get_queryset(self, request):
    qs = super().get_queryset(request)
    if request.user.is_superuser:
        return qs
    return qs.filter(created_by=request.user)
```
🔹 has_change_permission / has_view_permission
Restrict access:

```
def has_change_permission(self, request, obj=None):
    if obj and obj.created_by != request.user:
        return False
    return super().has_change_permission(request, obj)
```
# Example Summary
```
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    list_filter = ('category',)
    search_fields = ('name',)
    readonly_fields = ('created_at',)
    inlines = [ProductImageInline]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs if request.user.is_superuser else qs.filter(created_by=request.user)
```