#!/usr/bin/python3
"""Student """


class Student:
    """Contains student """

    def __init__(self, first_name, last_name, age):
        """ initialize student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary of Student """

        if '__dict__' in dir(self):
            res = dict()
            can_filter = False
            if (type(attrs) is list) and all(type(s) is str for s in attrs):
                can_filter = True
            for key in self.__dict__.keys():
                if (not can_filter) or (can_filter and key in attrs):
                    res[key] = self.__dict__[key]
            return res

    def reload_from_json(self, json):
        '''Replaces all attributes of this Student instance with the
        key-value pairs in the given dictionary.
        Args:
            json (dict): A dictionary of new attributes for this student.
        '''
        if isinstance(json, dict) and ('__dict__' in dir(self)):
            for key in json.keys():
                self.__dict__[key] = json[key]
