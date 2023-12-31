#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = 0
    counter = 0

    while index is not x:
        try:
            print("{:d}".format(my_list[index]), end='')
            index += 1
            counter += 1
        except (TypeError, ValueError):
            index += 1
            continue
    print()
    return counter
