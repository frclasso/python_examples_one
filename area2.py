#!/usr/bin/python


def area(type_,x):
    """Computes the area of a square or circle.
    type_ must be the string Circle or the string square
    We use type_ here, because type is a Python keyword."""
    if type_ == "circle":
        area = 3.14*x**2
        print(area)

    elif type_ == "square":
        area = x**2
        print(area)
    else:
        print("I don't  know that one.")


area("circle", 5)

area("square", 5)