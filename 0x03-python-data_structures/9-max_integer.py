#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return None

    biggest = my_list[0]
    for x in range(len(my_list)):
        if my_list[x] > biggest:
            biggest = my_list[i]
    return (biggest)
