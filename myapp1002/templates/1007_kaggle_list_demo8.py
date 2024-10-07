#!/bin/python3


"""
party list,
not the last person on list,
not the middle person on list,
if the list is short, then middle can be True
but after half have arrived,
are you considered fashion late
"""

list_one = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
list_two = ['Paul', 'John', 'Ringo', 'George']
list_tt = ['Alice', 'Bob', 'Charlie', 'David']
list_three = ["Jesus", "Jessica"]


def fashionably_late(arrivals, name):
    """define local variables here"""
    half_pty = len(arrivals) // 2  # <class 'int'>
    hal_str_pty = str(half_pty)    # <class 'str'>
    mid_points = ()
    first_gp = arrivals[:half_pty]
    aft_mid_not_last = arrivals[half_pty:-1]
    last_ppl = arrivals[-1]
    spliced_list = arrivals[half_pty+1]

    # check if list is small but has a midpoint
    if len(arrivals) <= 2:
        return True

    # determine the midpoints
    if len(arrivals) % 2 == 0:
        mid_points = (arrivals[half_pty - 1], arrivals[half_pty])
    else:
        mid_points = (arrivals[half_pty])

    # to chk if in the section
    if name in aft_mid_not_last:
        return True
    # elif name in spliced_list:
    #     return True
    elif name in first_gp:
        return False
    elif name in last_ppl:
        return False


    print("mid points are: " + mid_points)


hh = fashionably_late(list_tt, 'Charlie')
print(hh)
kk = fashionably_late(list_one, 'May')
print(kk)