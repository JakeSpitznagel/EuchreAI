from card_enums import Value, Suit
from card import Card
from from_str_decorator import from_str_init

class Hand:
    cards: list

    @from_str_init
    def __init__(self, *args):
        self.suit_sums = {}

    def from_str(self, s):
        card_s = [i.strip().upper() for i in s.split(",")]
        fin = []
        for card in card_s:
            val = Value.get(card[:-1])
            suit = Suit.get(card[-1:])
            
            fin.append(Card(val, suit))
        
        return (fin,)

    def __contains__(self, item):
        if not hasattr(self, 'cards'): return False
        else: return item in self.cards
    
    def remove(self, item):
        self.cards.remove(item)

    def __repr__(self):
        return f'{self.cards}' if hasattr(self, 'cards') else 'hand is empty'

    def sum_suits(self):
        self.suit_sums['hearts'] = len([heart for heart in self.cards if heart.value == 'Hearts'])
        self.suit_sums['diamonds'] = len([diamond for diamond in self.cards if diamond.value == 'Diamonds'])
        self.suit_sums['spades'] = len([spade for spade in self.cards if spade.value == 'Spades'])
        self.suit_sums['clubs'] = len([club for club in self.cards if club.value == 'Clubs'])

    def preferred_trump(self):
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

    def suit_strength(self, suit):
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
        strength = {"hearts": suit_sum,
                    "clubs": suit_sum,
                    "spades": suit_sum,
                    "diamonds": suit_sum}

        return 5

if __name__== '__main__':
    h = Hand('10c, 9d, ks, as, js')
    print(h.cards)
