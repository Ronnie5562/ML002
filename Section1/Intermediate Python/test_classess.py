import unittest
from classes import Employee

class Testclasses(unittest.TestCase):

    def setup(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_email(self):
        emp_1 = Employee('Corey', 'Schafer', 50000)
        emp_2 = Employee('Test', 'Employee', 60000)

        self.assertEqual(emp_1.email, 'Corey_Schafer@email.com')
        self.assertEqual(emp_2.email, 'Test_Employee@email.com')

        emp_1.first = 'Star'
        emp_2.first = 'Real'

        self.assertEqual(emp_1.email, 'Star_Schafer@email.com')
        self.assertEqual(emp_2.email, 'Real_Employee@email.com')
    
    def test_fullname(self):
        emp_1 = Employee('Corey', 'Schafer', 50000)
        emp_2 = Employee('Test', 'Employee', 60000)

        self.assertEqual(emp_1.fullname, 'Corey Schafer')
        self.assertEqual(emp_2.fullname, 'Test Employee')

        emp_1.first = 'Star'
        emp_2.first = 'Real'

        self.assertEqual(emp_1.fullname, 'Star Schafer')
        self.assertEqual(emp_2.fullname, 'Real Employee')
        




print(name('tot'))

if __name__ == '__main__':
    unittest.main()
    