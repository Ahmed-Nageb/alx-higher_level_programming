#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string.translate({ord(iter): None for iter in 'cC'})
    return new_string
