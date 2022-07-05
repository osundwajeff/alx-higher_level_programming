#!/usr/bin/python3
""" IO functions """


def write_file(filename="", text=""):
    """ write to file utf8 format
    Args:
        filename (str): name of file
        text (str): content to write to file
    Returns:
        int: number of chrachters written """
    n = 0
    with open(filename, mode="w", encoding="utf-8") as f:
        n = f.write(text)
