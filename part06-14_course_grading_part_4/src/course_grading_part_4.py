file_students = input("Student information: ")
file_exercises = input("Exercises completed: ")
file_exams = input("Exam points: ")
file_course = input("Course information: ")

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
with open("results.csv", "w") as results_csv:
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

        results_csv.write(f"{dni};{all_grade[dni][0]};{all_grade[dni][5]}\n")


print(all_grade)
# Determining the header with the course information
with open(file_course) as course_data:
    first = course_data.readline()
    second = course_data.readline()
    first = first[6:len(first) - 1]
    second = second[15:]
    header = f"{first}, {second} credits"

#Creating file results.txt
with open("results.txt", "w") as results_txt:
    results_txt.write(f"{header}\n{len(header)*'='}\n")
    first_line = ["name", "exec_nbr", "exec_pts.", "exm_pts.", "tot_pts.", "grade"]
    results_txt.write(f"{first_line[0]:30}{first_line[1]:10}{first_line[2]:10}{first_line[3]:10}{first_line[4]:10}{first_line[5]:10}\n") 
    for dni in all_grade:
        results_txt.write(f"{all_grade[dni][0]:30}{all_grade[dni][1]:<10}{all_grade[dni][2]:<10}{all_grade[dni][3]:<10}{all_grade[dni][4]:<10}{all_grade[dni][5]:<10}\n")

#Creating file results.csv
#with open("results.csv", "w") as results_csv:
    #results_txt.write(f"{")