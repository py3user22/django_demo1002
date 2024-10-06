#!/bin/python3


"""
party list,
not the last person on list,
not the middle person on list,
but after half have arrived,
are you considered fashion late
"""
list_one = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
list_two = ['Paul', 'John', 'Ringo', 'George']
list_three = ["Jesus", "Jessica"]


def fashionably_late(arrivals, name):
    """define variables"""
    mid_ele = len(arrivals) // 2  # middle section of the list as <class 'int'>
    sec_half_nolast = arrivals[mid_ele + 1:-1]  # from +1 after the middle --to 2nd to last
    fir_half = arrivals[:mid_ele]  # from the start to the middle
    last = arrivals[-1]  # last element in list

    if len(arrivals) <= 2:
        return True

    if name in fir_half:
        return False

    elif name in last:
        return False

    elif name in sec_half_nolast:
        return True

    else:
        return False


print(fashionably_late(list_one, 'May'))  # False
# print(fashionably_late(list_one, 'Adela'))  # False
print(fashionably_late(list_two, 'George'))  # False
print(fashionably_late(list_two, 'Ringo'))  # False

print(fashionably_late(list_three, 'Jessica'))  # True













