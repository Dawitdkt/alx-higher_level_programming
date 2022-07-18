#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    '''function that executes a function safely.'''
    try:
        result = fct(*args)
    except Exception as ex:
        sys.stderr.write(f"Exception: {ex} \n")
        result = None
    return result
