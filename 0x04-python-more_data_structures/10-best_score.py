#!/usr/bin/python3
def best_score(a_dictionary):
    big_k = None
    big_v = 0
    if a_dictionary:
        for key, value in a_dictionary.items():
            if value > big_v:
                big_v = value
                big_k = key
    else:
        return (None)
    return (big_k)
