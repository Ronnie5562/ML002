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

# To run the test, use: python -m unittest <name of the file>
# To make the code run normally without using the script above, add the below to your program:
if __name__  == '__main__':
    unittest.main()