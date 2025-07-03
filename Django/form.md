# 1. forms.Form vs forms.ModelForm
🔹 forms.Form
Manual fields, not tied to any model.

Use when you want full control (e.g., contact forms, filters).

```
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```
🔹 forms.ModelForm
Auto-generates form fields from a model.

Best for CRUD operations.

```
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock']
```
# 2. Form Validation
🔹 clean_<fieldname>()
For validating individual fields.

```
class ProductForm(forms.ModelForm):
    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError("Price must be positive.")
        return price
```
🔹 clean()
For cross-field validation.

```
    def clean(self):
        cleaned_data = super().clean()
        stock = cleaned_data.get('stock')
        price = cleaned_data.get('price')

        if stock == 0 and price > 0:
            raise forms.ValidationError("Out of stock items cannot have a price.")
```
# 3. Widgets and Customization
Widgets control the HTML rendering of form fields.

```
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'step': 0.01}),
        }
```
You can also use built-in widgets like:

forms.TextInput

forms.PasswordInput

forms.Textarea

forms.Select, forms.CheckboxInput

# 4. Handling POST Requests Securely
🔹 CSRF Protection
Django handles CSRF automatically in views rendered via templates:
```
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
</form>
```
🔹 In Views
```
from django.shortcuts import render, redirect
from .forms import ProductForm

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})
```
🔹 Secure Practice Checklist:

#Action                              |

-  Use `{% csrf_token %}`      
- Validate all form data 
- Never trust `request.POST` directly 
- Always call `form.is_valid()`  
# Summary Table
```
Feature	                    forms.Form	                        forms.ModelForm
Model Binding	            Manual	                            Automatic
Field Creation	            Manual via CharField, EmailField	Auto from Meta.fields
Use Case	                Custom inputs, filters	            Create/Update model instances
Validation	                clean_<field>(), clean()	        Same, with model-aware constraints
Widgets                     Yes, with widgets or attrs	        Yes, same syntax
```

