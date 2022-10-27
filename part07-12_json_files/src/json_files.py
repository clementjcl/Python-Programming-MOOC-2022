import json

def print_persons(filename: str):
    with open(filename) as my_file:
        data = my_file.read()
    students = json.loads(data)
    
    for student in students:
        name = student['name']
        age = student['age']
        hobbies = ", ".join(student['hobbies'])
        print(f"{name} {age} years ({hobbies})")
        
if __name__ == "__main__":
    print_persons("file4.json")