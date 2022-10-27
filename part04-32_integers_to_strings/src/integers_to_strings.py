def formatted(list): #list of floating
    list_str = []
    for i in list:
        list_str.append(f"{i:.2f}")
    return list_str



if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)