#!/bin/python3


"""
party list,
not the last person on list,
but after half have arrived,
are you considered fashion late
"""


def fashionably_late(arrivals, name):
    """define variables"""
    half_arrivals = len(arrivals) // 2   # <class 'int'>   # 3
    last_person = arrivals[-1]    # <class 'str'>
    b4_half = arrivals[:half_arrivals]    # names b4 the half point
    after_half_not_last = arrivals[half_arrivals:-1]   # names after half point but not the last 1

    if name in b4_half:
        return False
    elif name == arrivals[half_arrivals]:
        return False
    elif name in after_half_not_last:
        return True
    elif name == last_person:
        return False
    else:
        return False







    # print(after_half_not_last)  # ['May', 'Mona', 'Gilbert']
    # print(type(after_half_not_last))  # <class 'list'>
    # print(b4_half)    # ['Adela', 'Fleda', 'Owen']
    # print(type(b4_half))  # <class 'list'>
    # print(last_person)   # Ford
    # print(type(last_person))  # <class 'str'>




party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
party_attends2 = ['Paul', 'John', 'Ringo', 'George']

print("original list:")
print(party_attendees)
print("--------------------\n")

fashionably_late(party_attendees, 'Ford')
# fashionably_late(party_attendees, 'Owen')
# fashionably_late(party_attendees, 'Adela')

print("--------------------\n")

print("party list2:")
print(party_attends2)
fashionably_late(party_attends2, 'Ringo')
