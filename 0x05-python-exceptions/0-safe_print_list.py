#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for j in range(x):
            print("{}".format(my_list[i]), end="")
            i = i + 1
    except _:
        pass
    finally:
        print()
        return i
