#!/bin/python3


"""
party list,
not the last person on list,
not the middle person on list,
if the list is short, then middle can be True
but after half have arrived,
are you considered fashion late
"""


def fashionably_late(arrivals, name):
    """define local variables here"""
    half_pnt = len(arrivals) // 2  # <class 'int'>
    # print(half_pnt)  # 3
    # print(str(half_pnt))  # 3
    half_non = arrivals[half_pnt]
    # print(half_non)  # May
    fir_sec = arrivals[:half_pnt]
    aft_sec = arrivals[half_pnt:]
    las_ppl = arrivals[-1]

    if len(arrivals) <= 2:
        return True

    if name in fir_sec:
        return False
    elif name in las_ppl:
        return False
    elif name in aft_sec:
        return True




#              0        1        2      3      -3       -2        -1
list_one = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
list_two = ['Paul', 'John', 'Ringo', 'George']
list_tt = ['Alice', 'Bob', 'Charlie', 'David']
list_small = ['May', 'April']

hh = fashionably_late(list_one, 'Gilbert')
print(hh)
nn = fashionably_late(list_two, 'Ringo')
print(nn)
bb = fashionably_late(list_one, 'Fleda')
print(bb)
cc = fashionably_late(list_small, 'April')
print(cc)
dd = fashionably_late(list_one, 'May')
print(dd)  # should be False
