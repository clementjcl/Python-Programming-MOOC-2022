from string import punctuation

def most_common_words(filename: str, lower_limit: int):
    all_doc = []
    with open(filename) as new_file:
        for line in new_file:
            all_doc += "".join([char for char in line if char not in punctuation]).split()
            dic = {word : all_doc.count(word) for word in all_doc if all_doc.count(word) >= lower_limit}
    return(dic)

if __name__ == "__main__":
    most_common_words("comprehensions.txt", 3)