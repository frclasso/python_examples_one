#!/usr.bin/python


def absolutevalue(num):
    if num >= 0:
        abs_num = num
    else:
        abs_num = -num

    print("The absolute value of ", num, "is", abs_num)

absolutevalue(4)