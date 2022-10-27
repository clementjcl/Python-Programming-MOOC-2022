file_students = input("Student information: ")
file_exercises = input("Exercises completed: ")
file_exams = input("Exam points: ")

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

grade = {}
all_grade = {}
for dni, name in students.items():
    combined = (int(((sum(exercises[dni]) / 40) * 10))) + int(sum(exams[dni]))             
    a = 0
    limits = [15, 18, 21, 24, 28]
    while a < 5 and combined >= limits[a]:
        a += 1
    grade[dni] = a
    
    #Use the same loop to create a dictionary containing all information for a single student.
    all_grade[dni] = [(name[0] + " " + name[1]), int(sum(exercises[dni])), (int(((sum(exercises[dni]) / 40) * 10))), int(sum(exams[dni])), 
                      (int(((sum(exercises[dni]) / 40) * 10))) + int(sum(exams[dni])), grade[dni]]
    
first_line = ["name", "exec_nbr", "exec_pts.", "exm_pts.", "tot_pts.", "grade"]
print(f"{first_line[0]:30}{first_line[1]:10}{first_line[2]:10}{first_line[3]:10}{first_line[4]:10}{first_line[5]:10}") 
for dni in all_grade:
    print(f"{all_grade[dni][0]:30}{all_grade[dni][1]:<10}{all_grade[dni][2]:<10}{all_grade[dni][3]:<10}{all_grade[dni][4]:<10}{all_grade[dni][5]:<10}")
