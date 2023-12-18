#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    index = 0
    counter = 0
    div_list = []

    while index is not list_length:
        try:
            div_list.append(my_list_1[index] / my_list_2[index])
            index += 1
        except ZeroDivisionError:
            div_list.append(0)
            index += 1
            print('division by 0')
            continue
        except TypeError:
            div_list.append(0)
            index += 1
            print("wrong type")
            continue
        except IndexError:
            div_list.append(0)
            index += 1
            print("out of range")
            continue
        finally:
            pass

    return div_list
