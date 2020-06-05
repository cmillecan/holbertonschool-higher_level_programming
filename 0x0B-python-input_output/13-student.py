#!/usr/bin/python3
""" Task 13 """


class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        """
        Instantiation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of Student.
        """
        if attrs is None:
            return self.__dict__
        else:
            new = {}
            for key in attrs:
                if key in self.__dict__:
                    new[key] = self.__dict__[key]
            return new

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.
        """
        for key in json:
            setattr(self, key, json[key])
