"""
================================================================================
 Assignment 03 — Refactor the Messy Store System
 192-201 Advanced Computer Programming with Generative AI
 Week 5 — OOP Design & Refactoring   |   Faculty of IT (International), Siam University
 Lecturer: Hrang Kap Lian
================================================================================

 Maps to: CLO1 (object-oriented design) and CLO5 (responsible, verified AI use)
 Weight:  10 Points     AI-use level: Level 2 (AI-assisted + PROMPT LOG required)

--------------------------------------------------------------------------------
 THE TASK
--------------------------------------------------------------------------------
 You are given ONE working program that is badly written. Do NOT add features and
 do NOT change what it does. REFACTOR it: reshape the code into a clean,
 object-oriented design while producing the EXACT SAME output.

    The one rule of refactoring: same behaviour, cleaner code.
    If the output changes, it is no longer a refactor — it is a bug.

 How to run:
    python Assignment_03.py
 It prints PASS when your refactor reproduces the original output exactly,
 or FAIL with the first line that differs.
"""

import io
import contextlib


# ==============================================================================
# LEGACY STORE SYSTEM — DO NOT EDIT
# ==============================================================================

PRODUCTS = [
    ("Laptop", 1200.0, "electronics"),
    ("Headphones", 200.0, "electronics"),
    ("Coffee Beans", 15.0, "food"),
    ("Notebook", 5.0, "stationery"),
    ("Water Bottle", 10.0, "food"),
    ("Monitor", 300.0, "electronics"),
    ("Pen", 2.0, "stationery"),
]

TAXRATE = 0.07
foodtax = 0.0

ORDERS = [
    ("Alice", "gold", [(0, 1), (1, 2), (2, 3)]),
    ("Bob", "none", [(3, 10), (6, 5)]),
    ("Charlie", "platinum", [(5, 2), (4, 6), (2, 2)]),
    ("Dana", "silver", [(1, 1), (3, 3), (6, 10)]),
]


def calc(o):
    global TAXRATE

    n = o[0]
    t = o[1]
    items = o[2]

    sub = 0.0
    tax = 0.0

    print("Receipt for " + n + " (" + t + ")")
    print("-" * 40)

    for it in items:
        pi = it[0]
        q = it[1]

        p = PRODUCTS[pi][1]
        nm = PRODUCTS[pi][0]
        cat = PRODUCTS[pi][2]

        line = p * q
        sub = sub + line

        if cat == "food":
            tax = tax + line * foodtax
        else:
            tax = tax + line * TAXRATE

        print(nm + " x" + str(q) + " = " + str(line))

    d = 0.0

    if t == "none":
        d = 0.0
    elif t == "silver":
        if sub > 100:
            d = sub * 0.05
        else:
            d = sub * 0.02
    elif t == "gold":
        if sub > 100:
            d = sub * 0.10
        else:
            d = sub * 0.05
    elif t == "platinum":
        if sub > 100:
            d = sub * 0.15
        else:
            d = sub * 0.10

    totalqty = 0

    for it in items:
        totalqty = totalqty + it[1]

    if totalqty >= 10:
        d = d + sub * 0.03

    total = sub - d + tax

    pts = 0

    if t == "none":
        pts = int(total // 10)
    elif t == "silver":
        pts = int(total // 10) * 2
    elif t == "gold":
        pts = int(total // 10) * 3
    elif t == "platinum":
        pts = int(total // 10) * 5

    print("-" * 40)
    print("Subtotal: " + str(round(sub, 2)))
    print("Discount: " + str(round(d, 2)))
    print("Tax: " + str(round(tax, 2)))
    print("Total: " + str(round(total, 2)))
    print("Points earned: " + str(pts))
    print("")

    return total


def legacy_main():
    grand = 0.0

    for o in ORDERS:
        grand = grand + calc(o)

    print("GRAND TOTAL (all orders): " + str(round(grand, 2)))


# ==============================================================================
# BEHAVIOUR LOCK — DO NOT EDIT
# ==============================================================================

def capture(fn):
    """Run fn() and return everything it printed, as a string."""
    buf = io.StringIO()

    with contextlib.redirect_stdout(buf):
        fn()

    return buf.getvalue()


GOLDEN_OUTPUT = capture(legacy_main)


# ==============================================================================
# YOUR REFACTORED SOLUTION
# ==============================================================================

TAX_RATE = 0.07
FOOD_TAX_RATE = 0.0
FOOD_CATEGORY = "food"

DISCOUNT_THRESHOLD = 100
BULK_QTY_THRESHOLD = 10
BULK_DISCOUNT_RATE = 0.03

POINTS_DIVISOR = 10


class Product:
    def __init__(self, name, price, category):
        if not name:
            raise ValueError("Product name cannot be empty")

        if price < 0:
            raise ValueError("Product price cannot be negative")

        self.name = name
        self.price = price
        self.category = category

    def tax_rate(self):
        if self.category == FOOD_CATEGORY:
            return FOOD_TAX_RATE

        return TAX_RATE

    def __str__(self):
        return self.name


class OrderItem:
    def __init__(self, product, quantity):
        if quantity < 1:
            raise ValueError("Quantity must be at least 1")

        self.product = product
        self.quantity = quantity

    def line_total(self):
        return self.product.price * self.quantity

    def tax(self):
        return self.line_total() * self.product.tax_rate()


class Customer:
    tier_name = "none"

    def __init__(self, name):
        if not name:
            raise ValueError("Customer name cannot be empty")

        self.name = name

    def discount_rate(self, subtotal):
        return 0.0

    def points_multiplier(self):
        return 1


class Silver(Customer):
    tier_name = "silver"

    def discount_rate(self, subtotal):
        if subtotal > DISCOUNT_THRESHOLD:
            return 0.05

        return 0.02

    def points_multiplier(self):
        return 2


class Gold(Customer):
    tier_name = "gold"

    def discount_rate(self, subtotal):
        if subtotal > DISCOUNT_THRESHOLD:
            return 0.10

        return 0.05

    def points_multiplier(self):
        return 3


class Platinum(Customer):
    tier_name = "platinum"

    def discount_rate(self, subtotal):
        if subtotal > DISCOUNT_THRESHOLD:
            return 0.15

        return 0.10

    def points_multiplier(self):
        return 5


class Order:
    def __init__(self, customer, items):
        if not items:
            raise ValueError("Order must contain at least one item")

        self.customer = customer
        self.items = items

    def subtotal(self):
        return sum(item.line_total() for item in self.items)

    def discount(self):
        subtotal = self.subtotal()

        membership_discount = (
            subtotal * self.customer.discount_rate(subtotal)
        )

        total_quantity = sum(
            item.quantity for item in self.items
        )

        bulk_discount = 0.0

        if total_quantity >= BULK_QTY_THRESHOLD:
            bulk_discount = subtotal * BULK_DISCOUNT_RATE

        return membership_discount + bulk_discount

    def tax(self):
        return sum(item.tax() for item in self.items)

    def total(self):
        return self.subtotal() - self.discount() + self.tax()

    def points(self):
        return (
            int(self.total() // POINTS_DIVISOR)
            * self.customer.points_multiplier()
        )

    def receipt(self):
        lines = []

        lines.append(
            f"Receipt for {self.customer.name} "
            f"({self.customer.tier_name})"
        )

        lines.append("-" * 40)

        for item in self.items:
            lines.append(
                f"{item.product.name} "
                f"x{item.quantity} = "
                f"{item.line_total()}"
            )

        lines.append("-" * 40)
        lines.append(f"Subtotal: {round(self.subtotal(), 2)}")
        lines.append(f"Discount: {round(self.discount(), 2)}")
        lines.append(f"Tax: {round(self.tax(), 2)}")
        lines.append(f"Total: {round(self.total(), 2)}")
        lines.append(f"Points earned: {self.points()}")

        # Two blank lines are required here so that the printed
        # output contains the same blank line as the legacy program.
        lines.append("")
        lines.append("")

        return "\n".join(lines)


def refactored_main():

    # Products
    laptop = Product("Laptop", 1200.0, "electronics")
    headphones = Product("Headphones", 200.0, "electronics")
    coffee = Product("Coffee Beans", 15.0, "food")
    notebook = Product("Notebook", 5.0, "stationery")
    water = Product("Water Bottle", 10.0, "food")
    monitor = Product("Monitor", 300.0, "electronics")
    pen = Product("Pen", 2.0, "stationery")

    # Customers
    alice = Gold("Alice")
    bob = Customer("Bob")
    charlie = Platinum("Charlie")
    dana = Silver("Dana")

    # Orders
    alice_order = Order(
        alice,
        [
            OrderItem(laptop, 1),
            OrderItem(headphones, 2),
            OrderItem(coffee, 3),
        ],
    )

    bob_order = Order(
        bob,
        [
            OrderItem(notebook, 10),
            OrderItem(pen, 5),
        ],
    )

    charlie_order = Order(
        charlie,
        [
            OrderItem(monitor, 2),
            OrderItem(water, 6),
            OrderItem(coffee, 2),
        ],
    )

    dana_order = Order(
        dana,
        [
            OrderItem(headphones, 1),
            OrderItem(notebook, 3),
            OrderItem(pen, 10),
        ],
    )

    orders = [
        alice_order,
        bob_order,
        charlie_order,
        dana_order,
    ]

    grand_total = 0.0

    for order in orders:
        print(order.receipt(), end="")
        grand_total += order.total()

    print(
        "GRAND TOTAL (all orders): "
        + str(round(grand_total, 2))
    )


# ==============================================================================
# SELF-TEST — DO NOT EDIT
# ==============================================================================

def _check():
    try:
        your_output = capture(refactored_main)

    except NotImplementedError:
        print("Solution not implemented yet.\n")
        print(
            "Below is the TARGET output your refactor "
            "must reproduce exactly:\n"
        )
        print(GOLDEN_OUTPUT)
        return

    if your_output == GOLDEN_OUTPUT:
        print(
            "PASS - behaviour is unchanged. "
            "Your refactor is safe.\n"
        )

    else:
        print(
            "FAIL - the output changed, so this is "
            "not yet a valid refactor.\n"
        )

        g = GOLDEN_OUTPUT.splitlines()
        y = your_output.splitlines()

        for i in range(max(len(g), len(y))):
            gl = g[i] if i < len(g) else "<no line>"
            yl = y[i] if i < len(y) else "<no line>"

            if gl != yl:
                print(
                    "First difference at line "
                    + str(i + 1)
                    + ":"
                )
                print(
                    "  expected: "
                    + repr(gl)
                )
                print(
                    "  yours:    "
                    + repr(yl)
                )
                break


if __name__ == "__main__":
    _check()