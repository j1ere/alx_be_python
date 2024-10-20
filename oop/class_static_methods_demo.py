# Calculator class demonstrating static and class methods
class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        Does not access or modify the class state.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        Can access and modify class-level attributes.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
