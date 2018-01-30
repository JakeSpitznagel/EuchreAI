from card_enums import Value, Suit
from card import Card
import random

class Deck:
    def __init__(self):
        self.suits = [s for s in Suit]
        self.values = [val for val in Value if val < Value.l_bower]
        self.cards = [Card(value, suit) for value in self.values for suit in self.suits]
        random.shuffle(self.cards)

