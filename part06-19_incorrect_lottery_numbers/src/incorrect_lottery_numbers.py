def filter_incorrect():
    open("correct_numbers.csv", "w").close()
    all_lottery = {}
    correct_lottery = {}
    with open("lottery_numbers.csv") as file_num:
        for line in file_num:
            line = line.replace("\n", "")
            week_num = line.split(";")
            all_lottery[week_num[0]] = week_num[1].split(",")
    
    for key, value in all_lottery.items():
        error = False
        try:
            check_key = key.split(" ")
            if check_key[0] != "week" or int(check_key[1]) != int(check_key[1]):
                print(f"'week' is not written properly: ({check_key[0]} {check_key[1]})")
                error = True       
        except ValueError:
            print(f"name of week ({check_key[0]} {check_key[1]}) is not valid")
            error = True
     
        for i in value:
            try:    
                if int(i) > 39 or int(i) < 1:
                    print(f"numbers are too small (<1) or too large (>39): {key} {value}")
                    error = True
            except ValueError:
                print(f"one or more numbers are not correct: ({key} {value}")
                error = True
            if value.count(i) > 1:
                print(f"same number {i} appears twice: ({key} {value})")                        
                error = True
          
        if error == False:         
            correct_file = open("correct_numbers.csv", "a")
            try:
                correct_file.write(f"{key};{value[0]},{value[1]},{value[2]},{value[3]},{value[4]},{value[5]},{value[6]}\n")
            except IndexError:
                print(f"too few numbers (must be 7): ({key} {value})")
                error = True
        
if __name__ == "__main__":        
    filter_incorrect()