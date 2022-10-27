def matrix_sum():
    with open("matrix.txt") as new_file:
        line_temp = []
        result = 0
                
        for line in new_file:
            line = line.replace("\n", "")
            line_temp = line.split(",")
                    
            for i in range(len(line_temp)):
                line_temp[i] = int(line_temp[i])
                
            result += sum(line_temp)
        return result
    
def matrix_max():
    with open("matrix.txt") as new_file:
        line_temp = []
        line_max = ""
        max_val = ""
         
        for line in new_file:
            line = line.replace("\n", "")
            line_temp = line.split(",")

            for i in range(len(line_temp)):
                if line_temp[i] > max_val:
                    max_val = line_temp[i]

        return int(max_val)

def row_sums():
    with open("matrix.txt") as new_file:
        line_temp = []
        result = []
              
        for line in new_file:
            line = line.replace("\n", "")
            line_temp = line.split(",")
                    
            for i in range(len(line_temp)):
                line_temp[i] = int(line_temp[i])
            
            result.append(sum(line_temp))
        return result
            

if __name__ == "__main__":            
    print("Total sum: ", matrix_sum())  
    print("Max val:", matrix_max())
    print(row_sums())
          
        