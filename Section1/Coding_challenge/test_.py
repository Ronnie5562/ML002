from __future__ import print_function

import unittest


def fib(n):
    return 1 if n <= 2 else fib(n - 1) + fib(n - 2)


class TestFib(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.n = 10

    def tearDown(self):
        print("tearDown")
        del self.n

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def test_fib_assert_equal(self):
        self.assertEqual(fib(self.n), 55)

    def test_fib_assert_true(self):
        self.assertTrue(fib(self.n) == 55)


# The code above is run in the {test_for_test.py} file in this directory.

# Study the output of this code to understand setUp and tearDown hierarchy
print(TestFib.__class__.__name__)
print()
