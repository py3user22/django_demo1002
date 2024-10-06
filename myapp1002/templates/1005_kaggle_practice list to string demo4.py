#!/bin/python3


"""
Put the list into new list, have the following format: 1st character as the last, middle, last as first,
"""

def purple_shell(racers):
    """step1: define variables"""
    first_ele = racers[0]  # Mario  # <class 'str'>
    mid = racers[1:-1]     # ['Peach', 'Luigi']  # <class 'list'>
    last_ele = racers[-1]  # Yoshi  # <class 'str'>

    """Converting a sliced list to string"""
    res_str = ' '.join(mid)         # Peach Luigi   # <class 'str'>
    res_str0 = ''.join(first_ele)   # Mario    # <class 'str'>
    res_str1 = ''.join(last_ele)    # Yoshi    # <class 'str'>

    fin_str2 = "{} {} {}".format(last_ele, res_str, first_ele)

    fin_lst4 = fin_str2.split()

    if len(racers) <= 2:
        racers[0], racers[-1] = racers[-1], racers[0]
        print(racers)
    else:
        print(fin_lst4)



    # print(first_ele, mid, last_ele) # Mario ['Peach', 'Luigi'] Yoshi
    # print(res_str)    # Peach Luigi
    # print(type(res_str))  # <class 'str'>
    # print(res_str0)   # Mario
    # print(type(res_str0))   # <class 'str'>
    # print(res_str1)   # Yoshi
    # print(type(res_str1))   # <class 'str'>
    # print(fin_str)      # Yoshi Peach Luigi Mario
    # print(fin_lst)
    # print(type(first_ele))  # <class 'str'>
    # print(type(mid))        # <class 'list'>
    # print(type(last_ele))   # <class 'str'>

list_ex1 = ["Mario", "Peach", "Luigi", "Yoshi"]

purple_shell(list_ex1)

print("\n--ex3 --using only 1 letter --------------------")

list_ex2 = ["M", "P", "L", "Y", "O"]
purple_shell(list_ex2)

print("\n--ex3 --using 2 or less in list --------------------")
list_ex3 = ["M", "P"]
purple_shell(list_ex3)   # ['P', 'M']

print("\n --ex4 --using exactly 3 letters in the list --------------------")
list_ex4 = ['M', 'L', 'J']
purple_shell(list_ex4)
