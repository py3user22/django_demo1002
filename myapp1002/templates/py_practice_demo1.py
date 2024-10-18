#!/bin/python3


def miles(x):
    # mile is 5280 feet
    mile = 5280
    convert = mile * x
    print("There are {} feet in {} miles.".format(convert, x))


miles(13)  # There are 68640 feet in 13 miles.


def time(h, m, s):
    hour = h
    minutes = m
    seconds = 60

    convert1 = hour * seconds
    convert2 = minutes * seconds
    convert3 = s
    combo = convert1 + convert2 + convert3

    print(f"For {h} hours to seconds is  {convert1}\n",
          f"For {m} minutes to seconds is {convert2}\n",
          f"final seconds of all: {combo}",
    )


time(4, 27, 33)  # 1893 seconds


def rect(w, h):
    perimeter = (2 * w) + (2 * h)
    area = w * h
    print(perimeter)   # 22
    print(area)   # 28


rect(4, 7)   # 22


def circle(r):
    pi = 3.14
    radius = r
    area = pi * (radius * radius)
    print(area)


circle(8)  # 200.96

def dollars(p, r, y):
    money = p
    future_value = round((1 + 0.01 * r) ** y, 2)
    compound = money * future_value
    print(future_value)   # w/o the money 1.967...
    print(type(money))   # <class 'int'>
    print(type(compound))  # <class 'float'>
    print(compound)   # 1970.0


dollars(1000,7,10)  # 1970.0


print("Hola, my name is: " + "Jesus " + "Gomez " + "and is 43 years old")


import math


def distance(x0, y0, x1, y1):
    inside = (x0 - x1) ** 2 + (y0 - y1) ** 2
    roots = math.sqrt(inside)
    print(roots)


distance(2,2,5,6)    # 5.0

print(8/-2)  # -4.0

