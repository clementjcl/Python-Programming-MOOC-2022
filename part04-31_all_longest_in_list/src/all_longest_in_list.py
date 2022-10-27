def all_the_longest (list): #list of strings
    length = 0
    longest = []
    for i in list:
        if len(i) > length:
          length = len(i)
    for i in list:
        if len(i) == length:
            longest.append(i)
    return longest


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']
