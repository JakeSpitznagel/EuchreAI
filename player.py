gameState = {'phase': 0, 
			'trump': 'hearts', 
			'winning_card': Card('king', 'hearts'), 
			'lead_suit': 'hearts', 
			'active_cards': 'kh, qd, as', 
			'all_played_cards': 'kh, qd, as, 10s, 9s, ah, kd', 
			'flipped_card': 'jh',
			'current_player': 0,
			'is_solo': False}


class player:
	def __init__(self, isAI):
		self.isAI = isAI

	def notify(self, gameState):
		if self.isAI:
			
