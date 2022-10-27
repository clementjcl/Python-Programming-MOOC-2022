import urllib.request
import json

def retrieve_all():
    url_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    url_json = json.loads(url_request.read())
       
    courses_active = []
    for course in url_json:
        if course['enabled'] == True:
            sing_course_act = (course['fullName'], course['name'], course['year'], sum(course['exercises']))
            courses_active.append(sing_course_act)
    return courses_active

def retrieve_course(course_name: str):
    url_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    url_json = json.loads(url_request.read())
      
    students_max = 0
    hours_total = 0
    exercises_total = 0
    for key, value in url_json.items():
        if value['students'] > students_max:
            students_max = value['students']
        hours_total += value['hour_total']
        exercises_total += value['exercise_total']
            
    return {
            'weeks' : len(url_json),
            'students' : students_max,
            'hours' : hours_total,
            'hours_average' : hours_total // students_max,
            'exercises' : exercises_total,
            'exercises_average' : exercises_total // students_max
            }        
        

if __name__ == "__main__":
    retrieve_all()
    print(retrieve_course('docker2019'))
    
    