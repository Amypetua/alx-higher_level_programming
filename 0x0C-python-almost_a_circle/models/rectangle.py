#!/usr/bin/python3

"""defines a Rectangle module"""
from models.base import Base

"""defines a Rectangle class"""


class Rectangle(Base):
    """private instance attributes with its own public getter and setter"""
    __width -> width
    __height -> height
    __x -> x
    __y -> y
    """class constructor"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # Retrieve or getter and setter of width
    @property
    def width(self):
        """retrieving the size of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the size of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    # Retrieve or getter and setter of height
    @property
    def height(self):
        """retrieving the size of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the size of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    # Retrieve or getter and setter of x
    @property
    def x(self):
        """retrieving the size of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting the size of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    # Retrieve or getter and setter of y
    @property
    def y(self):
        """retrieving the size of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setting the size of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """return the area of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """prints out in stdout the Rectangle instance with the character #"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + self.width * '#')

    def __str__(self):
        """overriding the str method"""

        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """changes order of arguments for the Rectangle instance"""
        dict_order = ['id', 'width', 'height', 'x', 'y']
        if args is not None and bool(args) is True:
            i = 0
            for key in dict_order:
                try:
                    setattr(self, key, args[i])
                except IndexError:
                    pass
                i += 1
        else:
            for key in dict_order:
                try:
                    setattr(self, key, kwargs[key])
                except KeyError:
                    pass

        def to_dictionary(self):
            """returns a dictionary with attributes of the instance"""
            dict_order = ['x', 'y', 'id', 'height', 'width']
            dict_attrs = {}
            for key in dict_order:
                dict_attrs[key] = getattr(self, key)
            return dict_attrs
