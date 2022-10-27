result = 0

print(f"{result}")

while True:
    cal_str = input("Type in a calculation or quit: ")
    if cal_str == "quit":
        break
    elif cal_str[0] == "-":
        result -= int(cal_str[1:])
    elif cal_str[0] == "+":
        result += int(cal_str[1:])

    print(f"{result}")