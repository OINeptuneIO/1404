from car import Car
import random

class UnreliableCar(Car):
    """Specialised version of a Car with reliability factor."""
    
    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but only if random number is less than reliability."""
        if random.randint(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0
