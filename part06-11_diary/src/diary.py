while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = int(input("Function: "))
    if function == 0:
        print("Bye now!")
        break
    if function == 1:
        entry = input("Diary entry: ") + "\n"
        with open("diary.txt", "a") as diary:
            diary.write(entry)
            print("Diary saved")   
    if function == 2:
        print("Entries: ")
        with open("diary.txt") as diary:
            for row in diary:
                print(row)