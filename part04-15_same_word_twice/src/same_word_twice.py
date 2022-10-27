# Write your solution here
list = []

while True:
    word = input("Word: ")

    if list.count(word) > 0:
        print(f"You typed in {len(list)} different words")
        break
    else:
        list.append(word)
