#!/usr/bin/python3
"""Rectangle module that definesba square"""
from models.rectangle import Rectangle


"""define a class Square that inherits from Rectangle"""


class Square(Rectangle):
    """class constructor"""
    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns a string"""
        return ("[square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.width))

        @property
        def size(self):
            """retrieving the size of the square"""
            return self.width

        @size.setter
        def size(self, value):
            """setting the size of the square"""
            self.width = value
            self.height = value

        def update(self, *args, **kwargs):
            """update arguments for square instance"""
            dict_order = ['id', 'size', 'x', 'y']
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
        """returns the dictionary representation of a square"""
        dict_order = ['id', 'x', 'size', 'y']
        dict_attrs = {}
        for key in dict_order:
            dict_attrs[key] = getattr(self, key)
        return dict_attrs
