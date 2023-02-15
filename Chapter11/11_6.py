from random import shuffle

from FrenchDeck import FrenchDeck

def set_card(deck, position, card):
    deck._cards[position] = card

deck = FrenchDeck()
FrenchDeck.__setitem__ = set_card
shuffle(deck)
print(deck[:5])
