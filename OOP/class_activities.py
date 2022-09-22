"""class Human:
    count = 0

    def __init__(self, name="", age=0):
        self._name = name
        self._age = age
        Human.count += 1

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, name: str):
        print("Calling the Setter Name")
        if name.islower():
            raise ValueError("Name Cannot Be All Lower Case")
        self._name = name

    @age.setter
    def age(self, age: int):
        print("Calling the Setter Age")
        # if age.__neg__():
        if age.__float__():
            raise FloatingPointError("You cannot have a Float Value Age")
        self._age = age

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def is_minor(age):
        return age <= 16


school_boy = Human("Joshua", 12)
print(school_boy.name, "is a Student, and", school_boy.age, "Years Old")
pastor = Human("Pastor Gabriel", 45)
print(pastor.name, "is", pastor.age, "Years Old")
print(school_boy.is_minor(14))"""


# @name.deleter
# def name(self):
# print("Deleting...")
# del self._name


class Human(object):
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def full_name(self):
        return f'{self.last_name} {self.first_name}'

    def __str__(self):
        return f"name={self.last_name} {self.first_name}, age={self.age}, sex={self.sex}"


class Manager(Human):
    def __init__(self, first_name: str, last_name: str, age: int, sex: str, bonus: float):
        self.bonus = bonus
        super().__init__(first_name, last_name, age, sex)

    def full_name(self):
        return f'{self.last_name[0].upper()} {self.first_name}, {self.sex}'

    def pay_salary(self, salary):
        return salary + self.bonus


class Employee(Human):
    def pay_salary(self, salary):
        return salary


operation_manager: Manager = Manager("James", "Samson", 29, "Female", 1250.00)
employee1: Employee = Employee("David", "Boris", 22, "Male")
# print(employee1.full_name(), employee1.age, employee1.sex)

# print(operation_manager.full_name())

# human_list = [employee1, operation_manager, Human("Sapiens", "Homo", 0, "Unknown")]
human_list = [employee1, operation_manager]
for human in human_list:
    print(human.full_name())
    print(human.pay_salary(75_000))


# 15th September 2022

class Practice:
    count = 0

    def __init__(self, first):
        self.first = first
        Practice.count += 2

    def play(self):
        return f"Playing With {self.first}"

    @classmethod
    def get_count(cls):
        return cls.count

    @classmethod
    def create(cls, name):
        return cls(name)

    @staticmethod
    def just_here():
        return f"Just Staying Here.....!"


p1 = Practice("James")
p2 = Practice.create("Daniel")

print(p1.first)
print(p1.count)
print(p1.play())
