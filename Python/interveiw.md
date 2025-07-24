# Complete Python Interview Guide

## 1. Mutable and Immutable Data Types

### Immutable Data Types
- **Definition**: Objects whose state cannot be modified after creation
- **Examples**: int, float, string, tuple, frozenset, bool
- **Characteristics**:
  - When you "modify" them, a new object is created
  - Safe to use as dictionary keys
  - Thread-safe by nature

### Mutable Data Types
- **Definition**: Objects whose state can be modified after creation
- **Examples**: list, dict, set, bytearray
- **Characteristics**:
  - Can be modified in-place
  - Cannot be used as dictionary keys
  - Need synchronization in multi-threaded environments

```python
# Immutable example
x = "hello"
y = x
x += " world"
print(x)  # "hello world"
print(y)  # "hello" (unchanged)

# Mutable example
list1 = [1, 2, 3]
list2 = list1
list1.append(4)
print(list1)  # [1, 2, 3, 4]
print(list2)  # [1, 2, 3, 4] (both changed)
```

## 2. Difference Between List and Tuple

| Aspect | List | Tuple |
|--------|------|-------|
| Mutability | Mutable | Immutable |
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Performance | Slower | Faster |
| Memory | More memory | Less memory |
| Use case | Dynamic data | Fixed data |
| Methods | Many methods (append, remove, etc.) | Few methods (count, index) |

```python
# List operations
my_list = [1, 2, 3]
my_list.append(4)  # Works
my_list[0] = 10    # Works

# Tuple operations
my_tuple = (1, 2, 3)
# my_tuple.append(4)  # Error!
# my_tuple[0] = 10    # Error!
```

## 3. List Comprehension and Filter

### List Comprehension
```python
# Basic syntax: [expression for item in iterable if condition]
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# Nested comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
```

### Filter Function
```python
# filter(function, iterable)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Filter with list comprehension (more Pythonic)
even_numbers = [x for x in numbers if x % 2 == 0]
```

## 4. Lambda Functions

### Definition
Anonymous functions defined using the `lambda` keyword.

```python
# Basic lambda
square = lambda x: x**2
print(square(5))  # 25

# Lambda with multiple arguments
add = lambda x, y: x + y
print(add(3, 4))  # 7

# Lambda in higher-order functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
filtered = list(filter(lambda x: x > 2, numbers))
```

### Use Cases
- Short, simple functions
- With map(), filter(), reduce()
- Event handling
- Sorting with custom keys

## 5. Difference Between Dictionary and Set

| Aspect | Dictionary | Set |
|--------|------------|-----|
| Structure | Key-value pairs | Unique elements only |
| Syntax | `{'key': 'value'}` | `{1, 2, 3}` |
| Ordering | Ordered (Python 3.7+) | Unordered |
| Duplicates | Keys must be unique | No duplicates allowed |
| Access | `dict[key]` | `item in set` |
| Use case | Mapping, lookup | Uniqueness, set operations |

```python
# Dictionary
person = {'name': 'John', 'age': 30}
print(person['name'])  # John

# Set
unique_numbers = {1, 2, 3, 3, 4}
print(unique_numbers)  # {1, 2, 3, 4}
```

## 6. Difference Between `is` and `==` Operator

### `==` Operator (Equality)
- Compares **values**
- Checks if objects have the same content

### `is` Operator (Identity)
- Compares **object identity**
- Checks if variables point to the same object in memory

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True (same values)
print(a is b)  # False (different objects)
print(a is c)  # True (same object)

# Special case with small integers
x = 256
y = 256
print(x is y)  # True (Python caches small integers)

x = 257
y = 257
print(x is y)  # False (not cached)
```

## 7. Bug in `def fun(a=[]):`

### The Problem
Default mutable arguments are evaluated only once at function definition time, creating a shared object.

```python
# Buggy code
def append_item(item, target_list=[]):
    target_list.append(item)
    return target_list

print(append_item(1))  # [1]
print(append_item(2))  # [1, 2] - Bug! Should be [2]
```

### The Solution
```python
def append_item(item, target_list=None):
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list
```

## 8. Pros and Cons of Python

### Pros
- **Easy to learn**: Simple, readable syntax
- **Versatile**: Web development, data science, AI, automation
- **Large ecosystem**: Extensive libraries and frameworks
- **Cross-platform**: Runs on multiple operating systems
- **Community support**: Active community and documentation
- **Rapid development**: Quick prototyping and development
- **Object-oriented**: Supports multiple programming paradigms

### Cons
- **Performance**: Slower than compiled languages (C++, Java)
- **Mobile development**: Limited native mobile app support
- **Runtime errors**: Dynamic typing can lead to runtime issues
- **Memory consumption**: Higher memory usage
- **GIL limitation**: Global Interpreter Lock limits threading
- **Dependency management**: Can become complex in large projects

## 9. Generator

### Definition
Functions that return an iterator object, yielding items one at a time using `yield`.

```python
# Generator function
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Generator expression
squares = (x**2 for x in range(10))

# Usage
fib = fibonacci()
for _ in range(5):
    print(next(fib))  # 0, 1, 1, 2, 3
```

### Benefits
- **Memory efficient**: Generates values on-demand
- **Lazy evaluation**: Computes values only when needed
- **Infinite sequences**: Can represent infinite data

## 10. Decorator

### Definition
Functions that modify or extend the behavior of other functions without changing their code.

```python
# Basic decorator
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Decorator with parameters
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello!")
```

### Use Cases
- Logging
- Authentication
- Caching
- Timing functions
- Input validation

## 11. Iterator (iter and next)

### Definition
An object that implements the iterator protocol (`__iter__` and `__next__` methods).

```python
# Creating an iterator
class Counter:
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count < self.max_count:
            self.count += 1
            return self.count
        raise StopIteration

# Usage
counter = Counter(3)
for num in counter:
    print(num)  # 1, 2, 3

# Using iter() and next()
my_list = [1, 2, 3]
iterator = iter(my_list)
print(next(iterator))  # 1
print(next(iterator))  # 2
```

## 12. Iterable (iter)

### Definition
An object that can be iterated over (implements `__iter__` method).

```python
# Examples of iterables
my_list = [1, 2, 3]        # List
my_tuple = (1, 2, 3)       # Tuple
my_string = "hello"        # String
my_dict = {'a': 1, 'b': 2} # Dictionary

# Check if object is iterable
from collections.abc import Iterable
print(isinstance(my_list, Iterable))  # True
print(isinstance(42, Iterable))       # False
```

## 13. Difference Between Static and Class Method

### Instance Method
- Has access to `self` and instance data
- Can access and modify instance state

### Class Method
- Decorated with `@classmethod`
- Receives `cls` as first parameter
- Can access class attributes but not instance attributes

### Static Method
- Decorated with `@staticmethod`
- No access to `self` or `cls`
- Behaves like a regular function but belongs to the class namespace

```python
class MyClass:
    class_variable = "I'm a class variable"
    
    def __init__(self, value):
        self.instance_variable = value
    
    def instance_method(self):
        return f"Instance: {self.instance_variable}"
    
    @classmethod
    def class_method(cls):
        return f"Class: {cls.class_variable}"
    
    @staticmethod
    def static_method():
        return "Static method called"

# Usage
obj = MyClass("test")
print(obj.instance_method())      # Instance: test
print(MyClass.class_method())     # Class: I'm a class variable
print(MyClass.static_method())    # Static method called
```

## 14. Memory Management and Garbage Collector

### Python Memory Management
- **Private heap**: All Python objects stored in private heap
- **Memory manager**: Handles allocation/deallocation automatically
- **Reference counting**: Primary garbage collection mechanism

### Garbage Collector Role
```python
import gc

# Reference counting example
a = [1, 2, 3]  # Reference count = 1
b = a          # Reference count = 2
del a          # Reference count = 1
del b          # Reference count = 0, object deleted

# Circular reference (needs GC)
class Node:
    def __init__(self, value):
        self.value = value
        self.ref = None

a = Node(1)
b = Node(2)
a.ref = b
b.ref = a  # Circular reference

# Manual garbage collection
gc.collect()  # Force garbage collection
print(gc.get_count())  # Get collection statistics
```

### Memory Management Features
- **Automatic allocation**: No manual memory allocation needed
- **Reference counting**: Objects deleted when reference count reaches 0
- **Cycle detection**: Handles circular references
- **Memory pools**: Optimized allocation for small objects

## 15. Multithreading and GIL

### Global Interpreter Lock (GIL)
- **Purpose**: Prevents multiple threads from executing Python code simultaneously
- **Impact**: Limits CPU-bound multithreading effectiveness
- **Benefit**: Simplifies memory management and prevents race conditions

```python
import threading
import time

def cpu_bound_task(n):
    """CPU-intensive task"""
    total = 0
    for i in range(n):
        total += i * i
    return total

def io_bound_task():
    """I/O-intensive task"""
    time.sleep(1)
    return "Task completed"

# Threading is effective for I/O-bound tasks
threads = []
for i in range(3):
    t = threading.Thread(target=io_bound_task)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

### When to Use Multithreading
- **I/O-bound operations**: File operations, network requests, database queries
- **Concurrent user interfaces**: Keeping UI responsive
- **Producer-consumer patterns**: Background processing

## 16. Variable Passing: Value or Reference

### Python's Approach
Python uses "call by object reference" or "call by sharing":
- **Immutable objects**: Behave like pass-by-value
- **Mutable objects**: Behave like pass-by-reference

```python
def modify_immutable(x):
    x = x + 10  # Creates new object
    print(f"Inside function: {x}")

def modify_mutable(lst):
    lst.append(4)  # Modifies original object
    print(f"Inside function: {lst}")

# Immutable example
num = 5
modify_immutable(num)
print(f"Outside function: {num}")  # Still 5

# Mutable example
my_list = [1, 2, 3]
modify_mutable(my_list)
print(f"Outside function: {my_list}")  # [1, 2, 3, 4]
```

## 17. List/Dict/String Comprehension and Tuple Comprehension

### List Comprehension
```python
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

### Dictionary Comprehension
```python
square_dict = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### String Comprehension
```python
# Not directly supported, but can create strings
vowels = ''.join([char for char in "hello world" if char in "aeiou"])
```

### Why No Tuple Comprehension?
```python
# This creates a generator, not a tuple
gen = (x**2 for x in range(5))

# To create a tuple, use tuple()
tup = tuple(x**2 for x in range(5))  # (0, 1, 4, 9, 16)
```

**Reason**: Parentheses are used for generator expressions, which are more useful than tuple comprehensions.

## 18. List/String Slicing

### Basic Slicing Syntax
`sequence[start:stop:step]`

```python
# List slicing
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[2:7])     # [2, 3, 4, 5, 6]
print(my_list[:5])      # [0, 1, 2, 3, 4]
print(my_list[5:])      # [5, 6, 7, 8, 9]
print(my_list[::2])     # [0, 2, 4, 6, 8]
print(my_list[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# String slicing
text = "Hello, World!"
print(text[0:5])        # "Hello"
print(text[-6:])        # "World!"
print(text[::2])        # "Hlo ol!"
```

### Advanced Slicing
```python
# Negative indices
print(my_list[-3:])     # [7, 8, 9]
print(my_list[:-3])     # [0, 1, 2, 3, 4, 5, 6]

# Step parameter
print(my_list[1:8:2])   # [1, 3, 5, 7]
```

## 19. Memory and Speed: List vs Tuple Comprehension

### Performance Comparison
```python
import timeit

# List comprehension
list_time = timeit.timeit(
    '[x**2 for x in range(1000)]', 
    number=10000
)

# Tuple creation from generator
tuple_time = timeit.timeit(
    'tuple(x**2 for x in range(1000))', 
    number=10000
)

print(f"List comprehension: {list_time}")
print(f"Tuple from generator: {tuple_time}")
```

### Memory Usage
- **Tuples**: More memory-efficient, immutable
- **Lists**: Less memory-efficient, mutable, more functionality

### When to Use Each
- **Lists**: When you need to modify data
- **Tuples**: When data is fixed, need hashable type, or want better performance

## 20. Difference Between Python 2 and Python 3

| Feature | Python 2 | Python 3 |
|---------|----------|----------|
| Print | `print "Hello"` | `print("Hello")` |
| Division | `5/2 = 2` | `5/2 = 2.5` |
| Unicode | Separate unicode type | Default string is unicode |
| xrange | `xrange()` exists | Only `range()` (which is lazy) |
| Exceptions | `except Exception, e:` | `except Exception as e:` |
| Input | `raw_input()` and `input()` | Only `input()` |
| Iterators | `dict.keys()` returns list | Returns view object |
| String formatting | `%` formatting | f-strings, `.format()` |

### Migration Considerations
```python
# Python 2 style
print "Hello, %s!" % name
for i in xrange(10):
    pass

# Python 3 style
print(f"Hello, {name}!")
for i in range(10):
    pass
```

## 21. Deep Copy vs Shallow Copy

### Shallow Copy
Creates a new object but references to nested objects are shared.

```python
import copy

original = [[1, 2, 3], [4, 5, 6]]
shallow = copy.copy(original)
# or shallow = original.copy()
# or shallow = original[:]

shallow[0][0] = 999
print(original)  # [[999, 2, 3], [4, 5, 6]] - Original affected!
```

### Deep Copy
Creates completely independent copy, including nested objects.

```python
import copy

original = [[1, 2, 3], [4, 5, 6]]
deep = copy.deepcopy(original)

deep[0][0] = 999
print(original)  # [[1, 2, 3], [4, 5, 6]] - Original unchanged
print(deep)      # [[999, 2, 3], [4, 5, 6]]
```

### When to Use Each
- **Shallow copy**: When nested objects shouldn't be modified
- **Deep copy**: When you need completely independent objects

## 22. Optimizing Python Program Performance

### Profiling Tools
```python
import cProfile
import timeit

# Using cProfile
def slow_function():
    return sum(i**2 for i in range(10000))

cProfile.run('slow_function()')

# Using timeit
time_taken = timeit.timeit(
    'sum(i**2 for i in range(10000))', 
    number=1000
)
```

### Optimization Techniques

#### 1. Use Built-in Functions
```python
# Slow
total = 0
for i in range(10000):
    total += i

# Fast
total = sum(range(10000))
```

#### 2. List Comprehensions
```python
# Slower
result = []
for i in range(1000):
    if i % 2 == 0:
        result.append(i**2)

# Faster
result = [i**2 for i in range(1000) if i % 2 == 0]
```

#### 3. Use Local Variables
```python
import math

# Slower - repeated global lookup
def calculate_distances(points):
    distances = []
    for point in points:
        distances.append(math.sqrt(point[0]**2 + point[1]**2))
    return distances

# Faster - local variable
def calculate_distances(points):
    sqrt = math.sqrt  # Local reference
    distances = []
    for point in points:
        distances.append(sqrt(point[0]**2 + point[1]**2))
    return distances
```

#### 4. Use Appropriate Data Structures
```python
# Slow for membership testing
items = ['apple', 'banana', 'orange', 'grape']
if 'banana' in items:  # O(n) complexity
    pass

# Fast for membership testing
items = {'apple', 'banana', 'orange', 'grape'}
if 'banana' in items:  # O(1) complexity
    pass
```

## 23. Handling Multithreading and Multiprocessing

### Threading (I/O-bound tasks)
```python
import threading
import requests

def fetch_url(url):
    response = requests.get(url)
    print(f"Status: {response.status_code} for {url}")

urls = ['http://google.com', 'http://github.com', 'http://stackoverflow.com']

# Using threading
threads = []
for url in urls:
    t = threading.Thread(target=fetch_url, args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
```

### Multiprocessing (CPU-bound tasks)
```python
import multiprocessing

def cpu_intensive_task(n):
    return sum(i**2 for i in range(n))

if __name__ == '__main__':
    # Using multiprocessing
    with multiprocessing.Pool() as pool:
        numbers = [100000, 200000, 300000, 400000]
        results = pool.map(cpu_intensive_task, numbers)
        print(results)
```

### Asyncio (Concurrent I/O)
```python
import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = ['http://google.com', 'http://github.com']
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

# Run the async function
# asyncio.run(main())
```

## 24. Handling Large Datasets

### Memory-Efficient Techniques

#### 1. Generators for Large Files
```python
def read_large_file(file_path):
    """Generator to read large files line by line"""
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Usage
for line in read_large_file('large_file.txt'):
    process_line(line)  # Process one line at a time
```

#### 2. Chunking Data
```python
import pandas as pd

def process_large_csv(file_path, chunk_size=10000):
    """Process large CSV in chunks"""
    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        # Process each chunk
        processed_chunk = chunk.groupby('category').sum()
        yield processed_chunk

# Usage
results = []
for chunk_result in process_large_csv('large_data.csv'):
    results.append(chunk_result)

# Combine results
final_result = pd.concat(results).groupby(level=0).sum()
```

#### 3. Memory Mapping
```python
import mmap

def search_large_file(file_path, search_term):
    """Search in large file using memory mapping"""
    with open(file_path, 'r') as file:
        with mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as mmapped_file:
            if mmapped_file.find(search_term.encode()) != -1:
                return True
    return False
```

#### 4. Using Databases
```python
import sqlite3

def process_with_database(data_iterator):
    """Use SQLite for large data processing"""
    conn = sqlite3.connect(':memory:')  # In-memory database
    conn.execute('''CREATE TABLE data (id INTEGER, value REAL, category TEXT)''')
    
    # Insert data in batches
    batch = []
    for i, item in enumerate(data_iterator):
        batch.append(item)
        if len(batch) >= 10000:  # Process in batches
            conn.executemany('INSERT INTO data VALUES (?, ?, ?)', batch)
            conn.commit()
            batch = []
    
    # Process remaining items
    if batch:
        conn.executemany('INSERT INTO data VALUES (?, ?, ?)', batch)
        conn.commit()
    
    # Perform aggregations
    result = conn.execute('SELECT category, AVG(value) FROM data GROUP BY category').fetchall()
    conn.close()
    return result
```

## 25. Python: Compiled or Interpreted?

### Python is Both!

#### Compilation Phase
1. **Source code (.py)** → **Bytecode (.pyc)**
2. Python compiles source code to bytecode
3. Bytecode is stored in `__pycache__` directory

#### Interpretation Phase
1. **Python Virtual Machine (PVM)** executes bytecode
2. Bytecode is interpreted line by line

```python
import dis

def simple_function(x, y):
    return x + y

# View bytecode
dis.dis(simple_function)
```

### Different Python Implementations
- **CPython**: Reference implementation (compiles to bytecode, interprets bytecode)
- **PyPy**: Just-In-Time compilation for performance
- **Jython**: Compiles to Java bytecode
- **IronPython**: Compiles to .NET bytecode

## 26. Static vs Dynamic Typing

### Static Typing
- **Definition**: Variable types are checked at compile time
- **Examples**: C++, Java, C#
- **Benefits**: Early error detection, better performance, better IDE support

### Dynamic Typing
- **Definition**: Variable types are checked at runtime
- **Python is dynamically typed**: Types are determined during execution

```python
# Dynamic typing in Python
x = 5        # x is int
x = "hello"  # x is now str
x = [1, 2]   # x is now list

# Type hints (optional static typing)
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Using typing module
from typing import List, Dict, Optional

def process_items(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}
```

### Benefits of Each Approach
**Static Typing:**
- Catches type errors early
- Better performance
- Better IDE support and documentation

**Dynamic Typing:**
- More flexible and concise code
- Faster development
- Duck typing support

## 27. *args and **kwargs

### *args (Arbitrary Arguments)
Allows function to accept variable number of positional arguments.

```python
def sum_all(*args):
    """Accept variable number of arguments"""
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))  # 15
print(sum_all(10, 20))         # 30

def greet(greeting, *names):
    """Mix regular and arbitrary arguments"""
    for name in names:
        print(f"{greeting}, {name}!")

greet("Hello", "Alice", "Bob", "Charlie")
```

### **kwargs (Keyword Arguments)
Allows function to accept variable number of keyword arguments.

```python
def create_profile(**kwargs):
    """Accept variable keyword arguments"""
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

profile = create_profile(name="John", age=30, city="New York")
print(profile)  # {'name': 'John', 'age': 30, 'city': 'New York'}

def process_data(required_param, *args, **kwargs):
    """Combine all three types"""
    print(f"Required: {required_param}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

process_data("test", 1, 2, 3, name="John", age=30)
```

### Unpacking Arguments
```python
def multiply(x, y, z):
    return x * y * z

numbers = [2, 3, 4]
result = multiply(*numbers)  # Unpack list

data = {'x': 2, 'y': 3, 'z': 4}
result = multiply(**data)    # Unpack dictionary
```

## 28. Built-in Data Types

### Numeric Types
```python
# int
age = 25
big_number = 123_456_789  # Underscores for readability

# float
price = 19.99
scientific = 1.5e-4  # Scientific notation

# complex
z = 3 + 4j
print(z.real)  # 3.0
print(z.imag)  # 4.0
```

### Boolean Type
```python
is_valid = True
is_empty = False

# Boolean operations
print(True and False)  # False
print(True or False)   # True
print(not True)        # False
```

### Sequence Types
```python
# String
text = "Hello, World!"
multiline = """This is a
multiline string"""

# List
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# Tuple
coordinates = (10, 20)
single_item_tuple = (42,)  # Note the comma

# Range
numbers = range(0, 10, 2)  # 0, 2, 4, 6, 8
```

### Mapping Type
```python
# Dictionary
person = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
```

### Set Types
```python
# Set
unique_numbers = {1, 2, 3, 4, 5}
empty_set = set()  # Note: {} creates dict, not set

# Frozenset (immutable set)
immutable_set = frozenset([1, 2, 3, 4, 5])
```

### Binary Types
```python
# Bytes
data = b"Hello"
print(type(data))  # <class 'bytes'>

# Bytearray (mutable)
mutable_data = bytearray(b"Hello")
mutable_data[0] = ord('h')  # Change first character

# Memoryview
mv = memoryview(b"Hello World")
print(mv[0:5])  # View first 5 bytes
```

## 29. Docstrings

### Definition
Documentation strings that describe what a function, class, or module does.

### Types of Docstrings

#### Function Docstrings
```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    
    Returns:
        float: The area of the rectangle
    
    Raises:
        ValueError: If length or width is negative
    
    Examples:
        >>> calculate_area(5, 3)
        15.0
        >>> calculate_area(2.5, 4)
        10.0
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be positive")
    return length * width
```

#### Class Docstrings
```python
class Rectangle:
    """
    A class to represent a rectangle.
    
    Attributes:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    """
    
    def __init__(self, length, width):
        """
        Initialize a Rectangle instance.
        
        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
        """
        self.length = length
        self.width = width
```

#### Module Docstrings
```python
"""
geometry.py

This module provides basic geometric calculations.

Classes:
    Rectangle: Represents a rectangle shape
    Circle: Represents a circle shape

Functions:
    calculate_area: Calculate area of various shapes
"""
```

### Accessing Docstrings
```python
print(calculate_area.__doc__)  # Print function docstring
help(calculate_area)           # Show formatted help
```

### Docstring Formats
- **Google Style**: Used above
- **NumPy Style**: Popular in scientific computing
- **Sphinx Style**: reStructuredText format

## 30. Exception Handling

### Basic Exception Handling
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
    result = None
else:
    print("No exception occurred")
finally:
    print("This always executes")
```

### Multiple Exceptions
```python
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    except TypeError:
        print("Invalid type for division")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
```

### Custom Exceptions
```python
class CustomError(Exception):
    """Custom exception class"""
    def __init__(self, message, error_code=None):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)

def validate_age(age):
    if age < 0:
        raise CustomError("Age cannot be negative", error_code=1001)
    if age > 150:
        raise CustomError("Age seems unrealistic", error_code=1002)
    return True

# Usage
try:
    validate_age(-5)
except CustomError as e:
    print(f"Validation error: {e.message}, Code: {e.error_code}")
```

### Exception Hierarchy
```python
# Common exception hierarchy
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- Exception
      +-- ArithmeticError
      |    +-- ZeroDivisionError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- ValueError
      +-- TypeError
      +-- FileNotFoundError
```

## 31. List vs Array

### Python Lists
```python
# Lists are dynamic, can hold different types
my_list = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, [1, 2]]

# List operations
my_list.append(6)
my_list.remove(3)
my_list.insert(0, 0)
```

### Arrays (from array module)
```python
import array

# Arrays are homogeneous, more memory efficient
int_array = array.array('i', [1, 2, 3, 4, 5])  # 'i' for integers
float_array = array.array('f', [1.1, 2.2, 3.3])  # 'f' for floats

# Array operations
int_array.append(6)
int_array.remove(3)
```

### NumPy Arrays (Third-party)
```python
import numpy as np

# NumPy arrays are highly optimized
np_array = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2], [3, 4]])

# Vectorized operations
result = np_array * 2  # Multiply all elements by 2
```

### Comparison Table
| Feature | List | Array | NumPy Array |
|---------|------|-------|-------------|
| Type flexibility | Mixed types | Homogeneous | Homogeneous |
| Memory efficiency | Less efficient | More efficient | Most efficient |
| Performance | Good for general use | Better for numbers | Best for numerical |
| Built-in | Yes | Yes | Third-party |

## 32. Modules and Packages

### Modules
A module is a single Python file containing functions, classes, and variables.

```python
# math_utils.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

PI = 3.14159

# Using the module
import math_utils
result = math_utils.add(5, 3)

# Alternative imports
from math_utils import add, PI
from math_utils import *  # Import all (not recommended)
import math_utils as mu  # Alias
```

### Packages
A package is a collection of modules organized in directories.

```python
# Package structure
mypackage/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        submodule.py
```

```python
# __init__.py makes it a package
# Can be empty or contain initialization code

# mypackage/__init__.py
from .module1 import function1
from .module2 import Class1

__all__ = ['function1', 'Class1']  # Define public API
```

```python
# Using packages
import mypackage
from mypackage import module1
from mypackage.subpackage import submodule
```

### Module Search Path
```python
import sys
print(sys.path)  # Shows where Python looks for modules

# Adding to path
sys.path.append('/path/to/custom/modules')
```

## 33. Variable Scope (LEGB Rule)

### LEGB Rule
Python resolves names using LEGB rule:
- **L**ocal: Inside current function
- **E**nclosing: In enclosing functions
- **G**lobal: At module level
- **B**uilt-in: Built-in names

```python
# Built-in scope
print(len([1, 2, 3]))  # 'len' is built-in

# Global scope
global_var = "I'm global"

def outer_function():
    # Enclosing scope
    enclosing_var = "I'm enclosing"
    
    def inner_function():
        # Local scope
        local_var = "I'm local"
        print(local_var)      # Local
        print(enclosing_var)  # Enclosing
        print(global_var)     # Global
        print(len)            # Built-in
    
    inner_function()

outer_function()
```

### Global and Nonlocal Keywords
```python
x = 10  # Global

def modify_global():
    global x
    x = 20  # Modifies global x

def outer():
    y = 30  # Enclosing
    
    def inner():
        nonlocal y
        y = 40  # Modifies enclosing y
    
    inner()
    print(y)  # Prints 40

modify_global()
print(x)  # Prints 20
outer()
```

### Local vs Global Variables
```python
count = 0  # Global

def increment():
    global count
    count += 1

def local_increment():
    count = 0  # Local variable (shadows global)
    count += 1
    return count

print(increment())  # Modifies global count
print(count)        # Global count is modified
print(local_increment())  # Local count, doesn't affect global
```

## 34. Logging Module

### Basic Logging
```python
import logging

# Basic configuration
logging.basicConfig(level=logging.DEBUG,
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Logging levels
logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')
```

### Advanced Logging
```python
import logging
from logging.handlers import RotatingFileHandler

# Create custom logger
logger = logging.getLogger('my_app')
logger.setLevel(logging.DEBUG)

# Create handlers
file_handler = RotatingFileHandler('app.log', maxBytes=1024*1024, backupCount=5)
console_handler = logging.StreamHandler()

# Create formatters
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_formatter = logging.Formatter('%(levelname)s - %(message)s')

# Add formatters to handlers
file_handler.setFormatter(file_formatter)
console_handler.setFormatter(console_formatter)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Usage
logger.info('Application started')
logger.error('An error occurred')
```

### Logging Configuration
```python
import logging.config

# Configuration dictionary
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': False
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)
```

## 35. Debugging with PDB

### Basic PDB Usage
```python
import pdb

def buggy_function(x, y):
    pdb.set_trace()  # Set breakpoint
    result = x + y
    result = result * 2
    return result

# Alternative: python -m pdb script.py
```

### PDB Commands
```python
# Common PDB commands:
# n (next): Execute next line
# s (step): Step into functions
# c (continue): Continue execution
# l (list): Show current code
# p variable_name: Print variable value
# pp variable_name: Pretty print
# w (where): Show stack trace
# u (up): Move up in stack
# d (down): Move down in stack
# q (quit): Quit debugger
```

### Advanced Debugging
```python
import pdb

def complex_function(data):
    for i, item in enumerate(data):
        if item < 0:
            pdb.set_trace()  # Conditional breakpoint
        processed = item * 2
        data[i] = processed
    return data

# Post-mortem debugging
import sys

def risky_function():
    return 1 / 0

try:
    risky_function()
except:
    pdb.post_mortem(sys.exc_info()[2])
```

### Using breakpoint() (Python 3.7+)
```python
def modern_debugging():
    x = 10
    y = 20
    breakpoint()  # Modern way (Python 3.7+)
    result = x + y
    return result
```

## 36. Multiple Inheritance

### Basic Multiple Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Mammal:
    def __init__(self, warm_blooded=True):
        self.warm_blooded = warm_blooded
    
    def give_birth(self):
        return "Gives birth to live young"

class Bird:
    def __init__(self, can_fly=True):
        self.can_fly = can_fly
    
    def lay_eggs(self):
        return "Lays eggs"

class Bat(Animal, Mammal):
    def __init__(self, name):
        Animal.__init__(self, name)
        Mammal.__init__(self)
    
    def speak(self):
        return "Screech!"

# Usage
bat = Bat("Bruce")
print(bat.name)         # From Animal
print(bat.give_birth()) # From Mammal
print(bat.speak())      # Overridden method
```

### Method Resolution Order (MRO)
```python
class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        print("B")

class C(A):
    def method(self):
        print("C")

class D(B, C):
    pass

# Check MRO
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)

d = D()
d.method()  # Prints "B" (follows MRO)
```

### Diamond Problem Solution
```python
class Base:
    def __init__(self):
        print("Base init")

class Left(Base):
    def __init__(self):
        super().__init__()
        print("Left init")

class Right(Base):
    def __init__(self):
        super().__init__()
        print("Right init")

class Child(Left, Right):
    def __init__(self):
        super().__init__()
        print("Child init")

# Using super() ensures Base.__init__ is called only once
child = Child()
# Output: Base init, Right init, Left init, Child init
```

## 37. OOP Concepts

### Inheritance
```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start(self):
        return f"{self.brand} {self.model} is starting"

class Car(Vehicle):  # Inheritance
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
    
    def start(self):  # Method overriding
        return f"Car {super().start()} with {self.doors} doors"
```

### Encapsulation
```python
class BankAccount:
    def __init__(self, initial_balance):
        self._balance = initial_balance    # Protected (convention)
        self.__account_id = "ACC123"      # Private (name mangling)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
    
    @property
    def balance(self):  # Getter
        return self._balance
    
    @balance.setter
    def balance(self, value):  # Setter
        if value >= 0:
            self._balance = value

account = BankAccount(1000)
print(account.balance)  # 1000
account.balance = 1500  # Uses setter
```

### Abstraction
```python
from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract base class
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# Cannot instantiate abstract class
# shape = Shape()  # TypeError

rectangle = Rectangle(5, 3)
print(rectangle.area())  # 15
```

### Polymorphism
```python
class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

class Cow:
    def make_sound(self):
        return "Moo!"

def animal_sound(animal):
    return animal.make_sound()  # Polymorphism

# Same method call, different behaviors
animals = [Dog(), Cat(), Cow()]
for animal in animals:
    print(animal_sound(animal))  # Woof!, Meow!, Moo!
```

## 38. Accessing Second Parent Class Method

### Method Resolution Order
```python
class GrandParent:
    def method(self):
        return "GrandParent method"

class Parent1(GrandParent):
    def method(self):
        return "Parent1 method"

class Parent2(GrandParent):
    def method(self):
        return "Parent2 method"

class Child(Parent1, Parent2):
    def access_parent2_method(self):
        # Direct access to Parent2's method
        return Parent2.method(self)
    
    def access_via_super(self):
        # Access next in MRO
        return super().method()
    
    def access_grandparent(self):
        # Access GrandParent directly
        return GrandParent.method(self)

child = Child()
print(child.access_parent2_method())  # "Parent2 method"
print(child.access_via_super())       # "Parent1 method" (follows MRO)
print(child.access_grandparent())     # "GrandParent method"
```

### Using super() with Arguments
```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    def get_b_method(self):
        # Get B's method specifically
        return super(C, self).method()  # Skip C, get B
    
    def get_c_method(self):
        # Get C's method specifically  
        return C.method(self)

d = D()
print(d.get_b_method())  # "B"
print(d.get_c_method())  # "C"
```

## 39. Pickling and Unpickling

### Basic Pickling
```python
import pickle

# Pickling (serialization)
data = {'name': 'John', 'age': 30, 'hobbies': ['reading', 'coding']}

# Save to file
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

# Unpickling (deserialization)
with open('data.pickle', 'rb') as f:
    loaded_data = pickle.load(f)

print(loaded_data)  # {'name': 'John', 'age': 30, 'hobbies': ['reading', 'coding']}
```

### Pickling Custom Objects
```python
import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

# Pickle custom object
person = Person("Alice", 25)
pickled_person = pickle.dumps(person)  # To bytes

# Unpickle
unpickled_person = pickle.loads(pickled_person)
print(unpickled_person)  # Person('Alice', 25)
```

### Custom Pickling Behavior
```python
import pickle

class CustomPickle:
    def __init__(self, data):
        self.data = data
        self.temp_data = "temporary"
    
    def __getstate__(self):
        # Custom pickling behavior
        state = self.__dict__.copy()
        del state['temp_data']  # Don't pickle temp_data
        return state
    
    def __setstate__(self, state):
        # Custom unpickling behavior
        self.__dict__.update(state)
        self.temp_data = "restored"  # Restore temp_data

obj = CustomPickle("important data")
pickled = pickle.dumps(obj)
unpickled = pickle.loads(pickled)
print(unpickled.data)      # "important data"
print(unpickled.temp_data) # "restored"
```

## 40. Difference Between dumps and pickle

### pickle.dump() vs pickle.dumps()
```python
import pickle

data = {'key': 'value'}

# pickle.dump() - writes to file object
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)  # Writes directly to file

# pickle.dumps() - returns bytes string
pickled_bytes = pickle.dumps(data)  # Returns bytes object
print(type(pickled_bytes))  # <class 'bytes'>

# Corresponding load methods
# pickle.load() - reads from file object
with open('data.pickle', 'rb') as f:
    loaded_data = pickle.load(f)

# pickle.loads() - loads from bytes string
loaded_from_bytes = pickle.loads(pickled_bytes)
```

### JSON Comparison
```python
import json
import pickle

data = {'name': 'John', 'age': 30}

# JSON serialization
json_string = json.dumps(data)  # Returns string
json.dump(data, open('data.json', 'w'))  # Writes to file

# Pickle serialization
pickle_bytes = pickle.dumps(data)  # Returns bytes
pickle.dump(data, open('data.pickle', 'wb'))  # Writes to file

print(f"JSON: {type(json_string)}")    # <class 'str'>
print(f"Pickle: {type(pickle_bytes)}") # <class 'bytes'>
```

## 41. Function Annotations

### Type Hints
```python
def greet(name: str, age: int) -> str:
    """
    Greet a person with their name and age.
    
    Args:
        name: Person's name
        age: Person's age
    
    Returns:
        Greeting message
    """
    return f"Hello {name}, you are {age} years old!"

# Function annotations are stored in __annotations__
print(greet.__annotations__)
# {'name': <class 'str'>, 'age': <class 'int'>, 'return': <class 'str'>}
```

### Complex Type Hints
```python
from typing import List, Dict, Optional, Union, Callable

def process_data(
    items: List[str],
    config: Dict[str, Union[str, int]],
    callback: Optional[Callable[[str], str]] = None
) -> Dict[str, List[str]]:
    """Process data with optional callback."""
    result = {}
    for item in items:
        processed = callback(item) if callback else item.upper()
        result[processed] = [item]
    return result

# Generic type hints
from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T:
        return self._items.pop()
```

### Runtime Type Checking
```python
from typing import get_type_hints

def validate_types(func):
    """Decorator to validate function arguments at runtime."""
    def wrapper(*args, **kwargs):
        hints = get_type_hints(func)
        # Type checking logic here
        return func(*args, **kwargs)
    return wrapper

@validate_types
def add_numbers(a: int, b: int) -> int:
    return a + b
```

## 42. Exception Groups (Python 3.11+)

### Basic Exception Groups
```python
# Exception groups allow raising multiple exceptions
def process_items(items):
    exceptions = []
    results = []
    
    for i, item in enumerate(items):
        try:
            result = 1 / item
            results.append(result)
        except ZeroDivisionError as e:
            exceptions.append(e)
    
    if exceptions:
        raise ExceptionGroup("Processing errors", exceptions)
    
    return results

# Handling exception groups
try:
    process_items([1, 0, 2, 0, 3])
except* ZeroDivisionError as eg:
    print(f"Caught {len(eg.exceptions)} zero division errors")
```

### Nested Exception Groups
```python
def complex_operation():
    validation_errors = []
    processing_errors = []
    
    # Validation phase
    try:
        validate_input()
    except ValueError as e:
        validation_errors.append(e)
    
    # Processing phase
    try:
        process_data()
    except RuntimeError as e:
        processing_errors.append(e)
    
    all_errors = []
    if validation_errors:
        all_errors.append(ExceptionGroup("Validation", validation_errors))
    if processing_errors:
        all_errors.append(ExceptionGroup("Processing", processing_errors))
    
    if all_errors:
        raise ExceptionGroup("Operation failed", all_errors)
```

## 43. Match Statement (Python 3.10+)

### Basic Pattern Matching
```python
def handle_data(data):
    match data:
        case int() if data > 0:
            return f"Positive integer: {data}"
        case int() if data < 0:
            return f"Negative integer: {data}"
        case 0:
            return "Zero"
        case str() if len(data) > 0:
            return f"Non-empty string: {data}"
        case []:
            return "Empty list"
        case [x] if isinstance(x, int):
            return f"List with one integer: {x}"
        case [x, y]:
            return f"List with two items: {x}, {y}"
        case {"name": name, "age": age}:
            return f"Person: {name}, age {age}"
        case _:  # Default case
            return "Unknown data type"

# Examples
print(handle_data(42))        # Positive integer: 42
print(handle_data("hello"))   # Non-empty string: hello
print(handle_data([1, 2]))    # List with two items: 1, 2
print(handle_data({"name": "John", "age": 30}))  # Person: John, age 30
```

### Advanced Pattern Matching
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def analyze_point(point):
    match point:
        case Point(x=0, y=0):
            return "Origin"
        case Point(x=0, y=y):
            return f"On Y-axis at {y}"
        case Point(x=x, y=0):
            return f"On X-axis at {x}"
        case Point(x=x, y=y) if x == y:
            return f"On diagonal at ({x}, {y})"
        case Point(x=x, y=y):
            return f"Point at ({x}, {y})"
        case _:
            return "Not a point"

# Usage
print(analyze_point(Point(0, 0)))    # Origin
print(analyze_point(Point(3, 3)))    # On diagonal at (3, 3)
```

## 44. Walrus Operator (:=)

### Assignment Expressions
```python
# Traditional approach
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared = []
for n in numbers:
    result = n ** 2
    if result > 25:
        squared.append(result)

# Using walrus operator
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared = [result for n in numbers if (result := n ** 2) > 25]
print(squared)  # [36, 49, 64, 81, 100]
```

### Common Use Cases
```python
# Reading files
with open('data.txt') as f:
    while (line := f.readline()):
        print(line.strip())

# Regular expressions
import re
pattern = r'\d+'
text = "The number is 42 and another is 123"

if (match := re.search(pattern, text)):
    print(f"Found: {match.group()}")  # Found: 42

# Function calls
def expensive_operation():
    # Simulate expensive computation
    return 42

# Avoid multiple calls
if (result := expensive_operation()) > 40:
    print(f"Result is {result}")
    # Use result again without recalling function
    print(f"Double result: {result * 2}")
```

## 45. Multithreading in New Python Versions

### Improvements in Recent Versions
```python
import asyncio
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

# Python 3.9+ ThreadPoolExecutor improvements
def io_task(n):
    import time
    time.sleep(1)
    return n ** 2

# Using ThreadPoolExecutor with context manager
with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(io_task, i) for i in range(5)]
    for future in as_completed(futures):
        result = future.result()
        print(f"Result: {result}")
```

### Async/Await Improvements
```python
import asyncio

# Python 3.11+ TaskGroup
async def fetch_data(url):
    await asyncio.sleep(1)  # Simulate network request
    return f"Data from {url}"

async def main():
    urls = ["http://site1.com", "http://site2.com", "http://site3.com"]
    
    # Using TaskGroup (Python 3.11+)
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(fetch_data(url)) for url in urls]
    
    results = [task.result() for task in tasks]
    return results

# asyncio.run(main())
```

### Sub-interpreters (Experimental)
```python
# Note: This is experimental and syntax may change
# Sub-interpreters can potentially bypass GIL limitations

import _xxsubinterpreters as interpreters

# Create sub-interpreter
interp_id = interpreters.create()

# Run code in sub-interpreter
code = """
import threading
import time

def worker():
    for i in range(5):
        print(f"Worker: {i}")
        time.sleep(0.1)

thread = threading.Thread(target=worker)
thread.start()
thread.join()
"""

interpreters.run_string(interp_id, code)
interpreters.destroy(interp_id)
```

## 46. How to implement unit testing in Python?

Unit testing in Python can be implemented using the built-in `unittest` module or third-party frameworks like `pytest`.

### Using unittest:
```python
import unittest

class Calculator:
    def add(self, a, b):
        return a + b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
```

### Using pytest:
```python
# test_calculator.py
import pytest

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(10, 0)
```

### Key Testing Concepts:
- **Test fixtures**: Setup and teardown code using `setUp()` and `tearDown()`
- **Test discovery**: Automatic test detection
- **Assertions**: Methods to check expected outcomes
- **Mocking**: Simulating external dependencies

## 47. What is scope resolution and name spaces in Python? What are LEGB rules?

**Namespace** is a mapping from names to objects. Python uses namespaces to organize and manage variable names.

**LEGB Rules** define the order of scope resolution:

1. **L - Local**: Inside the current function
2. **E - Enclosing**: In enclosing functions (closures)
3. **G - Global**: At the module level
4. **B - Built-in**: Built-in names like `print`, `len`

```python
# Built-in scope
print("Hello")  # print is in built-in scope

# Global scope
global_var = "I'm global"

def outer_function():
    # Enclosing scope
    enclosing_var = "I'm enclosing"
    
    def inner_function():
        # Local scope
        local_var = "I'm local"
        
        # LEGB resolution order
        print(local_var)      # Local
        print(enclosing_var)  # Enclosing
        print(global_var)     # Global
        print(len([1, 2, 3])) # Built-in
    
    inner_function()

# Example of scope modification
x = 10  # Global

def modify_scopes():
    global x
    x = 20  # Modifies global x
    
    def inner():
        nonlocal x
        x = 30  # Modifies enclosing x
    
    inner()
```

## 48. What is the difference between .py and .pyc files?

**.py files**:
- Source code files written in Python
- Human-readable text files
- Contain the actual Python code

**.pyc files**:
- Compiled bytecode files
- Binary files containing Python bytecode
- Created automatically by Python interpreter
- Stored in `__pycache__` directory
- Platform-independent but Python version-specific

```python
# When you run: python mymodule.py
# Python creates: __pycache__/mymodule.cpython-39.pyc

# Benefits of .pyc files:
# 1. Faster loading (no compilation step)
# 2. Source code protection (somewhat)
# 3. Reduced startup time for modules
```

**Process**:
1. Python compiles .py to bytecode
2. Bytecode is executed by Python Virtual Machine (PVM)
3. .pyc files are created for imported modules, not main script

## 49. What is the use of help() and dir() functions?

### help() function:
Provides documentation and help information about objects.

```python
help(list)          # Help for list class
help(list.append)   # Help for specific method
help('MODULES')     # List all available modules

# Custom function with docstring
def my_function():
    """This function does something useful."""
    pass

help(my_function)   # Shows the docstring
```

### dir() function:
Returns a list of valid attributes and methods for an object.

```python
# List attributes of an object
dir(list)           # All list methods and attributes
dir()               # Current namespace
dir(__builtins__)   # Built-in functions

class MyClass:
    def __init__(self):
        self.attribute = "value"
    
    def method(self):
        pass

obj = MyClass()
print(dir(obj))     # Shows all attributes and methods
```

## 50. What are closures and how are they different from decorators?

### Closures:
A closure is created when a nested function references variables from its enclosing scope.

```python
def outer_function(x):
    # Enclosing scope variable
    def inner_function(y):
        # Accesses variable from enclosing scope
        return x + y
    return inner_function

# Create closure
add_10 = outer_function(10)
print(add_10(5))  # Output: 15

# The closure remembers 'x' even after outer_function returns
print(add_10.__closure__)  # Shows closure variables
```

### Decorators:
Functions that modify or extend other functions without changing their code.

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def greet(name):
    return f"Hello, {name}!"

# Equivalent to: greet = my_decorator(greet)
```

### Key Differences:
- **Closures**: Capture and remember enclosing scope variables
- **Decorators**: Modify function behavior using closures
- **Purpose**: Closures for data encapsulation, decorators for function enhancement

## 51. What are Python descriptors and how do they work under the hood?

Descriptors are objects that define how attribute access is handled through special methods.

### Descriptor Protocol:
```python
class Descriptor:
    def __get__(self, obj, objtype=None):
        print("Getting value")
        return self.value
    
    def __set__(self, obj, value):
        print(f"Setting value to {value}")
        self.value = value
    
    def __delete__(self, obj):
        print("Deleting value")
        del self.value

class MyClass:
    attr = Descriptor()

obj = MyClass()
obj.attr = 42    # Calls __set__
print(obj.attr)  # Calls __get__
del obj.attr     # Calls __delete__
```

### Real-world Example - Property Descriptor:
```python
class Temperature:
    def __init__(self):
        self._celsius = 0
    
    def __get__(self, obj, objtype=None):
        return self._celsius
    
    def __set__(self, obj, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value

class Thermometer:
    celsius = Temperature()

thermo = Thermometer()
thermo.celsius = 25  # Valid
# thermo.celsius = -300  # Raises ValueError
```

## 52. Explain duck typing with a real-world example.

Duck typing follows the principle: "If it walks like a duck and quacks like a duck, then it's a duck."

Python doesn't check the type of an object, but rather whether it has the required methods/attributes.

```python
# Duck typing example
class Duck:
    def fly(self):
        return "Duck flying"
    
    def quack(self):
        return "Duck quacking"

class Airplane:
    def fly(self):
        return "Airplane flying"

class Dog:
    def bark(self):
        return "Dog barking"

def make_it_fly(flying_object):
    # Duck typing - we don't check the type
    # We just try to call the fly method
    return flying_object.fly()

# These work because they have fly() method
duck = Duck()
plane = Airplane()

print(make_it_fly(duck))    # "Duck flying"
print(make_it_fly(plane))   # "Airplane flying"

# This would raise AttributeError
dog = Dog()
# make_it_fly(dog)  # AttributeError: 'Dog' object has no attribute 'fly'
```

### Real-world File-like Objects:
```python
import io

def process_file(file_obj):
    # Works with any file-like object
    return file_obj.read()

# Works with actual files
with open('data.txt', 'r') as f:
    content = process_file(f)

# Works with StringIO (duck typing)
string_file = io.StringIO("Hello, World!")
content = process_file(string_file)
```

## 53. What is the difference between composition and inheritance in OOP? Which one do you prefer and why?

### Inheritance (IS-A relationship):
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):  # Dog IS-A Animal
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):  # Cat IS-A Animal
    def speak(self):
        return f"{self.name} says Meow!"
```

### Composition (HAS-A relationship):
```python
class Engine:
    def start(self):
        return "Engine starting"
    
    def stop(self):
        return "Engine stopping"

class Car:  # Car HAS-A Engine
    def __init__(self):
        self.engine = Engine()  # Composition
    
    def start_car(self):
        return self.engine.start()

# More flexible composition
class ElectricMotor:
    def start(self):
        return "Electric motor starting silently"

class ElectricCar:
    def __init__(self):
        self.motor = ElectricMotor()  # Different composition
    
    def start_car(self):
        return self.motor.start()
```

### Comparison:

**Inheritance Pros:**
- Code reuse
- Polymorphism support
- Clear hierarchical relationships

**Inheritance Cons:**
- Tight coupling
- Fragile base class problem
- Diamond problem in multiple inheritance

**Composition Pros:**
- Flexible and modular
- Loose coupling
- Easy to test and maintain
- Runtime behavior changes

**Composition Cons:**
- More code to write
- Delegation overhead

**Preference:** Composition is generally preferred because it provides better flexibility and maintainability. Follow "favor composition over inheritance" principle.

## 54. Compare threading, multiprocessing, and asyncio in Python. When do you use each?

### Threading:
```python
import threading
import time

def worker(name):
    for i in range(3):
        print(f"Worker {name}: {i}")
        time.sleep(1)

# Create threads
threads = []
for i in range(2):
    t = threading.Thread(target=worker, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

### Multiprocessing:
```python
import multiprocessing
import time

def cpu_bound_task(n):
    # CPU-intensive task
    total = 0
    for i in range(n):
        total += i * i
    return total

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(cpu_bound_task, [100000, 200000, 300000])
    print(results)
```

### Asyncio:
```python
import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = ['http://example.com', 'http://google.com']
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    return results

# Run async function
# asyncio.run(main())
```

### When to use each:

**Threading:**
- I/O bound tasks (file operations, network requests)
- Limited by GIL for CPU-bound tasks
- Shared memory space
- Good for concurrent I/O operations

**Multiprocessing:**
- CPU-bound tasks (calculations, data processing)
- Bypasses GIL limitation
- Separate memory spaces
- Good for parallel computing

**Asyncio:**
- I/O bound tasks with many concurrent operations
- Single-threaded event loop
- Excellent for web servers, APIs
- Best for high-concurrency I/O

## 55. How does async/await work in Python?

Async/await enables asynchronous programming using coroutines.

### Basic Concepts:
```python
import asyncio

# Coroutine function
async def say_hello():
    print("Hello")
    await asyncio.sleep(1)  # Non-blocking sleep
    print("World")

# Running coroutines
async def main():
    # Sequential execution
    await say_hello()
    await say_hello()
    
    # Concurrent execution
    await asyncio.gather(
        say_hello(),
        say_hello()
    )

# Run the event loop
asyncio.run(main())
```

### Event Loop and Coroutines:
```python
async def fetch_data(url, delay):
    print(f"Fetching {url}")
    await asyncio.sleep(delay)  # Simulate network delay
    return f"Data from {url}"

async def main():
    # Create tasks for concurrent execution
    task1 = asyncio.create_task(fetch_data("api1", 2))
    task2 = asyncio.create_task(fetch_data("api2", 1))
    
    # Wait for both tasks
    result1, result2 = await asyncio.gather(task1, task2)
    print(result1, result2)
```

### Error Handling:
```python
async def risky_operation():
    await asyncio.sleep(1)
    raise ValueError("Something went wrong")

async def main():
    try:
        await risky_operation()
    except ValueError as e:
        print(f"Caught error: {e}")
```

## 56. Can you explain how the concurrent.futures module works?

The `concurrent.futures` module provides a high-level interface for asynchronously executing callables.

### ThreadPoolExecutor:
```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import requests

def fetch_url(url):
    response = requests.get(url)
    return f"{url}: {response.status_code}"

urls = [
    'http://httpbin.org/delay/1',
    'http://httpbin.org/delay/2',
    'http://httpbin.org/delay/3'
]

# Using ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit tasks
    future_to_url = {executor.submit(fetch_url, url): url for url in urls}
    
    # Process completed tasks
    for future in as_completed(future_to_url):
        url = future_to_url[future]
        try:
            result = future.result()
            print(result)
        except Exception as exc:
            print(f'{url} generated an exception: {exc}')
```

### ProcessPoolExecutor:
```python
from concurrent.futures import ProcessPoolExecutor
import math

def cpu_bound_task(n):
    return sum(i * i for i in range(n))

numbers = [100000, 200000, 300000, 400000]

with ProcessPoolExecutor(max_workers=4) as executor:
    # Map function to inputs
    results = list(executor.map(cpu_bound_task, numbers))
    print(results)
```

### Future Objects:
```python
from concurrent.futures import ThreadPoolExecutor
import time

def slow_function(seconds):
    time.sleep(seconds)
    return f"Slept for {seconds} seconds"

with ThreadPoolExecutor() as executor:
    # Submit returns a Future object
    future = executor.submit(slow_function, 2)
    
    # Check if done
    print(f"Done: {future.done()}")
    
    # Get result (blocks until complete)
    result = future.result(timeout=5)
    print(result)
```

## 57. How would you implement a producer-consumer pattern using Python's queue module?

```python
import threading
import queue
import time
import random

def producer(q, producer_id):
    """Produces items and puts them in the queue"""
    for i in range(5):
        item = f"Item-{producer_id}-{i}"
        q.put(item)
        print(f"Producer {producer_id} produced: {item}")
        time.sleep(random.uniform(0.1, 0.5))
    
    # Signal completion
    q.put(None)
    print(f"Producer {producer_id} finished")

def consumer(q, consumer_id):
    """Consumes items from the queue"""
    while True:
        try:
            item = q.get(timeout=1)
            if item is None:
                # Poison pill - shutdown signal
                q.task_done()
                break
            
            print(f"Consumer {consumer_id} consumed: {item}")
            time.sleep(random.uniform(0.1, 0.3))
            q.task_done()
            
        except queue.Empty:
            print(f"Consumer {consumer_id} timeout")
            break

# Create queue
q = queue.Queue(maxsize=10)

# Create and start threads
threads = []

# Start producers
for i in range(2):
    t = threading.Thread(target=producer, args=(q, i))
    threads.append(t)
    t.start()

# Start consumers
for i in range(3):
    t = threading.Thread(target=consumer, args=(q, i))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("All tasks completed")
```

### Priority Queue Example:
```python
import queue
import threading

def priority_producer(pq):
    items = [
        (1, "High priority task"),
        (3, "Low priority task"),
        (2, "Medium priority task"),
        (1, "Another high priority task")
    ]
    
    for priority, task in items:
        pq.put((priority, task))
        print(f"Added: {task} (priority: {priority})")

def priority_consumer(pq):
    while True:
        try:
            priority, task = pq.get(timeout=2)
            print(f"Processing: {task} (priority: {priority})")
            pq.task_done()
        except queue.Empty:
            break

# Priority queue (lower number = higher priority)
pq = queue.PriorityQueue()

producer_thread = threading.Thread(target=priority_producer, args=(pq,))
consumer_thread = threading.Thread(target=priority_consumer, args=(pq,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
```

## 58. How do you create and distribute your own Python package?

### Project Structure:
```
my_package/
├── setup.py
├── pyproject.toml
├── README.md
├── LICENSE
├── requirements.txt
├── my_package/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
└── tests/
    ├── __init__.py
    └── test_module1.py
```

### Using setuptools (setup.py):
```python
# setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="my-awesome-package",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A short description of your package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my-package",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.25.0",
        "click>=7.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black",
            "flake8",
        ],
    },
    entry_points={
        "console_scripts": [
            "my-cli-tool=my_package.cli:main",
        ],
    },
)
```

### Using Poetry (pyproject.toml):
```toml
[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry]
name = "my-awesome-package"
version = "0.1.0"
description = "A short description of your package"
authors = ["Your Name <your.email@example.com>"]
readme = "README.md"
homepage = "https://github.com/yourusername/my-package"
repository = "https://github.com/yourusername/my-package"
keywords = ["python", "package"]

[tool.poetry.dependencies]
python = "^3.8"
requests = "^2.25.0"
click = "^7.0"

[tool.poetry.group.dev.dependencies]
pytest = "^6.0"
black = "^22.0"
flake8 = "^4.0"

[tool.poetry.scripts]
my-cli-tool = "my_package.cli:main"
```

### Building and Distribution:
```bash
# Using setuptools
python setup.py sdist bdist_wheel
pip install twine
twine upload dist/*

# Using poetry
poetry build
poetry publish
```

## 59. What's the difference between requirements.txt, Pipfile, and pyproject.toml?

### requirements.txt:
```txt
# requirements.txt
requests==2.28.0
flask>=2.0.0,<3.0.0
numpy
pytest>=6.0.0  # Dev dependency (not separated)
```

**Characteristics:**
- Simple text file
- No dependency resolution
- No dev/prod separation
- No lock file concept
- Compatible with pip

### Pipfile (Pipenv):
```toml
# Pipfile
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
requests = "~=2.28.0"
flask = ">=2.0.0,<3.0.0"
numpy = "*"

[dev-packages]
pytest = ">=6.0.0"
black = "*"
flake8 = "*"

[requires]
python_version = "3.9"
```

**Features:**
- TOML format
- Separates dev and production dependencies
- Automatic Pipfile.lock generation
- Dependency resolution
- Virtual environment management

### pyproject.toml (Poetry/Modern Python):
```toml
# pyproject.toml
[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry]
name = "my-project"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.9"
requests = "^2.28.0"
flask = "^2.0.0"

[tool.poetry.group.dev.dependencies]
pytest = "^6.0.0"
black = "^22.0"
flake8 = "^4.0"

[tool.black]
line-length = 88
target-version = ['py39']

[tool.pytest.ini_options]
testpaths = ["tests"]
```

**Advantages:**
- Standard Python packaging format (PEP 518)
- Tool configuration in one file
- Advanced dependency resolution
- Build system specification
- Lock file support (poetry.lock)

## 60. What are the differences between pickle, json, and marshal?

### JSON:
```python
import json

# JSON - Human readable, cross-language
data = {
    'name': 'John',
    'age': 30,
    'scores': [85, 90, 78]
}

# Serialize
json_string = json.dumps(data)
print(json_string)  # {"name": "John", "age": 30, "scores": [85, 90, 78]}

# Deserialize
parsed_data = json.loads(json_string)

# Limitations: Only basic Python types
# Can't serialize: functions, classes, complex objects
```

### Pickle:
```python
import pickle

# Pickle - Python-specific, can serialize almost anything
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)
function_obj = lambda x: x * 2

# Serialize complex objects
with open('data.pickle', 'wb') as f:
    pickle.dump([person, function_obj, {1, 2, 3}], f)

# Deserialize
with open('data.pickle', 'rb') as f:
    loaded_data = pickle.load(f)

# Security warning: Never unpickle untrusted data!
```

### Marshal:
```python
import marshal

# Marshal - Internal Python use, fast but limited
data = [1, 2, 3, "hello", (4, 5)]

# Serialize
marshaled = marshal.dumps(data)

# Deserialize
unmarshaled = marshal.loads(marshaled)

# Limitations: Only code objects and basic types
# Used internally by Python for .pyc files
```

### Comparison Table:

| Feature | JSON | Pickle | Marshal |
|---------|------|--------|---------|
| **Human Readable** | Yes | No | No |
| **Cross-language** | Yes | No | No |
| **Security** | Safe | Unsafe | Unsafe |
| **Python Objects** | Limited | All | Limited |
| **Performance** | Moderate | Good | Fast |
| **Version Compatibility** | Good | Limited | Python version specific |
| **Use Case** | APIs, Config | Python objects | Internal Python |

## 61. When would you use memory-mapped files in Python?

Memory-mapped files allow you to treat a file as if it were in memory, useful for large files and shared memory.

### Basic Usage:
```python
import mmap
import os

# Create a large file
with open('large_file.txt', 'w') as f:
    f.write('A' * 1000000)  # 1MB of 'A's

# Memory map the file
with open('large_file.txt', 'r+b') as f:
    # Map the entire file
    with mmap.mmap(f.fileno(), 0) as mm:
        # Read like a string
        print(mm[0:10])  # First 10 bytes
        
        # Modify in place
        mm[0:5] = b'HELLO'
        
        # Search
        index = mm.find(b'HELLO')
        print(f"Found at index: {index}")
        
        # Get size
        print(f"File size: {len(mm)}")
```

### Large File Processing:
```python
import mmap
import re

def process_large_log_file(filename):
    """Process a large log file efficiently"""
    with open(filename, 'rb') as f:
        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
            # Find all IP addresses
            ip_pattern = rb'\d+\.\d+\.\d+\.\d+'
            ip_addresses = re.findall(ip_pattern, mm)
            
            # Count occurrences
            ip_counts = {}
            for ip in ip_addresses:
                ip_str = ip.decode('utf-8')
                ip_counts[ip_str] = ip_counts.get(ip_str, 0) + 1
            
            return ip_counts

# Usage for large files (GBs) without loading into memory
# ip_stats = process_large_log_file('access.log')
```

### Shared Memory Between Processes:
```python
import mmap
import multiprocessing
import time

def worker(shared_array, start_idx, end_idx):
    """Worker process modifies shared memory"""
    for i in range(start_idx, end_idx):
        shared_array[i] = i * i

def main():
    # Create shared memory
    size = 1000000
    with mmap.mmap(-1, size) as shared_memory:
        # Convert to array-like object
        import array
        shared_array = array.array('i', shared_memory)
        
        # Initialize
        for i in range(len(shared_array)):
            shared_array[i] = 0
        
        # Create processes to work on different parts
        processes = []
        chunk_size = len(shared_array) // 4
        
        for i in range(4):
            start = i * chunk_size
            end = start + chunk_size if i < 3 else len(shared_array)
            p = multiprocessing.Process(
                target=worker, 
                args=(shared_array, start, end)
            )
            processes.append(p)
            p.start()
        
        # Wait for completion
        for p in processes:
            p.join()
        
        # Verify results
        print(f"First 10 values: {shared_array[:10]}")

if __name__ == '__main__':
    main()
```

### Use Cases:
- **Large file processing**: Reading/writing large files without loading into RAM
- **Database files**: SQLite uses mmap for performance
- **Shared memory**: Inter-process communication
- **Random access**: Efficient seeking in large files
- **Performance**: Faster than traditional file I/O for certain patterns

## 62. How do you structure unit tests in Python using unittest or pytest?

### Project Structure:
```
project/
├── src/
│   ├── __init__.py
│   ├── calculator.py
│   ├── database.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # pytest fixtures
│   ├── test_calculator.py
│   ├── test_database.py
│   ├── test_utils.py
│   └── integration/
│       ├── __init__.py
│       └── test_integration.py
├── requirements.txt
└── pytest.ini              # pytest configuration
```

### Using unittest:
```python
# src/calculator.py
class Calculator:
    def add(self, a, b):
        return a + b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# tests/test_calculator.py (unittest)
import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
    
    def tearDown(self):
        """Clean up after each test method."""
        pass
    
    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
    
    def test_add_negative_numbers(self):
        """Test addition of negative numbers."""
        result = self.calc.add(-2, -3)
        self.assertEqual(result, -5)
    
    def test_divide_valid(self):
        """Test valid division."""
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5.0)
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")
    
    def test_divide_by_zero_message(self):
        """Test the error message for division by zero."""
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            self.calc.divide(5, 0)

class TestCalculatorAdvanced(unittest.TestCase):
    """Advanced test cases with more complex scenarios."""
    
    @classmethod
    def setUpClass(cls):
        """Set up class-level fixtures."""
        cls.calc = Calculator()
    
    def test_multiple_operations(self):
        """Test multiple operations in sequence."""
        result1 = self.calc.add(1, 2)
        result2 = self.calc.divide(result1, 3)
        self.assertAlmostEqual(result2, 1.0, places=7)
    
    @unittest.skip("Skipping this test for demonstration")
    def test_skipped(self):
        """This test will be skipped."""
        pass
    
    @unittest.skipIf(sys.version_info < (3, 8), "Requires Python 3.8+")
    def test_conditional_skip(self):
        """This test runs only on Python 3.8+."""
        self.assertTrue(True)

if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
```

### Using pytest:
```python
# tests/test_calculator_pytest.py
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import Calculator

class TestCalculator:
    """Test class for Calculator using pytest."""
    
    def setup_method(self):
        """Set up method called before each test."""
        self.calc = Calculator()
    
    def teardown_method(self):
        """Clean up method called after each test."""
        pass
    
    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        result = self.calc.add(2, 3)
        assert result == 5
    
    def test_add_negative_numbers(self):
        """Test addition of negative numbers."""
        result = self.calc.add(-2, -3)
        assert result == -5
    
    def test_divide_valid(self):
        """Test valid division."""
        result = self.calc.divide(10, 2)
        assert result == 5.0
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)
    
    @pytest.mark.parametrize("a,b,expected", [
        (1, 2, 3),
        (0, 5, 5),
        (-1, 1, 0),
        (10, -5, 5),
    ])
    def test_add_parametrized(self, a, b, expected):
        """Test addition with multiple parameter sets."""
        result = self.calc.add(a, b)
        assert result == expected
    
    @pytest.mark.slow
    def test_slow_operation(self):
        """Test marked as slow for selective running."""
        import time
        time.sleep(0.1)  # Simulate slow operation
        assert self.calc.add(1, 1) == 2

# conftest.py - pytest fixtures
import pytest

@pytest.fixture
def calculator():
    """Fixture providing a Calculator instance."""
    return Calculator()

@pytest.fixture
def sample_data():
    """Fixture providing sample test data."""
    return {
        'numbers': [1, 2, 3, 4, 5],
        'operations': ['add', 'divide'],
        'expected_results': [15, 0.2]
    }

@pytest.fixture(scope="session")
def database_connection():
    """Session-scoped fixture for database connection."""
    # Setup - create connection
    connection = "mock_db_connection"
    yield connection
    # Teardown - close connection
    print("Closing database connection")

# Using fixtures in tests
def test_calculator_with_fixture(calculator):
    """Test using calculator fixture."""
    result = calculator.add(3, 4)
    assert result == 7

def test_with_sample_data(calculator, sample_data):
    """Test using multiple fixtures."""
    numbers = sample_data['numbers']
    total = sum(numbers)
    assert calculator.add(total, 0) == 15
```

### Advanced Test Organization:
```python
# tests/conftest.py - Advanced fixtures
import pytest
import tempfile
import os

@pytest.fixture
def temp_file():
    """Create a temporary file for testing."""
    fd, path = tempfile.mkstemp()
    try:
        yield path
    finally:
        os.close(fd)
        os.unlink(path)

@pytest.fixture
def mock_external_service(monkeypatch):
    """Mock external service calls."""
    def mock_api_call(*args, **kwargs):
        return {"status": "success", "data": "mocked"}
    
    monkeypatch.setattr("src.utils.external_api_call", mock_api_call)
    return mock_api_call

# pytest.ini - Configuration
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    -v
    --strict-markers
    --disable-warnings
markers =
    slow: marks tests as slow
    integration: marks tests as integration tests
    unit: marks tests as unit tests
```

### Running Tests:
```bash
# unittest
python -m unittest discover tests/
python -m unittest tests.test_calculator.TestCalculator.test_add

# pytest
pytest                          # Run all tests
pytest tests/test_calculator.py # Run specific file
pytest -k "add"                 # Run tests matching pattern
pytest -m "not slow"            # Skip slow tests
pytest --cov=src                # Run with coverage
pytest -x                       # Stop on first failure
pytest -v                       # Verbose output
```

## 63. How would you mock external APIs or database calls in your tests?

### Using unittest.mock:
```python
# src/weather_service.py
import requests

class WeatherService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.weather.com/v1"
    
    def get_temperature(self, city):
        """Get temperature for a city."""
        response = requests.get(
            f"{self.base_url}/current",
            params={'city': city, 'key': self.api_key}
        )
        
        if response.status_code != 200:
            raise Exception(f"API Error: {response.status_code}")
        
        data = response.json()
        return data['temperature']

# tests/test_weather_service.py
import unittest
from unittest.mock import Mock, patch, MagicMock
import json

from src.weather_service import WeatherService

class TestWeatherService(unittest.TestCase):
    def setUp(self):
        self.service = WeatherService("fake_api_key")
    
    @patch('src.weather_service.requests.get')
    def test_get_temperature_success(self, mock_get):
        """Test successful API call."""
        # Configure mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'temperature': 25.5}
        mock_get.return_value = mock_response
        
        # Test the method
        temperature = self.service.get_temperature("London")
        
        # Assertions
        self.assertEqual(temperature, 25.5)
        mock_get.assert_called_once_with(
            "https://api.weather.com/v1/current",
            params={'city': 'London', 'key': 'fake_api_key'}
        )
    
    @patch('src.weather_service.requests.get')
    def test_get_temperature_api_error(self, mock_get):
        """Test API error handling."""
        # Configure mock to return error
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        # Test that exception is raised
        with self.assertRaises(Exception) as context:
            self.service.get_temperature("InvalidCity")
        
        self.assertIn("API Error: 404", str(context.exception))

# Using context manager for multiple mocks
class TestWeatherServiceAdvanced(unittest.TestCase):
    def setUp(self):
        self.service = WeatherService("test_key")
    
    def test_multiple_cities(self):
        """Test getting temperature for multiple cities."""
        with patch('src.weather_service.requests.get') as mock_get:
            # Configure different responses for different calls
            mock_responses = [
                Mock(status_code=200, json=lambda: {'temperature': 20.0}),
                Mock(status_code=200, json=lambda: {'temperature': 15.5}),
                Mock(status_code=200, json=lambda: {'temperature': 30.2})
            ]
            mock_get.side_effect = mock_responses
            
            cities = ["London", "Paris", "Tokyo"]
            temperatures = []
            
            for city in cities:
                temp = self.service.get_temperature(city)
                temperatures.append(temp)
            
            expected = [20.0, 15.5, 30.2]
            self.assertEqual(temperatures, expected)
            self.assertEqual(mock_get.call_count, 3)
```

### Database Mocking:
```python
# src/user_repository.py
import sqlite3

class UserRepository:
    def __init__(self, db_path):
        self.db_path = db_path
    
    def get_user(self, user_id):
        """Get user by ID."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, name, email FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return {'id': row[0], 'name': row[1], 'email': row[2]}
        return None
    
    def create_user(self, name, email):
        """Create a new user."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (name, email)
        )
        user_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return user_id

# tests/test_user_repository.py
import unittest
from unittest.mock import Mock, patch, MagicMock
import sqlite3

from src.user_repository import UserRepository

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.repo = UserRepository(":memory:")  # Use in-memory database
    
    @patch('src.user_repository.sqlite3.connect')
    def test_get_user_found(self, mock_connect):
        """Test getting existing user."""
        # Setup mock database connection
        mock_conn = Mock()
        mock_cursor = Mock()
        
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = (1, "John Doe", "john@example.com")
        
        # Test the method
        user = self.repo.get_user(1)
        
        # Verify results
        expected = {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'}
        self.assertEqual(user, expected)
        
        # Verify database interactions
        mock_connect.assert_called_once_with(":memory:")
        mock_cursor.execute.assert_called_once_with(
            "SELECT id, name, email FROM users WHERE id = ?", (1,)
        )
        mock_conn.close.assert_called_once()
    
    @patch('src.user_repository.sqlite3.connect')
    def test_get_user_not_found(self, mock_connect):
        """Test getting non-existent user."""
        mock_conn = Mock()
        mock_cursor = Mock()
        
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = None
        
        user = self.repo.get_user(999)
        
        self.assertIsNone(user)
    
    @patch('src.user_repository.sqlite3.connect')
    def test_create_user(self, mock_connect):
        """Test creating a new user."""
        mock_conn = Mock()
        mock_cursor = Mock()
        
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.lastrowid = 42
        
        user_id = self.repo.create_user("Jane Doe", "jane@example.com")
        
        self.assertEqual(user_id, 42)
        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            ("Jane Doe", "jane@example.com")
        )
        mock_conn.commit.assert_called_once()
```

### Using pytest with pytest-mock:
```python
# tests/test_weather_service_pytest.py
import pytest
import requests
from src.weather_service import WeatherService

class TestWeatherServicePytest:
    def setup_method(self):
        self.service = WeatherService("test_key")
    
    def test_get_temperature_success(self, mocker):
        """Test successful API call using pytest-mock."""
        # Mock the requests.get call
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'temperature': 22.5}
        
        mock_get = mocker.patch('src.weather_service.requests.get')
        mock_get.return_value = mock_response
        
        temperature = self.service.get_temperature("Berlin")
        
        assert temperature == 22.5
        mock_get.assert_called_once_with(
            "https://api.weather.com/v1/current",
            params={'city': 'Berlin', 'key': 'test_key'}
        )
    
    def test_get_temperature_with_fixture(self, mocker, mock_weather_api):
        """Test using a custom fixture."""
        temperature = self.service.get_temperature("Madrid")
        assert temperature == 18.0

# conftest.py
import pytest

@pytest.fixture
def mock_weather_api(mocker):
    """Fixture to mock weather API calls."""
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'temperature': 18.0}
    
    mock_get = mocker.patch('src.weather_service.requests.get')
    mock_get.return_value = mock_response
    
    return mock_get
```

### Advanced Mocking Patterns:
```python
# tests/test_advanced_mocking.py
import unittest
from unittest.mock import Mock, patch, PropertyMock, call
import datetime

class TestAdvancedMocking(unittest.TestCase):
    
    def test_mock_property(self):
        """Test mocking properties."""
        with patch('datetime.datetime') as mock_datetime:
            # Mock datetime.now() property
            mock_datetime.now.return_value = datetime.datetime(2023, 1, 1, 12, 0, 0)
            mock_datetime.side_effect = lambda *args, **kw: datetime.datetime(*args, **kw)
            
            now = datetime.datetime.now()
            self.assertEqual(now.year, 2023)
    
    def test_mock_multiple_calls(self):
        """Test mocking multiple calls with different returns."""
        mock_func = Mock()
        mock_func.side_effect = [1, 2, 3, Exception("Fourth call fails")]
        
        self.assertEqual(mock_func(), 1)
        self.assertEqual(mock_func(), 2)
        self.assertEqual(mock_func(), 3)
        
        with self.assertRaises(Exception):
            mock_func()
    
    def test_mock_with_spec(self):
        """Test mocking with specification."""
        from src.weather_service import WeatherService
        
        # Mock only allows methods that exist on WeatherService
        mock_service = Mock(spec=WeatherService)
        mock_service.get_temperature.return_value = 25.0
        
        # This works
        temp = mock_service.get_temperature("London")
        self.assertEqual(temp, 25.0)
        
        # This would raise AttributeError
        # mock_service.non_existent_method()
    
    @patch.multiple('src.weather_service', requests=Mock())
    def test_patch_multiple(self):
        """Test patching multiple objects."""
        # Multiple patches applied at once
        pass
    
    def test_mock_call_tracking(self):
        """Test tracking mock calls."""
        mock_obj = Mock()
        
        # Make some calls
        mock_obj.method1("arg1", kwarg1="value1")
        mock_obj.method2("arg2")
        mock_obj.method1("arg3")
        
        # Check call history
        expected_calls = [
            call.method1("arg1", kwarg1="value1"),
            call.method2("arg2"),
            call.method1("arg3")
        ]
        
        self.assertEqual(mock_obj.mock_calls, expected_calls)
        self.assertEqual(mock_obj.method1.call_count, 2)
```

## 64. What's the difference between assert, assertEqual, and assertRaises in testing?

### Basic assert vs unittest assertions:
```python
import unittest

class TestAssertions(unittest.TestCase):
    
    def test_basic_assert(self):
        """Basic Python assert statement."""
        x = 5
        y = 5
        
        # Basic assert - can be disabled with -O flag
        assert x == y, "x should equal y"
        assert x > 0, "x should be positive"
        
        # Problem: assert can be disabled in production
        # Not recommended for unit tests
    
    def test_assertEqual(self):
        """unittest assertEqual method."""
        x = 5
        y = 5
        
        # unittest assertion - never disabled
        self.assertEqual(x, y)
        
        # Provides better error messages
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        self.assertEqual(list1, list2)
        
        # Better diff output for complex objects
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'a': 1, 'b': 2}
        self.assertEqual(dict1, dict2)
    
    def test_other_assert_methods(self):
        """Other useful unittest assertion methods."""
        # Numeric comparisons
        self.assertGreater(10, 5)
        self.assertLess(3, 7)
        self.assertGreaterEqual(5, 5)
        self.assertLessEqual(3, 5)
        
        # Approximate equality for floats
        self.assertAlmostEqual(3.14159, 3.14, places=2)
        self.assertAlmostEqual(1.0, 1.0001, delta=0.001)
        
        # Boolean checks
        self.assertTrue(True)
        self.assertFalse(False)
        
        # None checks
        self.assertIsNone(None)
        self.assertIsNotNone("not none")
        
        # Identity checks
        x = [1, 2, 3]
        y = x
        self.assertIs(x, y)
        self.assertIsNot(x, [1, 2, 3])
        
        # Membership
        self.assertIn('a', 'abc')
        self.assertNotIn('x', 'abc')
        
        # Type checks
        self.assertIsInstance(5, int)
        self.assertNotIsInstance("5", int)
    
    def test_assertRaises(self):
        """Testing exception handling."""
        
        def divide_by_zero():
            return 10 / 0
        
        def custom_error():
            raise ValueError("Custom error message")
        
        # Test that specific exception is raised
        with self.assertRaises(ZeroDivisionError):
            divide_by_zero()
        
        # Test exception message
        with self.assertRaises(ValueError) as context:
            custom_error()
        
        self.assertEqual(str(context.exception), "Custom error message")
        
        # Test with regex pattern
        self.assertRaisesRegex(
            ValueError, 
            r"Custom.*message",
            custom_error
        )
        
        # Alternative syntax
        self.assertRaises(ValueError, custom_error)
    
    def test_collection_assertions(self):
        """Assertions for collections."""
        list1 = [1, 2, 3, 4]
        list2 = [4, 3, 2, 1]
        
        # Count items
        self.assertCountEqual(list1, list2)  # Same items, different order
        
        # Sequence comparison
        self.assertSequenceEqual([1, 2, 3], [1, 2, 3])
        self.assertListEqual([1, 2], [1, 2])
        self.assertSetEqual({1, 2, 3}, {3, 2, 1})
        self.assertDictEqual({'a': 1}, {'a': 1})
        
        # Multiline string comparison
        text1 = "line1\nline2\nline3"
        text2 = "line1\nline2\nline3"
        self.assertMultiLineEqual(text1, text2)

# Comparison with pytest assertions
class TestPytestAssertions:
    """pytest uses plain assert with introspection."""
    
    def test_pytest_assertions(self):
        """pytest provides detailed failure information."""
        x = 5
        y = 5
        
        # Simple and readable
        assert x == y
        assert x > 0
        
        # Works with complex objects
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        assert list1 == list2
        
        # Exception testing
        with pytest.raises(ValueError, match="Custom error"):
            raise ValueError("Custom error message")
        
        # Approximate equality
        import math
        assert math.pi == pytest.approx(3.14, rel=0.01)

# Error message comparison
class TestErrorMessages(unittest.TestCase):
    
    def test_assert_vs_assertEqual_errors(self):
        """Compare error messages."""
        
        # Basic assert - minimal error info
        try:
            assert [1, 2, 3] == [1, 2, 4]
        except AssertionError as e:
            print(f"assert error: {e}")
        
        # assertEqual - detailed diff
        try:
            self.assertEqual([1, 2, 3], [1, 2, 4])
        except AssertionError as e:
            print(f"assertEqual error: {e}")
            # Output shows: Lists differ: [1, 2, 3] != [1, 2, 4]
            # First differing element 2: 3 != 4
    
    def test_custom_error_messages(self):
        """Adding custom error messages."""
        x = 10
        y = 20
        
        self.assertEqual(x, y, f"Expected {x} to equal {y}, but they differ")
        self.assertTrue(x > y, f"{x} should be greater than {y}")
        
        # With context information
        user_data = {'name': 'John', 'age': 25}
        self.assertIn('email', user_data, 
                      f"User data missing email field: {user_data}")
```

### Summary of Differences:

| Method | Purpose | Error Info | Can be Disabled |
|--------|---------|------------|----------------|
| `assert` | Basic assertion | Minimal | Yes (with -O) |
| `assertEqual` | Equality check | Detailed diff | No |
| `assertRaises` | Exception testing | Exception details | No |

**Best Practices:**
- Use unittest assertion methods in unittest tests
- Use plain assert in pytest tests
- Always provide meaningful error messages
- Choose specific assertion methods for better error reporting
- Use `assertRaises` for exception testing, not try/except blocks

## 65. How would you optimize a slow-running Python function?

### 1. Profiling First - Measure Before Optimizing:
```python
import cProfile
import pstats
import time
from functools import wraps

def slow_function():
    """Example slow function to optimize."""
    # Inefficient operations
    result = []
    for i in range(1000):
        temp = []
        for j in range(1000):
            temp.append(i * j)
        result.extend(temp)
    return result

# Profiling with cProfile
def profile_function():
    """Profile the slow function."""
    profiler = cProfile.Profile()
    profiler.enable()
    
    slow_function()
    
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats(10)  # Top 10 functions

# Timing decorator
def timer(func):
    """Decorator to time function execution."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def optimized_function():
    """Optimized version using list comprehension."""
    return [i * j for i in range(1000) for j in range(1000)]
```

### 2. Algorithmic Optimization:
```python
# Before: O(n²) complexity
def find_duplicates_slow(numbers):
    """Slow O(n²) approach."""
    duplicates = []
    for i, num1 in enumerate(numbers):
        for j, num2 in enumerate(numbers[i+1:], i+1):
            if num1 == num2 and num1 not in duplicates:
                duplicates.append(num1)
    return duplicates

# After: O(n) complexity
def find_duplicates_fast(numbers):
    """Fast O(n) approach using set."""
    seen = set()
    duplicates = set()
    
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)

# Using Counter for even better performance
from collections import Counter

def find_duplicates_counter(numbers):
    """Using Counter for cleaner code."""
    counts = Counter(numbers)
    return [num for num, count in counts.items() if count > 1]
```

### 3. Data Structure Optimization:
```python
# Before: Using lists for membership testing
def process_data_slow(data, valid_items):
    """Slow version using list for lookups."""
    valid_items_list = ['item1', 'item2', 'item3', '...', 'item1000']
    result = []
    
    for item in data:
        if item in valid_items_list:  # O(n) lookup
            result.append(item.upper())
    
    return result

# After: Using sets for O(1) lookups
def process_data_fast(data, valid_items):
    """Fast version using set for lookups."""
    valid_items_set = {'item1', 'item2', 'item3', '...', 'item1000'}
    result = []
    
    for item in data:
        if item in valid_items_set:  # O(1) lookup
            result.append(item.upper())
    
    return result

# Even better: Using list comprehension
def process_data_fastest(data, valid_items_set):
    """Fastest version with list comprehension."""
    return [item.upper() for item in data if item in valid_items_set]
```

### 4. Memory Optimization:
```python
# Before: Loading everything into memory
def process_large_file_slow(filename):
    """Memory-intensive approach."""
    with open(filename, 'r') as f:
        lines = f.readlines()  # Loads entire file
    
    result = []
    for line in lines:
        if line.strip():
            result.append(line.strip().upper())
    
    return result

# After: Using generators for memory efficiency
def process_large_file_fast(filename):
    """Memory-efficient generator approach."""
    with open(filename, 'r') as f:
        for line in f:  # Process line by line
            stripped = line.strip()
            if stripped:
                yield stripped.upper()

# Usage
def use_generator():
    # Memory-efficient processing
    for processed_line in process_large_file_fast('large_file.txt'):
        # Process one line at a time
        print(processed_line)
```

### 5. Caching and Memoization:
```python
from functools import lru_cache
import time

# Before: Expensive repeated calculations
def fibonacci_slow(n):
    """Slow recursive fibonacci."""
    if n < 2:
        return n
    return fibonacci_slow(n-1) + fibonacci_slow(n-2)

# After: Using memoization
@lru_cache(maxsize=None)
def fibonacci_fast(n):
    """Fast fibonacci with memoization."""
    if n < 2:
        return n
    return fibonacci_fast(n-1) + fibonacci_fast(n-2)

# Custom cache implementation
def memoize(func):
    """Custom memoization decorator."""
    cache = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(sorted(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

@memoize
def expensive_calculation(x, y):
    """Simulate expensive calculation."""
    time.sleep(1)  # Simulate delay
    return x ** y + y ** x
```

### 6. Using Built-in Functions and Libraries:
```python
import numpy as np
from collections import defaultdict, Counter
import bisect

# Before: Manual implementation
def calculate_stats_slow(numbers):
    """Slow manual statistics calculation."""
    total = 0
    for num in numbers:
        total += num
    mean = total / len(numbers)
    
    variance_sum = 0
    for num in numbers:
        variance_sum += (num - mean) ** 2
    variance = variance_sum / len(numbers)
    
    # Sorting for median
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n % 2 == 0:
        median = (sorted_nums[n//2-1] + sorted_nums[n//2]) / 2
    else:
        median = sorted_nums[n//2]
    
    return {'mean': mean, 'variance': variance, 'median': median}

# After: Using NumPy
def calculate_stats_fast(numbers):
    """Fast statistics using NumPy."""
    arr = np.array(numbers)
    return {
        'mean': np.mean(arr),
        'variance': np.var(arr),
        'median': np.median(arr)
    }

# Before: Manual grouping
def group_data_slow(items):
    """Slow manual grouping."""
    groups = {}
    for item in items:
        key = item['category']
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups

# After: Using defaultdict
def group_data_fast(items):
    """Fast grouping with defaultdict."""
    groups = defaultdict(list)
    for item in items:
        groups[item['category']].append(item)
    return dict(groups)
```

### 7. Parallel Processing:
```python
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import threading

# CPU-bound task optimization
def cpu_intensive_task(n):
    """Simulate CPU-intensive work."""
    return sum(i * i for i in range(n))

# Before: Sequential processing
def process_sequential(numbers):
    """Sequential processing."""
    results = []
    for num in numbers:
        results.append(cpu_intensive_task(num))
    return results

# After: Parallel processing
def process_parallel(numbers):
    """Parallel processing using multiprocessing."""
    with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        results = list(executor.map(cpu_intensive_task, numbers))
    return results

# I/O-bound task optimization
import requests

def fetch_url(url):
    """Simulate I/O-bound work."""
    response = requests.get(url)
    return response.status_code

# Before: Sequential I/O
def fetch_sequential(urls):
    """Sequential URL fetching."""
    results = []
    for url in urls:
        results.append(fetch_url(url))
    return results

# After: Concurrent I/O
def fetch_concurrent(urls):
    """Concurrent URL fetching."""
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(fetch_url, urls))
    return results
```

### 8. String and Loop Optimization:
```python
# Before: Inefficient string concatenation
def build_string_slow(items):
    """Slow string building."""
    result = ""
    for item in items:
        result += str(item) + ", "  # Creates new string each time
    return result[:-2]  # Remove last comma

# After: Using join
def build_string_fast(items):
    """Fast string building."""
    return ", ".join(str(item) for item in items)

# Before: Multiple loops
def process_data_multiple_loops(data):
    """Multiple passes through data."""
    # First pass: filter
    filtered = []
    for item in data:
        if item > 0:
            filtered.append(item)
    
    # Second pass: transform
    transformed = []
    for item in filtered:
        transformed.append(item * 2)
    
    # Third pass: sum
    total = 0
    for item in transformed:
        total += item
    
    return total

# After: Single pass with generator
def process_data_single_pass(data):
    """Single pass through data."""
    return sum(item * 2 for item in data if item > 0)
```

### 9. Profile-Guided Optimization:
```python
import line_profiler
import memory_profiler

# Line-by-line profiling
@profile  # Use with kernprof -l -v script.py
def function_to_profile():
    """Function to profile line by line."""
    data = list(range(1000))
    result = []
    
    for i in data:  # This line will show time spent
        if i % 2 == 0:  # This line will show time spent
            result.append(i ** 2)  # This line will show time spent
    
    return result

# Memory profiling
@memory_profiler.profile
def memory_intensive_function():
    """Function to profile memory usage."""
    # This will show memory usage line by line
    big_list = [i for i in range(1000000)]
    another_list = [x * 2 for x in big_list]
    return sum(another_list)
```

### 10. Optimization Checklist:
```python
class OptimizationChecklist:
    """Systematic approach to optimization."""
    
    def __init__(self):
        self.checklist = [
            "1. Profile first - measure don't guess",
            "2. Optimize algorithms - reduce time complexity",
            "3. Use appropriate data structures",
            "4. Minimize memory usage",
            "5. Cache expensive operations",
            "6. Use built-in functions and libraries",
            "7. Consider parallel processing",
            "8. Optimize loops and string operations",
            "9. Use generators for large datasets",
            "10. Profile again to verify improvements"
        ]
    
    def print_checklist(self):
        for item in self.checklist:
            print(item)

# Example: Complete optimization workflow
def optimization_workflow():
    """Complete optimization example."""
    
    # 1. Original slow function
    def slow_function(data):
        result = []
        for i in range(len(data)):
            for j in range(len(data)):
                if data[i] + data[j] > 100:
                    result.append((i, j, data[i] + data[j]))
        return result
    
    # 2. Profiled and identified bottlenecks
    # 3. Optimized version
    def fast_function(data):
        # Use enumerate for cleaner indexing
        # Use list comprehension for better performance
        # Cache len(data) to avoid repeated calls
        return [
            (i, j, data[i] + data[j])
            for i, val_i in enumerate(data)
            for j, val_j in enumerate(data)
            if val_i + val_j > 100
        ]
    
    # 4. Even more optimized with NumPy for large datasets
    def numpy_function(data):
        import numpy as np
        arr = np.array(data)
        i_indices, j_indices = np.meshgrid(range(len(arr)), range(len(arr)), indexing='ij')
        sums = arr[i_indices] + arr[j_indices]
        mask = sums > 100
        return list(zip(i_indices[mask], j_indices[mask], sums[mask]))
```

## 66. What tools do you use for profiling and debugging performance bottlenecks?

### 1. Built-in Profiling Tools:

#### cProfile - Statistical Profiler:
```python
import cProfile
import pstats
import io

def example_function():
    """Function to profile."""
    # Some operations to profile
    data = []
    for i in range(1000):
        data.append(i ** 2)
    
    # More operations
    result = sum(data)
    return result

# Method 1: Direct profiling
def profile_with_cProfile():
    """Profile using cProfile directly."""
    profiler = cProfile.Profile()
    profiler.enable()
    
    example_function()
    
    profiler.disable()
    
    # Create stats object
    s = io.StringIO()
    ps = pstats.Stats(profiler, stream=s)
    ps.sort_stats('cumulative')
    ps.print_stats()
    
    print(s.getvalue())

# Method 2: Command line profiling
# python -m cProfile -s cumulative script.py

# Method 3: Context manager
class ProfileContext:
    """Context manager for profiling."""
    
    def __init__(self, sort_by='cumulative'):
        self.sort_by = sort_by
        self.profiler = cProfile.Profile()
    
    def __enter__(self):
        self.profiler.enable()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.profiler.disable()
        stats = pstats.Stats(self.profiler)
        stats.sort_stats(self.sort_by)
        stats.print_stats(10)  # Top 10

# Usage
with ProfileContext():
    example_function()
```

#### timeit - Micro-benchmarking:
```python
import timeit
from functools import partial

# Method 1: Using timeit.timeit()
def benchmark_operations():
    """Benchmark different operations."""
    
    # List comprehension vs loop
    list_comp_time = timeit.timeit(
        lambda: [i**2 for i in range(1000)],
        number=1000
    )
    
    loop_time = timeit.timeit(
        '''
result = []
for i in range(1000):
    result.append(i**2)
        ''',
        number=1000
    )
    
    print(f"List comprehension: {list_comp_time:.4f}s")
    print(f"Loop: {loop_time:.4f}s")
    
    # String operations
    join_time = timeit.timeit(
        lambda: ''.join(str(i) for i in range(100)),
        number=10000
    )
    
    concat_time = timeit.timeit(
        '''
result = ""
for i in range(100):
    result += str(i)
        ''',
        number=10000
    )
    
    print(f"Join: {join_time:.4f}s")
    print(f"Concatenation: {concat_time:.4f}s")

# Method 2: IPython magic commands
# %timeit function_call()
# %time function_call()
# %%timeit (for cell timing)

# Method 3: Custom timing decorator
import time
from functools import wraps

def benchmark(func):
    """Decorator to benchmark function calls."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        times = []
        for _ in range(100):  # Run 100 times
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            times.append(end - start)
        
        avg_time = sum(times) / len(times)
        min_time = min(times)
        max_time = max(times)
        
        print(f"{func.__name__}:")
        print(f"  Average: {avg_time:.6f}s")
        print(f"  Min: {min_time:.6f}s")
        print(f"  Max: {max_time:.6f}s")
        
        return result
    return wrapper

@benchmark
def test_function():
    return sum(i**2 for i in range(1000))
```

### 2. Line-by-Line Profiling:

#### line_profiler:
```python
# Install: pip install line_profiler

# Method 1: Using @profile decorator
@profile  # This decorator is injected by kernprof
def function_to_profile():
    """Function with line-by-line profiling."""
    data = []
    
    # Line 1: This will show timing
    for i in range(10000):
        data.append(i)
    
    # Line 2: This will show timing
    squared = [x**2 for x in data]
    
    # Line 3: This will show timing
    result = sum(squared)
    
    return result

# Run with: kernprof -l -v script.py

# Method 2: Programmatic usage
from line_profiler import LineProfiler

def programmatic_line_profiling():
    """Use line_profiler programmatically."""
    profiler = LineProfiler()
    profiler.add_function(function_to_profile)
    profiler.enable_by_count()
    
    function_to_profile()
    
    profiler.print_stats()
```

### 3. Memory Profiling:

#### memory_profiler:
```python
# Install: pip install memory-profiler psutil

from memory_profiler import profile, memory_usage
import time

@profile
def memory_intensive_function():
    """Function with memory profiling."""
    # Line 1: Memory usage will be shown
    big_list = [i for i in range(1000000)]
    
    # Line 2: Memory usage will be shown
    another_list = [x * 2 for x in big_list]
    
    # Line 3: Memory usage will be shown
    del big_list
    
    # Line 4: Memory usage will be shown
    result = sum(another_list)
    
    return result

# Run with: python -m memory_profiler script.py

# Method 2: Monitor memory usage over time
def monitor_memory():
    """Monitor memory usage of a function."""
    def slow_function():
        data = []
        for i in range(100000):
            data.append([i] * 100)
            time.sleep(0.001)
        return data
    
    mem_usage = memory_usage((slow_function, ()))
    print(f"Memory usage: {mem_usage}")
    print(f"Peak memory: {max(mem_usage):.2f} MB")

# Method 3: Memory usage context manager
from memory_profiler import memory_usage
import psutil
import os

class MemoryMonitor:
    """Context manager for memory monitoring."""
    
    def __enter__(self):
        self.process = psutil.Process(os.getpid())
        self.start_memory = self.process.memory_info().rss / 1024 / 1024
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_memory = self.process.memory_info().rss / 1024 / 1024
        print(f"Memory used: {self.end_memory - self.start_memory:.2f} MB")

# Usage
with MemoryMonitor():
    big_data = [i for i in range(1000000)]
```

### 4. Advanced Profiling Tools:

#### py-spy - Sampling Profiler:
```bash
# Install: pip install py-spy

# Profile a running Python process
py-spy record -o profile.svg --pid 12345

# Profile a Python script
py-spy record -o profile.svg -- python script.py

# Live profiling
py-spy live --pid 12345
```

#### Scalene - CPU and Memory Profiler:
```bash
# Install: pip install scalene

# Profile script with CPU and memory
scalene script.py

# Profile with specific options
scalene --cpu --memory --profile-interval 0.01 script.py
```

### 5. Custom Profiling Tools:
```python
import time
import functools
import sys
import tracemalloc
from collections import defaultdict

class PerformanceProfiler:
    """Custom performance profiler."""
    
    def __init__(self):
        self.call_times = defaultdict(list)
        self.call_counts = defaultdict(int)
        self.memory_usage = {}
    
    def profile_time(self, func):
        """Decorator to profile function execution time."""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            
            execution_time = end_time - start_time
            func_name = f"{func.__module__}.{func.__name__}"
            
            self.call_times[func_name].append(execution_time)
            self.call_counts[func_name] += 1
            
            return result
        return wrapper
    
    def profile_memory(self, func):
        """Decorator to profile memory usage."""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            tracemalloc.start()
            
            result = func(*args, **kwargs)
            
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            
            func_name = f"{func.__module__}.{func.__name__}"
            self.memory_usage[func_name] = {
                'current': current / 1024 / 1024,  # MB
                'peak': peak / 1024 / 1024  # MB
            }
            
            return result
        return wrapper
    
    def print_stats(self):
        """Print profiling statistics."""
        print("\n=== TIME PROFILING ===")
        for func_name, times in self.call_times.items():
            avg_time = sum(times) / len(times)
            total_time = sum(times)
            count = self.call_counts[func_name]
            
            print(f"{func_name}:")
            print(f"  Calls: {count}")
            print(f"  Total time: {total_time:.4f}s")
            print(f"  Average time: {avg_time:.4f}s")
            print(f"  Min time: {min(times):.4f}s")
            print(f"  Max time: {max(times):.4f}s")
        
        print("\n=== MEMORY PROFILING ===")
        for func_name, memory in self.memory_usage.items():
            print(f"{func_name}:")
            print(f"  Current: {memory['current']:.2f} MB")
            print(f"  Peak: {memory['peak']:.2f} MB")

# Usage example
profiler = PerformanceProfiler()

@profiler.profile_time
@profiler.profile_memory
def example_function():
    data = [i**2 for i in range(100000)]
    return sum(data)

# Run function multiple times
for _ in range(5):
    example_function()

# Print statistics
profiler.print_stats()
```

### 6. Debugging Performance Issues:
```python
import dis
import inspect

class PerformanceDebugger:
    """Tools for debugging performance issues."""
    
    @staticmethod
    def analyze_bytecode(func):
        """Analyze function bytecode."""
        print(f"Bytecode for {func.__name__}:")
        dis.dis(func)
    
    @staticmethod
    def compare_implementations(*funcs):
        """Compare multiple implementations."""
        import timeit
        
        results = {}
        for func in funcs:
            time_taken = timeit.timeit(func, number=1000)
            results[func.__name__] = time_taken
        
        # Sort by performance
        sorted_results = sorted(results.items(), key=lambda x: x[1])
        
        print("Performance comparison:")
        for func_name, time_taken in sorted_results:
            print(f"  {func_name}: {time_taken:.4f}s")
        
        return sorted_results
    
    @staticmethod
    def profile_hot_spots(func, *args, **kwargs):
        """Identify hot spots in function execution."""
        import cProfile
        import pstats
        
        profiler = cProfile.Profile()
        profiler.enable()
        
        result = func(*args, **kwargs)
        
        profiler.disable()
        
        # Get top 10 most time-consuming functions
        stats = pstats.Stats(profiler)
        stats.sort_stats('cumulative')
        stats.print_stats(10)
        
        return result

# Example usage
def slow_implementation():
    return sum(i**2 for i in range(10000))

def fast_implementation():
    return sum(i*i for i in range(10000))

def numpy_implementation():
    import numpy as np
    arr = np.arange(10000)
    return np.sum(arr**2)

# Debug and compare
debugger = PerformanceDebugger()

# Analyze bytecode
debugger.analyze_bytecode(slow_implementation)

# Compare implementations
debugger.compare_implementations(
    slow_implementation,
    fast_implementation,
    numpy_implementation
)

# Profile hot spots
debugger.profile_hot_spots(slow_implementation)
```

### 7. Profiling Best Practices:
```python
class ProfilingBestPractices:
    """Best practices for profiling Python code."""
    
    @staticmethod
    def profile_checklist():
        """Checklist for effective profiling."""
        checklist = [
            "1. Profile with realistic data sizes",
            "2. Profile the actual bottleneck, not toy examples",
            "3. Use statistical profiling for overall performance",
            "4. Use line profiling for specific functions",
            "5. Profile memory usage for memory-intensive applications",
            "6. Profile both CPU and I/O bound operations",
            "7. Profile in production-like environment",
            "8. Profile before and after optimizations",
            "9. Focus on functions that consume most time",
            "10. Consider profiling concurrency and parallelism"
        ]
        
        for item in checklist:
            print(item)
    
    @staticmethod
    def when_to_use_which_tool():
        """Guide for choosing profiling tools."""
        tools = {
            "cProfile": "Overall performance analysis, function-level profiling",
            "line_profiler": "Line-by-line analysis of specific functions",
            "memory_profiler": "Memory usage analysis",
            "timeit": "Micro-benchmarking small code snippets",
            "py-spy": "Profiling production applications without modification",
            "scalene": "Combined CPU and memory profiling",
            "Custom profilers": "Specific use cases and continuous monitoring"
        }
        
        print("Profiling tool selection guide:")
        for tool, use_case in tools.items():
            print(f"  {tool}: {use_case}")
```

## 67. What is the with statement in Python and how does context management work?

### Basic Context Management:
```python
# Traditional file handling (problematic)
def traditional_file_handling():
    """Traditional approach - resource leaks possible."""
    f = open('example.txt', 'w')
    f.write('Hello, World!')
    # If an exception occurs here, file won't be closed
    f.close()  # Might not execute

# Context manager approach (safe)
def context_manager_approach():
    """Using with statement - guaranteed cleanup."""
    with open('example.txt', 'w') as f:
        f.write('Hello, World!')
        # File automatically closed even if exception occurs

# Multiple context managers
def multiple_contexts():
    """Using multiple context managers."""
    with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
        data = infile.read()
        outfile.write(data.upper())
    # Both files automatically closed
```

### Creating Custom Context Managers:

#### Method 1: Using __enter__ and __exit__ methods:
```python
class DatabaseConnection:
    """Custom context manager for database connections."""
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connection = None
    
    def __enter__(self):
        """Setup: Called when entering 'with' block."""
        print(f"Connecting to {self.host}:{self.port}")
        self.connection = f"Connection to {self.host}:{self.port}"
        return self.connection  # This is assigned to 'as' variable
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Cleanup: Called when exiting 'with' block."""
        print(f"Closing connection to {self.host}:{self.port}")
        
        if exc_type is not None:
            print(f"Exception occurred: {exc_type.__name__}: {exc_value}")
            # Return False to propagate exception
            # Return True to suppress exception
        
        self.connection = None
        return False  # Don't suppress exceptions

# Usage
with DatabaseConnection("localhost", 5432) as conn:
    print(f"Using {conn}")
    # Connection automatically closed

# Example with exception handling
class SafeFileWriter:
    """Context manager with exception handling."""
    
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __enter__(self):
        print(f"Opening {self.filename}")
        self.file = open(self.filename, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing {self.filename}")
        
        if exc_type is Exception:
            print(f"An error occurred: {exc_value}")
            # Could log error, send notification, etc.
        
        if self.file:
            self.file.close()
        
        # Return False to let exception propagate
        return False

# Usage with exception
try:
    with SafeFileWriter("test.txt") as f:
        f.write("Hello")
        raise ValueError("Something went wrong")
        f.write("This won't execute")
except ValueError as e:
    print(f"Caught: {e}")
```

#### Method 2: Using contextlib module:
```python
from contextlib import contextmanager
import time
import tempfile
import os

@contextmanager
def timer():
    """Simple timing context manager."""
    start = time.time()
    print("Timer started")
    
    try:
        yield  # This is where the with block executes
    finally:
        end = time.time()
        print(f"Timer finished: {end - start:.4f} seconds")

# Usage
with timer():
    time.sleep(1)
    print("Doing some work...")

@contextmanager
def temporary_file(content):
    """Context manager for temporary files."""
    # Setup
    fd, path = tempfile.mkstemp()
    try:
        with os.fdopen(fd, 'w') as f:
            f.write(content)
        
        yield path  # Provide the file path to the with block
        
    finally:
        # Cleanup
        if os.path.exists(path):
            os.unlink(path)
            print(f"Temporary file {path} deleted")

# Usage
with temporary_file("Hello, temporary world!") as temp_path:
    with open(temp_path, 'r') as f:
        print(f"File content: {f.read()}")

@contextmanager
def managed_resource(resource_name):
    """Generic resource management."""
    print(f"Acquiring {resource_name}")
    resource = f"Resource: {resource_name}"
    
    try:
        yield resource
    except Exception as e:
        print(f"Error with {resource_name}: {e}")
        raise  # Re-raise the exception
    finally:
        print(f"Releasing {resource_name}")

# Usage
with managed_resource("Database Connection") as resource:
    print(f"Using {resource}")
```

### Advanced Context Managers:

#### Reusable Context Managers:
```python
from contextlib import contextmanager
import threading
import sys

class ThreadSafeCounter:
    """Thread-safe counter with context manager."""
    
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()
    
    @contextmanager
    def increment(self):
        """Context manager for thread-safe incrementing."""
        with self._lock:
            self._value += 1
            try:
                yield self._value
            finally:
                # Could add cleanup logic here
                pass
    
    @property
    def value(self):
        with self._lock:
            return self._value

# Usage
counter = ThreadSafeCounter()

with counter.increment() as current_value:
    print(f"Current value: {current_value}")

# Nested context managers
@contextmanager
def redirect_stdout(new_target):
    """Redirect stdout temporarily."""
    old_target = sys.stdout
    sys.stdout = new_target
    try:
        yield new_target
    finally:
        sys.stdout = old_target

# Usage
import io

output_buffer = io.StringIO()
with redirect_stdout(output_buffer):
    print("This goes to the buffer")
    print("So does this")

print("This goes to normal stdout")
print(f"Buffer contents: {output_buffer.getvalue()}")
```

#### Exception Handling in Context Managers:
```python
from contextlib import contextmanager, suppress
import logging

class LoggingContextManager:
    """Context manager with comprehensive logging."""
    
    def __init__(self, operation_name):
        self.operation_name = operation_name
        self.logger = logging.getLogger(__name__)
    
    def __enter__(self):
        self.logger.info(f"Starting {self.operation_name}")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self.logger.info(f"Successfully completed {self.operation_name}")
        else:
            self.logger.error(
                f"Error in {self.operation_name}: {exc_type.__name__}: {exc_value}"
            )
        
        # Always return False to propagate exceptions
        return False

# Usage
logging.basicConfig(level=logging.INFO)

with LoggingContextManager("Data Processing"):
    # Some operation
    data = [1, 2, 3, 4, 5]
    result = sum(data)
    print(f"Result: {result}")

# Using contextlib.suppress for ignoring specific exceptions
with suppress(FileNotFoundError):
    os.remove("nonexistent_file.txt")  # Won't raise exception

# Custom exception suppression
@contextmanager
def ignore_errors(*exception_types):
    """Context manager to ignore specific exception types."""
    try:
        yield
    except exception_types as e:
        print(f"Ignored exception: {type(e).__name__}: {e}")

# Usage
with ignore_errors(ValueError, TypeError):
    int("not a number")  # This error will be ignored
    print("This won't execute")

print("This will execute")
```

### Context Manager Patterns:

#### Resource Pool Management:
```python
from contextlib import contextmanager
import threading
from queue import Queue, Empty
import time

class ConnectionPool:
    """Connection pool with context manager support."""
    
    def __init__(self, create_connection, max_connections=5):
        self.create_connection = create_connection
        self.pool = Queue

