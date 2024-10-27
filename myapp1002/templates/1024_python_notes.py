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


import datetime


date1 = datetime.datetime(2024, 10, 26)

today = datetime.date.today()

# can access the year, month, day using . notation
match1 = today.year
match2 = today.month
match3 = today.day



print(f"Today is {today}")  #
print(date1)  # 2024-10-26
print(match2)  # 10
print("------------------------\n")


#ex1 using function to convert string to integer


def name_to_num(name: str) -> int:
    """
    take string name as input (rock, Spock, paper, lizard, scissors)
    and returns integer 0-4
    """
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Name not found to match"


print(name_to_num("rock"))    # 0
print(name_to_num("Spock"))   # 1
print(name_to_num("paper"))   # 2
print(name_to_num("lizard"))  # 3
print(name_to_num("scissors"))  # 4
print(name_to_num("Jumps"))

# run some test to make sure
print(name_to_num("rock") == 0)    # True
print(name_to_num("Spock") == 1)   # True
print(name_to_num("paper"))   # 2
print(name_to_num("lizard"))  # 3
print(name_to_num("scissors"))  # 4


# print("------------------------\n")
# print("------------------------\n")
# print("------------------------\n")

