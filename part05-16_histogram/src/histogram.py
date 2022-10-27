def histogram(string: str):
    dictionary = {}
    for letter in string:
        if letter not in dictionary:
            dictionary[letter] = 0
        dictionary[letter] += 1
    for key, value in dictionary.items():
        print(key, "*" * value)
    return dictionary



if __name__ == "__main__":
    histogram("abba")
    histogram("statistically")

    