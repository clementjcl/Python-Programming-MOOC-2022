def invert(dictionary: dict):
    inv_dict = {}
    for key in dictionary:
        val = dictionary[key]
        inv_dict[val] = key
    dictionary.clear()
    for key in inv_dict:
        dictionary[key] = inv_dict[key]
        

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    print(s)
    invert(s)
    print(s)