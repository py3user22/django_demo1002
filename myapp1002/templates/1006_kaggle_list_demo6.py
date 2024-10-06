#!/bin/python3


"""
party list,
not the last person on list,
but after half have arrived,
are you considered fashion late
"""


def fashionably_late(arrivals, name):
    """define variables"""
    mid_section = len(arrivals) // 2
    # first_half = arrivals[:mid_section]
    # sec_half_not_last = arrivals[mid_section:-1]
    last_ppl = arrivals[-1]

    if len(arrivals) <= 3:
        return True

    if name in arrivals[mid_section:-1]:
        return True
    elif name == last_ppl:
        return False
    elif name == arrivals[mid_section]:
        return False
    else:
        return False


list1 = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
list2 = ['Paul', 'John', 'Ringo', 'George']
list3 = ['Jesus', 'Jessica']

res1 = fashionably_late(list1, "Mona")   # T
res12 = fashionably_late(list1, "May")   # xT but F
res2 = fashionably_late(list2, "John")   # xF but T
res3 = fashionably_late(list3, "Jesus")  # T

print(res1)  # True
print(res12)  # False
print(res2)  # False
print(res3)  # True




