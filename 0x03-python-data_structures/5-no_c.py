#!/usr/bin/python3
def no_c(my_string):
    new_list = []
    iter = 0
    for iter in range(len(my_string)):
        if my_string[iter] not in 'cC':
            new_list.append(my_string[iter])
    return new_list
