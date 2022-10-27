# Write your solution here
def greatest_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(9, -1, 3)
    print(greatest)