#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > 1 and len(tuple_b) > 1:
        new_tuple = (int(tuple_a[0]) + int(tuple_b[0]), int(tuple_a[1] + int(tuple_b[1])))
    elif len(tuple_a) == 1 and len(tuple_b) > 1:
        tuple_ar = tuple_a + (0,)
        new_tuple = (int(tuple_ar[0]) + int(tuple_b[0]), int(tuple_ar[1] + int(tuple_b[1])))
    elif len(tuple_b) == 1 and len(tuple_a) > 1:
        tuple_br = tuple_b + (0,)
        new_tuple = (int(tuple_a[0]) + int(tuple_br[0]), int(tuple_a[1] + int(tuple_br[1])))
    elif len(tuple_a) == 0 and len(tuple_b) > 1:
        tuple_ar = tuple_a + (0,)
        new_tuple = (int(tuple_ar[0]) + int(tuple_b[0]), int(tuple_ar[1] + int(tuple_b[1])))
    
    return new_tuple
