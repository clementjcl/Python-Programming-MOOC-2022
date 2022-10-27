# Write your solution here
def same_chars(string, index1, index2):
    if (len(string) <= index1 or len(string) <= index2):
        return False
    elif string[index1] != string[index2]:
        return False
    else:
        return True

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(len("aaaa"))
    print(same_chars("aaaa", 1, 2))
