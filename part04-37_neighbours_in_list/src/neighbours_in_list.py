def longest_series_of_neighbours(list): #list of integers
    neighbours = 1
    total = 1
    for i in range(len(list)-1):
        if i < len(list):
            if list[i] == (list[i+1] - 1) or list[i] == (list[i+1] + 1) :
                neighbours += 1
            else:
                neighbours = 1
            if neighbours > total:
                total = neighbours        
    return total




if __name__ == "__main__":
    my_list = [1, 2]
    print(longest_series_of_neighbours(my_list))