# Function Definition
"""def print_this_function(money):
    return money


print(print_this_function("$80 Billion Dollar"))"""

# def celsius_to_fahrenheit(param_float):
#     return param_float * 1.8 + 32
#
#
# print("Convert Celsius to Fahrenheit.\n=============================\n")
# celsius_float = float(input("Enter a Celsius Temperature:"))
# fahrenheit_float = celsius_to_fahrenheit(celsius_float)
# print(celsius_float, " converts to ", fahrenheit_float, " Fahrenheit")


# def get_digit(number, position):
#     '''return digit at position in number, counting from right'''
#     return number//(10**position)%10
# number = int(input("Enter a Number:"))
# print(get_digit(2789, 2))


# def add(even_number, odd_number):
#     """
#     :param even_number:
#     :param odd_number:
#     :return:
#     """
#     return even_number + odd_number
#
#
# print(add(5, 10))
# help(add)


# def multiply(first_num: int, second_num: int, third_num: int) -> int:
#     return first_num * second_num + third_num
#
#
# print(multiply(70, 10, 5))
# print(multiply.__doc__)
# print(multiply.__name__)
# print(multiply.__annotations__)

"""import math


def get_length(number: int) -> int:
    import math
    return math.ceil(math.log10(number))

    # return len(str(number))

print(get_length(7633))

print(math.sqrt(1000))"""

# FINDING THE MAXIMUM OF THREE INTEGERS
# def checkingMaximumValue(a, b, c):
#     maximum = a
#     if b > maximum and b < c:
#         maximum = b
#
#     if c > maximum:
#         maximum = c
#
#         return maximum
#
#
# first_num = int(input("Enter the First Integer\n"))
# second_num = int(input("Enter the Second Integer\n"))
# third_num = int(input("Enter the Third Integer\n"))
#
# # Function Call
# print("The Maximum Integer is: ", checkingMaximumValue(first_num, second_num, third_num))
# print("")

a = 5


def func1():
    global a
    a += 7
    print(a)


func1()

print("########################")
b = 10


def funct():
    c = 12

    def inner_func():
        # global b
        nonlocal c
        c += 6
        print(c)

    inner_func()
    print(c)


funct()

emma = [23, 203, 67, 89, 12, 10, 4]
print(len(emma))

print(id(emma))

name = ["Tolu", 12, {True}, "Seun", [56]]
print(any(name))

"""Return the maximum of three values."""


def maximum(value1, value2, value3):
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value


print(maximum(56, 90, 23))

name = "Joshua"
fruit = ["orange", "cucumber", "mango", "grape"]


def greet():
    print(f"Hello, {name}!")
    return


greet()


# !/usr/bin/python

# total = 0; # This is global variable.
# # Function definition is here
# def sum( arg1, arg2 ):
#    # Add both the parameters and return them."
#    total = arg1 + arg2; # Here total is local variable.
#    print "Inside the function local total : ", total
#    return total;
#
# # Now you can call sum function
# sum( 10, 20 );
# print "Outside the function global total : ", total


def my_fun(param):
    param.append(5)
    return param


my_list = [1, 2, 3, 4]
new_list = my_fun(my_list)

print(my_list, new_list)


def name(bank_staff):
    bank_staff = ["David", "Joshua", "Thomas"]
    bank_staff.append("Emmanuel")
    return bank_staff


stu_name = ["Daniel", "John", "James"]
new_name = name(stu_name)
print(new_name, stu_name)

# Default Argument
"""
A default argument is an argument that assumes a default value if a value is not provided in the function call 
for that argument. The following example gives an idea on default arguments, it prints default age if it is not passed
"""

print("\n============DEFAULT ARGUMENT ==> PERSON'S NAME")


# Function definition is here
def person_details(name, age=35):
    "This prints a passed info into this function"
    print("Name: ", name)
    print("Age ", age)
    return


person_details(age=50, name="Peter")
person_details(name="Caleb")


def mixed(a="5", b="7"):
    print(a + b)


mixed("\n78", "10")


def sum_all(*args):
    total = 0
    for arg in args:
        total += arg
    print(total)


sum_all(2, 5, 8, 45, 17)


def school(**all):
    print(all)


school(Ibadan="UI", Ife="OAU", Benin="UNIBEN", Kwara="Unilorin")


def func_again(a, b, /, c, *, d):
    print(a, b, c, d)


func_again(1, 2, c=6, d=4)

"""def invest(amount, rate_amount, years):
    investment_return = amount
    rate = (rate_amount * amount) / 100
    for i in range(1, years + 1):
        investment_return += rate
        print(f"years {i}", f"{investment_return:.2f}")


amount: float = float(input("Enter Amount: \n"))
rate_amount: float = float(input("Enter Rate: \n"))
years: int = int(input("Enter Years: \n"))

invest(amount, rate_amount, years)"""

# MIN and MAX Function
countries = ['Netherlands', 'Nigeria', 'Jordan', 'Liberia', "Saudi Arabia", "Dubai"]
population = [100_845_12, 200_034_000, 43_000_091, 56_213_765, 43_012_456, 34_845_099]


def get_population(pair):
    countries, population = pair
    return population


print(min(zip(countries, population), key=get_population))


# print(max(population))
# print(min(countries))

# EXCEPTIONS
# def add(a: float, b: float) -> float | None:
#     try:
#         # c = a + "b"
#         # print(name)
#         name = int("David")
#         return a / b
#     except ZeroDivisionError:
#         print("Cannot Divide with Zero")
#         return None
#     except (TypeError, NameError):
#         print("TypeError")
#
#
# print(add(1, 0))
