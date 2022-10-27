from random import sample
from string import ascii_lowercase, digits


def generate_password(length, num=False, special=False):
    password = ""
    all_characters = ascii_lowercase
    if num:
        all_characters += digits
    if special:
        all_characters += "!?=+-()#"
    
    while True:    
        pass_list = sample(all_characters, length)
        for i in pass_list:
            if i in ascii_lowercase:
                return (password.join(pass_list))
            
            
if __name__ == "__main__":
    for i in range(10):
        print(generate_password(10, True, True))
    