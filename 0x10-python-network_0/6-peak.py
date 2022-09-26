#!/usr/bin/python3
""" finds a peak in a list of unsoerted integers """


def find_peak(list_of_integers):
    """ finds peak.
    Args:
        list_of_intergers (list): list of integers.
    """
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
