#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    j = number * -1
    i = j % 10
    print(f"Last digit of {number} is {i * -1} and is less than 6 and not 0")
elif number == 0 or number > 0:
    i = number % 10
    if i > 5:
        print(f"Last digit of {number} is {i} and is greater than 5")
    elif i == 0:
        print(f"Last digit of {number} is {i} and is 0")
    elif i < 6 and not 0:
        print(f"Last digit of {number} is {i} and is less than 6 and not 0")
