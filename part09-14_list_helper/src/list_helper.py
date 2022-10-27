class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        if len(my_list) > 0:
            max_rep = 0
            for i in my_list:
                if my_list.count(i) > max_rep:
                    max_rep = my_list.count(i)
                    num = i
            return num
        else:
            return None
    
    
    @classmethod    
    def doubles(cls, my_list: list):
        num_rep = []
        for i in my_list:
            if i not in num_rep:
                if my_list.count(i) > 1:
                    num_rep.append(i)
                    
        return len(num_rep)

if __name__ == "__main__":
    numbers = []
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))