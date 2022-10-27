# Write your solution here
num_items = int(input("How many items: "))
list = []

i = 1
while i <= num_items:
    item = int(input(f"Item {i}: "))
    list.append(item)
    i += 1
print(list)
