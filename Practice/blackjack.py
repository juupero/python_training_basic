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

    def __len__(self):
        return len(self.deck)

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

    def __str__(self):
        return str(self.purse)

    def __repr__(self):
        return self.purse

    def lost_round(self, bet):
        self.purse -= bet

    def won_round(self, bet):
        self.purse += bet

class BlackjackTable():

    def __init__(self):
        given_input = ""
        while given_input != "exit":
            print("Are you ready to play Black Jack?!")
            print("Hell yes! [yes] / Hell no! [no]")
            given_input = input("> ")
            if given_input == "yes":
                game = Game()
            else:
                print("Why are you here then?")
                break
        print("Get out of here!")



class Game():

    def __init__(self):

        print("How much money do you got?")
        money_amount = input("> ")
        self.purse = Purse(int(money_amount))
        print("\nOkay Hotshot, let's play! \n**dealer starts shuffling cards**")
        self.deck = Deck()
        self.deck.shuffle()
        while self.purse.__repr__() > 0:
            self.play_round()
            if len(self.deck) < 10:
                print("Oh, we need to reshuffle the cards!")
                self.deck = Deck()
        print("\nYou ran out of money. Now get out!\n")
        exit()


    def play_round(self):
        print(f"\nYou got {self.purse} in your purse. I hope you are ready Hotshot. \nPlace your bets! \n")
        self.bet = int(input("> "))
        self.player_hand, self.dealer_hand = Hand(), Hand()
        self.player_hand.add_card(self.deck.deal_card())
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        print(f"You got {self.player_hand} which makes {self.player_hand.get_value()}.")
        print(f"Dealer has {self.dealer_hand} which makes {self.dealer_hand.get_value()}.")
        if self.player_hand.get_value() == 21:
            self.won_round()
        response = "hit"
        while response == "hit":
            print("What do you want to do now? [stand] [hit]\n")
            response = input("> ")
            if response == "stand":
                self.dealer_plays()
            elif response == "hit":
                self.player_hand.add_card(self.deck.deal_card())
                print(f"You got {self.player_hand} which makes {self.player_hand.get_value()}.")
                if self.player_hand.get_value() > 21:
                    self.lost_round()
                    break
                elif self.player_hand.get_value() == 21:
                    self.won_round()
                    break


    def dealer_plays(self):
        while self.dealer_hand.get_value() < 17:
            self.dealer_hand.add_card(self.deck.deal_card())
            print(f"Dealer has {self.dealer_hand} which makes {self.dealer_hand.get_value()}.")
        if self.dealer_hand.get_value() > 21:
            self.won_round()
        elif self.dealer_hand.get_value() == 21:
            self.lost_round()
        elif self.dealer_hand.get_value() >= self.player_hand.get_value():
            self.lost_round()
        else:
            self.won_round()


    def lost_round(self):
        print("Hahaha! You lost this one Hotshot.")
        self.purse.lost_round(self.bet)


    def won_round(self):
        print("You won Hotshot.")
        self.purse.won_round(self.bet)

BlackjackTable()
