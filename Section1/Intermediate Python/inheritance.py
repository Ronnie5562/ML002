
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
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
        return super().fullname() + f' Programming_languages: {self.prog_lang}'

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
dev_1 = Developer('Ronald', 'Abimbola', 120000, 'Python, C++, Java, R, Golang')

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
print(dev_1.fullname())
print(dev_1.full_info())
