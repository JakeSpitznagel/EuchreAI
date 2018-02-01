from enum import Enum


class OrderedEnum(Enum):
	def __ge__(self, other):
		if self.__class__ is other.__class__:
			return self.value >= other.value
		return NotImplemented

	def __gt__(self, other):
		if self.__class__ is other.__class__:
			return self.value > other.value
		return NotImplemented

	def __le__(self, other):
		if self.__class__ is other.__class__:
			return self.value <= other.value
		return NotImplemented

	def __lt__(self, other):
		if self.__class__ is other.__class__:
			return self.value < other.value
		return NotImplemented


class Suit(Enum):
	hearts = 'Hearts'
	diamonds = 'Diamonds'
	spades = 'Spades'
	clubs = 'Clubs'

	@staticmethod
	def is_red(suit):  # TODO add test for this
		if isinstance(suit, Enum): suit = suit.value
		return suit == Suit.hearts or suit == Suit.diamonds

	@staticmethod
	def is_black(suit):  # not really necessary but I've left it for consistency
		if isinstance(suit, Enum): suit = suit.value
		return suit == Suit.spades or suit == Suit.clubs

	@staticmethod
	def opposite_suit(suit):
		if isinstance(suit, Enum): suit = suit.value
		if suit == Suit.hearts.value: return Suit.diamonds.value
		elif suit == Suit.diamonds.value: return Suit.hearts.value
		elif suit == Suit.spades.value: return Suit.clubs.value
		elif suit == Suit.clubs.value: return Suit.spades.value


class Value(OrderedEnum):
	nine = 1
	ten = 2
	jack = 3
	queen = 4
	king = 5
	ace = 6
	l_bower = 10
	r_bower = 15
