#!/usr/bin/python3
"""a function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """
     a function that inserts a line of text to a file
     after each line containing a specific string

     Args:
        filename: the file will read and write from it.
        search_string : the string will search about it in the filename
        new_string: the new string will added after the lines.
    """
    with open(filename, "r") as f:
        L = f.readlines()

    with open(filename, "w") as f:
        string = ""
        for line in L:
            string += line
            if search_string in line:
                string += new_string
        f.write(string)
