def store_personal_data(person: tuple):
    with open("people.csv", "a") as people_file:
        line = f"{person[0]};{person[1]};{person[2]}"
        people_file.write(line + "\n")
        