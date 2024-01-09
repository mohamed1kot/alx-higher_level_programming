#!/usr/bin/python3
""" a function that writes a string to a text file """


def write_file(filename="", text=""):
    """
     function that writes a string to a text file (UTF8)
     and returns the number of characters written
     Args:
        filename: the name of file will write the ext in this file
        text: the text will wrie it
    """
    with open(filename, "w", encoding="utf-8") as file:
        writer = file.write(text)
        return (writer)
