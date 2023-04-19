#!/usr/bin/python3
"""Write a class Rectangle that defines a rectangle"""


class Rectangle:
    """A class that represents a rectangle"""
    def __init__(self, width=0, height=0):
        """initialize class Rectangle private instance attributes"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieving and setting the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieving and setting the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

        def __str__(self):
            if self.__width == 0 or self.__height == 0:
                return ("")

            rectangle = ""
            for col in range(self.__height):
                for row in range(self.__width):
                    rectangle += "#"
                if col < self.__height - 1:
                    rectangle += "\n"
            return (rectangle)
