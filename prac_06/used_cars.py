"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from car import Car

def main():
    """Demo test code to show how to use car class."""
    # Create a new Car object called "limo" that is initialized with 100 units of fuel.
    limo = Car(100, name="Luxury Car")

    # Add 20 more units of fuel to this new car object using the add_fuel method.
    limo.add_fuel(20)

    # Print the amount of fuel in the car.
    print(f"Amount of fuel in the car: {limo.fuel}")

    # Attempt to drive the car 115 km using the drive method.
    actual_distance_driven = limo.drive(115)
    print(f"Actual distance driven: {actual_distance_driven}")

    # Print the car object to ensure that the __str__ method is working as expected.
    print(limo)

main()
