#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    iter = 0
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    else:
        for iter in range(len(my_list)):
            new_list.append(my_list[iter])
        new_list[idx] = element
        return new_list
