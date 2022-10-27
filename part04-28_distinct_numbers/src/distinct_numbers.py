def distinct_numbers(my_list: list):
    results = []
    for item in my_list:
        if item not in results:
            results.append(item)
 
    results.sort()
    return results

if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 2, 3]
    print(distinct_numbers(my_list)) # [1, 2, 3]