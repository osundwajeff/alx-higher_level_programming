#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argc = len(argv)
    index = 1
    if argc == 0:
        print("{:D} argumnets.".format(argc))
    elif argc == 1:
        print("{:d} arguments:".format(argc))
        print("{:d}: {:s}".format(index, sys.argv[1]))
    else:
        print("{:d} arguments:".format(argc))
        while index <= argc:
            print("{:d}: {:s}".format(index, sys.argv[index]))
            index += 1
