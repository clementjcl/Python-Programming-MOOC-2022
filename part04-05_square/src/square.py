# Copy here code of line function from previous exercise
def line(length, char):
    if len(char) > 0:
        print(char[0] * length)
    else:
        print("*" * length)

def square(length: int, char: str):
    for i in range(length):
        line(length, char)
    
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "c")