#!/usr/bin/python3
def print_list_integer(my_list=[]):
    counter = 0
    while (counter < len(my_list)):
        print("{:d}".format(my_list[counter]))
        counter += 1
