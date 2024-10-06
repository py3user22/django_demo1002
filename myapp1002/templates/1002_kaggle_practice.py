#!/bin/python3


def purple_shell(racers):

    str2 = racers[1:-1]
    put_str2 = ''.join(str2)

    str1 = str(racers[-1]) + put_str2 + str(racers[0])

    listr1 = list(str1)

    #list_str1 = str1.split(',')
    print(str2)
    print(str1)
    print(put_str2)
    print(listr1)




r = ["Mario", "Luigi", "Princess"]
purple_shell(r)

print("-------------------\n")


s = ["M", "L", "O", "P"]
purple_shell(s)