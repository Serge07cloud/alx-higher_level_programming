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
