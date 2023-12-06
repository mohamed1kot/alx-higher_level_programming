#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    SUM = 0
    for num in my_list:
        if num not in new:
            new.append(num)
    for num in new:
        SUM += num
    return (SUM)
