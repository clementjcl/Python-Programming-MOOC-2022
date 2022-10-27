def separate_list(numbers: list) -> tuple:
    pos_list = []
    neg_list = []
    for i in numbers:
        if i > 0:
            pos_list.append(i)
        elif i < 0:
            neg_list.append(i)
    return (pos_list, neg_list)


if __name__ == "__main__":  
    numbers = [1, -1, 2, -3, 5, -1, 1, 1, 9, -30, 40, 2, -9]
     
    numbers1, numbers2 = separate_list(numbers)
    print(numbers1)
    print(numbers2)