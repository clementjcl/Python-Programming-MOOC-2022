import random

def lottery_numbers(amount: int, lower: int, upper: int):
    pool_numbers = list(range(lower, upper + 1))
    weekly_draw = random.sample(pool_numbers, amount)
    return sorted(weekly_draw)           


if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)
    print(lottery_numbers)