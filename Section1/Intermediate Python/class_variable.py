# In Python, class variables are variables that are shared among all instances of a class . Class variables are defined within the class definition,
# but outside of any method. They are referenced using the class name, rather than an instance of the class . Class variables are usually used to
# store values that are common to all instances of a class, such as constants or default values for attributes.

# Here's an example of how you can define and use class variables in Python:

# class Car:
#     wheels = 4  # class variable

#     def __init__(self, make, model):
#         self.make = make
#         self.model = model


# Access the class variable using the class name
#print(Car.wheels)  # Output: 4

# Create an instance of the class
#my_car = Car("Toyota", "Camry")

# Access the class variable through the instance
#print(my_car.wheels)  # Output: 4

# Change the value of the class variable
#Car.wheels = 5

# The change is reflected in all instances of the class
#print(my_car.wheels)  # Output: 5

# It's important to note that class variables are shared by all instances of a class, so if you modify the value of a class variable, the change
# will be reflected in all instances. On the other hand, instance variables are unique to each instance and are used to store values that are
# specific to a particular instance.

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



emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)


print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
