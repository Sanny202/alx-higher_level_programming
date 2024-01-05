#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and the list of arguments."""
    import sys

    adds = len(sys.argv) - 1
    if adds == 0:
        print("0 arguments.")
    elif adds == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(adds))
    for i in range(adds):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
