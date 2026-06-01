

"""
Requirements
The vending machine should support multiple products with different prices and quantities.
The machine should accept coins and notes of different denominations.
The machine should dispense the selected product and return change if necessary.
The machine should keep track of the available products and their quantities.
The machine should handle multiple transactions concurrently and ensure data consistency.
The machine should provide an interface for restocking products and collecting money.

There should be product with quantity and price
price with notes and coins
"""
"""
Vending Machine — complete implementation
"""
from enum import Enum
from collections import defaultdict
import threading


class Note(Enum):
    FIVE_HUNDRED = 500
    HUNDRED = 100
    FIFTY = 50
    TWENTY = 20
    TEN = 10
    FIVE = 5
    TWO = 2
    ONE = 1


class Coin(Enum):
    TEN = 10
    FIVE = 5
    TWO = 2
    ONE = 1


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_quantity(self, qty):
        self.quantity += qty

    def remove_quantity(self, qty):
        if qty > self.quantity:
            raise ValueError(f"Only {self.quantity} unit(s) of '{self.name}' available")
        self.quantity -= qty

    def get_price(self, qty=1):
        return self.price * qty

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price}, quantity={self.quantity})"


class InsufficientFundsError(Exception):
    pass


class ChangeUnavailableError(Exception):
    pass


class Machine:
    def __init__(self):
        self.products: list[Product] = []
        # Denomination -> count stored in the machine
        self.notes: dict[Note, int] = defaultdict(int)
        self.coins: dict[Coin, int] = defaultdict(int)
        self._lock = threading.Lock()


    def add_product(self, name: str, price: int, quantity: int) -> Product:
        with self._lock:
            prod = Product(name, price, quantity)
            self.products.append(prod)
            return prod

    def restock_product(self, product: Product, qty: int):
        with self._lock:
            product.add_quantity(qty)

    def available_products(self):
        with self._lock:
            if not self.products:
                print("No products available.")
                return
            print(f"{'Name':<20} {'Price':>8} {'Stock':>6}")
            print("-" * 36)
            for p in self.products:
                status = f"{p.quantity}" if p.quantity > 0 else "OUT OF STOCK"
                print(f"{p.name:<20} ₹{p.price:>7} {status:>6}")

    # ------------------------------------------------------------------ #
    #  Cash management                                                    #
    # ------------------------------------------------------------------ #

    def add_notes(self, notes: list[Note]):
        with self._lock:
            for note in notes:
                self.notes[note] += 1

    def add_coins(self, coins: list[Coin]):
        with self._lock:
            for coin in coins:
                self.coins[coin] += 1

    def collect_cash(self) -> int:
        """Empty the machine and return total collected."""
        with self._lock:
            total = sum(d.value * cnt for d, cnt in self.notes.items())
            total += sum(d.value * cnt for d, cnt in self.coins.items())
            self.notes.clear()
            self.coins.clear()
            print(f"Collected ₹{total} from the machine.")
            return total

    def _machine_balance(self) -> int:
        total = sum(d.value * cnt for d, cnt in self.notes.items())
        total += sum(d.value * cnt for d, cnt in self.coins.items())
        return total

    # ------------------------------------------------------------------ #
    #  Change-making (greedy, largest denomination first)                 #
    # ------------------------------------------------------------------ #

    def _make_change(self, amount: int) -> dict:
        """
        Return the denominations to give back as change.
        Raises ChangeUnavailableError if exact change can't be made.
        NOTE: caller must hold self._lock.
        """
        if amount == 0:
            return {}

        change = {}
        remaining = amount

        # All denominations sorted largest → smallest
        all_denoms = sorted(
            [(d, self.notes[d]) for d in Note] +
            [(d, self.coins[d]) for d in Coin],
            key=lambda x: x[0].value,
            reverse=True
        )

        for denom, count in all_denoms:
            if remaining <= 0:
                break
            use = min(count, remaining // denom.value)
            if use:
                change[denom] = use
                remaining -= use * denom.value

        if remaining != 0:
            raise ChangeUnavailableError(
                f"Cannot make exact change of ₹{amount}. "
                f"Still need ₹{remaining}."
            )
        return change

    def _apply_change(self, change: dict):
        """Deduct change denominations from machine stock. Caller holds lock."""
        for denom, count in change.items():
            if isinstance(denom, Note):
                self.notes[denom] -= count
            else:
                self.coins[denom] -= count

    def return_money(self, amount: int):
        """Public helper to return a specific amount to the user (e.g. on cancel)."""
        with self._lock:
            change = self._make_change(amount)
            self._apply_change(change)
            self._print_change(change)

    @staticmethod
    def _print_change(change: dict):
        if not change:
            print("  No change returned.")
            return
        print("  Change returned:")
        for denom, count in sorted(change.items(), key=lambda x: x[0].value, reverse=True):
            print(f"    {count} × ₹{denom.value}")

    # ------------------------------------------------------------------ #
    #  Core transaction                                                   #
    # ------------------------------------------------------------------ #

    def buy_product(
        self,
        product: Product,
        notes: list[Note] | None = None,
        coins: list[Coin] | None = None,
        quantity: int = 1,
    ):
        notes = notes or []
        coins = coins or []

        with self._lock:
            # 1. Validate stock
            if product.quantity < quantity:
                raise ValueError(
                    f"Only {product.quantity} unit(s) of '{product.name}' in stock."
                )

            # 2. Count inserted money
            inserted = sum(n.value for n in notes) + sum(c.value for c in coins)
            cost = product.get_price(quantity)

            if inserted < cost:
                raise InsufficientFundsError(
                    f"Inserted ₹{inserted} but '{product.name}' costs ₹{cost}."
                )

            # 3. Add inserted money to machine first (so change can use it)
            for note in notes:
                self.notes[note] += 1
            for coin in coins:
                self.coins[coin] += 1

            # 4. Calculate and reserve change
            change_amount = inserted - cost
            try:
                change = self._make_change(change_amount)
            except ChangeUnavailableError:
                # Rollback inserted cash
                for note in notes:
                    self.notes[note] -= 1
                for coin in coins:
                    self.coins[coin] -= 1
                raise

            # 5. Commit: deduct product, apply change
            product.remove_quantity(quantity)
            self._apply_change(change)

            # 6. Receipt
            print(f"\n✓ Dispensing {quantity} × '{product.name}'  (₹{cost})")
            print(f"  Inserted: ₹{inserted}")
            self._print_change(change)
            print(f"  Machine balance: ₹{self._machine_balance()}\n")


# ------------------------------------------------------------------ #
#  Demo                                                               #
# ------------------------------------------------------------------ #

if __name__ == "__main__":
    machine = Machine()

    # Seed the machine with change float
    machine.add_notes([Note.TEN, Note.FIVE, Note.TWO, Note.TWO])
    machine.add_coins([Coin.FIVE, Coin.TWO, Coin.ONE, Coin.ONE])

    # Add products
    chips  = machine.add_product("Lays Chips",   20, 5)
    water  = machine.add_product("Water Bottle",  15, 3)
    cola   = machine.add_product("Coca-Cola",     35, 2)
    coffee = machine.add_product("Coffee",        50, 1)

    print("=== Available Products ===")
    machine.available_products()

    print("\n=== Transaction 1: Buy Chips with ₹50 ===")
    machine.buy_product(chips, notes=[Note.FIFTY])

    print("=== Transaction 2: Buy Water with exact change ===")
    machine.buy_product(water, notes=[Note.TEN], coins=[Coin.FIVE])

    print("=== Transaction 3: Buy 2 × Cola with ₹100 ===")
    machine.buy_product(cola, notes=[Note.HUNDRED], quantity=2)

    print("=== Products after transactions ===")
    machine.available_products()

    print("\n=== Collect cash ===")
    machine.collect_cash()

    print("\n=== Error case: insufficient funds ===")
    try:
        machine.buy_product(coffee, coins=[Coin.TEN])
    except InsufficientFundsError as e:
        print(f"  Error: {e}")

    print("\n=== Error case: out of stock ===")
    try:
        machine.buy_product(cola, notes=[Note.HUNDRED])
    except ValueError as e:
        print(f"  Error: {e}")