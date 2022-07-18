#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    '''function that prints an integer.'''
    try:
        print("{:d}".format(value))
    except ValueError as ex:
        sys.stderr.write(f"Exception: {ex} \n")
        return False
    return True
