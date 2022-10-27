class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.list = []

    def add_number(self, number:int):
        self.list.append(number)

    def count_numbers(self):
        return len(self.list)
    
    def get_sum(self):
        try:
            return sum(self.list)
        except:
            return 0

    def average(self):
        try:
            return sum(self.list)/len(self.list)
        except:
            return 0
        
        
all_num = NumberStats()
even_num = NumberStats()
odd_num = NumberStats()

while True:
    num = int(input("Please type in integer numbers: "))
    if num == -1:
        print(f"Sum of numbers: {all_num.get_sum()}")
        print(f"Mean of numbers: {all_num.average()}")
        print(f"Sum of even numbers: {even_num.get_sum()}")
        print(f"Sum of odd numbers: {odd_num.get_sum()}")
        break
    
    all_num.add_number(num)
    
    if num % 2 == 0:
        even_num.add_number(num)
    else:
        odd_num.add_number(num)





        

