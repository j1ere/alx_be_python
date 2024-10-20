import math

# Base class - Shape
class Shape:
    def area(self):
        """Method to calculate the area of the shape. Must be overridden by subclasses."""
        raise NotImplementedError("Subclasses must override this method.")

# Derived class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize a Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width

# Derived class - Circle
class Circle(Shape):
    def __init__(self, radius):
        """Initialize a Circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle using the formula πr²."""
        return math.pi * (self.radius ** 2)
