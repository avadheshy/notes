Custom Manager in Django
A custom manager in Django is a class that inherits from models.Manager and is used to add custom query methods or modify the default query behavior for a model. Django models come with a default manager (objects), but you can create your own manager to encapsulate commonly used queries, filtering, and other logic related to your models.

Custom managers allow you to extend the functionality of your models by adding custom query methods that can be reused across your application.

Creating a Custom Manager
To create a custom manager, you need to:

Define a new manager class that inherits from models.Manager.
Add custom methods to the manager that perform the queries you need.
Example 1: Basic Custom Manager
Suppose you have a Product model, and you want to create a custom manager to get all available products (i.e., products that are in stock).

python
Copy
Edit
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

# Custom Manager
class ProductManager(models.Manager):
    def available(self):
        return self.filter(stock__gt=0)  # Only products with stock greater than 0

# Attach the custom manager to the model
Product.add_to_class('available', ProductManager())

Usage:

python
Copy
Edit
# Get all products that are available
available_products = Product.available.all()
Example 2: Custom Manager with Method to Create New Objects
You can also define a method in a custom manager to simplify creating objects with some default behavior.

python
Copy
Edit
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

class ProductManager(models.Manager):
    def create_product(self, name, price, stock):
        product = self.create(name=name, price=price, stock=stock)
        return product

# Attach the custom manager
Product.add_to_class('objects', ProductManager())

# Usage:
new_product = Product.objects.create_product('Laptop', 999.99, 10)
Example 3: Custom Manager with Query Parameters
You can create methods in the custom manager that allow filtering based on specific parameters.

python
Copy
Edit
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

class ProductManager(models.Manager):
    def in_category(self, category_name):
        return self.filter(category=category_name)

    def below_price(self, max_price):
        return self.filter(price__lt=max_price)

# Attach the custom manager
Product.add_to_class('objects', ProductManager())

# Usage:
# Get products in a specific category
electronics = Product.objects.in_category('Electronics')

# Get products that are below a certain price
cheap_products = Product.objects.below_price(500)
Using Custom Managers in a Model
To attach a custom manager to a model, you can either use the default objects manager or define a new attribute.

Using the default objects manager:
python
Copy
Edit
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    # Custom Manager
    objects = ProductManager()  # Use 'objects' as the manager name

    def __str__(self):
        return self.name
Creating Multiple Managers:
You can attach more than one manager to a model. For example:

python
Copy
Edit
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    # Custom Managers
    objects = ProductManager()  # Default manager
    available = ProductManager()  # Another manager for specific queries

    def __str__(self):
        return self.name
In this case, you can use Product.objects for default queries and Product.available for specific queries (e.g., available products).

Common Use Cases for Custom Managers
Encapsulating common queries: For example, getting active users, recent orders, or products that are on sale.
Simplifying object creation: Providing a convenient method for creating instances with default values or specific logic.
Query abstraction: Encapsulating complex queries into simple method calls (e.g., filtering based on certain criteria).
Benefits of Using Custom Managers
Reusability: Custom query methods can be reused throughout your code, ensuring consistency.
Encapsulation: Encapsulates complex query logic inside the model manager, keeping your views and other logic clean.
Improved readability: Custom managers make it easier to understand common queries by giving them descriptive method names.
Maintainability: Changes to query logic are centralized in the manager, making your application easier to maintain.
Custom Manager Methods for QuerySet
Custom managers typically return QuerySet objects, so they can chain methods like the default manager does.

Example:

python
Copy
Edit
class ProductManager(models.Manager):
    def available(self):
        return self.filter(stock__gt=0)

    def in_category(self, category_name):
        return self.filter(category=category_name)

# Usage:
Product.objects.available().in_category('Electronics')
Conclusion
Custom managers are a powerful tool in Django for encapsulating custom queries and logic. They allow for cleaner, reusable, and more maintainable code by centralizing complex query logic inside the model. Whether you're building custom filters, object creation methods, or query abstraction, custom managers can help you keep your codebase clean and concise.