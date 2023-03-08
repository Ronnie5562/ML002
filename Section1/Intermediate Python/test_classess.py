import unittest
from classes import Employee
from unittest.mock import patch

class Testclasses(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Test', 'Employee', 60000)
    
    def tearDown(self):
        pass
    
    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Corey_Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Test_Employee@email.com')

        self.emp_1.first = 'Star'
        self.emp_2.first = 'Real'

        self.assertEqual(self.emp_1.email, 'Star_Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Real_Employee@email.com')
    
    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Test Employee')

        self.emp_1.first = 'Star'
        self.emp_2.first = 'Real'

        self.assertEqual(self.emp_1.fullname, 'Star Schafer')
        self.assertEqual(self.emp_2.fullname, 'Real Employee')

    def test_monthly_schedule(self):
        with patch('classes.urllib.request.urlopen') as moked_get:
            moked_get.return_value.ok = True
            moked_get.return_value.text = 'success'

            schedule = self.emp_1.monthly_schedule('May')
            moked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'success')
        


print(dir(Testclasses)) # It contains the list of asserts you can use.

if __name__ == '__main__':
    unittest.main()
    