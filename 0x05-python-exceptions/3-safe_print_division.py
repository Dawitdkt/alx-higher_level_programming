#!/usr/bin/python3

from decimal import DivisionByZero


def safe_print_division(a, b):
    '''divides 2 integers and prints the result.'''
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        result =  None
    finally:
        print(f"Inside result: {result}")
    
    return result
