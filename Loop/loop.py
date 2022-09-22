"""church = "Methodist"

if church == "Anglican No 1":
    print(church)
elif church == "CAC":
    print(church + " is founded by Joseph Ayodele Babalola")
elif church == "Redemption":
    print(church + ": It is a Pentecostal")
    print("Founded by Pastor E.A Adeboye")
else:
    print(church + " is the Original Cathedral in Nigeria")
    print("It has its Headquarter in Abuja")

for i in range(3):
    num = eval(input('Enter a number: \n'))
    print('The square of your number is', num * num)
print('\nTHE LOOP IS  NOW DONE!')

print('A')
print('B')
for i in range(1, 11):
    print(i)
for i in range(5):
    print('D')
print('E')"""

phrase = "it mark the spot"
for character in phrase:
    if character == "X":
        print("Char 'X' is Found")
        break
else:
    print("There was no 'X' in the phrase")

books = ["Physics", "Chemistry", "Programming", "Technology", "Science", "HCI"]
for i in books:
    print(i.upper())

sum_of_evens = 0
for n in range(1, 100):
    if n % 2 == 0:
        sum_of_evens = sum_of_evens + n
print(sum_of_evens)

"""
Exercise 8.3
Write a script that prompts the user to enter a word using the
input() function, stores that input in a variable, and then displays
whether the length of that string is less than 5 characters, greater
than 5 characters, or equal to 5 characters by using a set of if, elif and else statements.
"""

# users_input = str(input("Please Enter a Word\n"))
# if len(users_input) < 5:
#     print(f"The Character {users_input.upper()} is Less than 5")
# elif len(users_input) > 5:
#     print(f"The Character {users_input.upper()} is Greater than 5")
# elif len(users_input.lower()) == 5:
#     print(f"The Character {users_input.upper()} is Equal To 5")
# else:
#     print(f"The Character {users_input.upper()} is Unknown")

"""
Exercise 8.4
Write a script factors.py that asks the user to input a positive integer
and then prints out the factors of that number. Here’s a sample run
of the program with output:
"""

# USERS LOGIN DETAILS A
# users_create_account = {'Name': 'Daniel Gabriel', 'Username': 'daniel-g', 'Password': 'godisgood1234',
#                         'Email': 'daniel.gabriel@gmail.ocm'}
# user_login_uname = input("\n=============================\nEnter Your Login Details\nYour Username:\n")
# user_login_upass = input("Your Password:\n")
# for details in users_create_account:
#     user_name = users_create_account.get("Username")
#     password = users_create_account.get("Password")
#     if user_name == users_create_account.get("Username") in user_login_uname and password == users_create_account.get(
#             "Password") in user_login_upass:
#         print("Successfully Login!.")
#     else:
#         print("Incorrect Login Details.")
#     break
# else:
#     print("Warning! Suspicious Activities")
# print("========================================")

# USERS LOGIN DETAILS B
print("CREATE A NEW ACCOUNT")
users_create_account_details = {
    'fullname': input("Enter Your Full Name:\n"),
    'email': input("Enter Your Email:\n"),
    'username': input("Enter Your Username:\n"),
    'password': input("Enter Your Password:\n")
}

print("Account Successfully Created!\n====================================")
print(users_create_account_details.__str__())
print("====================================")

user_login = input("\nWant to Login?\nYour Username:\n")
user_login = input("Enter Password:\n")

for user_details in users_create_account_details:
    user_n = users_create_account_details.get("username")
    user_p = users_create_account_details.get("password")

    while user_login != users_create_account_details.get('username') and user_login != users_create_account_details.get("password"):
        print("Incorrect Login Details.")
        break
    else:
        # if user_n == users_create_account_details.get('username') and user_p == users_create_account_details.get("password") in user_login:
        print("You're Successfully Login!\n WELCOME TO THE HOME PAGE")
    break
# print("Warning! Suspicious and Unknown Activities")
print("Page Closed!")
