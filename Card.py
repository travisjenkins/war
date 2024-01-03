class Card:
    def __init__(self, suit, kind):
        self.suit = suit
        self.kind = kind

    def card_value(self):
        value = 0

        if (self.kind == "Jack"):
            value = 11
        elif (self.kind == "Queen"):
            value = 12
        elif (self.kind == "King"):
            value = 13
        elif (self.kind == "Ace"):
            value = 14
        else:
            value = int(self.kind)

        return value