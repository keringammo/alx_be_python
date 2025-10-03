# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Create a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method with positive, negative, and zero values."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        """Test the subtract method with various inputs."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(5, 0), 5)

    def test_multiplication(self):
        """Test the multiply method with positive, negative, and zero values."""
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_division(self):
        """Test the divide method, including division by zero."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertEqual(self.calc.divide(-9, -3), 3)
        self.assertEqual(self.calc.divide(0, 5), 0)

        # Division by zero should return None
        self.assertIsNone(self.calc.divide(5, 0))


if __name__ == "__main__":
    unittest.main()
