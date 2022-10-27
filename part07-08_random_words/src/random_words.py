import random

def words(n: int, beginning: str):
    list_words = []
    with open("words.txt") as all_words:
        for line in all_words:
            line = line.replace("\n", "")
            if line.startswith(beginning):
                list_words.append(line)
    
    if len(list_words) < n:
        raise ValueError("Not enough suitable words can be found!")
        
    return random.sample(list_words, n)
        


if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)