# Write your solution here
list = [1, 2, 3, 4, 5]

while True:
    i = int(input("Index: "))
    if i == -1 or i > len(list):
        break
    else:
        new_v = int(input("New value: "))
        list[i] = new_v
        print(list)