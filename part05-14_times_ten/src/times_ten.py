# Write your solution here
def times_ten(start_index: int, end_index: int):
    dictionary = {}
    for i in range(start_index, end_index + 1):
        dictionary[i] = i * 10
    return dictionary

if __name__ == "__main__":
    print(times_ten(1, 10))