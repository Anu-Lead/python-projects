# import random
#
# # Counting the Index and Character of a String
# from Tools.scripts.make_ctype import values
#
# print("COUNTING\n==============================================\nCounting the Index and Character of a String")
# school = 'SEMICOLON AFRICA'
# index = 0
# while index < len(school):
#     letter = school[index]
#     print(index, letter)
#     index = index + 1
#
# print("\nLIST\n=================================================================================================")
# a_list = [1, 2, 'abc', 3.14159]
# week_days_list = ['Monday', 'Tuesday', 'Wednesday', "Thursday", "Friday", 'Saturday', "Sunday"]
# list_of_lists = [[1, 2, 3], ['a', 'B', 'c', 'D', 90, 56]]
#
# print(a_list + week_days_list)
#
# print(list_of_lists)
# print(len(list_of_lists[1]))
#
# # SIMILARITIES WITH STRINGS
# number = [1, 2, 3] + [90, 5, 6]
# print(number[3])
#
# """fruit = ['Orange', 'Mango', "Apple", 'Pineapple', 'Watermelon', 7, True, 10, 23, 87, 9]
# print(fruit[0: 10: 2])
# print(fruit[::2])"""
#
# """hobby = ["Noise Making", [["Table", 1, 4, 78], [67, 89, "Good"], 23], False, 'Billion']
# print(hobby)
# print(hobby[2])
# print(hobby[1][1][2])
# print(hobby[1][2])
# print(hobby[3])
#
# del hobby[2]
# print("\nAfter Deleting Value at Index 2: ", "\n==========================================")
# print(hobby)"""
#
# """
# friend = ["a", [1, 2, 3], "z"]
# print(friend[0])
# print(friend[1][2])
# print(friend[2])
# print(friend[0], friend[1][2], friend[2])
# """
#
# # Mutable. It means to change
# # You can change the content of a list, you can change for a string.
#
# # my_list = [2, 4, 6, 8, 10]
# # my_list[2] = "David Mark"
# # print(my_list)
#
#
# # lst = list(range(1, 11))
# # print(lst)
# #
# # random.shuffle(lst)
# # print(lst)
# #
# # print(random.choice(lst))
# # lst.append(145)
# # print(lst)
#
# """
# banks = ["1. First Bank", "2. GTB", "3. UBA", "4: Union Bank"]
# print(banks)
# banks.append("5: Fidelity Bank")
# print(banks)
# banks.extend([56, 12, 18, 19])
# print(banks)
# banks += [30, 50, 90, 100]
# print(banks)
# banks.insert(2, "Sterling Bank")
# print(banks)
# """
#
# # .POP REMOVES THE LAST ELEMENT ON THE LIST AND RETURN IT
# food_items = ["Maggi", "Oil", "Rice", "Chicken", "Milk", "Pepper Soup", 0, 8, 8, 8, 2, 2, 1, 0, 6, 6, 6, 6, 6]
# print("\n=======================================================================================================")
# print(food_items)
# last_item = food_items.pop(2)
# print(last_item)
# print(food_items)
#
# # Remove and Count
# food_items.remove("Chicken")
# print(food_items)
# print(food_items.count(0))
# print("========================================================================================================")
#
# # Shallow Copy
# name = ['emma', 1, 2, 3, ['olaifa']]
# full_name = name[:]
# print(full_name)
# print("========================================================\n")
#
# # DEEP COPY
# import copy
#
# local_student = [1, "Segun", 2, "Daniel", [3, 5], "Joshua", ["Caleb", "Francis"], 4, "Olaitan"]
# foreign_student = copy.deepcopy(local_student)
#
# print(
#     "DEEP COPY\n================================================================\n The Original Elements of Local "
#     "Student Before Deep Copying")
# for i in range(0, len(local_student)):
#     print(local_student[i], end=" ")
#
# print("\r")
#
# foreign_student[4][1] = 10
#
# print("The New List of Elements After Deep Copying ")
# for i in range(0, len(local_student)):
#     print(foreign_student[i], end=" ")
#
# print("\r")
#
# # Reverse
# animal = ["Goal", "Snake", 45, 16, "Hen", "Pig", [True, 5], 34, "Cow"]
# print("\nREVERSE\n========================================================")
# print(animal)
# animal.reverse()
# print(animal)
#
# # SPLIT ==> Splitting this sentence
# sentence = "I am a Great Engineer, Philanthropy, and Politician"
# print("\nSPLIT\n========================================================")
# print(sentence)
# spl_sentence = sentence.split()
# print(spl_sentence)
#
# # SORT ==> Sorting this words
# fruits_words = ["Banana", "Cucumber", "Orange", "Mangoes", "Pineapple", "Brown Pako", "Yellow Pawpaw"]
# print("\nSORT\n========================================================")
# print(fruits_words)
# fruits_words.sort()
# print(fruits_words)
#
# # COMPARE LIST
# list1 = ['{[()]}']
# for element in list1:
#     if list1.__contains__("()"):
#         new_list = list1[element]
#         print(list1)
# print(list1.__contains__('}'))
#
# # Appending to a List with += Let’s start with an empty aList[], then use a for statement and += to append the values
# # 1 through 20 within range 2 to the list. The list grows dynamically to accommodate each item.
#
# aLists = []
# for number in range(1, 20, 2):
#     aLists += [number]
# print("The value of aList is:", aLists)


# Creating A Histogram from A List of Value
value = []
print("Enter Any 10 Different Integers:")

for index in range(10):
    histogram = int(input("Enter Integer %d: " % (index + 1)))
    value += [histogram]

    # print("\nCreating a histogram from values:")

    print("%s %10s %10s" % ("Element", "\tValue", "\tHistogram"))
    for i in range(len(value)):
        print("%7d %10d %s%s" % (i, value[i], "\t", "#" * value[i]))
