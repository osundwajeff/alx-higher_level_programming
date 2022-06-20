#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        lst = 0
        while lst < x:
            print("{}".format(my_list[lst], end = "")
            lst += 1
        print("")
        return (lst)
    except IndexError:
        print("")
        return (lst)
        pass
