#  1. Singleton Design Pattern
Singleton Pattern is a creational design pattern that guarantees a class has only one instance and provides a global point of access to it.

Singleton is useful in scenarios like:

- Managing Shared Resources (database connections, thread pools, caches, configuration settings)

- Coordinating System-Wide Actions (logging, print spoolers, file managers)

- Managing State (user session, application state)

Pros and Cons of Singleton Design Pattern

  ```
  Pros                                                                           Cons

Insure a single instanse of object and provide global access to it.              Voilates Single Responsbilty principle. Solve 2 problems at a time.
only one instance is created which can be benificial for resource heavy classe.    in multithreading special care shoulde taken for race condiotion.
provides a way to maintain global state in an application.                        global state maintaince is very difficult.
support lazy initialization                                                       classes using singleton can become tightly coupled to the singelon class.

  ```

There are many  design strategies for singleton design pattern
## ✅ 1. Eager Initialization Singleton
Create the singleton instance when the class is loaded.


```
class EagerSingleton:
    _instance = None  # Class variable for storing the instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(EagerSingleton, cls).__new__(cls)
            cls._instance.value = 42  # initialize value once
        return cls._instance

# Eagerly create the instance
EagerSingleton._instance = EagerSingleton()

# Usage
s1 = EagerSingleton()
s2 = EagerSingleton()

assert s1 is s2  # ✅ True, same instance

```
Pros: Simple, thread-safe

Cons: Instance created even if never used

## ✅ 2. Lazy Initialization Singleton
Only create the instance when it is needed.

```
class LazySingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LazySingleton, cls).__new__(cls)
        return cls._instance
```
Pros: Saves resources if instance is never used

Cons: Not thread-safe

## ✅ 3. Synchronized Lazy Initialization (Thread-safe)
Using threading.Lock to synchronize access.


```
import threading

class SynchronizedSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:  # synchronized block
            if cls._instance is None:
                cls._instance = super(SynchronizedSingleton, cls).__new__(cls)
        return cls._instance
```
Pros: Thread-safe

Cons: Every call acquires lock, even if instance exists

## ✅ 4. Double-Checked Locking Singleton
Reduces lock overhead by checking instance twice (before and after locking).


```
import threading

class DoubleCheckedSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(DoubleCheckedSingleton, cls).__new__(cls)
        return cls._instance
```
Pros: Thread-safe + avoids unnecessary locking

Cons: Slightly more complex
---
# 2 Builder design pattern
The Builder Design Pattern is a creational design pattern that lets you construct complex objects step-by-step, separating the construction logic from the final representation.

It’s particularly useful in situations where:

- An object requires many optional fields, and not all of them are needed every time.

- You want to avoid telescoping constructors or large constructors with multiple parameters.

- The object construction process involves multiple steps that need to happen in a particular order.
  
```
class Computer:
    def __init__(self, cpu=None, ram=None, storage=None, gpu=None):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.gpu = gpu

    def __str__(self):
        return f"Computer(cpu={self.cpu}, ram={self.ram}, storage={self.storage}, gpu={self.gpu})"

class ComputerBuilder:
    def __init__(self):
        self._cpu = None
        self._ram = None
        self._storage = None
        self._gpu = None

    def set_cpu(self, cpu):
        self._cpu = cpu
        return self

    def set_ram(self, ram):
        self._ram = ram
        return self

    def set_storage(self, storage):
        self._storage = storage
        return self

    def set_gpu(self, gpu):
        self._gpu = gpu
        return self

    def build(self):
        return Computer(self._cpu, self._ram, self._storage, self._gpu)

builder = ComputerBuilder()
computer = (
    builder
    .set_cpu("Intel i7")
    .set_ram("16GB")
    .set_storage("512GB SSD")
    .set_gpu("NVIDIA RTX 4060")
    .build()
)

print(computer)
# Output: Computer(cpu=Intel i7, ram=16GB, storage=512GB SSD, gpu=NVIDIA RTX 4060)

```
---
# 3. Prototype Design Pattern
The Prototype Design Pattern is a creational design pattern that lets you create new objects by cloning existing ones, instead of instantiating them from scratch.

It’s particularly useful in situations where:

Creating a new object is expensive, time-consuming, or resource-intensive.

You want to avoid duplicating complex initialization logic.

You need many similar objects with only slight differences.
The Challenge of Cloning Objects
Imagine you have an object in your system, and you want to create an exact copy of it. How would you do it?

Your first instinct might be to:

- Create a new object of the same class.

- Manually copy each field from the original object to the new one.

Simple enough, right?

Well—not quite.

# Problem 1: Encapsulation Gets in the Way
This approach assumes that all fields of the object are publicly accessible. But in a well-designed system, many fields are private and hidden behind encapsulation. That means your cloning logic can’t access them directly.

Unless you break encapsulation (which defeats the purpose of object-oriented design), you can’t reliably copy the object this way.

# Problem 2: Class-Level Dependency
Even if you could access all the fields, you'd still need to know the concrete class of the object to instantiate a copy.

This tightly couples your cloning logic to the object's class, which introduces problems:

It violates the Open/Closed Principle.

It reduces flexibility if the object's implementation changes.

It becomes harder to scale when you work with polymorphism.

# Problem 3: Interface-Only Contexts
In many cases, your code doesn’t work with concrete classes at all—it works with interfaces.

For example:

public void processClone(Shape shape) {
    Shape cloned = ???; // we only know it implements Shape
}
Here, you know the object implements a certain interface (Shape), but you don’t know what class it is, let alone how to create a new instance of it. You’re stuck unless the object knows how to clone itself.

The Better Way: Let the Object Clone Itself
This is where the Prototype Design Pattern comes in.

Instead of having external code copy or recreate the object, the object itself knows how to create its clone. It exposes a clone() or copy() method that returns a new instance with the same data.

This:

- Preserves encapsulation

- Eliminates the need to know the concrete class

- Makes the system more flexible and extensible
