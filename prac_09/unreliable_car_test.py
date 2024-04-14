from unreliable_car import UnreliableCar

# Create a new unreliable car object with 50% reliability
my_car = UnreliableCar("Unreliable Car", 100, 50)

# Drive the car 40 km
distance_driven = my_car.drive(40)

# Print the car's details and the distance driven
print("Car Details:", my_car)
print("Distance Driven:", distance_driven)

