#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        devide = a / b
    except ZeroDivisionError:
        devide = None
    finally:
        print("Inside result: {}".format(devide))
        return devide
