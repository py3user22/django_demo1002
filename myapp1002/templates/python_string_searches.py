"""
String searching examples
"""


sentence = ("When I tell you pick up the "
            "left rock, it will be the "
            "right one, and then only "
            "the right rock will be left")

print(sentence)
# finding strings w/in strings
print("Finding lefts")
first_left = sentence.find("left")
print(first_left)  # 28

# using rfind() function to reverse from end to find search
last_left = sentence.rfind("left")
print(last_left)  # 102

# counting substrings w/in strings
print("counting substrings")
print("Number of lefts: ", sentence.count("left"))  # 2
print("Number of rights: ", sentence.count("right"))  # 2
print("Number of apples: ", sentence.count("apple"))  # 0


word1 = "everything"
print(word1[1:5])  # very
print(word1[5:9])  # thin

# ex3 format specification
name1 = "Pierre"
age1 = 7
name2 = "May"
age2 = 13

line1 = "{0:^7} {1:>3}".format(name1, age1)
line2 = "{0:^7} {1:>3}".format(name2, age2)
print(line1)
print(line2)

num = 3.283663293
output = "{0:>10.3f} {0:.2f}".format(num)
print(output)  # .........3.284 3.28   # 10th space on output


# change to uppercase string
my_str = "Jesus G was here"
print(my_str.upper())

# practice test methods


def count_vowels(word):
    search1 = word.count("a")
    search2 = word.count("e")
    search3 = word.count("i")
    search4 = word.count("o")
    search5 = word.count("u")

    total = search1 + search2 + search3 + search4 + search5
    return total


print(count_vowels("Jesus"))  # 2
print(count_vowels("aaassseefffgggiiijjjoOOkkkuuuu"))  # 13
print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))  # 17


# take a string and replace w/ another character
def demystify(l1_string):
    search1 = l1_string.find("l")
    search2 = l1_string.find("1")

    l2_str = l1_string.replace("l", "a")
    l3_str = l2_str.replace("1", "b")
    return l3_str


print(demystify("lll111l1l1l1111lll"))
print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))


# a_str = ""
# print(a_str.index("sub"))  # raises ValueError: substring not found






