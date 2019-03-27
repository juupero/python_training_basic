import random

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

class NoMoreCards(Exception):
    pass

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank}{self.suit}'

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank



class Hand:
    def __init__(self):
        """
        createa a list to store the cards in
        """
        self.cards = []

    def __str__(self):
        return ', '.join(
            str(card) for card in self.cards
        )

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        """
        First count ace as 1,
        after counting the rest
        check if adding 10 doesnt
        go over 21
        """
        value = 0
        has_ace = False
        for card in self.cards:
            rank = card.get_rank()
            if rank == 'A':
                has_ace = True
            value += VALUES[rank]
        if value < 12 and has_ace:
            return value + 10
        return value


class Deck:
    def __init__(self):
        """
        store all cards in a deck
        """
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        try:
            return self.deck.pop()
        except IndexError:
            raise NoMoreCards('No cards left in the deck!')

class Purse:
    def __init__(self, money):
        self.purse = money

    def lost_round(self):
        self.purse -= 1

    def won_round(self):
        self.purse += 1

def play_blackjack():
    given_input = ""
    while given_input != "exit":
        print("Are you ready to play Black Jack?!")
        print("Hell yes! [yes] / Hell no! [no]")
        given_input = input("> ")

        if given_input == "yes":
            print("How much money do you got?")
            money_amount = input("> ")

            purse = Purse(money_amount)




ten = Card('C', 'T')
ace = Card('D', 'A')

hand = Hand()
hand.add_card(ten)
hand.add_card(ace)

print(hand.get_value())