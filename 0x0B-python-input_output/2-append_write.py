#!/usr/bin/python3
""" IO function """


def append_write(filename="", text=""):
    """ Appends file in utf-8 format.
    Args:
        filename (str): The name of the file to write to.
        text (str): The content to store in the file.
    Returns:
        int: The number of characters written."""
    n = 0
    with open(filename, mode='a', encoding='utf-8') as f:
        n = f.write(text)
    return n
