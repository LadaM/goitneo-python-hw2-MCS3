# goitneo-python-hw2-MCS3
Created for submission of the homework assignment Nr 2. Tier 1. Python Programming: Foundations and Best Practices
# Structure of the project
Using flat structure of the project because setup of relative or absolute imports took too much time
Folder `hw2` contains:
- task 1: `bot_assistant.py`
- task 2: `address_book_classes.py`
- `contacts.json` with several contacts stored to be used a a storage for bot_assistant
- `constants.py` storing constants used in bot_assistant.py
- `exceptions.py` with definitions of custom exceptions for both tasks
# Task 1
For the CLI created in the [HW1](https://github.com/LadaM/goitneo-python-hw-1-MCS3) add custom error handling using decorator functions. I've created custom exceptions `DuplicateEntry` and `ValueNotFound` that accept username as parameter and are raised when either username has already been added or such username hasn't been stored respectively. `FileNotFoundError` is a built-in error that I'm using when the file where the contacts are stored isn't there or is empty. `ValueError` is a built-in error that I'm catchning whenever parsing of the command hasn't been successful, raising a custom `InvalidCommand` exception that accepts optional command name argument to handle all such cases in one place. 
  ```python
  # decorator for exception handling
  def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except DuplicateEntry as error:
            return f"We alreay have a contact with name {error.name}"
        except ValueNotFound as error:
            return f"No contact for name {error.name} found"
        except FileNotFoundError:
            # if the file is empty there are no contacts to show
            return "We haven't stored any contacts yet"
    return inner
  
  # example of using the decorator
  @input_error
  def add_contact(args, contacts):
      name, phone = args
      contacts[name] = phone
      return "Contact added."
  ```
# Task 2
Create classes for future storing of the contact information of the users:
- `Field`: basic class for the creation of the fields in the address book
- `Name`: class storing a name of the contact, name is obligatory
- `Phone`: class for storing phone number, has a format validation - 10 digits
- `Record`: class for storing the information about the contact including name and list of phone numbers. **Supported operations:**
    * adding phone numbers
    * deleting phone numbers
    * editing phone numbers
    * searching phone number
- `AddressBook`: class for storing and managing records. **Supported operations:**
    * adding records
    * searching records by name
    * deleting records by name
