#!/usr/bin/python3
def no_c(my_string):
    new_str = [idx for idx in my_string if idx != 'c' and idx != 'C']
    return ("".join(new_str))
