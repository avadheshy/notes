# LLD Fundamentals in Python

> A practical reference for Low Level Design (LLD) concepts using Python.
> Focus: how each concept shapes system design — not just syntax.

---

## Table of Contents

1. [Classes and Objects](#1-classes-and-objects)
2. [Enums](#2-enums)
3. [Interfaces (Abstract Base Classes)](#3-interfaces-abstract-base-classes)
4. [Encapsulation](#4-encapsulation)
5. [Abstraction](#5-abstraction)
6. [Inheritance](#6-inheritance)
7. [Polymorphism](#7-polymorphism)

---

## 1. Classes and Objects

### What is a Class?

A **class** is a blueprint that defines the **attributes** (data) and **behaviors** (methods) that its objects will have. In LLD, every real-world entity — `User`, `Order`, `Payment`, `Vehicle` — is modeled as a class.

### What is an Object?

An **object** is a concrete instance of a class. It holds its own state and can invoke the behaviors defined by the class.

### LLD Perspective

When designing a system, you identify **entities**, **responsibilities**, and **relationships** — each entity becomes a class.

**Example: Food Delivery System**

```python
class FoodItem:
    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category

    def get_details(self) -> str:
        return f"{self.name} | ₹{self.price} | {self.category}"


class Order:
    def __init__(self, order_id: str, customer_name: str):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items: list[FoodItem] = []
        self.total: float = 0.0

    def add_item(self, item: FoodItem):
        self.items.append(item)
        self.total += item.price

    def get_summary(self) -> str:
        item_names = [item.name for item in self.items]
        return f"Order #{self.order_id} for {self.customer_name}: {item_names} | Total: ₹{self.total}"


# Creating objects
burger = FoodItem("Burger", 150.0, "Fast Food")
pizza  = FoodItem("Pizza",  300.0, "Italian")

order = Order("ORD001", "Avadhesh")
order.add_item(burger)
order.add_item(pizza)

print(order.get_summary())
# Order #ORD001 for Avadhesh: ['Burger', 'Pizza'] | Total: ₹450.0
```

### Key Design Rules

- One class = one responsibility (Single Responsibility Principle)
- Attributes describe **what** the entity is; methods describe **what** it does
- Avoid "God classes" that know and do everything

---

## 2. Enums

### What is an Enum?

An **Enum** (Enumeration) is a set of named, constant values. In LLD it replaces magic strings/integers with meaningful, type-safe identifiers.

### LLD Perspective

Use enums to represent **states**, **categories**, **roles**, or **statuses** — anything with a fixed set of valid values.

```python
from enum import Enum, auto

class OrderStatus(Enum):
    PLACED     = auto()
    CONFIRMED  = auto()
    PREPARING  = auto()
    OUT_FOR_DELIVERY = auto()
    DELIVERED  = auto()
    CANCELLED  = auto()

class PaymentMethod(Enum):
    UPI    = "upi"
    CARD   = "card"
    COD    = "cod"
    WALLET = "wallet"

class UserRole(Enum):
    CUSTOMER   = "customer"
    RESTAURANT = "restaurant"
    DELIVERY   = "delivery"
    ADMIN      = "admin"
```

### Using Enums in a Class

```python
class Order:
    def __init__(self, order_id: str):
        self.order_id    = order_id
        self.status      = OrderStatus.PLACED
        self.payment     = PaymentMethod.UPI

    def update_status(self, new_status: OrderStatus):
        print(f"Order {self.order_id}: {self.status.name} → {new_status.name}")
        self.status = new_status

    def cancel(self):
        if self.status in (OrderStatus.DELIVERED, OrderStatus.CANCELLED):
            print("Cannot cancel.")
            return
        self.update_status(OrderStatus.CANCELLED)


order = Order("ORD002")
order.update_status(OrderStatus.CONFIRMED)
order.update_status(OrderStatus.PREPARING)
order.cancel()
```

### Key Design Rules

- Never use raw strings like `"pending"`, `"active"` for states — use enums
- Enums make `if/switch` logic readable and refactor-safe
- Enum comparisons are identity-based (`status == OrderStatus.PLACED`), not string-prone

---

## 3. Interfaces (Abstract Base Classes)

### What is an Interface?

An **interface** is a contract — it defines **what methods a class must implement**, without specifying how. Python uses **Abstract Base Classes (ABCs)** for this.

### LLD Perspective

Interfaces are the backbone of **design patterns** and **SOLID principles**. They let you program to abstractions, not concrete implementations — making the system easily extendable.

```python
from abc import ABC, abstractmethod

# Interface: any payment gateway must implement these
class PaymentGateway(ABC):

    @abstractmethod
    def pay(self, amount: float, user_id: str) -> bool:
        pass

    @abstractmethod
    def refund(self, transaction_id: str) -> bool:
        pass

    @abstractmethod
    def get_transaction_status(self, transaction_id: str) -> str:
        pass


# Interface: any notification service must implement these
class NotificationService(ABC):

    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
        pass
```

### Implementing the Interface

```python
class RazorpayGateway(PaymentGateway):

    def pay(self, amount: float, user_id: str) -> bool:
        print(f"[Razorpay] Charging ₹{amount} to user {user_id}")
        return True  # simulate success

    def refund(self, transaction_id: str) -> bool:
        print(f"[Razorpay] Refunding txn {transaction_id}")
        return True

    def get_transaction_status(self, transaction_id: str) -> str:
        return "SUCCESS"


class PhonePeGateway(PaymentGateway):

    def pay(self, amount: float, user_id: str) -> bool:
        print(f"[PhonePe] Charging ₹{amount} to user {user_id}")
        return True

    def refund(self, transaction_id: str) -> bool:
        print(f"[PhonePe] Refunding txn {transaction_id}")
        return True

    def get_transaction_status(self, transaction_id: str) -> str:
        return "SUCCESS"


# The OrderService doesn't care WHICH gateway — just that it follows the contract
class OrderService:
    def __init__(self, payment_gateway: PaymentGateway):
        self.gateway = payment_gateway

    def checkout(self, amount: float, user_id: str):
        success = self.gateway.pay(amount, user_id)
        if success:
            print("Order confirmed!")


# Swap gateways without touching OrderService
service = OrderService(RazorpayGateway())
service.checkout(450.0, "user_123")

service = OrderService(PhonePeGateway())
service.checkout(450.0, "user_123")
```

### Key Design Rules

- Depend on interfaces, not concrete classes (Dependency Inversion Principle)
- One interface = one responsibility (Interface Segregation Principle)
- Adding a new provider only requires a new class — no changes to existing code (Open/Closed Principle)

---

## 4. Encapsulation

### What is Encapsulation?

**Encapsulation** means bundling data and the methods that operate on it inside a class, and **restricting direct access** to internal state from the outside. You expose only what is necessary.

### LLD Perspective

Encapsulation protects the integrity of an object's state. External code cannot put the object in an invalid state because all modifications go through controlled methods (getters/setters or domain methods).

```python
class BankAccount:
    def __init__(self, account_id: str, owner: str, initial_balance: float = 0.0):
        self.__account_id = account_id        # private
        self.__owner      = owner             # private
        self.__balance    = initial_balance   # private
        self.__transactions: list[str] = []   # private

    # Read-only access to sensitive fields
    @property
    def account_id(self) -> str:
        return self.__account_id

    @property
    def owner(self) -> str:
        return self.__owner

    @property
    def balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        self.__transactions.append(f"DEPOSIT  ₹{amount:>10.2f}  |  Balance: ₹{self.__balance:.2f}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
        self.__transactions.append(f"WITHDRAW ₹{amount:>10.2f}  |  Balance: ₹{self.__balance:.2f}")

    def get_statement(self) -> str:
        header = f"Statement for {self.__owner} (Acc: {self.__account_id})\n"
        return header + "\n".join(self.__transactions)


acc = BankAccount("ACC001", "Avadhesh", 5000.0)
acc.deposit(2000.0)
acc.withdraw(500.0)

print(acc.balance)          # ✅ allowed via property
# acc.__balance = 99999    # ❌ AttributeError — cannot bypass the class

print(acc.get_statement())
```

### Python Visibility Conventions

| Prefix | Convention | Meaning |
|--------|-----------|---------|
| `name` | Public | Accessible from anywhere |
| `_name` | Protected | Internal use, accessible but not recommended outside |
| `__name` | Private | Name-mangled; not accessible from outside the class |

### Key Design Rules

- Never expose raw mutable fields — use properties or explicit methods
- Validation logic lives inside the class, not scattered in calling code
- Encapsulation = the object owns and guards its own state

---

## 5. Abstraction

### What is Abstraction?

**Abstraction** means hiding complex implementation details and exposing only a clean, simple interface. The caller knows **what** something does, not **how** it does it.

### LLD Perspective

Abstraction reduces coupling. A `NotificationService` caller doesn't need to know whether it uses SMTP, SNS, or a third-party API — it just calls `send()`.

```python
from abc import ABC, abstractmethod

# Abstract layer — defines WHAT
class NotificationService(ABC):

    @abstractmethod
    def send(self, recipient: str, subject: str, message: str) -> None:
        pass


# Concrete implementation — defines HOW
class EmailNotificationService(NotificationService):

    def __init__(self, smtp_host: str, smtp_port: int):
        self._smtp_host = smtp_host
        self._smtp_port = smtp_port

    def send(self, recipient: str, subject: str, message: str) -> None:
        # Internal complexity hidden from callers
        self._connect()
        self._authenticate()
        self._send_email(recipient, subject, message)
        self._disconnect()
        print(f"[Email] Sent to {recipient}: {subject}")

    def _connect(self):
        print(f"  → Connecting to {self._smtp_host}:{self._smtp_port}")

    def _authenticate(self):
        print("  → Authenticating...")

    def _send_email(self, recipient, subject, message):
        print(f"  → Sending email...")

    def _disconnect(self):
        print("  → Disconnecting.")


class SMSNotificationService(NotificationService):

    def __init__(self, api_key: str):
        self._api_key = api_key

    def send(self, recipient: str, subject: str, message: str) -> None:
        # Completely different internals — caller doesn't care
        print(f"[SMS] Sent to {recipient}: {message[:50]}...")


# Caller only interacts with the abstraction
class OrderNotifier:
    def __init__(self, notifier: NotificationService):
        self._notifier = notifier

    def notify_order_placed(self, customer_email: str, order_id: str):
        self._notifier.send(
            recipient=customer_email,
            subject="Order Confirmed",
            message=f"Your order #{order_id} has been placed."
        )


notifier = OrderNotifier(EmailNotificationService("smtp.gmail.com", 587))
notifier.notify_order_placed("user@example.com", "ORD003")
```

### Abstraction vs Encapsulation

| | Encapsulation | Abstraction |
|---|---|---|
| **Focus** | Hiding internal state/data | Hiding implementation complexity |
| **Goal** | Protect integrity | Reduce coupling |
| **Tool** | Private fields, properties | Abstract classes, interfaces |
| **Question** | "How is the data protected?" | "What does this do?" |

### Key Design Rules

- Abstract away anything likely to change (database, payment provider, messaging)
- A well-abstracted system lets you swap implementations without touching callers
- Every method name should describe intent, not mechanism (`send_otp()` not `post_to_twilio_api()`)

---

## 6. Inheritance

### What is Inheritance?

**Inheritance** allows a class (child) to acquire the properties and behaviors of another class (parent). It models **"is-a"** relationships.

### LLD Perspective

Use inheritance to share common structure. A `Vehicle` base class can define shared attributes (`brand`, `speed`), while `Car`, `Bike`, `Truck` each extend it with specific behavior.

```python
from abc import ABC, abstractmethod
from enum import Enum

class VehicleType(Enum):
    CAR   = "car"
    BIKE  = "bike"
    TRUCK = "truck"


# Base class
class Vehicle(ABC):
    def __init__(self, brand: str, model: str, speed_kmh: float):
        self.brand     = brand
        self.model     = model
        self.speed_kmh = speed_kmh
        self._is_running = False

    def start(self):
        self._is_running = True
        print(f"{self.brand} {self.model} started.")

    def stop(self):
        self._is_running = False
        print(f"{self.brand} {self.model} stopped.")

    @abstractmethod
    def get_type(self) -> VehicleType:
        pass

    @abstractmethod
    def calculate_fare(self, distance_km: float) -> float:
        pass

    def __str__(self):
        return f"{self.brand} {self.model} ({self.get_type().value}) | {self.speed_kmh} km/h"


# Child classes
class Car(Vehicle):
    def __init__(self, brand: str, model: str, speed_kmh: float, seats: int):
        super().__init__(brand, model, speed_kmh)
        self.seats = seats

    def get_type(self) -> VehicleType:
        return VehicleType.CAR

    def calculate_fare(self, distance_km: float) -> float:
        return distance_km * 12.0  # ₹12 per km


class Bike(Vehicle):
    def __init__(self, brand: str, model: str, speed_kmh: float):
        super().__init__(brand, model, speed_kmh)

    def get_type(self) -> VehicleType:
        return VehicleType.BIKE

    def calculate_fare(self, distance_km: float) -> float:
        return distance_km * 7.0  # ₹7 per km


class Truck(Vehicle):
    def __init__(self, brand: str, model: str, speed_kmh: float, payload_tons: float):
        super().__init__(brand, model, speed_kmh)
        self.payload_tons = payload_tons

    def get_type(self) -> VehicleType:
        return VehicleType.TRUCK

    def calculate_fare(self, distance_km: float) -> float:
        return distance_km * 25.0  # ₹25 per km


# Usage
vehicles: list[Vehicle] = [
    Car("Toyota", "Innova", 120, 7),
    Bike("Honda", "Activa", 80),
    Truck("Tata", "Prima", 90, 20),
]

for v in vehicles:
    v.start()
    fare = v.calculate_fare(15)
    print(f"  {v}  |  15 km fare: ₹{fare}")
    v.stop()
```

### Inheritance vs Composition

> **Prefer composition over inheritance** in most LLD scenarios.

| | Inheritance | Composition |
|---|---|---|
| **Relationship** | "is-a" (Car is a Vehicle) | "has-a" (Car has an Engine) |
| **Coupling** | Tight — child depends on parent internals | Loose — components are independent |
| **Flexibility** | Hard to change base class | Easy to swap components |
| **Use when** | True "is-a", shared structure | Behaviour reuse, multiple capabilities |

### Key Design Rules

- Use inheritance only for true "is-a" relationships
- Always call `super().__init__()` in child constructors
- Avoid deep inheritance chains (3+ levels) — they become hard to reason about
- Favour abstract base classes as parents so children are forced to define their contract

---

## 7. Polymorphism

### What is Polymorphism?

**Polymorphism** means "many forms". The same interface or method call behaves differently depending on the actual object at runtime.

There are two main types:

- **Runtime Polymorphism** (Method Overriding) — subclass provides its own version of a parent method
- **Compile-time Polymorphism** (Method Overloading) — Python handles this via default args or `*args`

### LLD Perspective

Polymorphism is what makes a system genuinely extensible. You write code against an interface once; new implementations plug in without touching existing code.

```python
from abc import ABC, abstractmethod

# --- Runtime Polymorphism via Method Overriding ---

class Discount(ABC):

    @abstractmethod
    def apply(self, original_price: float) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass


class NoDiscount(Discount):
    def apply(self, original_price: float) -> float:
        return original_price

    def description(self) -> str:
        return "No discount"


class PercentageDiscount(Discount):
    def __init__(self, percent: float):
        self._percent = percent

    def apply(self, original_price: float) -> float:
        return original_price * (1 - self._percent / 100)

    def description(self) -> str:
        return f"{self._percent}% off"


class FlatDiscount(Discount):
    def __init__(self, flat_amount: float):
        self._flat = flat_amount

    def apply(self, original_price: float) -> float:
        return max(0.0, original_price - self._flat)

    def description(self) -> str:
        return f"₹{self._flat} flat off"


class BuyOneGetOneFree(Discount):
    def apply(self, original_price: float) -> float:
        return original_price / 2  # paying for one

    def description(self) -> str:
        return "Buy 1 Get 1 Free"


# Polymorphic usage — same call, different behavior
def print_final_price(price: float, discount: Discount):
    final = discount.apply(price)
    print(f"Original: ₹{price:.2f} | {discount.description()} | Final: ₹{final:.2f}")


discounts: list[Discount] = [
    NoDiscount(),
    PercentageDiscount(20),
    FlatDiscount(100),
    BuyOneGetOneFree(),
]

for d in discounts:
    print_final_price(500.0, d)
```

Output:
```
Original: ₹500.00 | No discount | Final: ₹500.00
Original: ₹500.00 | 20% off | Final: ₹400.00
Original: ₹500.00 | ₹100 flat off | Final: ₹400.00
Original: ₹500.00 | Buy 1 Get 1 Free | Final: ₹250.00
```

### Duck Typing — Python's Natural Polymorphism

Python also supports polymorphism without formal inheritance via **duck typing**:

> "If it walks like a duck and quacks like a duck, it's a duck."

```python
class PDFReport:
    def generate(self, data: dict) -> str:
        return f"[PDF] Report for {data}"

class ExcelReport:
    def generate(self, data: dict) -> str:
        return f"[Excel] Report for {data}"

class JSONReport:
    def generate(self, data: dict) -> str:
        return f"[JSON] Report for {data}"

# No shared base class needed — all have .generate()
def export_report(reporter, data: dict):
    print(reporter.generate(data))

for reporter in [PDFReport(), ExcelReport(), JSONReport()]:
    export_report(reporter, {"orders": 42})
```

### Key Design Rules

- Polymorphism eliminates `if/elif` chains like `if type == "car": ... elif type == "bike": ...`
- New types are added by creating new classes, not modifying existing ones (Open/Closed Principle)
- Write functions/methods that accept a base type or interface — let the runtime dispatch to the right implementation

---

## Quick Reference: LLD Concept Map

```
System Design
│
├── Identify Entities         →  Classes & Objects
│
├── Model Fixed States/Roles  →  Enums
│
├── Define Contracts          →  Interfaces (ABC)
│     │
│     ├── Hide Data           →  Encapsulation
│     ├── Hide Complexity     →  Abstraction
│     ├── Share Structure     →  Inheritance
│     └── One Call, Many Forms→  Polymorphism
│
└── Apply SOLID Principles
      S — Single Responsibility  (one class, one job)
      O — Open/Closed            (extend, don't modify)
      L — Liskov Substitution    (subtypes replace base types)
      I — Interface Segregation  (small, focused interfaces)
      D — Dependency Inversion   (depend on abstractions)
```

---

## Summary Table

| Concept | LLD Role | Python Tool |
|---|---|---|
| **Class & Object** | Model real-world entities | `class`, `__init__` |
| **Enum** | Fixed states, categories, roles | `from enum import Enum` |
| **Interface** | Define contracts for components | `ABC`, `@abstractmethod` |
| **Encapsulation** | Protect and control internal state | `__private`, `@property` |
| **Abstraction** | Expose clean API, hide internals | `ABC` + concrete classes |
| **Inheritance** | Reuse structure in "is-a" hierarchies | `class Child(Parent)` |
| **Polymorphism** | Same call, different runtime behaviour | Method overriding, duck typing |