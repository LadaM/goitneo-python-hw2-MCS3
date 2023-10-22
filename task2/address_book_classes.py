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
    def __init__(self, name: Name, phones=[]) -> None:
        self.name = name
        self.phones = phones

    def add_phone(phone: str):
        pass

    def delete_phone(phone: str):
        pass

    def edit_phone(old_phone: str, new_phone: str):
        pass

    def find_phone(phone: Phone):
        pass


class AddressBook(UserDict):

    def find(name: str) -> Record:
        '''finds record by username'''
        pass

    def delete(name: str):
        '''deletes record with the name from address book'''
        pass

    def add(record: Record):
        '''adds record to the address book'''
        pass
