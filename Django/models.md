# Types of model inheritance
In Django, model inheritance allows you to reuse and extend models efficiently. There are three main types of model inheritance, each serving different use cases:

# 1. Abstract Base Classes
## Purpose:
 Used when you want to define reusable fields and methods that other models can inherit, but you don’t want to create a table for the base class in the database.
## Behavior:
 The parent class doesn’t have its own database table; its fields are added to the child models.
## Use Case: 
Sharing common fields and methods among multiple models without creating an actual table for the base class.
## Example:
```
from django.db import models

class CommonInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Student(CommonInfo):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)

class Teacher(CommonInfo):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)

```

No table for CommonInfo.
Student and Teacher tables will have the created_at and updated_at fields.
# 2. Multi-table Inheritance
## Purpose: 
Used when you want each model in the inheritance hierarchy to have its own database table.
## Behavior: 
The parent class has its own table, and each child class gets its own table with a foreign key linking to the parent.
## Use Case:
 Extending an existing model while keeping the parent table separate.
Example:
```
class Person(models.Model):
    name = models.CharField(max_length=100)

class Student(Person):
    grade = models.CharField(max_length=10)
```
A Person table is created with a name field.
A Student table is created with a grade field and a foreign key to Person.
# 3. Proxy Models
## Purpose: 
Used to change the behavior (e.g., default ordering, methods) of an existing model without changing its database schema.
## Behavior: 
The proxy model doesn’t create a new table; it uses the table of the original model.
## Use Case:
Adding custom behavior, managers, or methods to an existing model.
## Example:
```
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        ordering = ['name']

class YoungPerson(Person):
    class Meta:
        proxy = True

    def is_young(self):
        return self.age < 30
```
No new table is created for YoungPerson.
You can use YoungPerson to apply custom logic or behavior (e.g., the is_young method).
# Comparison of the Inheritance Types
```
Feature	            Abstract Base Class	                        Multi-table Inheritance	                            Proxy Models
Separate Table?	    No	                                        Yes	                                                No
Field Inheritance	Yes	                                        No (only via relation)	                            Yes (inherits fields)
Custom Behavior?	Yes	                                        Yes	                                                Yes
Use Case	        Reusable                                    fields/methods	Extending existing models	        Customizing behavior
```
# When to Use Which?
Abstract Base Classes: When you need shared fields/methods across models but don’t want separate database tables.

Multi-table Inheritance: When you need separate tables for parent and child models with their own data.

Proxy Models: When you want to modify or extend behavior without changing the database schema.


# Difference between @property and method
   

```
#models.py
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=0)  # Discount as a percentage
    stock = models.PositiveIntegerField(default=0)

    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price

    def is_in_stock(self):
        return self.stock > 0


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()  # Quantity sold

# serializers.py

from rest_framework import serializers
class ProductSerializer(serializers.ModelSerializer):
    # Exposing a property
    discounted_price = serializers.ReadOnlyField()
    
    # Exposing a method
    is_in_stock = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['name', 'price', 'discount', 'discounted_price', 'is_in_stock']

    # Method to expose the 'is_in_stock' method
    def get_is_in_stock(self, obj):
        return obj.is_in_stock()

```

### property :
The value is computed within the model using @property. Defined with serializers.ReadOnlyField()
### method :
The logic is written in the serializer using a custom method (get_<field_name>) . Defined with serializers.SerializerMethodField().

## select_related/prefect_related

```
products = Product.objects.select_related('category').all()

for product in products:
    print(product.name, product.category.name)
# Fetch all categories and prefetch the related products (multiple queries but optimized)
categories = Category.objects.prefetch_related('products').all()

for category in categories:
    print(f"Category: {category.name}")
    print("Products:")
    for product in category.products.all():  # No additional query, thanks to prefetch_related
        print(f"- {product.name}")
```
# While writing query we should find which table with start the query.
## Calculating Total Sales for a Specific Category
```
category_name = "Electronics"

total_sales = Sale.objects.filter(
    product__category__name=category_name
).aggregate(
    total=Sum(F('product__price') * F('count'))
)['total']

print(total_sales) 
```
## Calculating Sales for All Categories

```
sales_by_category = Sale.objects.values(
    'product__category__name'
).annotate(
    total_sales=Sum(F('product__price') * F('count'))
)

for sale in sales_by_category:
    print(f"Category: {sale['product__category__name']}, Total Sales: {sale['total_sales']}")

```

# 1. Find the total revenue generated for each product and category combination

Get the total revenue for each product and group it by category.

```
product_category_sales = Product.objects.annotate(
    total_revenue=Sum(F('sale__count') * F('price'))
).values('category__name', 'name', 'total_revenue')
```
# 2. Find the top 3 best-selling products in each category
Get the top 3 products by sales count for every category.

```
from django.db.models import Sum
top_products_per_category = Product.objects.annotate(
    total_sales=Sum('sale__count')
).order_by('category', '-total_sales').values('category__name', 'name', 'total_sales')[:3]
```
# 3. Find the total number of products sold in each category
Calculate the sum of all products sold grouped by their category.

```
category_product_sales = Category.objects.annotate(
    total_products_sold=Sum('products__sale__count')
).values('name', 'total_products_sold')
```
# 4. Find products with a discount greater than 20% and their corresponding sales revenue
Filter products by their discount and calculate the revenue for these products.

```
discounted_products = Product.objects.filter(discount__gt=20).annotate(
    total_revenue=Sum(F('sale__count') * F('price'))
).values('name', 'discount', 'total_revenue')
```
# 5. Find the category with the highest average product price
Calculate the average product price for each category and find the one with the highest average.

```
category_avg_price = Category.objects.annotate(
    avg_price=Sum(F('products__price')) / Sum(F('products__stock'))
).order_by('-avg_price').first()
```
# 6. Find products that have not been sold
Retrieve all products that do not have any sales associated with them.

```
unsold_products = Product.objects.filter(sale__isnull=True).values('name', 'price', 'stock')
```
# 7. Find the most sold product in each category
Find the product with the highest sales in each category.

```
from django.db.models import Max
most_sold_products_per_category = Category.objects.annotate(
    max_sales=Max('products__sale__count')
).values('name', 'max_sales')
```
# 8. Calculate the total stock value for each category
Stock value is the price multiplied by the stock quantity.

```
category_stock_value = Category.objects.annotate(
    total_stock_value=Sum(F('products__price') * F('products__stock'))
).values('name', 'total_stock_value')
```
# 9. Find categories that have more than 10 products listed
Count the number of products in each category and filter categories with more than 10 products.

```
categories_with_many_products = Category.objects.annotate(
    product_count=Count('products')
).filter(product_count__gt=10).values('name', 'product_count')
```
# 10. Find the product with the maximum revenue in a specific category
Get the product that generates the most revenue in a given category (e.g., "Electronics").

```
from django.db.models import Q

max_revenue_product_in_category = Product.objects.filter(
    category__name="Electronics"
).annotate(
    total_revenue=Sum(F('sale__count') * F('price'))
).order_by('-total_revenue').first()
```
# 11. Find the total revenue grouped by both category and month
Group the sales revenue by category and the month the sales were made.

```
from django.db.models.functions import TruncMonth

category_monthly_revenue = Sale.objects.annotate(
    month=TruncMonth('id')  # Replace 'id' with a DateField/DateTimeField if you have one
).values('product__category__name', 'month').annotate(
    total_revenue=Sum(F('count') * F('product__price'))
).order_by('month', 'product__category__name')
```
# 12. Find categories where all products have stock greater than 10
Retrieve categories where every product has stock greater than 10.

```
categories_with_sufficient_stock = Category.objects.exclude(
    products__stock__lte=10
).distinct().values('name')
```
# 13. Find products that belong to multiple categories (if there's a many-to-many relationship)
Assume a ManyToManyField is added between Product and Category.

```
products_in_multiple_categories = Product.objects.annotate(
    category_count=Count('category')
).filter(category_count__gt=1).values('name', 'category_count')
```
# 14. Calculate the average discount offered by each category

Get the average discount for all products in each category.

```
category_avg_discount = Category.objects.annotate(
    avg_discount=Avg('products__discount')
).values('name', 'avg_discount')
```

# 15. Find the categories that contributed to more than 50% of the total sales revenue
Identify which categories generated more than half of the overall revenue.

```
from django.db.models import Sum

total_revenue = Product.objects.aggregate(
    total_revenue=Sum(F('sale__count') * F('price'))
)['total_revenue']

categories_contributing_50_percent = Category.objects.annotate(
    category_revenue=Sum(F('products__sale__count') * F('products__price'))
).filter(category_revenue__gt=0.5 * total_revenue).values('name', 'category_revenue')
```
These queries not only involve combining multiple tables but also test your knowledge of aggregations, annotations, and query optimizations. Make sure you understand how joins are implicitly handled in Django when using related fields!


 Constraints Summary
```
            Field Type	                        Main Constraints
            AutoField	                        primary_key=True, auto-increment
            CharField	                        max_length, unique=True
            IntegerField	                    validators=[Min/MaxValueValidator]
            FloatField	                        Prone to rounding issues
            DecimalField	                    max_digits, decimal_places (better for money)
            BooleanField	                    Stores True/False
            DateTimeField	                    auto_now, auto_now_add
            EmailField	                        Validates email format
            URLField	                        Validates URL format
            FileField	                        upload_to='path/'
            ForeignKey	                        on_delete=models.CASCADE
            OneToOneField	                    Enforces unique relationship
            ManyToManyField	                    Creates join table
            SlugField	                        Only letters, numbers, hyphens allowed
            UUIDField	                        Ensures uniqueness
            JSONField	                        Stores JSON objects
            ChoiceField	                        Restricts predefined choices
```

STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
]

status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
description = models.TextField(blank=True, null=True)
blank=True (allows empty values).
null=True (stores NULL instead of an empty string).