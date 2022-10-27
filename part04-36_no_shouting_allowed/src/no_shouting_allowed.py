def no_shouting(list): #list of strings
    result = []

    for i in list:
        if not i.isupper():
            result.append(i)
    return result  


if __name__ == "__main__":
    my_list = ["20", "100"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)