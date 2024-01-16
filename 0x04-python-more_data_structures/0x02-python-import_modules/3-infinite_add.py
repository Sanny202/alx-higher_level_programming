#!/usr/bin/python3
import sys
if __name__ == "__main__":
    ln = len(sys.argv)
    tally = 0
    for i in range(1, ln):
        tally += int(sys.argv[i])
    print(tally)
