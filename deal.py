from card_enums import Value, Suit
import random


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def assign_trump(self, trump):
        self.is_trump = self.suit == trump
        self.assign_bowers(trump)

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


class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.suit_sums = {}

    def sum_suits(self):
        self.suit_sums['hearts'] = len([heart for heart in self.cards if heart.value == 'Hearts'])
        self.suit_sums['diamonds'] = len([diamond for diamond in self.cards if diamond.value == 'Diamonds'])
        self.suit_sums['spades'] = len([spade for spade in self.cards if spade.value == 'Spades'])
        self.suit_sums['clubs'] = len([club for club in self.cards if club.value == 'Clubs'])

    def preferred_trump(self):  # TODO see current implementation notes in func. str
        """
            current implementation notes:
                - need to determine some sort of algorithm to determine preferred trump for a hand
                    - weigh value of cards vs. number of cards
                        - something like compare sum of suit enum.values
                    - account for left and right bower in the calculation

        :return: trump: Suit
        """
        suits = dict({})
        for card in self.cards:
            suit = card.suit.value
            is_bower = Card.is_bower(card, suit)
            value = card.value.value
            if is_bower:
                value = is_bower
                try:
                    suits[Suit.opposite_suit(suit)] += Value.l_bower.value
                except KeyError:
                    suits[Suit.opposite_suit(suit)] = Value.l_bower.value
            try:
                suits[suit] += value
            except KeyError:
                suits[suit] = value
        max_k = max_v = 0
        for (k, v) in suits.items():
            if v > max_v:
                max_k = k
                max_v = v
        return max_k


    def perceived_strength(self):  # TODO see current implementation notes in func. str
        """
            This is to be used for the bidding stage to determine if the preferred trump should be selected

            current implementation notes:
            - currently two ideas:
                - 1: predict number of rounds that can be won by the hand
                - 2: numerically rank the strength of the hand via some algorithm
                1:
                    - right bower is a guaranteed win -> this frees left bower to be a guaranteed win ...
                    - account for getting the kids off the block
                    - account for who is leading, and strength of a potential lead (eg. outside ace)
                2:
                    - determine some sort of algorithm to numerically evaluate hand strength
                        -  this can be done by combining several factors and prioritizing them somehow
                            - summing trump values
                            - short suited/number of trump cards
                            - outside aces
                - pros and cons for each:
                    pass

        :return: strength : int (est. num of tricks (1) or value to be compared to a threshold (2))
        """
        pass


class Deck:
    def __init__(self):
        self.suits = [s for s in Suit]
        self.values = [val for val in Value if val < Value.l_bower]
        self.cards = [Card(value, suit) for value in self.values for suit in self.suits]
        random.shuffle(self.cards)


def deal():
    d = Deck()
    h1 = Hand([d.cards.pop(i) for i in range(5)])
    h2 = Hand([d.cards.pop(i) for i in range(5)])
    h3 = Hand([d.cards.pop(i) for i in range(5)])
    h4 = Hand([d.cards.pop(i) for i in range(5)])
    return d, h1, h2, h3, h4


if __name__ == '__main__':
    d, h1, h2, h3, h4 = deal()
    print([card for card in h1.cards])
    print([card for card in h2.cards])
    print([card for card in h3.cards])
    print([card for card in h4.cards])
    print([card for card in d.cards])
    h1.preferred_trump()

