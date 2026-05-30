# Parent class: General Flight
class Flight:
    """Parent class representing any flight operated by Air New Zealand"""

    def __init__(self, flight_number, origin, destination, duration_hours):
        # Attributes shared by all flights
        self.flight_number = flight_number  # Inherited by subclass
        self.origin = origin                # Inherited by subclass 
        self.destination = destination      # Inherited by subclass
        self.duration_hours = duration_hours # Inherited by subclass
        self.airline = "Air New Zealand"    # Inherited by subclass

    # Method shared by all flights
    def get_flight_info(self):
        """Display basic flight info - inherited by DomesticFlight"""
        return f"{self.airline} {self.flight_number}: {self.origin} → {self.destination}, {self.duration_hours}h"

    def check_in(self, passenger_name):
        """Method inherited by subclass - same behavior for all flights"""
        return f"{passenger_name} checked in for {self.flight_number}"


# Subclass: Domestic Flight - inherits from Flight
class DomesticFlight(Flight):
    """Child class for domestic flights within New Zealand. Inherits all attributes/methods from Flight"""

    def __init__(self, flight_number, origin, destination, duration_hours, terminal, baggage_allowance_kg):
        # super() calls parent __init__ to inherit shared attributes
        super().__init__(flight_number, origin, destination, duration_hours)

        # Additional attributes specific to domestic flights only
        self.terminal = terminal  # NZ domestic terminal, not in parent
        self.baggage_allowance_kg = baggage_allowance_kg  # Domestic baggage rule, not in parent

    # Method overriding parent to add domestic-specific info
    def get_flight_info(self):
        """Extends parent method - shows inherited + specific attributes"""
        parent_info = super().get_flight_info()  # Reuse inherited method
        return f"{parent_info} | Terminal: {self.terminal}, Baggage: {self.baggage_allowance_kg}kg"

    # Additional method specific to domestic flights only
    def check_domestic_id(self, id_type):
        """Method specific to DomesticFlight - not in parent class"""
        return f"Domestic ID check: {id_type} verified for NZ domestic travel"


# Demo: Show inheritance in action
if __name__ == "__main__":
    # Create parent object
    flight1 = Flight("NZ101", "Auckland", "Los Angeles", 13)
    print("Parent - International Flight:")
    print(flight1.get_flight_info())
    print(flight1.check_in("John"))

    print("\n" + "="*50 + "\n")

    # Create child object - inherits parent attributes + has its own
    domestic1 = DomesticFlight("NZ501", "Auckland", "Wellington", 1.5, "Terminal 2", 23)
    print("Child - Domestic Flight:")
    print(domestic1.get_flight_info())  # Uses overridden method
    print(domestic1.check_in("Sarah"))  # Uses inherited method from parent
    print(domestic1.check_domestic_id("Driver License"))  # Uses child-specific method