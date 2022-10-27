def add_student(students: dict, name: str):
    students[name] = []
   
def add_course(students: dict, name: str, course: tuple):
    if name in students and course[1] > 0:
        if len(students[name]) == 0:
            students[name].append(course)
        else:
            l = len(students[name])
            for x in range(l):
                if course[0] != students[name][x][0]:
                    students[name].append(course)
                    return
                else:
                    if course[1] > students[name][x][1]:
                        students[name].pop(x)
                        students[name].append(course)
                                               
def print_student(students: dict, name: str):
    if name not in students:
        print(f"{name}: no such person in the database")
    else:
        grade_sum = 0
        print(f"{name}:")
        if students[name] == []:
            print(f" no completed courses")
        else:
            print(f" {len(students[name])} completed courses:")
            for course in range(len(students[name])):
                print(f"  {students[name][course][0]} {students[name][course][1]}")
                grade_sum += students[name][course][1]
            print(f" average grade {grade_sum / len(students[name])}")

def summary(students: dict):
    print(f"students {len(students)}")
    total = 0
    for key in students:
        if total < len(students[key]):
            total = len(students[key])
            name = key
    print(f"most courses completed {total} {name}")
    
    grade_sum = 0
    average = 0
    for key in students:
        grade_sum = 0
        for course in range(len(students[key])):
            grade_sum += students[key][course][1]
        if average < grade_sum / len(students[key]):
            average = grade_sum / len(students[key])
            name_av = key
    print(f"best average grade {average} {name_av}")
    

if __name__ == "__main__":
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    summary(students)