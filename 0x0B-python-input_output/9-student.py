#!/usr/bin/python3
"""Student """


class Student:
    """Contains student """

    def __init__(self, first_name, last_name, age):
        """ initialize student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary of Student"""

        return self.__dict__
