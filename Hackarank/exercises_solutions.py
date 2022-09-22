# Array Sum
"""
def solve_me_first(num1, num2):
    return num1 + num2


numb1 = int(input("SUM AN INTEGER.\nEnter A Number:\n"))
numb2 = int(input("Enter Another Number:\n"))
response = solve_me_first(numb1, numb2)
print(response)
"""


# COMPARE TRIPLET


def compare_triplet(a, b):
    # a = 21, 67, 23, 12, 67, 90
    # b = 89, 31, 45, 27, 22, 18

    alice = 0
    bob = 0
    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    return alice, bob



