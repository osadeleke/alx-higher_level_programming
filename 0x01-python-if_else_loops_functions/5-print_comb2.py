#!/usr/bin/python3
for i in range(0, 100):
    #print 0 to 100
    if i < 99:
        print("{:02d}, ".format(i), end='')
    elif i == 99:
        print("{:02d}".format(i))
