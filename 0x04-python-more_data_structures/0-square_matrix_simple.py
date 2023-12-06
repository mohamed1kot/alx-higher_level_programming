#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for lisst in matrix:
        new = []
        for num in lisst:
            new.append(num * num)
        new_matrix.append(new)
    return (new_matrix)
