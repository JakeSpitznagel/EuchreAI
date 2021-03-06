from card_enums import Value, Suit
from from_str_decorator import from_str_init

class Card:
    value: Value
    suit: Suit

    @from_str_init
    def __init__(self, *args):
        pass

    def from_str(self, s):
        return (Value.get(s[:-1]), Suit.get(s[-1:]))

    def assign_trump(self, trump):
        self.is_trump = self.suit == Suit.get(trump)
        self.assign_bowers(Suit.get(trump))

    def assign_bowers(self, trump):
        if self.value.name == 'jack':
            if self.is_trump:
                self.value = Value.r_bower
            if not Suit.is_red(trump) ^ Suit.is_red(self.suit):
                self.value = Value.l_bower

    @staticmethod
    def is_bower(card, trump):
        """
            checks if the given card is a bower of the suit and returns the internal value (Value.r_bower or Value.l_bower)
            if it is, else returns False
        :param card: Card
        :param trump: Suit.VALUE or str
        :return: Value.r_bower or Value.l_bower if is bower, else returns False
        """
        if isinstance(trump, Suit):
            trump = trump.value
        if card.value.name == 'jack':
            if card.suit.value == trump:
                return Value.r_bower.value
            elif not Suit.is_red(trump) ^ Suit.is_red(card.suit):
                return Value.l_bower.value
            else: return False

    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit

    def __gt__(self, other):
        try:
            assert hasattr(self, 'is_trump') and hasattr(other, 'is_trump'), 'One of the Cards compared has not been assigned trump'
            if self.is_trump and not other.is_trump:
                return True
            elif not self.is_trump and other.is_trump:
                return False
            else: return self.value > other.value
        except AssertionError as e:
            raise e

    def __lt__(self, other):
        try:
            assert hasattr(self, 'is_trump') and hasattr(other, 'is_trump'), 'One of the Cards compared has not been assigned trump'
            if self.is_trump and not other.is_trump:
                return False
            elif not self.is_trump and other.is_trump:
                return True
            else: return self.value > other.value
        except AssertionError as e:
            raise e

    def __repr__(self):  # use ord()
        value_map = {'nine': '9', 'ten': '10', 'jack': 'Jack', 'queen': 'Queen', 'king': 'King',
                    'ace': 'Ace', 'l_bower': 'Jack', 'r_bower': 'Jack'}
        suit_map = {'Hearts': '♥', 'Clubs': '♣', 'Spades': '♠', 'Diamonds': '♦'}
        return f'{value_map[self.value.name]} {suit_map[self.suit.value]}'

if __name__ == '__main__':
    c = Card('10h')
    print(c)
    #c.assign_trump('hearts')
    #b = Card('as')
    #b.assign_trump('hearts')

    #print(c > b)
