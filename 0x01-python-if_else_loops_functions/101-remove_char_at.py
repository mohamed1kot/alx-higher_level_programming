#!/usr/bin/python3
def remove_char_at(str, n):
    length = len(str)
    new = []
    for num in range(length):
        if num == n:
            continue
        new.append(str[num])
    return ("".join(new))
