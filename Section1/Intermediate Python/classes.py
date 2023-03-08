# In object-oriented programming, a class is a blueprint for creating objects (a particular data structure), providing initial values for state 
# (member variables or attributes), and implementations of behavior (member functions or methods). An object is an instance of a class and is a
# real-world entity that has a state and behavior. When you create an object, you are creating a specific instance of a class, with its own values
#  for attributes and methods.

#import random
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @property
    def email(self):
        return f'{self.first}_{self.last}@email.com'

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.email)

# In the example above {Employee} is the class and both {emp_1} and {emp_2} are the instances[objects] of the Employee class.

# When you run :
            # {   print(emp_1.fullname())  } 
# on your computer, Here is what happens under the hood: 
            # {  print(Employee.fullname(emp_1))}
