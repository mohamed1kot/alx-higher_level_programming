#!/usr/bin/python3
def print_last_digit(number):
    last = 0
    if number >= 0:
        last = number % 10
        print("{:d}".format(number % 10), end= "")
    else:
        last = -number % 10
        print("{:d}".format(-number % 10), end= "")
        return(last)
