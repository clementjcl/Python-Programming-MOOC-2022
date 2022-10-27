def palindromes(string):
    forward = ""
    reverse = ""
    for i in range(len(string)):
        forward += string[i]
    for i in reversed(range(len(string))):
        reverse += string[i]
    if forward == reverse:
        return True
    else:
        return False

def ask_palindromes():
    while True:
        word = input("Please type in a palindrome: ")
        if palindromes(word):
            print(f"{word} is a palindrome!")
            break
        print(f"that wasn't a palindrome")

ask_palindromes()