# REVERSE HILL PATTERN

# reversePat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for a in range(reversePat):
#     for b in range(len(reversePat)):
#         print(" ")
#
#     for b in len(reversePat[a]):
#         print("*")


# Left Angle Triangle
# for i in range(1, 10):
#     sym = "*" * i
#     print(f'{sym:>10}')

# Pyra
j: int
for j in range(10):
    for k in range(10):
        triangle = "*" * j
        triangle = "*" * k

        print(f'{triangle: ^10}')


def calBMI(weight, height):
    weight / height ** 2
    return calBMI


print(calBMI(52, 5.5))
