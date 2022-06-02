#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argc = len(argv)
    index = 1
    add = 0

    while index <= argc:
        add += int(sys.argv[index])
        index += 1
    print("{:d}".format(add))
