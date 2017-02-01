#!/usr/bin/env python3

import readline


def name():
    """Input first and last name, combine to one string and print"""

    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    fullname = fname + " " + lname

    print("You name is ", fullname)

name()