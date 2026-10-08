# Assignment 03 — Changes

## Name / Student ID

Name: Soe Wai Yan Htet Student ID: 6705140049

---

## 1. Changes Made During the Refactoring

| # | Code smell in the original                                                                      | What I changed it to                                                                                                   | OOP concept applied                    | How I verified behaviour was unchanged                                             |
| - | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------- | ---------------------------------------------------------------------------------- |
| 1 | Product details were accessed through tuple positions, making the code harder to read.          | Created a `Product` class with attributes for product name, price, and category.                                       | Classes / Encapsulation                | Ran the built-in self-test and checked the output.                                 |
| 2 | Order items used product indexes and quantities instead of representing each item as an object. | Created an `OrderItem` class containing a `Product` object and its quantity.                                           | Composition / Encapsulation            | Checked the item names, quantities, and line totals in the receipts.               |
| 3 | Membership discounts were calculated using repeated conditional statements.                     | Used a `Customer` base class with `Silver`, `Gold`, and `Platinum` subclasses to handle membership-specific behaviour. | Inheritance / Polymorphism             | Compared the discount calculations with the original output.                       |
| 4 | Reward points were calculated using multiple membership conditions.                             | Used the `points_multiplier()` method to define the reward multiplier for each customer tier.                          | Polymorphism                           | Checked the points earned by each customer.                                        |
| 5 | The original `calc()` function handled calculations and receipt printing together.              | Created an `Order` class with separate methods for subtotal, discount, tax, total, points, and receipt generation.     | Encapsulation / Separation of concerns | Ran the complete program and checked the self-test result.                         |
| 6 | Tax rates, discount rates, and thresholds were written directly into the calculation logic.     | Introduced named constants such as `TAX_RATE`, `FOOD_TAX_RATE`, `DISCOUNT_THRESHOLD`, and `BULK_DISCOUNT_RATE`.        | Clean code / Named constants           | Checked that the output remained unchanged after refactoring.                      |
| 7 | Product and order setup contained repeated code.                                                | Used collections and a loop to organize products and create customer orders more efficiently.                          | Abstraction / Composition              | Checked that all receipts appeared in the original order and the self-test passed. |

---

## 2. Short Reflection

The refactoring made the program easier to read and maintain by separating product information, order items, customer membership rules, and order calculations into different classes. Inheritance and polymorphism helped organize the different membership types, while named constants made the calculation rules easier to understand. I also simplified the order creation process to reduce repeated code. Throughout the refactoring, I kept the original products, prices, tax rules, discounts, reward points, and receipt formatting unchanged. I used the built-in self-test to verify that the refactored program produced the same output as the original.

---

## 3. Prompt Log

| # | My prompt to the AI                                              | What it suggested (summary)                                                                                                                              | Accept / reject / edited | How I checked it                                                              |
| - | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ----------------------------------------------------------------------------- |
| 1 | "Can you check my code?"                                         | Reviewed the Python code and checked the purpose of the built-in self-test.                                                                              | Edited                   | Reviewed the feedback before continuing with the refactoring.                 |
| 2 | "Refactor the code."                                             | Suggested restructuring the messy store system into an object-oriented design using classes, inheritance, composition, and separate calculation methods. | Edited                   | Reviewed the refactored code and checked the program's output.                |
| 3 | "Can you make the changes file for me?"                          | Prepared the `CHANGES.md` document using the required format, including the changes table, reflection, prompt log, and checklist.                        | Edited                   | Checked the document against the assignment format.                           |
| 4 | "Make the code cleaner and shorter without changing the output." | Simplified the code structure and reduced repeated code while preserving the original calculations and output.                                           | Accepted                 | Ran `python Assignment_03.py` and checked that the self-test reported `PASS`. |

---

## Ownership Statement

I will review the refactored code and make sure I understand the classes, methods, calculations, and receipt formatting before submitting it. This document records the AI assistance used during the refactoring process.

---

## 4. Before-you-submit Checklist

* [x] Product information is represented using a `Product` class.
* [x] Order items are represented using an `OrderItem` class.
* [x] Membership types use inheritance and polymorphism.
* [x] Order calculations are separated into individual methods.
* [x] Receipt generation is separated from calculation logic.
* [x] Repeated tax and discount values are stored as named constants.
* [x] Repeated order setup code has been reduced.
* [x] The built-in self-test reports that the output is unchanged.
* [ ] I have reviewed the code and can explain the changes before submitting.
