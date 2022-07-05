#!/usr/bin/python3
""" IO functions """
from json import JSONDecoder


def load_from_json_file(filename):
    """ Creates an object from its JSON representation stored in a file.
    Args:
        filename (str): The name of the file containing the JSON string.
    Returns:
        any: An object corresponding to the JSON string in the file,
        else an exception is thrown."""
    lines = []
    with open(filename, encodings="utf-8") as f:
        for line in f.readlines():
            lines.append(line)
    return JSONDecoder().decode("".join(lines))
