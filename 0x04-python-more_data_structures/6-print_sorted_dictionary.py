#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary)
    for element in sorted_dict:
        print("{}: {}".format(element, a_dictionary[element]))
