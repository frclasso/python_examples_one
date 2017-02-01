#!/usr/bin/env python3
import sys


def fahreinheit_to_celsius2():
    temp_str = input("Enter a Fahreinheit temperature: ")
    temp = int(temp_str)
    new_temp = 5*(temp-32)/9

    print("The Fahreinheit temperature", temp, "is equivalent to ", end='')
    print(new_temp, " degrees Celsius")


fahreinheit_to_celsius2()