#!/usr/bin/python


def count_down():
    ct =10
    while ct > 0:
        print(ct, end = ' ')
        ct = ct - 1
        print()
    print("BLASTOF!")

count_down()