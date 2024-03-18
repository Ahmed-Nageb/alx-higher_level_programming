#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for iter0 in matrix:
        for iter1 in iter0:
            print("{:d}".format(iter1), end=" " if iter1 != iter0[-1] else "")
        print()
