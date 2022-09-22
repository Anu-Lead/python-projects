# # CLASS EXERCISE Accessing and counting the item in a Dictionary
def check_the_index(fruit_letters: list | str | tuple) -> dict:
    # from collections import Counter, default-dict
    fruit = {}
    # fruit = default-dict(int)
    for letter in fruit_letters:
        if letter in fruit:
            fruit[letter] = fruit[letter] + 1
        else:
            fruit[letter] = 1
        # OR
        fruit[letter] = fruit.get(letter, 0) + 1
        # OR
        fruit[letter] = fruit_letters.count(letter)
        # OR

        fruit[letter] += 1

    return fruit


print(check_the_index("PINEAPPLE-IS-SWEET"))

# # COMPREHENSION IS USED TO ADD/BUILD/OR GENERATE A LIST
cont = []

for i in range(1, 11):
    cont.append(i)

# # #     OR
cont = [food for food in range(1, 11)]

print(cont)

from typing import List

square_root = [numbers ** 2 for numbers in range(1, 11)]

print(square_root)

schools = ["Harvard University", "cambridge University", "princeton University", "Yale University", "columbiaUniversity", "Standford University"]
my_schools = [school for school in schools if school.istitle()]


print(my_schools)

even_numbers = [e_num for e_num in range (1, 21) if e_num % 2 == 0]
print(even_numbers)

# # OTHERS
# names = ["james", "peter", "samuel", "elijah"]
# cont = [num for num in range(1, 11)]
# squares = [num ** 2 for num in range(1, 21)]
# upper_names = [name.upper() for name in names]
# evens = [even for even in range(1, 11) if even % 2 == 0]
#
# even_squared_odd_cubed = [num ** 2 if num % 2 == 0 else num ** 3 for num in range(1, 11)]
# print(even_squared_odd_cubed)
# print(upper_names)
# print(squares)
# print(evens)
# print("=============================================================")
# # number_of_time = int(input("How Many Name Do you want to Enter?\n"))
# # input_names = [input(f"{i+1}. Name? ") for i in range (number_of_time)]
# # input_schools = [input("Your School Name: \n") for _ in range(5)]
#
# x_and_y = [(x ** 2 if x % 2 == 0 else x, y) for x in range(1, 10, 2) for y in range(1, 10, 2)]
# print(x_and_y)
# print("===============================================================")
#
# listcomp = [num % 3 for num in range(1, 10)]  # List Comprehension
# setcomp = {num % 3 for num in range(1, 10)}  # Set Comprehension
# dictcomp = {k: v for k, v in enumerate(range(1, 10))}  # Dictionary Comprehension
# dictcomp = {k: v for k, v in enumerate("UNIVERSITY", 10)}  # Dictionary Comprehension
# # genexp = (num % 3 for num in range(1, 5))  # Generator Expression
# genexp = (num for num in range(0, 5))  # Generator Expression
# print(type(listcomp), listcomp)
# print(type(setcomp), setcomp)
# print(type(dictcomp), dictcomp)
# print(type(dictcomp), dictcomp)
# print(type(genexp), genexp)
# # print(next(genexp))
#
# # print([i for i in range(10_000_000)])
# genexpe = (i for i in range(1, 10_000_000, 2_000_000))
#
# for i in genexpe:
#     print(i)
#
users = [
    {'name': 'David',
     'age': 72,
     'gender': 'Male',
     'user_name': "davis28",
     'is_verified': False,
     'tweets': [{'content': "PO for President", 'likes': 450, 'retweets': 233},
                {'content': "Atiku for President", 'likes': 4, 'retweets': 2}]
     },

    {'name': 'Elijah',
     'age': 25,
     'gender': 'Transgender',
     'user_name': "elione",
     'is_verified': True,
     'tweets': [{'content': "What if you died today?", 'likes': 89, 'retweets': 31},
                {'content': "You won't still know", 'likes': 78, 'retweets': 8}]
     },

    {'name': 'Joseph',
     'age': 18,
     'gender': 'Male',
     'user_name': "joe1",
     'is_verified': True,
     'tweets': [{'content': "PO for President", 'likes': 40, 'retweets': 33},
                {'content': "Amazing Grace", 'likes': 1, 'retweets': 12},
                {'content': "Amazing Grace", 'likes': 1, 'retweets': 12},
                {'content': "Amazing Grace", 'likes': 1, 'retweets': 12}]
     },

    {'name': '_Rachael_Leah',
     'age': 30,
     'gender': 'Female',
     'user_name': "richyBaby",
     'is_verified': False,
     'tweets': [{'content': "Greatness is Costly", 'likes': 367, 'retweets': 19}]
     },

    {'name': 'Elizabeth',
     'age': 19,
     'gender': 'Male',
     'user_name': "zabeth",
     'is_verified': True,
     'tweets': [{'content': "Elizabeth is a student of UI", 'likes': 21, 'retweets': 93},
                {'content': "You will fail if you are not diligent", 'likes': 2, 'retweets': 7}]
     }
]
#
# no_of_users = len(users)
# usernames = {user["user_name"] for user in users}
# print(usernames)
#
# female_users = [user for user in users if user['gender'] == "Female"]
# print(female_users)
#
# likes_greater_than_fifty = [tweet for tweet in (user['tweets'] for user in users)]
# print("likes", likes_greater_than_fifty)
#
# inactive_users = [user for user in users if len(user['tweets']) < 2]
# print(inactive_users)
#
# users_name_and_age = [{'name': user['name'], 'age': user['age']} for user in users]
# print(users_name_and_age)
#
# ave_age_of_users = round(sum(user['age'] for user in users) / len(users))
# print(ave_age_of_users)
#
# print(max(users, key=lambda a: a['age']))
# print(max(users, key=lambda a: len(a['tweets'])))



# iterable1 = (1, 2, 3, 4)
# iterable2 = ("How", "Are", "You", "Doing")
# print(list(zip(iterable2, iterable1)))
# print(dict(zip(iterable2, iterable1)))
#
# print(sorted("SEMICOLON"))
# print(sorted("SEMIcolon"))
#
# print(sorted("Glory", reverse=True))
# print(sorted("Glory", reverse=False))
# print(sorted("Glory"))
#
# print("\nAVERAGE AGE OF USERS\n====================")
# print(sum(user['age'] for user in users) / len(users))
#
# print(any(user['is_verified'] for user in users))
# print(all(user['is_verified'] for user in users))
#
# print(any(user['gender'] == 'Female' for user in users))
