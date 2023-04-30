import unittest
from classes import Employee
from unittest.mock import patch
import sys


class Testclasses(unittest.TestCase):
    def setUp(self):
        self.emp_1 = Employee("Corey", "Schafer", 50000)
        self.emp_2 = Employee("Test", "Employee", 60000)

    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, "Corey_Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Test_Employee@email.com")

        self.emp_1.first = "Star"
        self.emp_2.first = "Real"

        self.assertEqual(self.emp_1.email, "Star_Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Real_Employee@email.com")

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, "Corey Schafer")
        self.assertEqual(self.emp_2.fullname, "Test Employee")

        self.emp_1.first = "Star"
        self.emp_2.first = "Real"

        self.assertEqual(self.emp_1.fullname, "Star Schafer")
        self.assertEqual(self.emp_2.fullname, "Real Employee")

    @unittest.skipIf(
        sys.platform.startswith("win"), "I don't want this to run on windows"
    )
    def test_monthly_schedule(self):
        with patch("classes.urllib.request.urlopen") as moked_file:
            moked_file.return_value.ok = True
            moked_file.return_value.text = "success"

            schedule = self.emp_1.monthly_schedule("May")
            moked_file.assert_called_with("http://company.com/Schafer/May")
            self.assertEqual(schedule, "success")


print(dir(Testclasses))  # It contains the list of asserts you can use.
print()
print("______________________________________________________________________")
print()
if __name__ == "__main__":
    unittest.main(verbosity=2)

# The verbose argument used above is to specify that we want a detailed result of the test


# Skipping tests and expected failures
# New in version 3.1.

# Unittest supports skipping individual test methods and even whole classes of tests. In addition, it supports marking a test as an “expected failure, ” a test that is broken and will fail, but shouldn’t be counted as a failure on a TestResult.

# Skipping a test is simply a matter of using the skip() decorator or one of its conditional variants.

# Basic skipping looks like this:


class MyTestCase(unittest.TestCase):
    @unittest.skip("demonstrating Skipping")
    def test_nothing(self):
        self.fail("Shouldn't happen")
        # The decorator takes an optional message argument, which is a string that explains why the test was skipped. In this case, the message is
        # "demonstrating Skipping".

    @unittest.skipIf(sys.version > (1, 2), "Not supported in this version of python")
    def test_format(self):
        # Tests that work for only a certain version of python.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "Requires windows")
    def test_windows_support(self):
        # windows specific testing code
        pass


# @unittest.skip(reason)
# Unconditionally skip the decorated test. reason should describe why the test is being skipped.


# @unittest.skipIf(condition, reason)
# Skip the decorated test if condition is true.


# @unittest.skipUnless(condition, reason)
# Skip the decorated test unless condition is true.


# @unittest.expectedFailure
# Mark the test as an expected failure. If the test fails when run, the test is not counted as a failure.

# exception unittest.SkipTest(reason)
# This exception is raised to skip a test.

# Test driven development simply indicates that you write the test for a given program before writing the program itself.
