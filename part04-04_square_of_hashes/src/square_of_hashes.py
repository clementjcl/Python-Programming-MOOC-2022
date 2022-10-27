# Copy here code of line function from previous exercise
def line(length, char):
    if len(char) > 0:
        print(char[0] * length)
    else:
        print("*" * length)

def square_of_hashes(size):
    i = size
    while i > 0:
        line(size, "#")
        i -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
