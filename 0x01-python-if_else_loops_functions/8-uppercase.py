#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
            #print("{}".format(chr(ord(char) - 32)), end='')
        else:
            char = char
            #print("{}".format(char), end='')
        print("{}".format(char), end='')
    print("")

