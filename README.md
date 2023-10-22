# goitneo-python-hw2-MCS3
Created for submission of the homework assignment Nr 2. Tier 1. Python Programming: Foundations and Best Practices

# Task 1
For the CLI created in the [HW1](https://github.com/LadaM/goitneo-python-hw-1-MCS3) add custom error handling using decorator functions
  ```python
  @input_error
  def add_contact(args, contacts):
      name, phone = args
      contacts[name] = phone
      return "Contact added."
  ```
# Task 2
Create classes for future storing of the contact information of the users:
- Field: basic class for the creation of the fields in the address book
- Name: class storing a name of the contact, name is obligatory
- Phone: class for storing phone number, has a format validation - 10 digits
- Record: class for storing the information about the contact including name and list of phone numbers. **Supported operations:**
    * adding phone numbers
    * deleting phone numbers
    * editing phone numbers
    * searching phone number
- AddressBook: class for storing and managing records. **Supported operations:**
    * adding records
    * searching records by name
    * deleting records by name
