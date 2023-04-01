# The normal tuple
# color = ('Red', 'Green', 'Blue')
# R = color[0]
# G = color[1]
# B = color[2]

# print(R, G, B)

# Named Tuples

# A named tuple is a subclass of tuple in Python that has named elements, which can be any valid Python identifier, instead of just accessing elements using indexes like regular tuples. Named tuples are like regular tuples, but they allow you to access the elements by name using dot(.) notation, instead of only using the index. Named tuples are also immutable, just like regular tuples, so you cannot modify their contents after creation.

# Here are two examples of how you can define a named tuple in Python:

# Example 1:

#from collections import namedtuple

# Define a named tuple type
#Point = namedtuple('Point', ['x', 'y'])
# The first parameter specifies the name of the new named tuple subclass that will be created

# Create an instance of the named tuple
#p = Point(x=1, y=2)

# Access the elements of the named tuple using dot notation
# print(p.x)  # Output: 1
# print(p.y)  # Output: 2


# Named tuples are a useful tool for creating simple, lightweight objects that represent data in a readable and self-documenting way. They are often used in cases where you need to store a small amount of related data, but you don't want to create a full-fledged class for that.


#Example 2:

from collections import namedtuple

color = namedtuple('color', ['Red', 'Green', 'Blue'])

Color = color(55, 155, 255)

print(Color.Red)