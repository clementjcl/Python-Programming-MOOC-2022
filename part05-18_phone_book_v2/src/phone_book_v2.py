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
            if name not in book:
                book[name] = []
            book[name].append(number)
            print("ok!")
        if command == 1:
            if name not in book:
                print("no number")
            else:
                for i in range(len(book[name])):
                    print(book[name][i])

phone_book()