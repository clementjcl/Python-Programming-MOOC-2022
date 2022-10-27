def read_input(phrase: str, min: int, max: int):
    while True:
        try:
            number = int(input(phrase))
            if number > min and number < max:
                return number
            else:
                print(f"You must type in an integer between {min} and {max}")
        except:
            print(f"You must type in an integer between {min} and {max}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)  