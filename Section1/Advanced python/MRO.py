'''
    MRO (Method Resolution Order) is the order in which Python looks for methods and attributes in a hierarchy of classes. When a method or 
    ttribute is called on an object, Python searches for that method or attribute in the object's class, and then in the classes of all its 
    ancestors in the inheritance hierarchy.

    The MRO is determined by a depth-first search of the inheritance tree, where each class is visited once in the order specified by its list of 
    base classes. The order of base classes is specified using the super() function or by listing the base classes in the class definition.

    The MRO can be accessed using the built-in mro() method. For example, consider the following classes:

    ==> EXAMPLE:

class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass

    >>> D.mro()
    OUTPUT ==>  [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


This indicates that when Python looks for a method or attribute in an object of class D, it will first look in class D, then in class B (because B is the first base class listed in the definition of D), then in class C (because C is the second base class listed in the definition of D), then in class A (because A is the base class of both B and C), and finally in the base class object.

The MRO is important for resolving method and attribute lookup order in complex inheritance hierarchies. It ensures that methods and attributes are found in a consistent and predictable order, which helps prevent errors and makes debugging easier.

In addition to the mro() method, Python also provides the super() function, which allows a method to call the method of its parent class. The super() function uses the MRO to determine which method to call. 
    ==>Here's an example:
class A:
    def foo(self):
        print("A.foo")

class B(A):
    def foo(self):
        print("B.foo")
        super().foo()

class C(A):
    def foo(self):
        print("C.foo")
        super().foo()

class D(B, C):
    def foo(self):
        print("D.foo")
        super().foo()

d = D()
d.foo()

When the foo() method of object d is called, it prints "D.foo" and then calls super().foo(). Since the MRO of class D is [D, B, C, A, object], the super() function will call the foo() method of class B, which will in turn call the foo() method of class C, which will finally call the foo() method of class A. The output of this program will be:

D.foo
B.foo
C.foo
A.foo
'''


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





'''
    ==> STUDY THE BELOW also learn more on the super() function
class A:
    def m1(self):
        print('A method')
class B(A):
    def m1(self):
        print('B method')
class C(B):
    def m1(self):
        print('C method')
class D(C):
    def m1(self):
        print('D method')
class E(D):
    def m1(self):
        super(C, self).m1()
        
e = E()
e.m1()
'''