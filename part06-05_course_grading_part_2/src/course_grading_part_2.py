if True:
    file_students = input("Student information: ")
    file_exercises = input("Exercises completed: ")
    file_exams = input("Exam points: ")
else:
    file_students = "students2.csv"
    file_exercises = "exercises2.csv"
    file_exams = "exam_points2.csv"

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


exams = {}
with open(file_exams) as exams_data:
    for line in exams_data:
        line = line.strip()
        parts3 = line.split(";")
        if parts3[0] == "id":
            continue
        id = parts3[0]
        exams[id] = []
        for exam in parts3[1:]:
            exams[id].append(int(exam))

#print(students)
#print(exercises)

grade = {}
for dni, name in students.items():
    combined = (int(((sum(exercises[dni]) / 40) * 10))) + int(sum(exams[dni]))             
    if combined >= 0 and combined <= 14:
        grade[dni] = 0
    elif combined >= 15 and combined <= 17:
        grade[dni] = 1
    elif combined >= 18 and combined <= 20:
        grade[dni] = 2
    elif combined >= 21 and combined <= 23:
        grade[dni] = 3
    elif combined >= 24 and combined <= 27:
        grade[dni] = 4
    elif combined >= 28:
        grade[dni] = 5

    
    print(f"{name[0]} {name[1]} {grade[dni]}")
#print(grade)
            