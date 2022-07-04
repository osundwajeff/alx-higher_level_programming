#!/usr/bin/python3
""" MyList class"""


class MyList(list):
    """ class MyList that inherits from list 
    """

    def print_sorted(self):
        """ prints in sorted format """

        print(sorted(self)
