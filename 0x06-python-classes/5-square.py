#!/usr/bin/python3
"""Square class documentation."""


class Square:
    """This class defines a new square."""

    def __init__(self, size=0):
        """Instanciation of a new square object."""
        try:
            if type(size) is int:
                if size > -1:
                    self.__size = size
                else:
                    raise ValueError("size must be >= 0")
            else:
                raise TypeError('size must be an integer')
        except (ValueError, TypeError):
            raise

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        try:
            if type(value) is int:
                if value > -1:
                    self.__size = value
                else:
                    raise ValueError("size must be >= 0")
            else:
                raise TypeError('size must be an integer')
        except (ValueError, TypeError):
            raise

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
