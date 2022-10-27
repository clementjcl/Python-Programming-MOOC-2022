def phone_book():
    book = {}
    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))
        if command == 3:
            print("quitting...")
            break
        name = input("name: ")
        if command == 2:
            number = input("number: ")
            book[name] = number
            print("ok!")
        if command == 1:
            if name not in book:
                print("no number")
            else:
                print(book[name])

phone_book()