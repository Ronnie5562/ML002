import unittest
import calc


# Method                      Checks that                 New in

# assertEqual(a, b)             a == b
# assertNotEqual(a, b)          a != b
# assertTrue(x)                 bool(x) is True
# assertFalse(x)                bool(x) is False
# assertIs(a, b)                a is b                      3.1
# assertIsNot(a, b)             a is not b                  3.1
# assertIsNone(x)               x is None                   3.1
# assertIsNotNone(x)            x is not None               3.1
# assertIn(a, b)                a in b                      3.1
# assertNotIn(a, b)             a not in b                  3.1
# assertIsInstance(a, b)        isinstance(a, b)            3.2
# assertNotIsInstance(a, b)     not isinstance(a, b)        3.2


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(5, 10), 15)
        self.assertEqual(calc.add(-5, 10), 5)
        self.assertEqual(calc.add(-5, -10), -15)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-10, 5), -15)
        self.assertEqual(calc.subtract(-10, -5), -5)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-10, 5), -50)
        self.assertEqual(calc.multiply(-10, -5), 50)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-10, 5), -2)
        self.assertEqual(calc.divide(-10, -5), 2)
        self.assertEqual(
            calc.divide(5, 2), 2.5
        )  # This will catch an error if we change the division sign to floor division in our actual file.

        # To run a test to if a specified error is raised, use the syntax below:
        # assertRaises(exception, callable, *args, **kwds)
        self.assertRaises(ZeroDivisionError, calc.divide, 10, 0)

        # We can also do the abaove using a context manager
        with self.assertRaises(ZeroDivisionError):
            calc.divide(10, 0)


# To run the test, use: python -m unittest <name of the file>
# To make the code run normally without using the script above, add the below to your program:
if __name__ == "__main__":
    unittest.main(verbosity=2)


# In Python's unittest framework, the order in which tests are run is determined by the test discovery process.

# By default, the unittest framework discovers and runs tests in a deterministic order, which is usually alphabetical order based on the names of
# the test methods. However, the exact order of the tests may vary depending on the version of Python, the operating system, and other factors.

# It's generally not recommended to rely on the specific order in which tests are run, as this can lead to fragile tests that fail unexpectedly if
#  the order changes. Instead, each test should be designed to be independent of other tests and should set up its own test data if necessary.

# That being said, if you do want to specify the order in which tests are run, you can use test suites to group tests together and run them in a
# specific order. You can also use the TestCase.addCleanup() method to specify cleanup code that will be run after each test method, regardless of
# whether the test passes or fails.
