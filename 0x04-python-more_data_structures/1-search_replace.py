#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list."""
    result = []
    for elm in my_list:
        if elm == search:
            result.append(replace)
        else:
            result.append(elm)
    return result
