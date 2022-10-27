class Person:
    def __init__(self, name: str):
        self.__name = name
        self.__numbers = []
        self.__address = ""
    
    def name(self):
        return self.__name
    
    def numbers(self):
        return self.__numbers
    
    def address(self):
        if self.__address == "":
            return None
        else:
            return self.__address
    
    def add_number(self, number: str):
        if number not in self.__numbers:
            self.__numbers.append(number)
    
    def add_address(self, address: str):
        self.__address = address
    

class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)

    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name].numbers()

    def all_entries(self):
        return self.__persons


phonebook = PhoneBook()
phonebook.add_number("Eric", "02-123456")
phonebook.add_number("Emily", "06-987654")
print(phonebook.get_entry("Eric"))
print(phonebook.get_entry("Emily"))

        
    
    

