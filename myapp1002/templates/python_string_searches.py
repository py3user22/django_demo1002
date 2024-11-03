"""
String searching examples
"""


sentence = ("When I tell you pick up the "
            "left rock, it will be the "
            "right one, and then only "
            "the right rock will be left")

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


word = "everything"
print(word[1:5])  # very
print(word[5:9])  # thin

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



