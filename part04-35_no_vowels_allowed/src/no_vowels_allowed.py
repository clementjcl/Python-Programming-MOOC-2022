def no_vowels(string):
    vowels = "aeiou"
    result = ""
    for i in string:
        if i not in vowels:
            result += i
    return result
            

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))