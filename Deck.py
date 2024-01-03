from Card import Card
import random

class Deck:
    def __init__(self):
        self.__deck = []
        suits = [ "Clubs", "Spades", "Diamonds", "Hearts" ]
        kinds = [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace" ]

        for suit in suits:
            for kind in kinds:
                self.__deck.append(Card(suit, kind))

    def deal(self, player1, player2):
        while (len(self.__deck) > 0):
            self.__deal_card(player1)
            self.__deal_card(player2)

    def __deal_card(self, player):
        card = self.__deck[random.randint(0, len(self.__deck) - 1)]
        player.cards.append(card)
        self.__deck.remove(card)

        print(f"{player.name} is dealt the {card.kind} of {card.suit}")
