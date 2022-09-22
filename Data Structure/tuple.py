# Creating and accessing tuples.
# Just as Strings, Values in tuple are immutable unlike List
# aTuple = (1, 2, 3, 4, 5)
# print("A Tuple Data Structure\n", aTuple)


# Retrieve Hour, Minute and Second from User
# hour = int(input("Enter hour: "))
# minute = int(input("Enter minute: "))
# second = int(input("Enter second: "))
#
# currentTime = hour, minute, second
#
# print("The Value of Current Time is:", currentTime)
# print("The Value of Current Time is:", hour, "Hours,", minute, "Minutes,", second, "Seconds.")
#
# if 0 > hour > 24:
#     if 0 > minute > 60 and 0 > second > 60:
#         print("Invalid Time")  # To write an exception block of code here
#     else:
#         print("The Number of Seconds Since Midnight is: \n",
#               (currentTime[0] * 3600 + currentTime[1] * 60 + currentTime[2]))

# character = ["{[()]}"]
# for index in character.__str__():
#     if character.__str__()[0] == character.__str__()[1]:
#         print(True)
#     else:
#         print(False)
#         break
#     print(character)

# Appending tuples to Lists. You can use += to append a tuple to a list.
# numbers = [12, 34, 23, 65, 17]
# numbers += (90, 80)
# print(numbers)

student = ("A B C", 12, 67, True, ["Victory", 89, False, 56.89], [78, 21, 90], 'University')
print(student)
student[-3][0] = "David"
print(student)

# Swapping Values Via Packing and Unpacking
# You can swap two variables’ values using sequence packing and unpacking:
"""
number1 = 99
number2 = 22
number1, number2 = (number2, number1)
print(f'number1 = {number1}; number2 = {number2}')

colors = ['red', 'orange', 'yellow']
list(enumerate(colors))
print(colors)

tuple(enumerate(colors))

for index, value in enumerate(colors):
    print(f'{index}: {value}')
"""
