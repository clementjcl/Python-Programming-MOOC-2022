# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        largest = ""
        for line in new_file:
            line = line.replace("\n", "")
            if largest < line:
                largest = line
    return(int(largest))
            
if __name__ == "__main__":            
    largest()
