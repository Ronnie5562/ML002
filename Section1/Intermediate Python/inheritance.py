import random
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f'{first}_{last}{random.randint(100, 999)}@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

# super() is used to refer to the class we inherit from
class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
    
    def full_info(self):
        return f'Name: {super().fullname()}. Email: {self.email}. Programming_languages: {self.prog_lang}'


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees
    

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def print_emp(self):
        for emp in self.employees:
            print()
            print('==>', emp.full_info())
            print()
        
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)




emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
dev_1 = Developer('Ronald', 'Abimbola', 500000, 'Python, C++, Java, R, Golang, Solidity.')
dev_2 = Developer('Julius', 'Drake', 300000, 'Python, C++, Golang, Javascript.')
dev_3 = Developer('Charlotte', 'Johnson', 500000, 'C, Java, Javascript, Flutter.')
dev_4 = Developer('Joy', 'James', 300000, 'Python, Flutter, Rust, Javascript.')

mgr_1 = Manager('Larry', 'Page', '1000000', [dev_1])
mgr_1.add_emp(dev_2)
mgr_1.add_emp(dev_3)
mgr_1.add_emp(dev_4)

print(mgr_1.employees[0].full_info())
mgr_1.print_emp()

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
print(dev_1.fullname())
print(dev_1.email)

# Python has this two methods that works with classes -- {isinstance() and issubclass()} They return either True or False.

print(isinstance(dev_1, Developer)) #Expected Output: True
print(isinstance(emp_1, Developer)) # Expected Output: False
print(isinstance(emp_2, Employee))  # Expected Output: True
print(isinstance(dev_2, Employee))  # Expected Output: True

print('_____________________________')

print(issubclass(Developer, Employee))  # Expected Output: True
print(issubclass(Manager, Developer))  # Expected Output: False
print(issubclass(Manager, Employee))  # Expected Output: True
print(issubclass(Employee, Developer))  # Expected Output: False
