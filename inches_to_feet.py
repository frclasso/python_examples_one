#!/usr/bin/env python3


def inches_to_feet1(inches):
    """converts inches to feet  and inches"""

    feet = inches//12  #division by integer with fraction throw away
    extra_inches = inches - 12*feet
    print(inches, 'inches is', feet, "feet and", extra_inches, "inches")


inches_to_feet1(77)