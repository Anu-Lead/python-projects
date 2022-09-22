from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} pages"


personal_development_book = Book("Time Management", "David Mark", 340, 1250.00)
research_book = Book("Ethnographic Research in Product Development", "John Joseph", 126, 4560.92)

print(personal_development_book.description)
print(research_book.description)

print("\n============================")


# MULTIPLE INHERITANCE
class CardiovascularCenter:
    def __init__(self):
        super().__init__()
        self.lab_name = "Cardiovascular-Heart Center"
        self.lab_type = "BP Laboratory"


class MaternityClinic:
    def __init__(self):
        super().__init__()
        self.name = "Maternity Clinic Center"
        self.room = "Labour Room"


class Hospital(MaternityClinic, CardiovascularCenter):
    def __init__(self):
        super().__init__()

    def show_properties(self):
        print(self.lab_name)
        print(self.lab_type)
        print(self.name)
        print(self.room)


general_hospital = Hospital()
general_hospital.show_properties()

print(Hospital.__mro__)
help(Hospital)