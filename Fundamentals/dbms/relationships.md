In object-oriented programming, relationships in classes define how different classes are connected or interact with one another. These relationships describe the structure of your software and how objects collaborate to fulfill its purpose. The three main types of relationships are:

# 1. Inheritance (IS-A Relationship)
Definition: Represents a hierarchical relationship where a subclass derives from a superclass. It signifies that the subclass "is a type of" the superclass.

Characteristics:

The subclass inherits fields and methods from the parent class.
Supports code reuse and polymorphism.
Use inheritance only when there is a clear "is-a" relationship.
Example:
```
class Animal:
    def eat(self):
        print("This animal eats food.")

class Dog(Animal):  # Dog IS-A Animal
    def bark(self):
        print("Woof!")

dog = Dog()
dog.eat()   # Output: This animal eats food.
dog.bark()  # Output: Woof!
```
# 2. Association (HAS-A Relationship)
Definition: Represents a relationship where one class uses another class. It is a "has-a" relationship.

## Characteristics:
Classes are linked but do not depend on each other to exist.

There are two main types:

## Aggregation: 
A weaker association where the lifecycle of the associated objects is independent.
## Composition: 
A stronger association where the lifecycle of the associated objects depends on the parent object.
```
class Engine:
    def start(self):
        print("Engine starts.")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Car HAS-A Engine

    def drive(self):
        self.engine.start()
        print("Car is driving.")

engine = Engine()
car = Car(engine)
car.drive()
# Output:
# Engine starts.
# Car is driving.
```
Composition Example:
```
class Engine:
    def start(self):
        print("Engine starts.")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car owns Engine (strong dependency)

    def drive(self):
        self.engine.start()
        print("Car is driving.")

car = Car()
car.drive()
# Output:
# Engine starts.
# Car is driving.
```
# 3. Dependency (Uses-A Relationship)
Definition: Represents a relationship where one class temporarily uses another class's functionality.

Characteristics:

Typically occurs through method parameters or local variables.
The dependency is short-lived and does not imply ownership.
Example:
```
class Printer:
    def print_message(self, message):
        print(f"Printing: {message}")

class Document:
    def __init__(self, content):
        self.content = content

    def print_document(self, printer):
        printer.print_message(self.content)  # Document USES-A Printer

printer = Printer()
document = Document("Hello, world!")
document.print_document(printer)
# Output: Printing: Hello, world!
```
Summary Table
```
Relationship	                            Description	                                            Keywords	                    Example
Inheritance	                                IS-A relationship	                                    extends, is-a	                Dog IS-A Animal
Association	                                HAS-A relationship	                                    has-a	Car                     HAS-A Engine
Dependency	                                USES-A relationship	                                    uses	Document                USES-A Printer
```