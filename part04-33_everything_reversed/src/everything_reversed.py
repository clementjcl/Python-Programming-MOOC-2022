def everything_reversed(list): #list of strings
    reversed_list = []
    for i in list:
        name_rev = i[::-1]
        reversed_list.append(name_rev)
    return reversed_list[::-1]


if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)