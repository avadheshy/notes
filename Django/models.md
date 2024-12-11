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

