import string
import random

def generate_password(length, num=False, special=False):
    password = ""
    while True: 
        all_characters = string.ascii_lowercase
        if num == True:
            all_characters += string.digits
        if special == True:
            all_characters += string.punctuation
        
        pass_list = random.sample(all_characters, length)
        
        for i in pass_list:
            if i in string.ascii_lowercase:
                return (password.join(pass_list))
            
    
    
    
if __name__ == "__main__":
    for i in range(10):
        print(generate_password(2))