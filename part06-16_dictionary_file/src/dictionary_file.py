def write_file(file_name: str, word_f: str, word_e: str):
    with open(file_name, 'a') as dictionary:
        dictionary.write(f"{word_f};{word_e}\n")
    print("Dictionary entry added")
    
def search_file(file_name: str, word_search: str):
    word_search = word_search.lower()
    with open(file_name) as dictionary:
        for line in dictionary:
            line = line.replace("\n", "")
            line = line.strip()
            parts = line.split(";")
            word_f = parts[0].lower()
            word_e = parts[1].lower()
            if word_search in word_f or word_search in word_e:
                print(f"{word_f} - {word_e}")

file_name = "dictionary.txt"
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = input("Function: ")
    if function == "3":
        print("Bye!")
        break
    elif function == "1":
        word_f = input("The word in Finnish: ")
        word_e = input("The word in English: ")
        write_file("dictionary.txt", word_f, word_e)
    elif function == "2":
        word_search = input("Search term: ")
        search_file("dictionary.txt", word_search)