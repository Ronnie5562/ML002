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
# print(Car.wheels)  # Output: 4

# Create an instance of the class
# my_car = Car("Toyota", "Camry")

# Access the class variable through the instance
# print(my_car.wheels)  # Output: 4

# Change the value of the class variable
# Car.wheels = 5

# The change is reflected in all instances of the class
# print(my_car.wheels)  # Output: 5

# It's important to note that class variables are shared by all instances of a class, so if you modify the value of a class variable, the change
# will be reflected in all instances. On the other hand, instance variables are unique to each instance and are used to store values that are
# specific to a particular instance.


class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@email.com"
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @classmethod
    def raise_amount(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "Employee", 60000)


print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)

print(new_emp_1.email)
print(new_emp_1.pay)
print(Employee.num_of_emps)

# static method
# In Python, a static method is a method that belongs to a class rather than an instance of the class. Static methods are defined using the @staticmethod decorator and
# are called using the class name, rather than an instance of the class. They do not have access to the instance of the class and do not modify the instance data.
# Static methods are usually used for utility functions that do not depend on the state of the instances.

# Here's an example of how you can define and use static methods in Python:


class Math:
    @staticmethod
    def add(a, b):
        return a + b


# Call the static method using the class name
result = Math.add(1, 2)
print(result)  # Output: 3

# Static methods are useful in cases where you want to define a function that is logically associated with a class, but you do not need to access the instance data. They
# provide a way to encapsulate the function within the class, making the code more organized and easier to maintain.

#                                                       _______________{    SUMMARY 🔥   }________________
# Static methods and class methods are both methods that belong to a class rather than an instance of the class in Python. Here are the differences and similarities
# between static methods and class methods:

# Differences:

# Access to the instance: Static methods do not have access to the instance of the class and do not take the instance as an argument. Class methods, on the other hand,
# take the class itself as the first argument, which is usually named cls.

# Purpose: Static methods are usually used for utility functions that do not depend on the state of the instances and do not modify the instance data. Class methods are
# usually used for factory methods, which are methods that return instances of the class , or for methods that modify class-level state and behavior.

# Similarities:

# Definition: Both static methods and class methods are defined using the @ staticmethod and @classmethod decorators, respectively.

# Call: Both static methods and class methods are called using the class name, rather than an instance of the class .

# Purpose: Both static methods and class methods provide a way to encapsulate the function within the class , making the code more organized and easier to maintain.

# In summary, the key difference between static methods and class methods is the access they have to the instance and the purpose they serve. Static methods are used for
# utility functions that do not depend on the state of the instances, while class methods are used for factory methods and methods that modify class -level state and
# behavior.
