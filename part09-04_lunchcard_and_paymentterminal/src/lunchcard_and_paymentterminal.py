# WRITE YOUR SOLUTION HERE:

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False


class PaymentTerminal:
    def __init__(self):
        self.funds = 1000
        self.lunches = 0
        self.specials = 0
        self.lunch_reg_price = 2.50
        self.lunch_spe_price = 4.30

    def eat_lunch(self, payment: float):
        change = payment
        if payment >= self.lunch_reg_price:
            change = payment - self.lunch_reg_price
            self.funds += self.lunch_reg_price
            self.lunches += 1
        return change   

    def eat_special(self, payment: float):
        change = payment
        if payment >= self.lunch_spe_price:
            change = payment - self.lunch_spe_price
            self.funds += self.lunch_spe_price
            self.specials += 1
        return change

    def eat_lunch_lunchcard(self, card: LunchCard):
        if card.balance >= self.lunch_reg_price:
            card.balance -= self.lunch_reg_price
            self.lunches += 1
            return True
        return False

    def eat_special_lunchcard(self, card: LunchCard):
        if card.balance >= self.lunch_spe_price:
            card.balance -= self.lunch_spe_price
            self.specials += 1
            return True
        return False

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.balance += amount
        self.funds += amount
    
    
if __name__ == "__main__":
    exactum = PaymentTerminal()

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)