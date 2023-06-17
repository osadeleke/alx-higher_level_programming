#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    else:
        i = 0
        for j in range(len(roman_string)):
            if roman_string[j] == 'M':
                i = i + 1000
            elif roman_string[j] == 'D':
                i = i + 500
            elif roman_string[j] == 'C':
                if j + 1 < len(roman_string):
                    if roman_string[j + 1] == 'D':
                        i = i - 100
                    elif roman_string[j + 1] == 'M':
                        i = i - 100
                    else:
                        i = i + 100
                else:
                    i = i + 100
            elif roman_string[j] == 'L':
                i = i + 50
            elif roman_string[j] == 'X':
                if j + 1 < len(roman_string):
                    if roman_string[j + 1] == 'L':
                        i = i - 10
                    elif roman_string[j + 1] == 'C':
                        i = i - 10
                    else:
                        i = i + 10
                else:
                    i = i + 10
            elif roman_string[j] == 'V':
                i = i + 5
            elif roman_string[j] == 'I':
                if j + 1 < len(roman_string):
                    if roman_string[j + 1] == 'X':
                        i = i - 1
                    elif roman_string[j + 1] == 'V':
                        i = i - 1
                    else:
                        i = i + 1
                else:
                    i = i + 1
        return i
