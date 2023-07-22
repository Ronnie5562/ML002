"""Define a class Square."""

class Square:
    """A class that defines a square"""

    def validate(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        Square.validate(self, size)
        
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
       Square.validate(self, value)

    def area(self):
        """Public instance method that returns the current square area"""
        return (self.__size**2)