#!/bin/python3


"""
Put the list into new list, have the following format: 1st character as the last, middle, last as first,
"""

def purple_shell(racers):
    # step1: define variables
    new_list = []
    str_list = ''
    for el in racers:
        str1 = str(el)
        str_list = str1
        rev_first_to_last = str_list[-1] + str_list[1:-1] + str_list[0]
        # new_list = ''.join(rev_first_to_last)  # only the last name in list is printed




        print(

            str_list + " --whole string\n",
            str_list[0] + " --string [0]\n",
            str_list[-1] + " --string [-1]\n",
            str_list[1:-1] + " --string [1:-1]\n",
        )
        print(
            str_list[-1] + str_list[1:-1] + str_list[0] + " --last to 1st, mid, 1st at last\n",
        )
        print(new_list)




list_ex1 = [1,2,3,4,5,6,7,8,9]

list_ex2 = ["Mary", "Jane", "Lady", "Sonia"]

#purple_shell(list_ex1)  #prints 1-9 vertical w/ \n
print("-----------------\n")

purple_shell(list_ex2)
print("-----------------\n")

