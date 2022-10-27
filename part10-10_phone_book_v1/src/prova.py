# WRITE YOUR SOLUTION HERE:
class PhoneBook:
    def __init__(self):
        self.__persons = {
            'Eric': ['1234', '5678'],
            'Ana': ['3456', '7890']
        }

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            # add a new dictionary entry with an empty list for the numbers
            self.__persons[name] = []

        self.__persons[name].append(number)

    def get_numbers(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]
    
    def get_names(self, number: str):
        print(self.__persons)
        for key, value in self.__persons.items():
            print(value)
            if number in value:
                return key
        return None
            
phone = PhoneBook()
phone.add_number('Juana', '8909')
print(phone.get_names("8909"))