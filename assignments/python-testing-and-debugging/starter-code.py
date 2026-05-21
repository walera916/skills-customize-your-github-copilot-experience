import unittest


def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


def is_even(value):
    """Return True if the value is even, otherwise False."""
    return value % 2 == 0


def format_greeting(name, age):
    """Return a formatted greeting message."""
    return f"Hello, {name}! You are {age} years old."


def calculate_discount(price, percent):
    """Return the price after applying a percentage discount."""
    # Fix the bug here: discount should subtract from the original price
    discounted_price = price - (price * percent / 100)
    return round(discounted_price, 2)


class TestMathFunctions(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(5, 4), 9)
        self.assertEqual(add_numbers(-1, 1), 0)

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(3))

    def test_format_greeting(self):
        self.assertEqual(format_greeting("Ava", 16), "Hello, Ava! You are 16 years old.")

    def test_calculate_discount(self):
        self.assertEqual(calculate_discount(100, 20), 80.00)
        self.assertEqual(calculate_discount(50, 50), 25.00)


if __name__ == "__main__":
    unittest.main()
