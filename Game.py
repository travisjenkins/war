from Player import Player
from Deck import Deck
from Battle import Battle

class Game:
    def __init__(self, player1_name, player2_name):
        self.__player1 = Player(player1_name)
        self.__player2 = Player(player2_name)

    def play(self):
        print("Dealing cards ...\n")
        Deck().deal(self.__player1, self.__player2)
        print("\nBegin battle ...")
        game_round = 0
        
        while (len(self.__player1.cards) != 0 and len(self.__player2.cards) != 0):
            print("\nPlayer 1 Cards:", len(self.__player1.cards), "\nPlayer 2 Cards:", len(self.__player2.cards), "\n")
            Battle().perform_battle(self.__player1, self.__player2)
            game_round += 1

            if (game_round > 24):
                break

            print("\n---------END ROUND:", game_round, "---------")

        self.__determine_winner()

    def __determine_winner(self):
        print("\n-------------RESULTS-------------")
        result = ""
        if (len(self.__player1.cards) > len(self.__player2.cards)):
            result += "\nPlayer 1 wins!"
        elif (len(self.__player2.cards) > len(self.__player1.cards)):
            result += "\nPlayer 2 wins!"
        else:
            result += "\nIt's a tie!"
        result += f"\n\nPlayer 1: {len(self.__player1.cards)} \nPlayer 2: {len(self.__player2.cards)}"
        print(result)

def play_war():
    game = Game("Player 1", "Player 2")
    game.play()

play_war()