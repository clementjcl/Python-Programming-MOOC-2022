def find_words(search_term: str):
    result = []
    with open("words.txt") as words:
        for word in words:
            word = word.replace("\n", "")
                        
            if search_term.count(".") and len(search_term) == len(word):
                match = True
                for i in range(len(word)):
                    if search_term[i] != "." and search_term[i] != word[i]:
                        match = False
                if match:
                    result.append(word)
 
            elif search_term.endswith("*"):                
                if word.startswith(search_term[:len(search_term) - 1]):
                    result.append(word)
            elif search_term.startswith("*"):
                if word.endswith(search_term[1:]):
                    result.append(word)
            else: 
                if word == search_term:
                    result.append(word)
                  
    return result
                
            

if __name__ == "__main__":
    print(find_words(input("Enter a word: ")))