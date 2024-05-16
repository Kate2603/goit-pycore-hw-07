from collections import UserDict
from datetime import datetime


# We create the Field class, which will be the base class for record fields
class Field:
    def __init__(self, value):
        self.value = value


    def __str__(self):
        return str(self.value)


# We create the Name class, which will
# be used to store the name of the contact
class Name(Field):
    pass


# We create the Phone class,
# which will be responsible for storing the phone number
class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must contain 10 digits")
        super().__init__(value)


# We create a Birthday class, which will be responsible for storing the birthday
class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(value)


# We create a Record class that will store contact information, including name, phone list, and birthday
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None


    def add_phone(self, phone):
        self.phones.append(Phone(phone))


    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]


    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break


    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None


    def add_birthday(self, birthday):
        if not self.birthday:
            self.birthday = Birthday(birthday)
        else:
            raise ValueError("Birthday already exists for this contact.")


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"


# We create an AddressBook class, which will be responsible for storing and managing records  
class AddressBook(UserDict):
    def __init__(self):
        self.data = {}


    def add_record(self, record):
        self.data[record.name.value] = record


    def find(self, name):
        return self.data.get(name)


    def delete(self, name):
        if name in self.data:
            del self.data[name]
   
    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming_birthdays = []
        for name, record in self.data.items():
            if record.birthday:
                birthday_date = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
                if (birthday_date - today).days <= 7:
                    upcoming_birthdays.append((record.name.value, birthday_date))
        return upcoming_birthdays


# Your original code
book = AddressBook()


john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
john_record.add_birthday("05.12.1985")  # Adding birthday


book.add_record(john_record)


jane_record = Record("Jane")
jane_record.add_phone("9876543210")
jane_record.add_birthday("12.05.1990")  # Adding birthday
book.add_record(jane_record)


for name, record in book.data.items():
    print(record)


upcoming_birthdays = book.get_upcoming_birthdays()
print("Upcoming birthdays:", upcoming_birthdays)

# Contact name: John, phones: 1234567890; 5555555555, birthday: 05.12.1985
# Contact name: Jane, phones: 9876543210, birthday: 12.05.1990
# Upcoming birthdays: [('John', datetime.date(1985, 12, 5)), ('Jane', datetime.date(1990, 5, 12))]