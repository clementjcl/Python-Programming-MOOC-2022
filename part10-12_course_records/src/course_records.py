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
        if credit > 0:
            self.__credit = credit
        else:
            raise ValueError('Credits value must be a positive value!')


class CourseRecords:
    def __init__(self):
        self.__courses = {}
    
    def add_course(self, name: str, grade: int, credit: int):
        if not name in self.__courses:
            self.__courses[name] = Course(name)
        if grade >= self.__courses[name].grade: 
            self.__courses[name].grade = grade
            self.__courses[name].credit = credit

    def get_data(self, name: str):
        if not name in self.__courses:
            return None
        return f"{self.__courses[name].name} ({self.__courses[name].credit} cr) grade {self.__courses[name].grade}"

    def statistics(self):
        completed = len(self.__courses)
        total_credits = 0
        total_grade = 0
        grade_1 = 0
        grade_2 = 0
        grade_3 = 0
        grade_4 = 0
        grade_5 = 0
        for key, value in self.__courses.items():
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
        if completed == 0:
            print('mean 0')
        else:
            print(f"mean {round(total_grade / completed, 1)}")
        print('grade distribution')
        print('5: ' + ('x' * grade_5))
        print('4: ' + ('x' * grade_4))
        print('3: ' + ('x' * grade_3))
        print('2: ' + ('x' * grade_2))
        print('1: ' + ('x' * grade_1))    

class CourseRecordsApplication:
    def __init__(self):
        self.__courserecords = CourseRecords()
    
    def help(self):
        print('')
        print('1 add course')
        print('2 get course data')
        print('3 statistics')
        print('0 exit')
        
    def add_course(self):
        name = input('course: ')
        grade = int(input('grade: '))
        credit = int(input('credits: '))
        self.__courserecords.add_course(name, grade, credit)
    
    def get_data(self):
        name = input('course: ')
        data = self.__courserecords.get_data(name)
        if data == None or data == "":
            print('no entry for this course')
        else:
            print(data)
    
    def statistics(self):
        self.__courserecords.statistics()
       
    def execute(self):
        self.help()
        while True:
            print("")
            command = input('command: ')
            if command == '0':
                break
            elif command == '1':
                self.add_course()
            elif command == '2':
                self.get_data()
            elif command == '3':
                self.statistics()
            else:
                self.help()

# Execution / Main program
application = CourseRecordsApplication()
application.execute()