# Python OOPs Concepts
## Python Class
A class is a collection of objects. Classes are blueprints for creating objects. A class defines a set of attributes and methods that the created objects (instances) can have. Classes are created by keyword class.
## Some points on Python class:  

Classes are created by keyword class.

Attributes are the variables that belong to a class methods are functions of that class.

Attributes are always public and can be accessed using the dot (.) operator. Example: Myclass.Myattribute

# Python Objects
An Object is an instance of a Class. It represents a specific implementation of the class and holds its own data.

## An object consists of:

State: It is represented by the attributes and reflects the properties of an object.

Behavior: It is represented by the methods of an object and reflects the response of an object to other objects.

Identity: It gives a unique name to an object and enables one object to interact with other objects.

# Self Parameter
self parameter is a reference to the current instance of the class. It allows us to access the attributes and methods of the object.

# __init__ Method
__init__ method is the constructor in Python, automatically called when a new object is created. It initializes the attributes of the class.

# Class and Instance Variables
In Python, variables defined in a class can be either class variables or instance variables, and understanding the distinction between them is crucial for object-oriented programming.

```
class Dog:
    # Class variable
    species = "Canine"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

# Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Access class and instance variables
print(dog1.species)  # (Class variable) Canine
print(dog1.name)     # (Instance variable) Buddy
print(dog2.name)     # (Instance variable) Charlie

# Modify instance variables
dog1.name = "Max"
print(dog1.name)     # (Updated instance variable) Max

# Modify class variable
dog1.species = "Feline"
print(dog1.species)  # (Updated class variable)Feline
print(dog2.species) # Charlie
```
# Python Inheritance
Inheritance allows a class (child class) to acquire properties and methods of another class (parent class). It supports hierarchical classification and promotes code reuse.
# Types of Inheritance:
## Single Inheritance:
A child class inherits from a single parent class.
```
class Parent:
    def __init__(self, name):
        self.name = name

    def func(self):
        print(f"This is a function from Parent class. Name: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call Parent's constructor
        self.age = age

    def func(self):
        print(f"This is a function from Child class. Name: {self.name}, Age: {self.age}")

# Testing
print("Single Inheritance:")
c = Child("Avadhesh", 25)
c.func()  # This is a function from Child class. Name: Avadhesh, Age: 25
super(Child, c).func()  # This is a function from Parent class. Name: Avadhesh

```

## Multiple Inheritance: 
A child class inherits from more than one parent class.
```
class Parent1:
    def __init__(self, name):
        self.name = name

    def func(self):
        print(f"This is a function from Parent1. Name: {self.name}")

class Parent2:
    def __init__(self, age):
        self.age = age

    def func(self):
        print(f"This is a function from Parent2. Age: {self.age}")

class MultipleChild(Parent1, Parent2):
    def __init__(self, name, age):
        Parent1.__init__(self, name)  # Explicitly call Parent1's constructor
        Parent2.__init__(self, age)   # Explicitly call Parent2's constructor

    def func(self):
        print(f"This is a function from MultipleChild. Name: {self.name}, Age: {self.age}")

# Testing
print("\nMultiple Inheritance:")
mc = MultipleChild("Avadhesh", 25)
mc.func()  # Calls the overridden method in MultipleChild

# Using super() to call Parent1's method
super(MultipleChild, mc).func()  # Calls Parent1's func()

# Using super() to call Parent2's method - This does NOT work directly
# super(Parent1, mc).func()  # ERROR: Parent2 is not in Parent1's MRO

# Other ways to call Parent2's func()
Parent2.func(mc)  # Explicit call to Parent2's method


```

## Multilevel Inheritance:
 A child class inherits from a parent class, which in turn inherits from another class.
```
class Grandparent:
    def __init__(self, surname):
        print("Initializing Grandparent")
        self.surname = surname

    def func1(self):
        print(f"This is a function from Grandparent. Surname: {self.surname}")

class Parent(Grandparent):
    def __init__(self, surname, father_name):
        print("Initializing Parent")
        super().__init__(surname)  # Call Grandparent's constructor
        self.father_name = father_name

    def func2(self):
        print(f"This is a function from Parent. Father: {self.father_name}, Surname: {self.surname}")

class Grandchild(Parent):
    def __init__(self, surname, father_name, child_name):
        print("Initializing Grandchild")
        super().__init__(surname, father_name)  # Call Parent's constructor
        self.child_name = child_name

    def func3(self):
        print(f"This is a function from Grandchild. Name: {self.child_name}, Father: {self.father_name}, Surname: {self.surname}")

# Testing
print("\nMultilevel Inheritance:")
gc = Grandchild("Sharma", "Rajesh", "Avadhesh")
gc.func1()  # Calls Grandparent's function
gc.func2()  # Calls Parent's function
gc.func3()  # Calls Grandchild's function

```

## Hierarchical Inheritance:
 Multiple child classes inherit from a single parent class.
```
class Parent:
    def __init__(self, surname):
        print("Initializing Parent")
        self.surname = surname

    def func1(self):
        print(f"This is a function from Parent. Surname: {self.surname}")

class Child1(Parent):
    def __init__(self, surname, name1):
        print("Initializing Child1")
        super().__init__(surname)  # Call Parent's constructor
        self.name1 = name1

    def func2(self):
        print(f"This is a function from Child1. Name: {self.name1}, Surname: {self.surname}")

class Child2(Parent):
    def __init__(self, surname, name2):
        print("Initializing Child2")
        super().__init__(surname)  # Call Parent's constructor
        self.name2 = name2

    def func3(self):
        print(f"This is a function from Child2. Name: {self.name2}, Surname: {self.surname}")

# Testing
print("\nHierarchical Inheritance:")
c1 = Child1("Sharma", "Avadhesh")
c2 = Child2("Sharma", "Rahul")

c1.func1()  # Calls Parent's function
c2.func1()  # Calls Parent's function
c1.func2()  # Calls Child1's function
c2.func3()  # Calls Child2's function

```

## Hybrid Inheritance:
 A combination of two or more types of inheritance.
```
class Base:
    def __init__(self, base_value):
        print("Initializing Base")
        self.base_value = base_value

    def func1(self):
        print(f"This is a function from Base. Base Value: {self.base_value}")

class HybridParent1(Base):
    def __init__(self, base_value, parent1_value):
        print("Initializing HybridParent1")
        super().__init__(base_value)  # Call Base's constructor
        self.parent1_value = parent1_value

    def func2(self):
        print(f"This is a function from HybridParent1. Parent1 Value: {self.parent1_value}, Base Value: {self.base_value}")

class HybridParent2(Base):
    def __init__(self, base_value, parent2_value):
        print("Initializing HybridParent2")
        super().__init__(base_value)  # Call Base's constructor
        self.parent2_value = parent2_value

    def func3(self):
        print(f"This is a function from HybridParent2. Parent2 Value: {self.parent2_value}, Base Value: {self.base_value}")

class HybridChild(HybridParent1, HybridParent2):
    def __init__(self, base_value, parent1_value, parent2_value, child_value):
        print("Initializing HybridChild")
        HybridParent1.__init__(self, base_value, parent1_value)  # Explicitly call HybridParent1's constructor
        HybridParent2.__init__(self, base_value, parent2_value)  # Explicitly call HybridParent2's constructor
        self.child_value = child_value

    def func4(self):
        print(f"This is a function from HybridChild. Child Value: {self.child_value}, Parent1 Value: {self.parent1_value}, Parent2 Value: {self.parent2_value}, Base Value: {self.base_value}")

# Testing
print("\nHybrid Inheritance:")
hc = HybridChild("BaseData", "Parent1Data", "Parent2Data", "ChildData")

hc.func1()  # Calls Base's function
hc.func2()  # Calls HybridParent1's function
hc.func3()  # Calls HybridParent2's function
hc.func4()  # Calls HybridChild's function

```

# Python Polymorphism
Polymorphism allows methods to have the same name but behave differently based on the object’s context. It can be achieved through method overriding or overloading.

## Types of Polymorphism
## Compile-Time Polymorphism: 
This type of polymorphism is determined during the compilation of the program. It allows methods or operators with the same name to behave differently based on their input parameters or usage. It is commonly referred to as method or operator overloading.
## Run-Time Polymorphism: 
This type of polymorphism is determined during the execution of the program. It occurs when a subclass provides a specific implementation for a method already defined in its parent class, commonly known as method overriding.
```
# Parent Class
class Dog:
    def sound(self):
        print("dog sound")  # Default implementation

# Run-Time Polymorphism: Method Overriding
class Labrador(Dog):
    def sound(self):
        print("Labrador woofs")  # Overriding parent method

class Beagle(Dog):
    def sound(self):
        print("Beagle Barks")  # Overriding parent method

# Compile-Time Polymorphism: Method Overloading Mimic
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c  # Supports multiple ways to call add()

# Run-Time Polymorphism
dogs = [Dog(), Labrador(), Beagle()]
for dog in dogs:
    dog.sound()  # Calls the appropriate method based on the object type dog sound/Labrador woofs/Beagle Barks


# Compile-Time Polymorphism (Mimicked using default arguments)
calc = Calculator()
print(calc.add(5, 10))  # Two arguments 15
print(calc.add(5, 10, 15))  # Three arguments 30
```
# Python Encapsulation
Encapsulation is the bundling of data (attributes) and methods (functions) within a class, restricting access to some components to control interactions.

A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.
## Types of Encapsulation:
Public Members: Accessible from anywhere.

Protected Members: Accessible within the class and its subclasses.

Private Members: Accessible only within the class.
```
class Dog:
    def __init__(self, name, breed, age):
        self.name = name  # Public attribute
        self._breed = breed  # Protected attribute
        self.__age = age  # Private attribute

    # Public method
    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"

    # Getter and Setter for private attribute
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")

# Example Usage
dog = Dog("Buddy", "Labrador", 3)

# Accessing public member
print(dog.name)  # Accessible #Buddy

# Accessing protected member
print(dog._breed)  # Accessible but discouraged outside the class #Labrador

# Accessing private member using getter
print(dog.get_age()) #3

# Modifying private member using setter
dog.set_age(5)
print(dog.get_info()) #Name: Buddy, Breed: Labrador, Age:5
```
# Data Abstraction 
Abstraction hides the internal implementation details while exposing only the necessary functionality. It helps focus on “what to do” rather than “how to do it.”

## Types of Abstraction:
Partial Abstraction: Abstract class contains both abstract and concrete methods.

Full Abstraction: Abstract class contains only abstract methods (like interfaces).
```
from abc import ABC, abstractmethod

class Dog(ABC):  # Abstract Class
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):  # Abstract Method
        pass

    def display_name(self):  # Concrete Method
        print(f"Dog's Name: {self.name}")

class Labrador(Dog):  # Partial Abstraction
    def sound(self):
        print("Labrador Woof!")

class Beagle(Dog):  # Partial Abstraction
    def sound(self):
        print("Beagle Bark!")

# Example Usage
dogs = [Labrador("Buddy"), Beagle("Charlie")]
for dog in dogs:
    dog.display_name()  # Calls concrete method # Dog's Name:
    dog.sound()  # Calls implemented abstract method #
```
# Inner class
Inner classes are useful in scenarios where you want to:

Keep closely related classes together.
Provide a helper or specialized class for a larger class.
Hide the implementation details and prevent misuse from the outside.
## signle level inner class
```
class Doctors:
    def __init__(self):
        self.name = 'Doctor'
        self.den = self.Dentist()
        self.car = self.Cardiologist()

    def show(self):
        print('In outer class')
        print('Name:', self.name)

    # create a 1st Inner class
    class Dentist:
        def __init__(self):
            self.name = 'Dr. Savita'
            self.degree = 'BDS'

        def display(self):
            print("Name:", self.name)
            print("Degree:", self.degree)

    # create a 2nd Inner class
    class Cardiologist:
        def __init__(self):
            self.name = 'Dr. Amit'
            self.degree = 'DM'

        def display(self):
            print("Name:", self.name)
            print("Degree:", self.degree)


# create a object
# of outer class
outer = Doctors()
outer.show()

# create a object
# of 1st inner class
d1 = outer.den

# create a object
# of 2nd inner class
d2 = outer.car
print()
d1.display()
print()
d2.display()
obj=Doctors.Dentist()
obj.display()
```
## Mutilable inner class
```
# create an outer class
class Geeksforgeeks:

    def __init__(self):
        # create an inner class object
        self.inner = self.Inner()

    def show(self):
        print('This is an outer class')

    # create a 1st inner class

    class Inner:
        def __init__(self):
            # create an inner class of inner class object
            self.innerclassofinner = self.Innerclassofinner()

        def show(self):
            print('This is the inner class')

        # create an inner class of inner

        class Innerclassofinner:
            def show(self):
                print('This is an inner class of inner class')


# create an outer class object
# i.e.Geeksforgeeks class object
outer = Geeksforgeeks()
outer.show()
print()

# create an inner class object
gfg1 = outer.inner
gfg1.show()
print()

# create an inner class of inner class object
gfg2 = outer.inner.innerclassofinner
gfg2.show()
```
