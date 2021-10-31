from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck():
    '''
    This is the Deck class. This object will create a deck of cards to initiate
    play. You can then use this Deck List of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    '''
    def __init__(self):
        self.deck = [{'suite': suite, 'rank': rank} for suite in SUITE for rank in RANKS]

    def shuffle_deck(self):
        shuffle(self.deck)

    def cut_and_deal(self):
        return self.deck[:26], self.deck[26:]

class Hand():
    '''
    This is the Hand class. Each player has a Hand, and can add or remove cards
    from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, hand):
        self.hand = hand
    
    def add(self, cards):
        self.hand.extend(cards)

    def remove(self):
        return self.hand.pop(0)

    def __len__(self):
        return (len(self.hand))

class Player():
    '''
    This is the PLayer class, which takes in a name and instanceo fo a Hand class
    object. The player can then play cards and check if they still have cards.
    '''
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        return self.hand.remove()

    def check_card_count(self):
        return len(self.hand)

# The game
def play_game():
    pass

print('Welcome to War. Because War doesn\'t actually require any decisions, \n the game will automatically play.')

# create the deck
deck = Deck()
deck.shuffle()
h1, h2 = deck.cut_and_deal()
# create players
computer = Player('computer', h1)
player = Player(input('What is your name, player?', h2))





# play the game