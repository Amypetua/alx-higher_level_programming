#!/usr/bin/python3
"""python modules"""
import json
import csv
from collections import *
import turtle

"""define a Base class"""


class Base:
    """represents a Base"""
    


def __init__(self, id=None):
    """class constructor"""
    if id is not None:
        """assign the public instance attribute id to int value id"""
        self.id = id
    else:
        Base.__nb_objects += 1
        Base.__nb_objects = self.id

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts python list of dictionaries to a JSON-formatted string"""
        if list_dictionaries is None or bool(list_dictionaries) is False:
            return '[]'
        else:
            json_string = json.dumps(list_dictionaries)
            return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        """write or save JSON-formatted string list of objects to a file"""
        file_name = "{}.json".format(cls.__name__)
        list_dictionaries = []
        if list_objs is not None:
            for obj in list_objs:
                dictionary = obj.to_dictionary()
                list_dictionaries.append(dictionary)
            json_string = Base.to_json_string(list_dictionaries)
        with open(file_name, 'w') as f:
            if list_objs is None:
                f.write('[]')
            else:
                f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """converts JSON-formatted string to python list of objects"""

        if json_string is None or bool(json_string) is False:
            json_string = '[]'
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """update class Base and returns an instance with all attributes"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns instances of the calling class (cls) from a JSON file"""
        file_name = "{}.json".format(cls.__name__)
        instance_list = []
        try:
            with open(file_name, 'r') as f:
                json_string = f.read()
                dictionary_list = cls.from_json_string(json_string)
                for item in dictionary_list:
                    instance = cls.create(**item)
                    instance_list.append(instance)
        except FileNotFoundError:
            return instance_list
        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the instances of the calling class to a CSV file"""
        file_name = "{}.csv".format(cls.__name__)
        data = []
        if list_objs is not None:
            for obj in list_objs:
                dictionary = obj.to_dictionary()
                data.append(dictionary)
        rectangle_header = ['id', 'width', 'height', 'x', 'y']
        square_header = ['id', 'size', 'x', 'y']
        with open(file_name, mode='w') as f:
            if list_objs is None:
                f.write('[]')
            else:
                if cls.__name__ == 'Rectangle':
                    result = csv.DictWriter(f, field_names=rectangle_header)
                elif cls.__name__ == 'Square':
                    result = csv.DictWriter(f, field_names=square_header)
                result.writeheader()
                result.writerow(data)

    @classmethod
    def load_from_file_csv(cls):
        """Deserialization: read or load a list of objects from a CSV file"""
        file_name = "{}.csv".format(cls.__name__)
        instance_list = []

        try:
            with open(file_name) as f:
                result = csv.DictReader(f)
                for row in result:
                    row = dict(row)
                    for key in row:
                        row[key] = int(row[key])
                    instance = cls.create(**row)
                    instance_list.append(instance)
        except FileNotFoundError:
            return instance_list
        return instance_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """creates the shape with turtle module"""
        # open and set the turtle at the centre
        t.screen = turtle.getscreen()
        t = turtle.Turtle()

        # set the title of the window
        t.title("My first python turtle graphic window")

        # customize turtle and the screen background color
        t.shape("turtle")
        t.bgcolor("white")

        # customize pen for rectangle
        t.pen(pencolor="black", fillcolor="red", pensize=3, penspeed=5)
        # extract the data from the instance rectangle list
        for instance in list_rectangles:
            data = instance.to_dictionary()
            # set the position according to the rectangle object
            t.home()
            t.goto(data['x'], data['y'])
            # the drawing process
            t.pd()
            for i in range(2):
                t.forward(data['width'])
                t.left(90)
                t.forward(data['height'])
                t.left(90)
            t.pu()

        # customize pen for square
        t.pen(pencolor="yellow", fillcolor="green", pensize=2, penspeed=3)
        # extract the data from the instance square list
        for instance in list_squares:
            data = instance.to_dictionary()
            # set the position according to the square object
            t.home()
            t.goto(data['x'], data['y'])
            # the drawing process
            t.pd()
            for i in range(4):
                t.forward(data['size'])
                t.left(90)
                t.pu()

            # keeps window open
            t.getscreen()._root.mainloop()
