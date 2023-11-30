#!/usr/bin/python3
import sys

if __name__ == "__main__":
    count = 0
    SUM = 0
    for arg in sys.argv:
        if count > 0:
            SUM += int(arg)
        count += 1
    print(SUM)
