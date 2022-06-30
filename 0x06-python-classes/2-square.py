#!/usr/bin/python3
"""Square class documentation."""


class Square:
    """This class defines a new square."""

    def __init__(self, size=0):
        """Instanciation of a new square object."""

        try:
            if type(size) is int:
                if size > -1:
                    self.__size = size  #: Size of the square
                else:
                    raise ValueError
            else:
                raise TypeError

        except ValueError:
            print("size must be >= 0")
        except TypeError:
            print("size must be an integer")
