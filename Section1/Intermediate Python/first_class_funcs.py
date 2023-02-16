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

# 3. Returning a function from a function:

def create_multiplier(factor):
    def multiplier(num):
        return num * factor
    return multiplier

double2 = create_multiplier(2)
triple = create_multiplier(3)

print(double2(5))  # Output: 10
print(triple(5))  # Output: 15

def outer(fac):
    def inner(num):
        return fac * num
    return inner

ans = outer(10)

print(ans(15))

# In summary, first-class functions in Python allow for more flexible and expressive code, making it easier to write reusable and composable code.

# More Examples


def html_tag(tag):
    def html_content(content):
        print(f'<{tag}>{content}<{tag}>')
    return html_content


html_h1 = html_tag('h1')
html_h1('Hello')


def mr_or_mrs(title):
    def your_name(name):
        print(f'{title} {name}')
    return your_name


Mrs = mr_or_mrs('Mrs')
Mrs('Bamidele')

Mr = mr_or_mrs('Mr')
Mr('Bamidele')
