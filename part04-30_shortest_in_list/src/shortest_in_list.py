# Write your solution here
def shortest(list): #list of strings
    shortest = ""
    for i in list:
        if len(i) < len(shortest) or shortest == "":
            shortest = i
    return shortest




if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)