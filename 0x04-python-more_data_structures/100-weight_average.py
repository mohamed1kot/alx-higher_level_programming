#!/usr/bin/python3
def weight_average(my_list=[]):
    Numerator = 0
    denominator = 0
    if my_list:
        for tup in my_list:
            Numerator += tup[0] * tup[1]
            denominator += tup[1]
        return (Numerator / denominator)
    return (0)
