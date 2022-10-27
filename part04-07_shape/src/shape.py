# Copy here code of line function from previous exercise and use it in your solution
def line(length, char):
    if len(char) > 0:
        print(char[0] * length)
    else:
        print("*" * length)

def triangle(length_t, char_t):
    for i in range(1, length_t + 1):
        line(i, char_t)
    
def shape(length_t: int, char_t: str, height_r: int, char_r: str):
    triangle(length_t, char_t)
    for i in range(1, height_r+1):
        line(length_t, char_r)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 3, "*")

