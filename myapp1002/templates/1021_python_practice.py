"""
Notes on python --functions calling

area = .5 * base * height
"""


def my_msg(msg, txt):
    print("My msg is here included in the function 'my_msg'\n"
          "Can take any input and return a message as the print\n"
          "return --> statement is what should go back after the caller of function run\n"
          "return statement also terminates the function, so anything after it will not run\n"
          )


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
    prod = prod * val3  # variable re-assign
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

# define points 2 at a time example global variables demo

x_0, y_0 = 2, 2
x_1, y_1 = 5, 6

print("assign 2 variables in one line example")
print(x_0, y_0, x_1, y_1)


print("--------------------------\n")

"""Compute area of triange w/ vertices x_0, y_0, x_1, y_1"""

def point_distance(x_0, y_0, x_1, y_1):
    """return distance between point x_0, y_0, x_1, y_1"""
    x_dist = x_0 - x_1
    y_dist = y_0 - y_1
    return (x_dist**2 + y_dist**2)**0.5


def triangle_area(x_0, y_0, x_1, y_1, x_2, y_2):
    """return area of triangle w/ vertices x_0, y_0, x_1, y_1, x_2, y_2"""

    # find the length of 3 sides
    len_01 = point_distance(x_0, y_0, x_1, y_1)
    len_02 = point_distance(x_0, y_0, x_2, y_2)
    len_03 = point_distance(x_1, y_1, x_2, y_2)

    # compute semi-perimeter length, 1/2 of perimeter
    # compute the area __> math > Herons formula
    semi_perim = (len_01 + len_02 + len_03) / 2
    return (semi_perim * (semi_perim - len_01) * (semi_perim - len_02) * (semi_perim - len_03)) * 0.5


x_0, y_0 = 10, 0
x_1, y_1 = 0, 0
x_2, y_2 = 0, 10

print(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2))


"""will give money even if false taking off 25, will execute next indented if statement"""


def greet(friend, money):

    if friend and money > 20:
        print("Hi")
        money = money - 20
    elif friend:
        print("Hi2")
    else:
        print("haha")
        money = money + 10

    # if money > 20:
    #     money = money - 20

    return money

money = 25

money = greet(False, money)





