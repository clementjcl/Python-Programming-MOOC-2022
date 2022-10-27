from datetime import datetime, timedelta
import csv

def cheaters():
    students_start = {}
    with open("start_times.csv") as start_file:
        for line in csv.reader(start_file, delimiter = ";"):
            students_start[line[0]] = line[1]
        #print(students_start)
    
    cheaters = []
    with open("submissions.csv") as submissions_file:
        for line in csv.reader(submissions_file, delimiter = ";"):
            start_time = datetime.strptime(f"{students_start[line[0]]}", "%H:%M")
            submission_time = datetime.strptime(f"{line[3]}", "%H:%M")
            total_time = submission_time - start_time
            if total_time.seconds > timedelta(hours=3).seconds and line[0] not in cheaters:
                cheaters.append(line[0])
    #print(cheaters)
    return cheaters

if __name__ == "__main__":
    cheaters()