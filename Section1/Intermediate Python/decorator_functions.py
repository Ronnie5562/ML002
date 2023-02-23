# Decorator is a function which can take a function as argument and extend its functionality and returns modified function with extended #functionality.

# The main objective of decorator functions is so that we can extend the functionality of existing functions without modifing the function.

def wish(name):
    print("Hello", name, "Good Morning")
# This function can always print same output for any name
# Hello Durga Good Morning
# Hello Ravi Good Morning
# Hello Sunny Good Morning
# But we want to modify this function to provide different message if name is Sunny.
# We can do this without touching wish() function by using decorator.


def decor(func):
    def inner(name):
        if name == "sunny":
            print("Hello sunny Bad morning")
        else:
            func(name)
    return inner


def wish(name):
    print(f'Hello {name} Good Morning')


greet = decor(wish)

greet('sunny')  # output: Hello sunny Bad morning
greet('Enny')  # Hello Enny Good Morning

# if you are confused with what is above, revisit ==> { Closures in python }
