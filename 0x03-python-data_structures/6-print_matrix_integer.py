#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for iter0 in matrix:
        for iter1 in iter0:
            print("{}".format(iter1), end="\t")
        print()
