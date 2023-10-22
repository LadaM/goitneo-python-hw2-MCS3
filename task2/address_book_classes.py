from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name: str) -> None:
        self.name = name
        super().__init__(value=name)


class Phone(Field):
    def __init__(self, phone: str) -> None:
        self.phone = phone
        super().__init__(value=phone)

    def validate(self, phone_number) -> bool:
        pass


class Record:
    def __init__(self, name) -> None:
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        pass

    def delete_phone(self, phone: str):
        pass

    def edit_phone(self, old_phone: str, new_phone: str):
        pass

    def find_phone(self, phone: Phone):
        pass


class AddressBook(UserDict):

    def find(self, name: str) -> Record:
        '''finds record by username'''
        pass

    def delete(self, name: str):
        '''deletes record with the name from address book'''
        pass

    def add_record(self, record: Record):
        '''adds record to the address book'''
        pass


if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    # john = book.find("John")
    # john.edit_phone("1234567890", "1112223333")

    # print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    # found_phone = john.find_phone("5555555555")
    # print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
