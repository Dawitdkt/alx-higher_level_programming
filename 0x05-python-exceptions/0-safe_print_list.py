#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    
    """Prints x elements of a list."""
    leng = 0
    try:
        for i in range(x):
            print(my_list[i],end="")
            leng+=1
            
        print(end="\n")
        
    except IndexError:
        print(end="\n")
    
    
    
    return leng
