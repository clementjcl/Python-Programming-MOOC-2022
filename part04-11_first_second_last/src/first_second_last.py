# Write your solution here
def find_word(str, num):
    index = 0
    word = ""
    counter = 0
    while index < len(str):
        if str[index] == " ":
            counter += 1
            index += 1
            if counter == num:
                break
            word = ""
        else:
            word += str[index]
            index += 1
    return word

def first_word(str):
    return find_word(str, 1)

def second_word(str):
    return find_word(str, 2)

def last_word(str):
    return find_word(str, 0)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "first second third"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))