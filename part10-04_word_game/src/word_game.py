import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
        
    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
        else:
            return 0


class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        vowels = "aeiou"
        count_v1 = 0
        count_v2 = 0
        for char in player1_word:
            if char in vowels:
                count_v1 += 1
        for chara in player2_word:
            if chara in vowels:
                count_v2 += 1
        if count_v1 > count_v2:
            return 1
        elif count_v1 < count_v2:
            return 2
        else:
            return 0


class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
        
    def round_winner(self, player1_word: str, player2_word: str):
        loses_to = {"scissors": "paper",
                    "paper": "rock",
                    "rock": "scissors"
                    }
        
        if player2_word not in loses_to and player1_word not in loses_to:
            return 0
        elif player1_word not in loses_to:
            return 2
        elif player2_word not in loses_to:
            return 1

        if player1_word == loses_to[player2_word]:
            return 2
        elif player2_word == loses_to[player1_word]:
            return 1
        elif player1_word == player2_word:
            return 0
            

if __name__ == "__main__":
    p = RockPaperScissors(4)
    p.play()