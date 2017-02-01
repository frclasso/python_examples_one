#!/usr/bin/env python3


def if_elif_else():
    x = 10
    y =6
    w = 5
    z =5

    if x > y:
        print("x is greater than y")
    else:
        print("y is greater than x")
    if y > w:
        print ("ys is greater than w")
    else:
        print("w is greater than y")

    if z >0:
        print("z is positive")
    elif z < 0:
        print("z is negative")
    else:
        print("z must be 0")

if_elif_else()