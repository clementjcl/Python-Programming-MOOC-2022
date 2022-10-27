def input_results():
    exam_exercises = []
    result_int = []
    all_points_str = ""
    while True:
        in_student = input("Exam points and exercises completed: ")
        if in_student == "":
            print("Statistics: ")
            break
        all_points_str += " " + in_student
    exam_exercises = all_points_str.split()
    for points in exam_exercises:
        result_int.append(int(points))
    #print(result_int)
    return result_int

def statistics(list):
    combined = []
    #print(list)
    for i in range(len(list)):
        if i % 2 != 0:
            list[i] = list[i] // 10
            combined.append(list[i] + list[i - 1])
        
    #print(list)
    #print(combined)

    grade = []
    for i in combined:
        if i >= 0 and i <= 14:
            grade.append(0)
        elif i >= 15 and i <= 17:
            grade.append(1)
        elif i >= 18 and i <= 20:
            grade.append(2)
        elif i >= 21 and i <= 23:
            grade.append(3)
        elif i >= 24 and i <= 27:
            grade.append(4)
        elif i >= 28 and i <= 30:
            grade.append(5)
    #print(grade)
    n = 0
    for i in range(len(list)):
        if i % 2 == 0:
            if list[i] < 10:
                grade[n] = 0
                n += 1
            else:
                n += 1
    #print(grade)
    average = sum(combined) / len(combined)
    print(f"Points average: {average:.1f}")
    percent = (len(grade) - grade.count(0)) / len(grade) * 100
    print(f"Pass percentage: {percent:.1f}")
    print("Grade distribution: ")
    
    print("    5: " + "*" * grade.count(5))
    print("    4: " + "*" * grade.count(4))
    print("    3: " + "*" * grade.count(3))
    print("    2: " + "*" * grade.count(2))
    print("    1: " + "*" * grade.count(1))
    print("    0: " + "*" * grade.count(0))
        
  

# Main function
def main():
    print("")


# Calling functions
results = input_results()
statistics(results)
main()




