#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    a = 10
    b = 5
    add = calc.add(a, b)
    sub = calc.sub(a, b)
    mul = calc.mul(a, b)
    div = calc.div(a, b)
    print("{} + {} = {}\n{} - {} = {}".format(a, b, add, a, b, sub))
    print("{} * {} = {}\n{} / {} = {}".format(a, b, mul, a, b, div))
