if True:
    file_students = input("Student information: ")
    file_exercises = input("Exercises completed: ")
else:
    file_students = "students1.csv"
    file_exercises = "exercises1.csv"

students = {}
with open(file_students) as students_data:
    for line in students_data:
        line = line.strip() 
        parts = line.split(";")
        if parts[0] == "id":
            continue
        id = parts[0]
        students[id] = []
        for stud in parts[1:]:
            students[id].append(stud)

exercises = {}
with open(file_exercises) as exercises_data:
    for line in exercises_data:
        line = line.strip()
        parts2 = line.split(";")
        if parts2[0] == "id":
            continue
        id = parts2[0]
        exercises[id] = []
        for exer in parts2[1:]:
            exercises[id].append(int(exer))
            
for dni, name in students.items():
    if dni in exercises:
        print(f"{name[0]} {name[1]} {sum(exercises[dni])}")
            
        
        