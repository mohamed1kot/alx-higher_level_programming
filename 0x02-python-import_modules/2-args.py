#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc == 1:
        print(f"{argc - 1} arguments.")
    else:
        print(f"{argc - 1} arguments:")
        count = 0
        for i in sys.argv:
            if count > 0:
                print(f"{count}: {i}")
            count +=1
