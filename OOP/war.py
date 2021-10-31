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

    def shuffle(self):
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

    def __str__(self):
        return self.hand.__str__()
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

    def card_count(self):
        return len(self.hand)



def compare_cards(card1, card2):
    # compare values
    # how account for face cards 
    index1 = RANKS.index(card1['rank'])
    index2 = RANKS.index(card2['rank'])
    if index1 == index2:
        return 'equal'
    elif index1 > index2:
        return 'one'
    else:
        return 'two'

def check_for_winner(p1, p2):
    if p1.card_count() == 0:
        return 'p2'
    elif p2.card_count() == 0:
        return 'p1'
    else:
        return False


def war(p1, p2):
        # check that each have enough cards(4), if not draw n-1 cards
        spoils_count = min(p1.card_count() - 1, p1.card_count() - 1, 3)
        spoils = []
        for num in range(spoils_count):
            print(f'p1 has {p1.card_count()} cards')
            spoils.append(p1.play_card())
            print(f'p2 has {p2.card_count()} cards')
            spoils.append(p2.play_card())
        return spoils

# The game
def play_game():
    print('Welcome to War. Because War doesn\'t actually require any decisions, \n the game will automatically play.')

    # create the deck
    deck = Deck()
    deck.shuffle()
    h1, h2 = deck.cut_and_deal()
    # create players
    p1 = Player('computer', Hand(h1))
    p2 = Player('player', Hand(h2))
    
    # play the game
    winner = False
    p1_card = p1.play_card()
    p2_card = p2.play_card()
    spoils = [p1_card, p2_card]
    rounds = 0
    while not winner:
        rounds += 1
        print(f'------------ ROUND {rounds} ------------------')
        comparison = compare_cards(p1_card, p2_card)
        if comparison == 'equal':
            spoils.extend(war(p1, p2))
            # set the new comparison cards
            print(f'spoils has {len(spoils)} cards', f'\n\t{spoils}')
            print(f'p1 has {p1.card_count()} cards', f'\n\t{p1.hand}')
            print(f'p2 has {p2.card_count()} cards', f'\n\t{p2.hand}')
            # p1_card = p1.play_card()
            # p2_card = p2.play_card()
            # spoils.extend([p1_card, p2_card])
            continue
        elif comparison == 'one':
            print(f'spoils has {len(spoils)} cards')
            print(f'p1 has {p1.card_count()} cards')
            print(f'p2 has {p2.card_count()} cards')
            p1.hand.add(spoils)
        else:
            print(f'spoils has {len(spoils)} cards')
            print(f'p1 has {p1.card_count()} cards')
            print(f'p2 has {p2.card_count()} cards')
            p2.hand.add(spoils)
        winner = check_for_winner(p1, p2)
        if not winner:
            p1_card = p1.play_card()
            p2_card = p2.play_card()
            spoils = [p1_card, p2_card]

    # print out the winner
    print(f'After {rounds}, ')
    print(f'{winner} has won!')
    print(f'{p1.name} had {p1.card_count()} cards')
    print(f'{p2.name} had {p2.card_count()} cards.')
    

play_game()


# play the game