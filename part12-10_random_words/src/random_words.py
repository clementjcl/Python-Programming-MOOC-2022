import random

def word_generator(characters: str, length: int, amount: int):
    return ("".join(random.choices(characters, k = length)) for j in range(amount))



if __name__ == "__main__":    
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)