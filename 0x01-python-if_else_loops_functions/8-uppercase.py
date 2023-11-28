#!/usr/bin/python3
def uppercase(str):
    for i in str:
        var =0
        if ord(i) >= 97 and ord(i) <= 122:
            var = 32
        else:
            var = 0
        print("{:c}".format(ord(i) - var), end= "")
    print()
