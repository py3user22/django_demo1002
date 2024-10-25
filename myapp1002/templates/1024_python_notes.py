print("using backslash \\ to escape quotes")
print("I like \"Monty Python\"\n")

print("ex2. using single quotes '' to escape quotes")
print('I like "Monty Python"')

#ex3 using many
print("\"I\'m\"\n\"\"learning\"\" \n\"\"\"Python\"\"\"")

# boolean logic ex1. truth tree

"""
A | Not A
----------
T | F  if A is false, then Not A must be True
F | T


# ex2. 
A | B | A or B | A and B
-------------------------
T | T | T | T
T | F | T | F
F | T | T | F
F | F | F | F

ex3.

not (p or not q)
---------------
p | q | 

the saying says:
not p ->> True
not not q  
|->> 1) q is False
|->> 2) not False is True
|->> 3) not True is False ending

p = True, q = False


ex4. using logically equal expressions
num1 >= num2

(num1 > num2) and (num1 != num2)


"""
print("------------------------\n")
def collatz(num: int) -> list:
    sequence = [num]
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        sequence.append(num)
    return sequence

number = 674
print(f"Collatz 0-7th sequence for {number}: {collatz(number)}")

number2 = 1071
print(f"Collatz 0-14th sequence for {number2}: {collatz(number2)}")


print("------------------------\n")






