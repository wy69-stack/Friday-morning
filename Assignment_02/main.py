from rental import Vehicle, Renter, ElectricCar, Motorbike


# Create vehicles
car = Vehicle("Toyota", "Yaris", "1AB234")
electric = ElectricCar("Tesla", "Model 3", "EV567", 75)
bike = Motorbike("Honda", "CB500", "MB789", 500)


# Create renter
renter = Renter("John", 12345)

print("Before rental:")
print(car)

# Rent vehicle
car.rent()
renter.rented.append(car)

print("\nAfter rental:")
print(car)

# Return vehicle
car.return_vehicle()
renter.rented.remove(car)

print("\nAfter return:")
print(car)


# Test invalid renter
print("\nTesting invalid renter:")

try:
    bad_renter = Renter("", 0)
except ValueError as e:
    print("Error:", e)


# Polymorphism
print("\nMixed vehicle list:")

vehicles = [car, electric, bike]

for vehicle in vehicles:
    print(vehicle)