#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] == '+':
        print("{} {} {} = {}".format(a, sys.argv[2], b, calc.add(a, b)))
    elif sys.argv[2] == '-':
        print("{} {} {} = {}".format(a, sys.argv[2], b, calc.sub(a, b)))
    elif sys.argv[2] == '*':
        print("{} {} {} = {}".format(a, sys.argv[2], b, calc.mul(a, b)))
    elif sys.argv[2] == '/':
        print("{} {} {} = {}".format(a, sys.argv[2], b, calc.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
