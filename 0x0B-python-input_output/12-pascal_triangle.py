#!/usr/bin/python3
"""a function that returns a list of lists of integers representing"""


def pascal_triangle(n):
    """a function that returns a list of lists of integers representing.

     Args:
        n: number of lists
    """
    if n <= 0:
        return ([])
    L = []
    L.append([1])
    for length in range(1, n):
        new = []
        new.append(1)
        for i in range(1, length):
            try:
                new.append(L[length - 1][i - 1] + L[length - 1][i])
            except IndexError:
                pass
        new.append(1)
        L.append(new)
    return (L)
