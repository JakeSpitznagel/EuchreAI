from card_enums import Value, Suit

def card_from_str(s):
	val = Value.get(s[:-1])
	suit = Suit.get(s[-1:])

	return Card(val, suit)

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


if __name__ == '__main__':
	c = card_from_str('10h')
	print(c)
