from dataclasses import dataclass, field, fields, make_dataclass


@dataclass(order=True)
class Person:
    # __slots__ = ['name', 'age', 'height']
    sort_with: tuple = field(init=False, repr=False)
    name: str
    age: int
    height: int
    # children: list = field(default_factory=lambda: [])
    #
    # def __post_init__(self):
    #     self.sort_with = (self.height, self.age)

    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    def get_name(self):
        return self.age


trader1 = Person(name="Mama Rebecca", age=78, height=15)
trader2 = Person(name="Mama Esther", age=48, height=17)

# trader1.name = "Jacob Francis"
# trader1.hello = "my_life"
# print(trader1)
# print(trader1.__dict__)
print(fields(trader1))
# print(trader1 == trader2)
# print(trader1 > trader2)

Human = make_dataclass("Human", ["name", "age"])
student = Human("James", 46)
print(student)

