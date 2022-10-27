from datetime import datetime, timedelta
import csv

def final_points() -> dict:
    students = {}
    final_exam = {}
    with open("start_times.csv") as start_file:
        for line in csv.reader(start_file, delimiter = ";"):
            students[line[0]] = {
                                'startTime' : line[1], '1' : 0, '2' : 0, '3' : 0,
                                '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0                              
                                }
    
    with open("submissions.csv") as submissions_file:
        for line in csv.reader(submissions_file, delimiter = ";"):
            overtime = False
            start_time = datetime.strptime(f"{students[line[0]]['startTime']}", "%H:%M")
            submission_time = datetime.strptime(f"{line[3]}", "%H:%M")
            total_time = submission_time - start_time
            if total_time.seconds > timedelta(hours=3).seconds:
                overtime = True
            if students[line[0]][line[1]] == 0 and overtime == False:
                students[line[0]][line[1]] = int(line[2])
            elif students[line[0]][line[1]] < int(line[2]) and overtime == False:
                students[line[0]][line[1]] = int(line[2])
    
    for key, value in students.items():
        final_exam[key] = 0
        for i in range(1, 9):
            final_exam[key] += students[key][str(i)]          
    return final_exam

if __name__ == "__main__":
    print(final_points())