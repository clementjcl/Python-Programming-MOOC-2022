# Copy here code of line function from previous exercise
def line(length, char):
    if len(char) > 0:
        print(char[0] * length)
    else:
        print("*" * length)

def box_of_hashes(height):
    while height > 0:
        line(10, "#")
        height -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
