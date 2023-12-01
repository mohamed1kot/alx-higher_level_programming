#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lisst in matrix:
        l = (len(lisst) - 1)
        for num in lisst:
            if l == 0:
                print("{:d}".format(num), end="")
            else:
                print("{:d}".format(num), end=" ")
            l -= 1
        print()

