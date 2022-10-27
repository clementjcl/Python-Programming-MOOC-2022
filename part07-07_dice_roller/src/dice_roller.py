from random import sample
def roll(die: str):
    if die == "A":
        sides = [3, 3, 3, 3, 3, 6]
    elif die == "B":
        sides = [2, 2, 2, 5, 5, 5]
    elif die == "C":
        sides = [1, 4, 4, 4, 4, 4]
    return sample(sides, 1)[0]

def play(die1: str, die2: str, times: int):
    die1_res = 0
    die2_res = 0
    ties = 0
    for i in range(times):
        roll_die1 = roll(die1)
        roll_die2 = roll(die2)
        if roll_die1 > roll_die2:
            die1_res += 1
        elif roll_die2 > roll_die1:
            die2_res += 1
        else:
            ties += 1
    return (die1_res, die2_res, ties)
        

if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")
    print()       
    result = play("A", "C", 100)
    print(result)
    result = play("B", "B", 1000)
    print(result)