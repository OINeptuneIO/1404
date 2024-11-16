"""
CP1404/CP5632 Practical
Car class
"""
from taxi import Taxi
class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes additional charges."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # Adjust the price_per_km based on the fanciness level
        self.price_per_km *=self.fanciness

    def get_fare(self):
        """Return the price for the taxi trip including flagfall."""
        # Calculate the fare including flagfall
        return super().get_fare() + SilverServiceTaxi.flagfall

    def calculate_fare(self):
        """Calculate the fare based on the total distance driven and adjusted price_per_km."""
        return self.odometer * self.price_per_km + SilverServiceTaxi.flagfall

    def __str__(self):
        """Return a string representation like a Taxi but with flagfall, adjusted price_per_km, and fanciness."""
        return f"{super().__str1__()}, ${self.price_per_km:.2f}/km plus flagfall of ${SilverServiceTaxi.flagfall:.2f}"

