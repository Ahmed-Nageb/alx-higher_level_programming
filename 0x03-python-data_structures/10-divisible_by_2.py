#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return my_list
    else:
        for num in my_list:
            if num % 2 == 0:
                num = True
            else:
                num = False
    return my_list
