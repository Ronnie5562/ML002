# Polymorphism in Python refers to the ability of objects to take on multiple forms. This means that objects of different classes can be treated 
# as if they were of the same class, allowing for more flexible and dynamic code. Polymorphism is achieved in Python through method overriding and 
# method overloading. Method overriding allows a subclass to provide its own implementation of a method already defined in its superclass, while 
# method overloading allows multiple methods with the same name but different parameters to coexist within the same class. This enables Python
# code to be more modular and easier to maintain.



# class Book:
#     def __init__(self, pages):
#         self.pages = pages

# b1 = Book(500)
# b2 = Book(375)

# result = b1 + b2
# print(result) # This throws an error, but look at the code below and notice the difference.

class Book:
    def __init__(self, pages):
        self.pages = pages
    
    def __add__(self, other):
        return self.pages + other.pages
    
    def __mul__(self, other):
        return self.pages * other.pages
    
    def __sub__(self, other):
        return abs(self.pages - other.pages)


b1 = Book(500)
b2 = Book(700)

add_result = b1 + b2
mul_result = b1 * b2
sub_result = b1 - b2

print(add_result)
print(mul_result)
print(sub_result)

# The following is the list of operators and corresponding magic methods.

# + -- -> object.__add__(self, other)
# - -- -> object.__sub__(self, other)
# * -- -> object.__mul__(self, other)
# / -- -> object.__div__(self, other)
#{}  // -- -> object.__floordiv__(self, other)
# % -- -> object.__mod__(self, other)
# ** -- -> object.__pow__(self, other)
# += -- -> object.__iadd__(self, other)
# -= -- -> object.__isub__(self, other)
# *= -- -> object.__imul__(self, other)
# /= -- -> object.__idiv__(self, other)
#{}  //= -- -> object.__ifloordiv__(self, other)
# %= -- -> object.__imod__(self, other)
# **= -- -> object.__ipow__(self, other)
# < -- -> object.__lt__(self, other)
# <= -- -> object.__le__(self, other)
# > -- -> object.__gt__(self, other)
# >= -- -> object.__ge__(self, other)
# == -- -> object.__eq__(self, other)
# != -- -> object.__ne__(self, other)


# Program to overload multiplication operator to work on Employee objects:

class Employer:
    def __init__(self, name, wage):
        self.name = name
        self.wage = wage

    def __mul__(self, other):
        return self.wage * other.days

class Timesheet:
    def __init__(self, name, days):
        self.name = name
        self.days = days


E = Employer('Ronald', 300000)
T = Timesheet('Ronald', 24)

This_month_salary =  E * T

print(f'This monh salary: {This_month_salary}')


# There is a limitation to all the codes above, guess what's that?
# The overloading methods - e.g {__add__(self)} can only add two variables of a class. When we input three, it throws an error
#To solve this problem, we have to modify the methods. ==> Check the code below


class Book:
    def __init__(self, pages) -> None:
        self.pages = pages
        
        # Keep an eye on the code directly below this and notice the difference
    def __add__(self, other):
        result = self.pages + other.pages
        b = Book(result)
        return b
    # The code above adds up the number of pages in each Book instance that is added with the '+' operator
    
    def __str__(self):
        return f'The total number of pages you are to read is: {self.pages}. You can do it, bro 💪'

book1 = Book(200)
book2 = Book(400)
book3 = Book(600)

Total_pages = book1 + book2 + book3

print(Total_pages)

# Confused?
# Watch: Advanced Python || Operator Overloading Part - 2 || by Durga On 26-07-2018 - on Youtube


# More examples

class Employee:
    def __init__(self, name, wage) -> None:
        self.name = name
        self.wage = wage

    def __mul__(self, other):
        if self.name == other.name:
            return f"{self.name}'s salary for this month is: ${self.wage * other.days}"
        else:
            return "You cannot multiply an employee's salary with another emplooyee TimeSheet"

class TimeSheet:
    def __init__(self, name, days):
        self.name = name
        self.days = days

Employee1 = Employee('Ronald', 500)
Days = TimeSheet('Ronald', 25)

print(Employee1 * Days)


# Method overriding:
# What ever members available in the parent class are bydefault available to the child class through
# inheritance. If the child class not satisfied with parent class implementation then child class is
# allowed to redefine that method in the child class based on its requirement. This concept is called
# overriding.
# Overriding concept applicable for both methods and constructors  -- durga

# Example:
