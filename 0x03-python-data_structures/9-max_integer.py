#!/usr/bin/python3
def max_integer(my_list=[]):
    MAX = my_list[0]
    for num in my_list:
        if num > MAX:
            MAX = num
    return (MAX)
