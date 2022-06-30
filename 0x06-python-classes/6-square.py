#!/usr/bin/python3
"""Square class documentation."""


class Square:
    """This class defines a new square."""

    def __init__(self, size=0, position=(0, 0)):
        """Instanciation of a new square object."""
        try:
            if type(size) is int:
                if size > -1:
                    self.__size = size
                else:
                    raise ValueError("size must be >= 0")
            else:
                raise TypeError('size must be an integer')
        except Exception:
            raise

        err_msg = "position must be a tuple of 2 positive integers"
        try:
            if type(position) is tuple and len(position) == 2:
                for i in range(2):
                    if type(position[i]) is int and position[i] > -1:
                        pass
                    else:
                        raise TypeError
                # If there is no error, then we set the value of the attribute
                self.__position = position
            else:
                raise TypeError(err_msg)
        except TypeError:
            raise

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size of the square."""
        return self.__size

    @property
    def position(self):
        """Returns the position ef a square"""
        return self.__position

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        try:
            if type(value) is int:
                if value > -1:
                    self.__size = value
                else:
                    raise ValueError("size must be >= 0")
            else:
                raise TypeError('size must be an integer')
        except Exception:
            raise

    @position.setter
    def position(self, pos):
        err_msg = "position must be a tuple of 2 positive integers"
        try:
            if type(pos) is tuple and len(pos) == 2:
                for i in range(2):
                    if type(pos[i]) is int and pos[i] > -1:
                        pass
                    else:
                        raise TypeError
                # If there is no error, then we set the value of the attribute
                self.__position = pos
            else:
                raise TypeError(err_msg)
        except TypeError:
            raise

    def my_print(self):
        """Prints a square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
