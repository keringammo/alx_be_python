import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up a new calculator instance before each test."""
        self.calc = SimpleCalculator()

    # ---------- Addition Tests ----------
    def test_addition(self):
        """Test the addition method with various cases."""
        self.assertEqual(self.calc.add(2, 3), 5)          # positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)         # negative + positive
        self.assertEqual(self.calc.add(-5, -7), -12)      # two negatives
        self.assertEqual(self.calc.add(0, 10), 10)        # zero + number
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)    # floats

    # ---------- Subtraction Tests ----------
    def test_subtraction(self):
        """Test the subtraction method with various cases."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(5.5, 2.2), 3.3)

    # ---------- Multiplication Tests ----------
    def test_multiplication(self):
        """Test the multiplication method with various cases."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-3, -3), 9)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)

    # ---------- Division Tests ----------
    def test_division(self):
        """Test the division method with various cases."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

    def test_division_by_zero(self):
        """Test that division by zero returns None."""
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))  # edge: 0/0


if __name__ == "__main__":
    unittest.main()
