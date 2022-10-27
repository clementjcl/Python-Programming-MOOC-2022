class BankAccount:
    def __init__(self, owner: str, account_num: str, balance: float):
        self.__owner = owner
        self.__account_num = account_num
        self.__balance = balance
    
    def deposit(self, amount: float):
        self.__balance += amount
        self.__service_charge()
    
    def withdraw(self, amount: float):
        self.__balance -= amount
        self.__service_charge()
    
    @property
    def balance(self):
        return self.__balance
    
    def __service_charge(self):
        one_percent = self.__balance / 100
        self.__balance -= one_percent
        

if __name__ == "__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)