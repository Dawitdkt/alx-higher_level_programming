#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    '''function that prints an integer.'''
    try:
        print("{:d}".format(value))
    except Exception as ex:
        sys.stderr.write("Exception: {}\n".format(ex))
        return False
    return True
