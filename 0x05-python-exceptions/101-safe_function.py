#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        return (fct(*args))
    except BaseException as f:
        print("Exception: {}".format(f), file=sys.stderr)
        return (None)
