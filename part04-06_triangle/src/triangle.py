# Copy here code of line function from previous exercise
def line(length, char):
    if len(char) > 0:
        print(char[0] * length)
    else:
        print("*" * length)

def triangle(size):
    len = 0
    while len < size:
        len += 1
        line(len, "#")
        
# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
