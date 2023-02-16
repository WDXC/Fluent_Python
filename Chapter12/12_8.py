print(bool.__mro__)

def print_mro(cls):
    print(', '.join(c.__name__ for c in cls.__mro__))

print_mro(bool)

from Chapter_11.FrenchDeck2 import FrenchDeck2
print_mro(FrenchDeck2)