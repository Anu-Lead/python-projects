import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"{self.x}i + {self.y}j"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __len__(self):
        return 0

    def __lt__(self, other):
        return abs(self) < abs(other)

    # def __bool__(self):
    #     return True


v1 = Vector(3, 2)
v2 = Vector(4, 8)
print(bool(v1))
print(v1)
v3 = v1 + v2
print(v3)

lst = [v3, v1, v2]
print(lst)
lst.sort()
print(lst)
