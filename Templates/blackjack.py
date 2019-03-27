SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J':10,
    'Q':10,
    'K':10
}


class Card:
    def __init__(self, suit, rank):
        pass

    def __str__(self):
        pass

    def get_suit(self):
        pass

    def get_rank(self):
        pass



class Hand:
    def __init__(self):
        """
        createa a list to store the cards in
        """

    def __str__(self):
        pass

    def add_card(self, card):
        pass

    def get_value(self):
        """
        First count ace as 1,
        after counting the rest
        check if adding 10 doesnt
        go over 21
        """
        pass


class Deck:
    def __init__(self):
        """
        store all cards in a deck
        """

    def shuffle(self):
        pass

    def deal_card(self):
        pass

