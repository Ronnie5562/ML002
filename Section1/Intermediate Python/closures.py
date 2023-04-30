# In Python, a closure is a function object that has access to variables in its enclosing lexical scope, even after the outer function has completed execution.
# Essentially, it's a way to "remember" and continue to access the values of variables from an outer function.

# To create a closure in Python, you need to define a function inside another function. The inner function can then access and modify the variables in the outer
# function's scope. Here's an example:


def outer_func(x):
    def inner_func(y):
        return x + y

    return inner_func


closure = outer_func(10)
print(closure(5))  # Output: 15


# In this example, outer_func takes an argument x and returns an inner function inner_func. inner_func takes an argument y and returns the sum of x and y.

# When we call outer_func(10), it returns inner_func, which we then assign to the variable closure. We can then call closure(5), which will use the value of x from the
# outer function and add it to y to give us a result of 15.

# Since the value of x is remembered by the inner function even after the outer function has completed execution, we can use the closure to perform operations that
# depend on some context that is captured by the closure.

# Closures can be used in a variety of ways, such as implementing decorators or creating functions with partially applied arguments.


# More on closures
# Write a code the stores the surname of a family and adds it to name of each member of the family. {implement in using closures}


def surname(family_name):
    def first_name(personal_name):
        return f"{family_name} {personal_name}"

    return first_name


each_member = surname("Johnson")

# Dad
print(each_member("Richards"))

# Mum
print(each_member("Sophia"))

# Daughter
print(each_member("Lizzy"))
# Son
print(each_member("Einstein"))
