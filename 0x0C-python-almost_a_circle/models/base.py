#!/usr/bin/python3
""" Base class """
import json


class Base:
    """ Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries is []:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        if list_objs is None:
            my_list = []
        else:
            my_list = []
            for obj in list_objs:
                my_list.append(obj.to_dictionary())
        with open('{}.json'.format(cls.__name__), 'w') as f:
            f.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation """
        if json_string is None or json_string is []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == 'Rectangle':
            new = cls(1, 1)
            new.update(**dictionary)
            return new

        if cls.__name__ == 'Square':
            new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = '{}.json'.format(cls.__name__)
        try:
            with open(filename) as f:
                data = f.read()
            new_list = []
            for thing in cls.from_json_string(data):
                new_list.append(cls.create(**thing))
            return new_list
        except FileNotFoundError:
            return []
