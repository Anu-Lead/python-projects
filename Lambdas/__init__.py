# Lambdas. You
"""
LEGB in Python
L = Local
E = Enclosure
G = Global
B = Builtin
"""
import random


def add(x: int, y: int) -> int:
    """This functions Adds Two Numbers """
    return x + y


print(add.__name__)
print(add.__doc__)
print(add.__annotations__)
print("=================================\n")


def multiply(x, y):
    return x * y


def operate(x, y, func):
    return func(x, y)


print(operate(5, 7, multiply))
print("=================================\n")


def division(a):
    def by(b):
        return a / b

    return by


# divide_by_twenty = division(50)
divide_by_twenty = division(50)(5)
print(divide_by_twenty)
print("================================="
      "\n\nLAMBDAS\n----------------------------------")

# def subtraction(i):
#     def by(j):
#         return by()
#
#     def and_multiply(k):
#         return i - j * k
#
#     return and_multiply()
#
#
# subtract_num = subtraction(60)(100)(2)
# print(and)

# LAMBDA
adder = lambda a, b: a + b
print(adder(60, 50))
print(operate(23, 7, adder))
print(operate(45, 2, lambda s, t: s - t))
# print(divide_by_twenty(40, 4, lambda e, f: e * f))

print("\nROUND NUMBERS\n========================")
print(round(78.9576))
print(round(26.68356, 1))

print("\nSUM NUMBERS & CONCATENATE\n==========================")
arr = [5, 6, 7, 8, 2]

print(sum(arr, 200))

letters = [['a'], ['b', 'c'], [23, 56], ['d'], ['e']]
print(sum(letters, []))

print("\nMINIMUM & MAXIMUM NUMBER\n=============================")
print(max([45, 6, 2, 19]))

fruits = "orange pear banana cucumber mango apple Grape water_melon carrot".split()
print(fruits)

print(min(fruits))
print(max(fruits))

print(min(fruits, key=len))
print(max(fruits, key=len))

print(max(fruits, key=lambda x: x[-1]))
print(min(fruits, key=lambda x: x[-1]))

print("\nSORTING\n=======")
print(fruits)
print("============================================================================================")
print(sorted(fruits))
print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len))
print(sorted(fruits, key=lambda i: i[-1]))

# Map is use for transformation of an object
print("\nMAP\n=====")
print(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])))

lst = [2, 4, 6, 8, 10]
print([x ** 2 for x in lst])

print(list(map(str.upper, fruits)))
print(list(map(lambda x: x.upper(), fruits)))

fruits.append("Coconut")
print(list(map(str.istitle, fruits)))
print(list(filter(str.istitle, fruits)))

print(list(map(lambda y: y.upper(), filter(lambda x: not x.istitle(), fruits))))
print([x.upper() for x in fruits if not x.istitle()])

# CLASS ==> MONDAY 29 AUGUST, 2022
from functools import reduce

# lst = [2, 4, 6, 8, 10, 12, 75]
lst = [2, 4, 6, 8, 80, 12, 5, 95, 25, 30, 105]
# REDUCE => Reduce will take two params and an accumulator
print(reduce(lambda acc, item: acc + item, lst))

from functools import reduce


def reduce_func(acc, item):
    print(f"acc -> {acc} <> item -> {item}")
    return acc + item


def max_func(acc, item):
    print(f"acc -> {acc} <> item -> {item}")
    return acc if acc > item else item


from math import prod

print("\n############ REDUCE ############")

print(random.shuffle(lst))

print(lst)
print(reduce(reduce_func, lst))

print("\n============ OR =============")
print(lst)
print(reduce(reduce_func, lst, 10))

print("\n############ PRODUCT #############")
print(lst)
print(reduce(reduce_func, lst, 100))
print(prod(lst, start=100))
# fruits.append("lettuces")
print(reduce(lambda acc, item: acc if acc > item else item, lst))
print(reduce(max_func, lst))

# MATCH
print("\n\n########### MATCH ############")
num = int(input("Enter A Number: \n"))

match num:
    case 1:
        print(1)
    case 2:
        print(2)
    case _:
        print("I don't Know You!")

print("\n########### MATCH IN RANGE OF NUMBERS ############")
num = int(input("Enter A Number: \n"))

match num:
    case _ as x if 1 <= x <= 10:
        print(x)
    case _ as x if 11 <= x <= 20:
        print(x)
    case 30 | 40 | 50:
        print(x)
    case _:
        print("Don't Know You!")

print("\n########### OR MATCH STRING ############")
word = str(input("Search for Your School Name. Enter the Abbreviation: \n"))

match word:
    case "UI":
        print("University of Ibadan")
    case "OAU":
        print("Obafemi Awolowo University")
    case _:
        print("Invalid Entry!")

print("\n########### MATCHING LIST ############")
student = ["David", "Gabriel", "Daniel", "Joseph"]

match student:
    case [i1, i2, i3, i4]:
        print(i4, i3, i2, i1)
    case _:
        print("Nothing Found")

lst = [20, [13, 5], "good"]

match lst:
    case [x, y, int(z)]:
        print(x, y, z)
    case [a, [b, c], d]:
        print(a, b, c, d)
    case _:
        print("Nothing Match")

print("\n########### MATCHING DICT ############")

d = {
    "name": "Jacob",
    "age": 21,
    "is_good": True
}

match d:
    case {"name": str(name), "age": int(age)}:
        print(name, age)
    case _:
        print("Nothing to Match")

print("\n########### MATCHING FUNCTION {FIZZBUZZ} ############")


def fizzbuzz(number):
    three = number % 3
    five = number % 5

    match (three, five):
        case (0, 0):
            return "FIZZBUZZ"
        case (0, _):
            return "Fizz"
        case (_, 0):
            return "Buzz"
        case _:
            return number


for i in range(1, 30):
    print(fizzbuzz(i))


def summing_list(list_: list[int]) -> int | None:
    match list_:
        case []:
            return 0
        case [int(first_value), *another_list]:
            return first_value + summing_list(another_list)
        case _:
            print("Can only accept int")
            return None


import itertools

print(summing_list([1, 2, 3, 4, 5]))
print(list(itertools.zip_longest([1, 2], [3, 4, 5], fillvalue=0)))


# Architect Adeyemo Adesokunbi


