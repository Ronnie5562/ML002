#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """A class that defines a square"""
    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """property(get&set) for the current size of the square."""
        return self.__size
    
    @size.setter
    def size(self, value):
        if (not isinstance(value, int) and not isinstance(value, float)):
            raise TypeError('size must be a number')
        if (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = value
    
    def area(self):
        """Returns the area of the current square."""
        return (self.__size**2)
    
    def __eq__(self, other_square):
        """Returns the == comparision to a Square."""
        return self.area() == other_square.area()

    def __ne__(self, other_square):
        """Returns the != comparison to a Square."""
        return self.area() != other_square.area()

    def __lt__(self, other_square):
        """Returns the < comparison to a Square."""
        return self.area() < other_square.area()

    def __le__(self, other_square):
        """Returns the <= comparison to a Square."""
        return self.area() <= other_square.area()

    def __gt__(self, other_square):
        """Returns the > comparison to a Square."""
        return self.area() > other_square.area()

    def __ge__(self, other_square):
        """Returns the >= compmarison to a Square."""
        return self.area() >= other_square.area()


s_5 = Square(5)
s_6 = Square(6)

if s_5 < s_6:
    print("Square 5 < Square 6")
if s_5 <= s_6:
    print("Square 5 <= Square 6")
if s_5 == s_6:
    print("Square 5 == Square 6")
if s_5 != s_6:
    print("Square 5 != Square 6")
if s_5 > s_6:
    print("Square 5 > Square 6")
if s_5 >= s_6:
    print("Square 5 >= Square 6")