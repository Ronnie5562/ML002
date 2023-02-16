# In Python, functions are first-class objects, which means that they can be assigned to variables, passed as arguments to other functions, and 
# returned as values from functions.

# This enables several powerful programming paradigms such as functional programming, where functions are treated as values and can be composed to 
# create more complex behavior.

# Here are some examples of using first-class functions in Python:

# 1. Assigning a function to a variable:

def greet(name):
    print(f'hello {name}')


greeting = greet

greeting('Star Boy')

# 2. Passing a function as an argument:


def apply(func, value):
    return func(value)

def double(num):
    return num * 2

result = apply(double, 5)
print(result)