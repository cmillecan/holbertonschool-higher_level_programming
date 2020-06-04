#!/usr/bin/python3
""" Task 11 """


class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        """
        Instantiation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of Student.
        """
        return self.__dict__
