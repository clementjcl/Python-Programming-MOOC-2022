# write your solution here
def read_fruits():
    with open("fruits.csv") as new_file:
        fruits = {}
        for line in new_file:
            parts = line.split(";")
            fruits[parts[0]] = float(parts[1])
        #print(fruits)
        return fruits
            
            
            
            
if __name__ == "__main__":            
    read_fruits()
