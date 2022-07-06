#!/usr/bin/python3

def roman_to_int(roman_string):
    """Converts a roman numeral to an integer."""
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return (0)

    roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    num = 0
    N = len(roman_string)
    i = N-1

    while i >= 0:
        if i < N-1 and roman_dict[roman_string[i]] < roman_dict[roman_string[i+1]]:
            num -= roman_dict[roman_string[i]]
        else:
            num += roman_dict[roman_string[i]]
    return (num)
