class Rectangle:
    """Represents a rectangular piece of land."""

    def __init__(self, length, width):
        self.length = float(length)
        self.width = float(width)

    def calculate_area(self):
        """Returns the area of the rectangle."""
        return self.length * self.width

    def calculate_perimeter(self):
        """Returns the perimeter of the rectangle."""
        return 2 * (self.length + self.width)

    def display_info(self):
        """Prints area and perimeter details."""
        print(f"\nLand Dimensions: {self.length}m x {self.width}m")
        print(f"Area: {self.calculate_area():.2f} sq metres")
        print(f"Perimeter: {self.calculate_perimeter():.2f} metres")
