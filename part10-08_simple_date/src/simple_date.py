class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year
        
    def __str__(self):
        return (f"{self.__day}.{self.__month}.{self.__year}")
        
    def __reverse(self):
        day_str = str(self.__day)
        month_str = str(self.__month)
        if len(str(self.__day)) == 1:
            day_str = "0" + str(self.__day)
        if len(str(self.__month)) == 1:  
            month_str = "0" + str(self.__month)  
        return int(str(self.__year) + month_str + day_str) 
    
    def __eq__(self, other):
        return self.__reverse() == other.__reverse()
    
    def __ne__(self, other):
        return self.__reverse() != other.__reverse()
            
    def __lt__(self, other):
        return self.__reverse() < other.__reverse()
    
    def __gt__(self, other):
        return self.__reverse() > other.__reverse()

    def __convert_days(self):
        return self.__year * 360 + self.__month * 30 + self.__day

    def __add__(self, other: int):
        total_days = self.__convert_days() + other
        year = (total_days // 360)
        month = ((total_days // 30) % 12)
        day = total_days % 30
        return SimpleDate(day, month, year)

    def __sub__(self, other: 'SimpleDate'):
        return abs(self.__convert_days() - other.__convert_days())


if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)
    d3 = SimpleDate(28, 12, 1985)

    print(d1)
    print(d2)
    print(d1 == d2)
    print(d1 != d2)
    print(d1 == d3)
    print(d1 < d2)
    print(d1 > d2)