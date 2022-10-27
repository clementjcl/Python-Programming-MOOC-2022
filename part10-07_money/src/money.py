# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents
        self.__value = self.__euros + self.__cents/100

    def __str__(self):
        return f"{self.__value:.2f} eur"
    
    def __eq__(self, another):
        return self.__value == another.__value
    
    def __lt__(self, another):
        return self.__value < another.__value
    
    def __gt__(self, another):
        return self.__value > another.__value
    
    def __ne__(self, another):
        return self.__value != another.__value
    
    def __add__(self, another):
        result = self.__value + another.__value
        euro, cents = divmod(result, 1)
        new_obj = Money(int(euro), cents * 100)
        return new_obj
    
    def __sub__(self, another):
        if self.__value - another.__value > 0:
            result = self.__value - another.__value
            euro, cents = divmod(result, 1)
            new_obj = Money(int(euro), cents * 100)
        else:
            raise ValueError(f"a negative result is not allowed")
        return new_obj


if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1
    
    print(e5)