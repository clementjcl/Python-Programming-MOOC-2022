# Write your solution here
def who_won(game_board: list):
    player1 = 0
    player2 = 0
    for row in game_board:
        for item in row:
            if item == 1:
                player1 += 1
            elif item == 2:
                player2 += 1
    if player1 == player2:
        return 0
    elif player1 > player2:
        return 1
    else:
        return 2

