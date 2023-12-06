#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    if len(tuple_b) >= 2:
        tuple_b = tuple_b[:2]
    elif len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)
    else:
        tuple_b = (0, 0)
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (new_tuple)