#!/usr/bin/python3
"""a function that reads a text file"""


def read_file(filename=""):
    """
     a function that reads a text file (UTF8) and prints it to stdout

     Args:
        filename : defult argument equal "".
    """
    with open(filename, "r", encoding="UTF8") as file:
        reader = file.read()
        print(reader, end="")
