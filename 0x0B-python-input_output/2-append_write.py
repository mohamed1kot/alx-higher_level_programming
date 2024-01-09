#!/usr/bin/python3
"""a function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """
    a function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Args:
        filename: the file will be created.
        text: the text will be write it in this file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        append = file.write(text)
        return (append)
