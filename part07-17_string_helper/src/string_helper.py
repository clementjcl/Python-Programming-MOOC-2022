from string import ascii_letters, digits, whitespace

def change_case(orig_string: str):
    return orig_string.swapcase()

def split_in_half(orig_string: str):
    i = (len(orig_string) // 2)
    return orig_string[:i], orig_string[i:]

def remove_special_characters(orig_string: str):
    new_list = []
    for i in orig_string:
        if i in ascii_letters:
            new_list.append(i)
        elif i in digits:
            new_list.append(i)
        elif i in whitespace:
            new_list.append(i)
    return "".join(new_list)


if __name__ == "__main__":
    my_string = "Well hello there!"

    print(change_case(my_string))

    p1, p2 = split_in_half(my_string)

    print(p1)
    print(p2)

    m2 = remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)