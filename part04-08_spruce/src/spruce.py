# Write your solution here
def spruce(size):
    print("a spruce!")
    i = 1
    row = ""
    while i <= size:
        row = "*" * (2*i-1)
        print(row.center(size*2-1))
        i += 1
    print("*".center(size*2))

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
