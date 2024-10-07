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

    """if odd list -> the middle element is not included & should be false"""
    # if len(arrivals) % 3 == 0:
    # mid_pnt2 = [arrivals[half_pnt - 1], arrivals[half_pnt])
    # if name in half_non:
    #     return False
    # elif name in mid_pnt2:
    #     return True
    # else:
    #     pass

    """if even list -> the two middle elements are included & should be true"""
    # if len(arrivals) % 2 == 0:
    #

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
list_small = ['June', 'April']

hh = fashionably_late(list_one, 'Gilbert')
print(hh)  # T
nn = fashionably_late(list_two, 'Ringo')
print(nn)  # F --> should be True
bb = fashionably_late(list_one, 'Fleda')
print(bb)  # F
cc = fashionably_late(list_small, 'April')
print(cc)  # T
dd = fashionably_late(list_one, 'May')
print(dd)  # F --> should be False
