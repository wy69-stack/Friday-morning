How to Run

Open a terminal in the project folder and run:

python main.py

The program demonstrates:

-Creating vehicles and a renter.
-Renting and returning a vehicle.
-Printing vehicle information and rental status.
-Handling invalid renter information using ValueError.
-Using a Vehicle, ElectricCar, and Motorbike in the same list.
-Demonstrating polymorphism through different __str__() methods.

Classes

    Vehicle

        The Vehicle class stores the vehicle's make, model, plate number, and rental status.

        It includes:

        rent() — changes the vehicle status to rented.
        return_vehicle() — changes the vehicle status back to available.
        __str__() — displays the vehicle information and rental status.

    Renter

        The Renter class stores the renter's name, licence number, and rented vehicles.

        The name and licence number are validated using @property. An empty name or a licence number that is zero or negative raises a ValueError.

    ElectricCar

        ElectricCar inherits from Vehicle and adds battery_kwh to store the battery capacity.

        It overrides __str__() to display electric-car information in its own format.

    Motorbike

        Motorbike inherits from Vehicle and adds engine_cc to store the engine size.

        It overrides __str__() to display motorbike information in its own format.

Object-Oriented Programming Concepts

    This project demonstrates:

        Classes and Objects — Vehicles and renters are represented as objects.
        Encapsulation — Renter information is controlled using properties and validation.
        Inheritance — ElectricCar and Motorbike inherit from Vehicle.
        Polymorphism — Different vehicle types can be stored in the same list and each uses its own __str__() method.

AI Use Note

    I used AI to help me understand the assignment instructions and Object-Oriented Programming concepts. I wrote and implemented the Python code myself and used AI explanations to help me understand and complete the assignment.