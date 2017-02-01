#!/usr/bin/env python3


def fahrenheit_to_celsius(temp):
    """Converts Farenheit  temperature to Celsius.
    Formula is 5/9 of temp minus 32"""

    new_temp = 5*(temp-32)/9
    print("The Fahsrenheit temperature", temp, "is equivalent to", new_temp)
    print(" degrees Celsius")


fahrenheit_to_celsius(212)

