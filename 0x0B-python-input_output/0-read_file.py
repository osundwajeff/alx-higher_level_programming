#!/usr/bin/python3
""" function that reads text files """


def read_file(filename=""):
    """ read file in utf8 format and print to stdout."""
    with(filename, encoding="utf8") as f:
        print(f.read(), end="")
