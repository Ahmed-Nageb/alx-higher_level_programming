#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0

    while counter is not x:
        try:
            print(my_list[counter], end='')
            counter += 1
        except IndexError:
            break

    print()
    return counter
