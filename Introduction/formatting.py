import math


minute = 5
arg = "Argument"
s = f"Sorry is this the {minute=} minute {arg=}?"
s = "Sorry is this {} minute {}?".format(5, "Argument")

print("{:10} is {:.2%} years old".format("Bill", math.pi * 25))
print("{:10} is {:.2} years old".format("Bill", math.pi * 25))
print(s)

for i in range(1, 10):
    sym = "*" * i
    print(f'{sym:>10}')