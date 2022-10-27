import string
def separate_characters(my_string: str):
    ascii_string = ""
    punct_string = ""
    other_string = ""
    for character in my_string:
        if character in string.ascii_letters:
            ascii_string += character
        elif character in string.punctuation:
            punct_string += character
        else:
            other_string += character
    return (ascii_string, punct_string, other_string)
    

        
if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])