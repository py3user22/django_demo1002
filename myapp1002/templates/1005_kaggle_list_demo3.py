#!/bin/python3


"""
party list,
not the last person on list,
but after half have arrived,
are you considered fashion late
"""


def fashionably_late(arrivals, name):
    """define variables"""
    last_knot = arrivals[-1]         # <class 'str'>
    half_list = len(arrivals) // 2   # <class 'int'>


    if arrivals == arrivals[-1]:
        print("You were the last knot to show on time")
    elif arrivals >= arrivals[half_list:]:
        print("You were fashionably late, but not the last knot)")
    elif arrivals <= arrivals[:half_list]:
        print("Thanks for coming to the party on time! Hope you had fun")
    else:
        print("You were not on the arrival list")


    # print(last_knot)   # Ford
    # print(type(last_knot))  # <class 'str'>
    # print(half_list)   # 3
    # print(type(half_list))  # <class 'int'>


#                   0         1         2     3       4        5         6
party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']

fashionably_late(party_attendees, 'Ford')

