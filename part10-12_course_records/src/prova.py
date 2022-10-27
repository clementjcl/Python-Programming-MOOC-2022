class Course:
    def __init__(self, name: str):
        if len(name) > 1:
            self.__name = name
        else:
            raise ValueError('Name value must be more than 2 characters')
        self.__grade = 0
        self.__credit = -1
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name: str):
        if len(name) > 1:
            self.__name = name
        else:
            raise ValueError('Name value must be more than 2 characters')
    
    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, grade: int):
        if grade > 0 and grade <= 5:
            self.__grade = grade
        else:
            raise ValueError('Grade value must be between 1-5 (included)')
 
    @property
    def credit(self):
        return self.__credit
    
    @credit.setter
    def credit(self, credit: int):
        if credit >= 0:
            self.__credit = credit
        else:
            raise ValueError('Credits value must be a positive value!')

python = Course('Python')
java = Course('Java')
c = Course('C++')
scada = Course('Scada')
c.grade = 1
c.credit = 9
python.grade = 5
python.credit = 14
java.grade = 3
java.credit = 5
scada.grade = 4
scada.credit = 2
print(f"{python.name} ({python.credit} cr) grade {python.grade}")
print(f"{java.name} ({java.credit} cr) grade {java.grade}")
print(f"{c.name} ({c.credit} cr) grade {c.grade}")
print(f"{scada.name} ({scada.credit} cr) grade {scada.grade}")

di = {'python': python,
      'java': java,
      'c': c,
      'scada': scada}


def statistics(courses: dict):
    completed = len(courses)
    total_credits = 0
    total_grade = 0
    grade_1 = 0
    grade_2 = 0
    grade_3 = 0
    grade_4 = 0
    grade_5 = 0
    for key, value in courses.items():
        total_credits += value.credit
        total_grade += value.grade
        if value.grade == 1:
            grade_1 += 1
        elif value.grade == 2:
            grade_2 += 1
        elif value.grade == 3:
            grade_3 += 1
        elif value.grade == 4:
            grade_4 += 1
        elif value.grade == 5:
            grade_5 += 1
    
    print(f"{completed} completed courses, a total of {total_credits} credits")
    print(f"mean {total_grade / completed}")
    print('grade distribution')
    print('5: ' + ('x' * grade_5))
    print('4: ' + ('x' * grade_4))
    print('3: ' + ('x' * grade_3))
    print('2: ' + ('x' * grade_2))
    print('1: ' + ('x' * grade_1))    

statistics(di)