"""
Notes on python --functions calling

area = .5 * base * height
"""


def my_msg(msg, txt):
    print("My msg is here included in the function 'my_msg'\nCan take any input and return a message as the print")


my_msg(1,2)


# function inside a function ex1...
def fiva(value):
    return value * 10


result = fiva(50) + 3500
print(result)


def seven(value):
    return 777


res2 = seven(5) + 33333
print(res2)
res3 = seven(5)
print(f"Here is the function seven(5) -> {res3}")
print(f"Here is the function used w/ another value to create new variable res2 --> \n"
      f"res2 = seven(5) + 33333 --> {res2}")


def product(val1, val2, val3):
    """  Ex1 to return the final product at the end of called assignments  """
    prod = val1 * val2
    prod = prod * val3
    return prod


res1 = product(38, 160, 10)
print(res1)

res2 = res1 * 12
print(res2)

def interest(val1, val2, val3):
    """  Ex2 to return the final product at the end of called assignments  """
    prod = val1
    rate = val2
    year = val3
    mixd = prod * rate
    fina = mixd * year
    return round(fina, 2)


def interest2(val2):
    chk1 = interest(200000, .08, 5) / val2
    return chk1



res5 = interest(125000, .05, 5)
print(f"125k @ .05 x 5 years = {res5}\n"
      f"{res5} / 5 years = 6250")  # 31250


print("--------------------------\n")


def temperature_change(val):
    """return celsius temperature to read from fahrenheit"""
    offset = 32
    multiplier = 5 / 9
    celsius = (val - offset) * multiplier
    return celsius

temp1 = temperature_change(94)
print(round(temp1, 2))


# print("--------------------------\n")
# print("--------------------------\n")
# print("--------------------------\n")
# print("--------------------------\n")
# print("--------------------------\n")
#
# print("--------------------------\n")
# print("--------------------------\n")
# print("--------------------------\n")
# print("--------------------------\n")
# print("--------------------------\n")
