# school_grade = int(input("Enter Your Score to Determine the Letter Grade: "))

# if school_grade >= 70 <= 100:
#     print("A")
# elif 60 <= school_grade <= 69:
#     print("B")
# elif 50 <= school_grade <= 59:
#     print("C")
# elif 45 <= school_grade <= 49:
#     print("D")
# elif 40 <= school_grade <= 44:
#     print("E")
# else:
#     print("F")


# GUESS GAME NUMBER
import random

#
# check_number = random.randint(0, 10)
# print(f'''
# ---------------------------
# CORRECT ANSWER IS: {check_number}
# ---------------------------
# ''')
#
# num_of_attempt = 4
# message = ''
# while num_of_attempt > 0:
#
#     user_input_number = int(input("Enter A Guess Number:\n"))
#     if user_input_number == check_number:
#         message = "You're Right. Congratulations!"
#         break
#     elif user_input_number > check_number:
#         print(f'{user_input_number} is greater.\nRemaining Attempts is: {num_of_attempt}.')
#         num_of_attempt -= 1
#
#     elif user_input_number < check_number:
#         print(f'{user_input_number} is smaller.\nRemaining Attempts: {num_of_attempt}.')
#         num_of_attempt -= 1
#
#     else:
#         print("Oops, Something Went Wrong!")
#         break
# print(message)

# FIZZ BUZZ GAME
# for number_range in range(1, 101):
#     if number_range % 3 == 0 and number_range % 5 == 0:
#         print("FIZZBUZZ")
#     elif number_range % 3 == 0:
#         print("FIZZ")
#     elif number_range % 5 == 0:
#         print("BUZZ")
#     else:
#         print(number_range)


# Prime Number
import string

"""
start = int(input("Enter the Beginner of An Integer Interval: "))
end_num = int(input("Enter the End of An Integer Interval: "))

for num in range(start, end_num, + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
            else:
                print(num)
"""

# MULTIPLICATION TABLE 1 TO 20
"""
for number in range(1, 21):
    print(" ")
    print("Multiplication Table", number)
    for num in range(1, 12+1):
        result = number * num
        print(number, "*", num, "=", result)
"""

# FIND A LETTER USING FOR LOOP
"""
name = "Oluwasemilogo Feranmi"
target = input("Input a Character to Find: ")
for index in range(len(name)):
    if name[index] == target:
        print("Letter Found at Index: ", index)
        break
    else:
        print("Letter", target, "Not Found At Index", index, name)
"""

# ENUMERATION
"""
name = "'Semicolon'"
target = input("Input a Character to Find: ")
for index, letter in enumerate(name):
    if letter == target:
        print("LETTER FOUND AT INDEX: ", index)
        break
    else:
        print("Letter", target, "Not Found At Index", name)
"""

# abc = string.ascii_lowercase
# word = "love"
# k = 5
# encoded = word.translate(str.maketrans(abc[:-5], abc[5:]))
# print(encoded)

# value = input("Input a Value: ")
#
# if type(value) == str:
#     print(value + "is a string")
# elif type(value) == int:
#     print(value + "is an integer")
# elif type(value) == list:
#     print(value + "is a list")
# else:
#     print("We don't know the type of " + value)

#
# school_name = ["University of Ibadan", "University of Lagos", "University of Ilorin", "University of London",
#                "Anuoluwa"]
# school_name.insert(3, "Yellow")
# print(school_name)
