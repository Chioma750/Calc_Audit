import unittest
from main import addition, subtraction, multiplication, division


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(5, 3), 8)

    def test_subtraction(self):
        self.assertEqual(subtraction(5, 3), 2)

    def test_multiplication(self):
        self.assertEqual(multiplication(5, 3), 15)

    def test_division(self):
        self.assertEqual(division(6, 3), 2)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division(10, 0)


if __name__ == "__main__":
    unittest.main()
