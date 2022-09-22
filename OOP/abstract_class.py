import abc


# class Mammal(metaclass=abc.ABCMeta):
#     pass

class Mammal(abc.ABC):
    @abc.abstractmethod
    def move(self):
        pass


# m1 = Mammal()


class Person(Mammal):
    def move(self):
        pass


p1 = Person()


# print(p1)


# INHERITANCE BUILTINS
class DoubleIt(int):
    def __new__(cls, value):
        return super().__new__(cls, value ** 10)


d = DoubleIt(2)
print(d)


# d += 6
# print(d)


class MyList(list):
    def __setitem__(self, key, value):
        # print("Called::Dollars!")
        if key < 1:
            raise IndexError("Index Can Neither Be Negative nor Zero")
        super().__setitem__(key - 1, value)

    def __getitem__(self, key):
        if key < 1:
            raise IndexError("Index Can Neither Be Negative nor Zero")
        super().__getitem__(key - 1)


l = MyList('Favour')
print(l)
# l.append(1)
l[1] = [True, 24, "Great"]
l[6] = ["Hallelujah", False, '$245']
print(l)

print("\n================================")


class Banks(dict):
    def __setitem__(self, bank_name, bank_id):
        if not isinstance(bank_name, str):
            raise TypeError("Can Only Take String as Key")
        super().__setitem__(bank_name, bank_id)


micro_finance_bank = Banks()
micro_finance_bank['UBA'] = 100111
micro_finance_bank["GTB"] = 101123
print(micro_finance_bank)
print(micro_finance_bank['GTB'])


# PYTHON DATA MODEL

class CustomClass:
    def __init__(self, num):
        self.num = num


