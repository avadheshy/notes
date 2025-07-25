# Django, DRF, and PostgreSQL Interview Q&A

---

## Django

### What is the purpose of Django's middleware?
- **Answer:** To process requests and responses globally.

### What is the effect of setting `queryset = None` in a ViewSet?
- **Answer:** It requires overriding `get_queryset`.

### How does Django handle circular imports in models?
- **Answer:** It uses lazy loading via `apps.get_model`.

### Which method is called when a serializer is saved?
- **Answer:** `save()`

### Which tool is used for profiling and optimizing Django queries?
- **Answer:** Django Debug Toolbar

---

## Django REST Framework (DRF)

### Which method in Django REST Framework is used to customize object-level permissions?
- **Answer:** `has_object_permission`

### What does the `Meta` class inside a serializer define?
- **Answer:** The fields to be serialized.

### Which renderer class allows API responses to be viewed in a web browser?
- **Answer:** `BrowsableAPIRenderer`

### What is the role of 'throttling' in DRF?
- **Answer:** To restrict API usage rate.

### Which DRF class is used to define custom pagination?
- **Answer:**
  - `PageNumberPagination`
  - `LimitOffsetPagination`
  - `CursorPagination`

### What does `allow_null=True` do in a serializer field?
- **Answer:** Allows `None` values.

### Which authentication method is stateless and suitable for APIs?
- **Answer:** Token-based

---

## API Tools & Best Practices

### What is the purpose of Swagger/OpenAPI in API development?
- **Answer:** To document and test APIs.

### What is the role of an API Gateway in microservices?
- **Answer:** To route requests and aggregate responses.

### What is the best practice for versioning REST APIs?
- **Answer:** Use URL path (e.g., `/api/v1/`)

---

## PostgreSQL

### What is the purpose of `EXPLAIN` in PostgreSQL?
- **Answer:** To analyze and show the execution plan of a query.

### Which PostgreSQL feature allows full-text search?
- **Answer:** `tsvector`

### What is the purpose of a PostgreSQL trigger?
- **Answer:** To automate actions on data changes.

### What is the safest way to execute raw SQL in Django?
- **Answer:** Using parameterized queries with `cursor.execute()`.

### Which PostgreSQL data type is best for storing structured JSON data?
- **Answer:** `JSONB`

---

## Django ORM

### What is the effect of using `exists()` on a queryset?
- **Answer:** Returns a boolean.

### Which ORM method is used to defer loading of specific fields?
- **Answer:** `defer()`

### Which ORM method is best for bulk updates?
- **Answer:** `bulk_update()`

### Which ORM method is used to annotate each object with a calculated field?
- **Answer:** `annotate()`

### What is the difference between `values()` and `values_list()` in Django ORM?
- **Answer:**
  - `values()` returns dictionaries.
  - `values_list()` returns tuples.

