#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set()
    for num in set_1:
        if num not in set_2:
            new_set.add(num)
    for num in set_2:
        if num not in set_1:
            new_set.add(num)
    return (new_set)
