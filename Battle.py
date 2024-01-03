class Battle:
    def __init__(self):
        self.__bounty = []

    def perform_battle(self, player1, player2):
        player1_card = self.__get_card(player1)
        player2_card = self.__get_card(player2)

        self.__perform_evaluation(player1, player2, player1_card, player2_card)
    
    def __get_card(self, player):
        card = player.cards[0]
        player.cards.remove(card)
        self.__bounty.append(card)
        return card
        
    def __perform_evaluation(self, player1, player2, card1, card2):
        self.__display_battle_cards(card1, card2)
        if (card1.card_value() == card2.card_value()):
            self.__war(player1, player2)
        if (card1.card_value() > card2.card_value()):
            self.__award_winner(player1)
        else:
            self.__award_winner(player2)

    def __award_winner(self, player):
        if (len(self.__bounty) == 0): return
        
        result = f"\n{player.name} Wins!"

        print(result)
        self.__display_bounty_cards()
        player.cards.extend(self.__bounty)
        self.__bounty.clear()

    def __war(self, player1, player2):
        print("\n*****************WAR*****************")
        self.__get_card(player1)
        self.__get_card(player1)
        war_card1 = self.__get_card(player1)

        self.__get_card(player2)
        self.__get_card(player2)
        war_card2 = self.__get_card(player2)

        self.__perform_evaluation(player1, player2, war_card1, war_card2)

    def __display_battle_cards(self, card1, card2):
        result = f"\nBattle Cards: {card1.kind} of {card1.suit} vs. {card2.kind} of {card2.suit}"
        print(result)
    
    def __display_bounty_cards(self):
        result = "\nBounty ..."

        for card in self.__bounty:
            result += f"\n{card.kind} of {card.suit}"
        
        print(result)