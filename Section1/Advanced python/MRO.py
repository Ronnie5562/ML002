class P:
    pass

class C(P):
    pass

print(C.mro()) # OUTPUT: [<class '__main__.C'>, <class '__main__.P'>, <class 'object'>]

# Explain < class 'object' > which is in the output above.

# In Python, object is the base class for all other classes. It is the root of the class hierarchy, and every class in Python is ultimately derived from object. This means that object is the most basic class in Python, and it provides the default implementation for some fundamental methods that are necessary for every Python object.

# The object class is defined in the built-in __builtin__ module, and it has several methods that can be overridden by derived classes, including:

# __init__(self): The constructor method, which is called when an object is created.
# __str__(self): The string representation of the object, which is used by the str() function and the print statement.
# __repr__(self): The string representation of the object, which is used by the repr() function and the interactive interpreter.
# Since every class is ultimately derived from object, it means that all classes have access to these fundamental methods. This allows Python to have a consistent and unified object model, which is one of the reasons why Python is so popular and easy to use.
