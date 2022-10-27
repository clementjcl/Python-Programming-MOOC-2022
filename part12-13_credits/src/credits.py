from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

def sum_of_all_credits(attempts: list):
    return reduce(lambda credit_sum, attempt : credit_sum + attempt.credits, attempts, 0)

def sum_of_passed_credits(attempts: list):
    return reduce(lambda credit_sum, attempt : credit_sum + attempt.credits, filter(lambda attempt : attempt.grade >= 1, attempts), 0)

def average(attempts: list):
    attempts_ok = list(map(lambda attempt: attempt.grade, filter(lambda attempt : attempt.grade >= 1, attempts)))
    sum_grades = reduce(lambda reduced_sum, item : (reduced_sum + item), attempts_ok, 0)
    return sum_grades / len(attempts_ok)

if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)