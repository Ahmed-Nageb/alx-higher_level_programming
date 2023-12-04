#!/usr/bin/python3
def no_c(my_string):
    new_string = []
    for chr in my_string:
        if chr == 'c' or chr == 'C':
            continue
        new_string.append(str(chr))

    return str(new_string)
