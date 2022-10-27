# WRITE YOUR SOLUTION HERE:
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []
        
    def __str__(self):
        return f"{self.name} {len(self.subordinates)}"

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)
        
    
        
        

def count_subordinates(employee: 'Employee'):
    if employee is None:
        return
    total_subor = len(employee.subordinates)
    for s in employee.subordinates:
        total_subor += (count_subordinates(s))
    return total_subor
    


if __name__ == "__main__":
    t1 = Employee("Sally")
    t2 = Employee("Matthew")
    t3 = Employee("Eric")
    t4 = Employee("Andy")
    t5 = Employee("Emily")
    t6 = Employee("James")
    t7 = Employee("John")
    t8 = Employee("Tina")
    t9 = Employee("Theodore")
    t10 = Employee("Arthur")
    t11 = Employee("Jack")
    t12 = Employee("Lea")
    t1.add_subordinate(t3)
    t1.add_subordinate(t4)
    t1.add_subordinate(t7)
    t3.add_subordinate(t8)
    t3.add_subordinate(t9)
    t3.add_subordinate(t10)
    t3.add_subordinate(t12)
    t9.add_subordinate(t2)
    t2.add_subordinate(t5)
    t2.add_subordinate(t11)
    t5.add_subordinate(t6)
    print(f"T1 :: {count_subordinates(t1)}")
    print(f"T4 :: {count_subordinates(t4)}")
    print(f"T5 :: {count_subordinates(t5)}")