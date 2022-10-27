def most_common_character(string): #string
    times = 0
    res = ""
    for i in string:
        if string.count(i) > times:
            times = string.count(i)
            result = i
    return result
        
        









if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))