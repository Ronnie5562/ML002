import random
class Employee:

    
    def __init__(self, first, last, pay, Employees=None):
        self.first = first
        self.last = last
        self.email = f'{first}_{last}{random.randint(100, 999)}@email.com'
        self.pay = pay
        if Employees == None:
            self.Employees = []
        else:
            self.Employees = Employees



    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def add_emp(self, emp):
        if emp not in self.Employees:
            self.Employees.append(emp)
    
    # def __repr__(self):
    #     return f"Employee('{self.first}', '{self.last}', {self.pay})"

    # def __str__(self):
    #     return f"{self.fullname()} - {self.email}"


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_1_1 = Employee('Test', 'Employee', 60000)
emp_1_2 = Employee('Exam', 'Student', 30000)


emp_1.add_emp(emp_1_1)
emp_1.add_emp(emp_1_2)

print(emp_1.Employees)
print(emp_1_1.Employees)

# for employ in emp_1.Employees:
#     print(employ.fullname())