import math
import random

# *radius: float = float(input("Enter the radius of a circle: ")) area = 3.142 * radius ** 2 print("The Area of a
# Circle with Radius", radius, "is", area, sep=" #### ",
# end="\n**************************************************************\nDone Printing")

# print("WELCOME HERE GEE!") height: float = float(input("Enter the Radius of a cylinder: ")) radius: float = float(
# input("Enter the Height of a cylinder: ")) height = 3.142 * radius ** 2 * height print("The Height of a Cylinder",
# radius, "is", height, sep=" ", end="\n**************************************************************\nDone
# Printing\n")


# for i in range (1, 21, 2):
#     print("*" * i).center(20))


import string

word = input("What Would You Like to Encode?")
key = int(input("Enter Your Key: "))

lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase

lower_letters_code = lower_letters[key:] + lower_letters[:key]
upper_letters_code = upper_letters[key:] + upper_letters[:key]


letters = lower_letters + upper_letters
letters_code = lower_letters_code + upper_letters_code

# print(letters)
# print(letters_code)

encoded_word = word.translate(
    str.maketrans(letters, letters_code)
)
# print(encoded_word)
#
# decoded_word = encoded_word.translate(str.maketrans(letters_code, letters))
# print(decoded_word)


print("Now Print the Brute Force Approach")
for i in range (1, 27):
    lower_letters_code = lower_letters[i:] + lower_letters[:i]
    upper_letters_code = upper_letters[i:] + upper_letters[:i]

    letters = lower_letters + upper_letters
    letters_code = lower_letters_code + upper_letters_code
    print(encoded_word.translate(str.maketrans(letters_code, letters)))


















