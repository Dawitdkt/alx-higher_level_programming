#!/usr/bin/python3

def safe_print_division(a, b):
    '''divides 2 integers and prints the result.'''
    result = 0
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print(f"Inside result: {result}")
    return result
