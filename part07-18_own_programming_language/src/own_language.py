import string

def run(program: list) -> list:
    output = []
    list_lines = []
    jumps = {}
    var = dict.fromkeys(string.ascii_uppercase, 0)
    
    k = 0
    for line in program:
        line = line.replace(":", "")
        line = line.split(" ")
        list_lines.append(line)
        if line[0].islower():
            jumps[line[0]] = k
        k += 1
    
    location = 0
    i = 0
    while i < len(program):
        row = program[i].split(" ") 
        if "PRINT" in row: #PRINT [value]
            if row[1] in string.ascii_uppercase:
                output.append(int(var[row[1]]))
            else:
                output.append(int(row[1]))          
        elif "MOV" in row: #MOV [variable] [value]
            if row[2] in string.ascii_uppercase:
                var[row[1]] = int(var[row[2]])
            else:
                var[row[1]] = int(row[2])              
        elif "ADD" in row: #ADD [variable] [value]
            if row[2] in string.ascii_uppercase:
                var[row[1]] += int(var[row[2]])
            else:
                var[row[1]] += int(row[2])             
        elif "SUB" in row: #SUB [variable] [value]
            if row[2] in string.ascii_uppercase:
                var[row[1]] -= int(var[row[2]])
            else:
                var[row[1]] -= int(row[2])          
        elif "MUL" in row: #MUL [variable] [value]
            if row[2] in string.ascii_uppercase:
                var[row[1]] *= int(var[row[2]])
            else:
                var[row[1]] *= int(row[2])         
        elif "JUMP" in row[0]: #JUMP [location]
            i = jumps[row[1]]      
        elif "IF" in row[0]: #IF [condition] JUMP [location]
            if row[1] in string.ascii_uppercase:
                variable1 = int(var[row[1]])
            else:
                variable1 = int(row[1])
            if row[3] in string.ascii_uppercase:
                variable2 = int(var[row[3]])
            else:
                variable2 = int(row[3])
            if row[2] == "==" and variable1 == variable2:
                    i = jumps[row[5]]
            elif row[2] == "!=" and variable1 != variable2:
                    i = jumps[row[5]]
            elif row[2] == "<" and variable1 < variable2:
                    i = jumps[row[5]]
            elif row[2] == "<=" and variable1 <= variable2:
                    i = jumps[row[5]]
            elif row[2] == ">" and variable1 > variable2:
                    i = jumps[row[5]]
            elif row[2] == ">=" and variable1 >= variable2:
                    i = jumps[row[5]]
        elif "END" in row:
            return output
        else: #[location]
            if row[0] in jumps:
                i = jumps[row[0]]
            
        i += 1
    return output

if __name__ == "__main__":
    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)