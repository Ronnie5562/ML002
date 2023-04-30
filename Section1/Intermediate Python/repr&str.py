# __repr__ and __str__ are special methods in Python that allow classes to define how instances of that class are represented as strings. Both
# methods return string representations of objects, but they are used in different contexts and have different default implementations.

# __repr__:

# The __repr__ method is used to provide a string representation of the object that is unambiguous and typically used for debugging and development
# purposes. When you type an object's name in the Python interpreter, it will call its __repr__ method to print a string representation of the
# object.
# This method is also used by the built-in repr() function.

# If a class does not define a __repr__ method, Python will use the default implementation which returns a string that looks like < __main__.MyClass
# object at 0x7f4c6d36b7f0 > where MyClass is the name of the class and the hexadecimal value represents the object's memory address.

# __________________________________________________________________
# Here is an example of defining __repr__ method for a simple class:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"


# In this example, we have defined a Person class with a name and an age attribute. The __repr__ method returns a string representation of the
# Person object using the f-string syntax, which allows us to embed the values of the name and age attributes in the string. The resulting string
# looks like this: Person(name='John', age=30).

# __str__:

# The __str__ method is used to provide a more user-friendly string representation of the object. This method is called by the built-in print()
# function and when you use the str() function to convert an object to a string.

# If a class does not define a __str__ method, Python will use the __repr__ method as a fallback, so it's often a good idea to define both methods
# for a class .

# Here is an example of defining __str__ method for a simple class:


class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

    def __str__(self):
        return f"{self.name}, {self.age} years old"


# In this example, we have defined both __repr__ and __str__ methods for the Person class . The __str__ method returns a string representation that
#  is more user-friendly than the __repr__ method. The resulting string looks like this: John, 30 years old.

# To summarize, __repr__ is used to provide an unambiguous string representation of an object, usually for debugging and development purposes.
#  __str__ is used to provide a more user-friendly string representation of an object. It's often a good idea to define both methods for a class,
# but if only one method is defined, Python will use it for both purposes.
