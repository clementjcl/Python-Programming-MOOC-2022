text_input = input("Write text: ")

words = []
with open("wordlist.txt") as word_file:
    for row in word_file:
        parts = row.split(" ")
        words.append(parts[0].strip())

for word_to_check in text_input.split(' '):
    if word_to_check.casefold() in words:
        print(f"{word_to_check}", end=" ")
    if word_to_check.casefold() not in words:
        print(f"*{word_to_check}*", end=" ")