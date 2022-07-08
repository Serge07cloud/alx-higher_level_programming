#!/usr/bin/python3
"""Rectangle class documentation."""


class Rectangle:
    """This class define a new rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        try:
            if type(value) is int:
                if value > -1:
                    self.__width = value
                else:
                    raise ValueError("width must be >= 0")
            else:
                raise TypeError("width must be an integer")
        except Exception:
            raise

    @height.setter
    def height(self, value):
        try:
            if type(value) is int:
                if value > -1:
                    self.__height = value
                else:
                    raise ValueError("height must be >= 0")
            else:
                raise TypeError("height must be an integer")
        except Exception:
            raise

    def area(self):
        """This method returns the rectangle area."""
        return self.__height * self.__width

    def perimeter(self):
        """This method returns the perimeter of a rectangle."""
        if self.__width != 0 and self.__height != 0:
            return (self.__height + self.__width) * 2
        else:
            return 0

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __str__(self):
        if self.__width != 0 and self.__height != 0:
            out = None
            for i in range(self.__height):
                for j in range(self.__width):
                    print(self.print_symbol, end="")
                if i != self.__height - 1:
                    print()
        return ""

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
