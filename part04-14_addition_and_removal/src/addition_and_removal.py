# Write your solution here
list = []

while True:
    print(f"The list is now {list}")
    act = input("a(d)d, (r)emove or e(x)it: ")
  
    last_value_pos = len(list) - 1    
    
    if act == "d":
        if len(list) == 0:
            list.append(1)
        else:
            list.append(list[last_value_pos] + 1)
    elif act == "r":
        list.pop(last_value_pos)
    elif act == "x":
        print("Bye!")
        break
