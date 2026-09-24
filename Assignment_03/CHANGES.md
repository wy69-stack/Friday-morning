# Assignment 03 — Changes

## Name / Student ID

Name: Soe Wai Yan Htet
Student ID: 6705140049

---

## 1. Changes Made During the Refactoring

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
|---|---|---|---|---|
| 1 | Product information was stored as tuples, which made the data harder to manage. | I created a `Product` class with attributes for the product name, price, and category. | Classes / Encapsulation | Ran the self-test and checked the product information in the receipts. |
| 2 | Order items stored a product index and quantity instead of representing the item directly. | I created an `OrderItem` class that contains a `Product` object and its quantity. | Composition / Encapsulation | Compared the receipt items and quantities with the original output. |
| 3 | Membership discounts were selected using multiple tier conditions. | I created a customer class hierarchy where each membership type provides its own discount rule. | Inheritance / Polymorphism | Tested all customer tiers and checked that their discounts matched the target output. |
| 4 | Points were calculated using another set of membership tier conditions. | I added a `points_multiplier()` method to the customer classes so each tier defines its own multiplier. | Polymorphism | Checked the points earned by every customer against the target output. |
| 5 | The original calculation function handled calculations, printing, and several other responsibilities together. | I created an `Order` class with separate methods for subtotal, discount, tax, total, points, and receipt generation. | Encapsulation / Separation of concerns | Ran the complete program and checked the self-test result. |
| 6 | Tax rates, discount rates, and quantity thresholds were written directly as values in the code. | I created named constants such as `TAX_RATE`, `FOOD_TAX_RATE`, `BULK_DISCOUNT_RATE`, and `DISCOUNT_THRESHOLD`. | Clean code / Encapsulation | Ran the program after replacing the values with constants and checked that the output stayed the same. |

---

## 2. Short Reflection

The change that improved the program the most was separating the membership rules into different customer classes. This made the discount and points calculations easier to understand because each membership type is responsible for its own behaviour. Creating separate `Product`, `OrderItem`, and `Order` classes also made the relationships between the different parts of the store clearer. I had to be careful not to change the original business rules, especially the tax, discounts, points, and receipt formatting. I used the self-test to compare the refactored output with the original target output.

---

## 3. Prompt Log

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 | "what do i need to do" | Explained the main requirements of the assignment and the different refactoring tasks. | Accepted | I compared the explanation with the assignment instructions. |
| 2 | "i dont understand please give me answer only" | Provided a complete refactored solution using classes, inheritance, composition, constants, and separate calculation methods. | Edited | I placed the solution into `Assignment_03.py` and reviewed the code. |
| 3 | "what is through" | Explained the meaning of “thorough” and what was expected from the written part. | Accepted | Used the explanation to understand what information needed to be included. |
| 4 | "PS ... Solution not implemented yet." | Explained that the placeholder `refactored_main()` was still being executed and showed where the refactored code needed to be placed. | Accepted | Checked my Python file and replaced the placeholder with the refactored solution. |
| 5 | "can you rewrite because if i submit this teacher will tell me its copy" | Helped rewrite the change table, reflection, and prompt log using different wording based on my own work. | Edited | Checked that the rewritten content matched the changes I actually made. |

---

## Ownership Statement

I confirm that I understand the code and changes included in my submission. I reviewed the refactored classes, methods, calculations, and receipt output before submitting. The prompt log reflects the AI assistance I used while working on this assignment.

---

## 4. Before-you-submit Checklist

- [x] Product, order item, customer, and order data are represented using objects.
- [x] Membership-specific behaviour is handled through the customer class hierarchy.
- [x] Calculation methods return values instead of printing results.
- [x] Receipt generation is separated from the calculation methods.
- [x] Repeated values such as tax and discount rates are stored as named constants.
- [x] Constructors validate important object data.
- [x] The change table and reflection have been completed.
- [x] The prompt log has been updated to reflect my actual AI use.
- [x] I have reviewed the submitted code and understand the changes I made.
