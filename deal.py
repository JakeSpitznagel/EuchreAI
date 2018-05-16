from card_enums import Value, Suit
from deck import Deck
from hand import Hand
import random


def deal():
    d = Deck()
    h1 = Hand([d.cards.pop(i) for i in range(5)])
    h2 = Hand([d.cards.pop(i) for i in range(5)])
    h3 = Hand([d.cards.pop(i) for i in range(5)])
    h4 = Hand([d.cards.pop(i) for i in range(5)])
    return d, h1, h2, h3, h4


if __name__ == '__main__':
    d, h1, h2, h3, h4 = deal()

    for hand in (h1, h2, h3, h4):
        print(f"{[card for card in hand.cards]}: {hand.preferred_trump()}")
    
    print([card for card in d.cards])
