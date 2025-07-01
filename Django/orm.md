
from django.contrib.auth.models import User
- auto_add_now it is initialized at the time of row insertion
- auto_now upadates every time when row is modified

- when we dont define related name django automaticaly defines a reverse relation
```
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

book = Book.objects.first()
book.author  # returns the Author instance
author = Author.objects.first()
author.book_set.all()  
author.books.all()  # more readable and customizable!
```
```
class PostLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'post')
```
- A user can like a post only once. The same (user, post) pair cannot exist more than once in the PostLike table.
Django ORM
```
from django.db import models

class MyModel(models.Model):
    field_name = models.CharField(max_length=100)
    another_field = models.IntegerField()
    date_field = models.DateTimeField(auto_now_add=True)

```
# Insert 
```
MyModel.objects.create(field_name='value', another_field=42)

obj = MyModel(field_name='value', another_field=42) 
obj.save()

MyModel.objects.bulk_create([
        MyModel(field_name='value1', another_field=42),
        MyModel(field_name='value2', another_field=43),
    ])
```
# Update
```
# update field_name of matching rows 
from django.db.models import F 
MyModel.objects.filter(field_name='old_value').update(field_name='new_value')


# Update fields with F-expression . This will add 10 to another_field of every field
MyModel.objects.update(another_field=F('another_field') + 10)

# Annotate with F-expression. This will add sum column in every row
annotated_objects = MyModel.objects.annotate(sum=F('another_field') + F('field_name'))

```

# Delete
```
MyModel.objects.filter(field_name='value').delete()

```
# Queryset Basics
```
from myapp.models import MyModel


# Retrieve all objects
all_objects = MyModel.objects.all()

# Retrieve a single object
single_object = MyModel.objects.get(pk=1)

# Filter objects
filtered_objects = MyModel.objects.filter(field_name='value')

# Chaining filters
chained_filters = MyModel.objects.filter(field_name='value', another_field=42)

# Exclude objects
excluded_objects = MyModel.objects.exclude(field_name='value')

# Ordering
ordered_objects = MyModel.objects.order_by('field_name')

# Count objects
count_objects = MyModel.objects.count()

# Check if an object exists
exists = MyModel.objects.filter(field_name='value').exists()

filtered_objects = MyModel.objects.filter(field_name='value').filter(another_field=42)

# Chain multiple excludes
excluded_objects = MyModel.objects.exclude(field_name='value').exclude(another_field=42)
```
# Querying with Q Objects 
```
from django.db.models import Q

# OR query
q = Q(field_name='value') | Q(another_field=42)
or_query = MyModel.objects.filter(q)

# AND query
q = Q(field_name='value') & Q(another_field=42)
and_query = MyModel.objects.filter(q)
```
# Aggregation and Annotation
```
from django.db.models import Avg, Sum, Count,Max, Min

# Aggregate functions
average_value = MyModel.objects.aggregate(avg=Avg('another_field'))
total_sum = MyModel.objects.aggregate(sum=Sum('another_field'))
total_count = MyModel.objects.aggregate(count=Count('pk'))

# Annotate (add calculated fields)
annotated_objects = MyModel.objects.annotate(avg=Avg('another_field'))

# Group by field_name and annotate
grouped_objects = MyModel.objects.values('field_name').annotate(count=Count('pk'))

# Group by field_name and calculate sum
grouped_objects = MyModel.objects.values('field_name').annotate(total_sum=Sum('another_field'))


# Get the sum of a specific field
total_sum = MyModel.objects.aggregate(total_sum=Sum('field_name'))

# Get the average value of a specific field
average_value = MyModel.objects.aggregate(average_value=Avg('field_name'))

# Get the maximum value of a specific field
max_value = MyModel.objects.aggregate(max_value=Max('field_name'))

# Get the minimum value of a specific field
min_value = MyModel.objects.aggregate(min_value=Min('field_name'))

# Get the count of objects in the queryset
object_count = MyModel.objects.aggregate(object_count=Count('pk'))
```
# Filtering with Lookups
```
# Case-insensitive exact match
filtered_objects = MyModel.objects.filter(field_name__iexact='value')

# Contains
filtered_objects = MyModel.objects.filter(field_name__contains='value')

# Startswith and Endswith
filtered_objects = MyModel.objects.filter(field_name__startswith='prefix')
filtered_objects = MyModel.objects.filter(field_name__endswith='suffix')

# In
filtered_objects = MyModel.objects.filter(another_field__in=[1, 2, 3])

# Range
filtered_objects = MyModel.objects.filter(another_field__range=(10, 20))
```
# Date and Time Queries
```
from datetime import date

# Exact Date Match
filtered_objects = MyModel.objects.filter(date_field__date=date(2023, 7, 31))

# Year, Month, Day
filtered_objects = MyModel.objects.filter(date_field__year=2023)
filtered_objects = MyModel.objects.filter(date_field__month=7)
filtered_objects = MyModel.objects.filter(date_field__day=31)

# Greater Than and Less Than
filtered_objects = MyModel.objects.filter(date_field__gt=date(2023, 7, 1))
filtered_objects = MyModel.objects.filter(date_field__lt=date(2023, 8, 1))
```
# Handling Null and Empty Values
```
# Filter for null values
filtered_objects = MyModel.objects.filter(field_name__isnull=True)

# Filter for empty strings (useful for CharField)
filtered_objects = MyModel.objects.filter(field_name='')

# Exclude empty strings
excluded_objects = MyModel.objects.exclude(field_name='')
```
# Union, Intersection, and Difference
```
# Union of two querysets (combines and removes duplicates)
union_result = MyModel.objects.filter(field_name='value') | MyModel.objects.filter(another_field=42)

# Intersection of two querysets
intersection_result = MyModel.objects.filter(field_name='value') & MyModel.objects.filter(another_field=42)

# Difference between two querysets
difference_result = MyModel.objects.filter(field_name='value').difference(MyModel.objects.filter(another_field=42))
```
# Defer and Only
```
# Fetch only the publication years and ratings of books, loading all other fields
books = Book.objects.only('publication_year', 'rating')

for book in books:
    print(book.title, book.author)  # All fields except publication_year and rating are deferred
    print(book.publication_year, book.rating)  # These fields are loaded from the database

# Fetch only the titles and authors of books, deferring other fields
books = Book.objects.defer('publication_year', 'summary', 'cover_image', 'rating', 'genre')

for book in books:
    print(book.title, book.author)  # Only these fields are loaded from the database
    # Accessing other fields will trigger database queries to load them
    print(book.publication_year, book.summary)
```
# Case and When Expressions
```
from django.db.models import Case, When, Value, IntegerField

# Use Case and When for conditional expressions
updated_objects = MyModel.objects.annotate(
    custom_field=Case(
        When(field_name='value1', then=Value(1)),
        When(field_name='value2', then=Value(2)),
        default=Value(0),
        output_field=IntegerField(),
    )
)
```

# Custom QuerySet Methods
```
# Create custom methods for QuerySet
class MyModelQuerySet(models.QuerySet):
    def custom_method(self):
        return self.filter(field_name='value')

# Use the custom QuerySet in the model
class MyModel(models.Model):
    field_name = models.CharField(max_length=100)

    objects = MyModelQuerySet.as_manager()
```
# Subqueries
```
from django.db.models import Subquery, OuterRef

# Subquery: Use a queryset as a subquery in another queryset
subquery = MyModel.objects.filter(field_name=OuterRef('related_field'))
main_query = MyModel.objects.filter(pk__in=subquery)

# Correlated Subquery: Use a subquery that references the outer query
correlated_subquery = MyModel.objects.filter(related_field=OuterRef('field_name'))
correlated_main_query = MyModel.objects.filter(pk__in=correlated_subquery)
```
# Subqueries and Outer Refs
```
from django.db.models import Subquery, OuterRef

# Get products with prices greater than the average price of all products
average_price = Product.objects.aggregate(avg_price=Sum('price'))['avg_price']
products = Product.objects.filter(price__gt=Subquery(Product.objects.filter(pk=OuterRef('pk')).values('price')))
```

# JSONField (PostgreSQL-specific)
```
from django.db import models
from django.contrib.postgres.fields import JSONField

class MyModel(models.Model):
    data = JSONField()
from myapp.models import MyModel

# Create a new record with JSON data
data = {
    "name": "John Doe",
    "age": 30,
    "email": "john@example.com"
}

my_instance = MyModel(data=data)
my_instance.save()
from myapp.models import MyModel

# Get all records where 'age' is 30
result = MyModel.objects.filter(data__age=30)

# Get all records where 'email' contains 'example.com'
result = MyModel.objects.filter(data__email__contains='example.com')
```
# ArrayField (PostgreSQL-specific)
```
from django.db import models
from django.contrib.postgres.fields import ArrayField

class MyModel(models.Model):
    tags = ArrayField(models.CharField(max_length=100))
# Get objects where tags contain 'django'
MyModel.objects.filter(tags__contains=['django'])

# Get objects where tags are exactly ['django', 'python']
MyModel.objects.filter(tags=['django', 'python'])

# Get objects where the number of tags is 3
MyModel.objects.filter(tags__len=3)
```
# PostGIS (Spatial Data Operations)
```
# Create a model with a PointField to store geographic coordinates
from django.contrib.gis.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    coordinates = models.PointField()

# Create a model with a PolygonField to store geographic boundaries
class Area(models.Model):
    name = models.CharField(max_length=100)
    boundary = models.PolygonField()

# Create a model with a LineStringField to store geographic paths/routes
class Route(models.Model):
    name = models.CharField(max_length=100)
    path = models.LineStringField()

# Query to find locations within a certain distance of a given point
from django.contrib.gis.measure import D
from myapp.models import Location

nearby_locations = Location.objects.filter(coordinates__distance_lte=(point, D(m=1000)))

# Perform a spatial union on all Area objects
from django.contrib.gis.db.models import Union
from myapp.models import Area

unioned_area = Area.objects.aggregate(union=Union('boundary'))['union']

# Get a buffer of 100 meters around a location
from django.contrib.gis.geos import Point
from myapp.models import Location

location = Location.objects.get(pk=1)
buffered_location = location.coordinates.buffer(100)

# Get the intersection of two areas
from django.contrib.gis.geos import Polygon
from myapp.models import Area

area1 = Area.objects.get(pk=1)
area2 = Area.objects.get(pk=2)
intersection = area1.boundary.intersection(area2.boundary)

# Enable spatial indexing for faster querying
from django.contrib.gis.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    coordinates = models.PointField(spatial_index=True)
```
