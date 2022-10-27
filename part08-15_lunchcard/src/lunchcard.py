class LunchCard:
    def __init__(self, balance: float):
        self.balance = float(balance)

    def __str__(self):
        string = "The balance is " + str(round(self.balance, 2)) + " euros"
        return string

    def eat_lunch(self):
        self.balance -= 2.60
        if self.balance < 0:
            self.balance += 2.60
    
    def eat_special(self):
        self.balance -= 4.60
        if self.balance < 0:
            self.balance += 4.60
            
    def deposit_money(self, deposit):
        if deposit < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")
        else:
            self.balance += deposit
        
    
peter_card = LunchCard(20)
grace_card = LunchCard(30)
peter_card.eat_special()
grace_card.eat_lunch()
print(f"Peter: {peter_card}")
print(f"Grace: {grace_card}")
peter_card.deposit_money(20)
grace_card.eat_special()
print(f"Peter: {peter_card}")
print(f"Grace: {grace_card}")
peter_card.eat_lunch()
peter_card.eat_lunch()
grace_card.deposit_money(50)
print(f"Peter: {peter_card}")
print(f"Grace: {grace_card}")

