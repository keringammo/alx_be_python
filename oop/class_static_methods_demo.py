# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static method - does not access class or instance
    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    # Class method - accesses class attributes via cls
    @classmethod
    def multiply(cls, a, b):
        """Return the product of two numbers, showing class-level info."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
