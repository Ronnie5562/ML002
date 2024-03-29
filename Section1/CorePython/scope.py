"""
L -> E -> G -> B ✅
B -> E -> G -> L ❌

Local, Enclosing, Global, Built-in.
    Local - Variables defined inside a functon.
    Enclosing - Variables in a function - which is inside another function
    Global - Variables defined at the top level of a module.
    Built-in - Variables that are pre-defined in python.
"""

x = "global x"


def scope():
    global z
    z = "global z"
    y = "local y"
    # print(x) ==> it throws an error ❌❌❌
    print(y)
    print(z)


# Without calling the scope function, { Z } remains local
scope()

print(x)
# print(y) ==> it throws an error ❌❌❌
print(z)

# To check all the built-in funcs and variables in python
import builtins

print(dir(builtins))  # output - All built-ins in python.

# Enclosing scope


def outer():
    x = "outer x"
    u = "outer u"

    def inner():
        # To create a variable that is global within the inner function and the outer function use: { nonlocal } key-word to craete the variable.
        nonlocal u
        u = "nonlocal u"
        x = "inner x"
        print(x)

    inner()
    print(x)


outer()

import sys

print(sys.executable)
