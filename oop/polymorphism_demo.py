import math

class Shape:
    def area(self):
        """Base method to be overridden by derived classes."""
        raise NotImplementedError("Subclasses must override this method.")


class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Override area() to calculate area of rectangle."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """Initialize Circle with radius."""
        self.radius = radius

    def area(self):
        """Override area() to calculate area of circle."""
        return math.pi * (self.radius ** 2)
