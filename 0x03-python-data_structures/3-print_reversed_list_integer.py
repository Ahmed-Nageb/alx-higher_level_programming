#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    counter = len(my_list)
    while (counter):
        print("{:d}".format(my_list[counter - 1]))
        counter -= 1
