 Here are some important use case of serializers
1.  for data serialization (django object to json)
2. for data deserializatio (json data to django object)
3.  data validation 
4. custom field validation

Thers are 2 type of serializer (custom serializer and model serialzer)
Here are different use case for serializer
1. Custom serializer
2. Model serializer
3. Nested serializer
4. custom field serializer
5. field validation serializer
6. dynamic fields serializer
7. Hyperlink model serializer

What is a Serializer in Django?
A serializer in Django (from the Django REST Framework - DRF) is a tool used to convert complex data types (like Django model instances) into native Python datatypes (like dictionaries) that can be easily rendered into JSON or other content types. Similarly, serializers can also validate and deserialize data from incoming JSON or other formats into Django objects.

Key Features of Serializers

Serialization: Converts complex Python objects (e.g., QuerySets, models) into JSON or other formats.

Deserialization: Converts JSON or other formats into Python objects or Django model instances.

Validation: Validates incoming data before saving or using it.
### property is evaluated in model so dont need to define methond in serialize but method is calculated in serializer so we need to define a method that start with get_ to fetch property.
```
from rest_framework import serializers
from myapp.models import Product, Category

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """ Allows selecting specific fields dynamically. """
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)

        if fields:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class CategorySerializer(serializers.ModelSerializer):
    """ Nested Serializer Example """
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(DynamicFieldsModelSerializer):
    category = CategorySerializer()  # Nested serializer
    discounted_price = serializers.SerializerMethodField()  # Custom Field
    final_price = serializers.SerializerMethodField()  # Calls Model Method
    is_expensive = serializers.BooleanField(source='is_expensive', read_only=True)  # Calls Model Property
    url = serializers.HyperlinkedIdentityField(view_name='product-detail')  # Hyperlinked ModelSerializer

    class Meta:
        model = Product
        fields = ['url', 'id', 'name', 'description', 'price', 'stock', 'category', 
                  'discounted_price', 'final_price', 'is_expensive']

    def get_discounted_price(self, obj):
        """ Custom logic for computed field """
        return obj.price * 0.9  # 10% discount

    def get_final_price(self, obj):
        """ Calls the model method `get_final_price` """
        return obj.get_final_price()

    def validate_price(self, value):
        """ Field-level validation """
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value

    def validate(self, data):
        """ Object-level validation """
        if data.get('stock', 0) <= 0 and data.get('price', 0) > 100:
            raise serializers.ValidationError("Cannot set a price above $100 for out-of-stock items.")
        return data


serializer = ProductSerializer(product, fields=['id', 'name'])
```
Best Practices for Using Serializers

Use ModelSerializer for models to reduce boilerplate.

Add custom validation using validate_<field_name> or validate.

Use SerializerMethodField for computed fields.

Use nested serializers for complex relationships.

Use dynamic serializers to control which fields are returned in responses.