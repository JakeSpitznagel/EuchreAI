from hand import Hand
from card import Card

gameState = {'phase': 0, 
            'trump': '', 
            'lead_suit': '', 
            'active_cards': '', 
            'all_played_cards': '', 
            'flipped_card': '',
            'current_player': 0,
            'is_solo': False}


class Player:
    hand: Hand

    def __init__(self, isAI):
        self.isAI = isAI
        self.fmap = {method_name: getattr(self, method_name) for method_name in dir(self) if callable(getattr(self, method_name)) and method_name[:1] != '_'}
        self.hand = Hand('kh, qc, as, 10d, ah')

    def _process_command(self, cmd, *args, **kwargs):
        ss_count = 0
        sub_cmd = ''
        if cmd in self.fmap: sub_cmd = cmd
        else:
            for map_cmd in self.fmap:
                if(map_cmd[:cmd.__len__()] == cmd):
                    sub_cmd = map_cmd
                    ss_count += 1
                if(ss_count >= 2): 
                    sub_cmd = ''
                    break
        
        if(sub_cmd): self.fmap[sub_cmd](*args, **kwargs)

    def _notify(self, gameState):
        if self.isAI:
            self.processState(gameState)
        
    def _processState(self, gameState):
        phase = gameState['phase']
        if phase == 0:
            self.play(self.hand.preferredCard())

    def play(self):
        card = Card(input(f'which card would you like to play? {self.hand}'))
        print(card)
        assert card in self.hand, 'Card not in hand'
        gameState['active_cards'] += f', {card}' if len(gameState['active_cards']) else str(card)
        gameState['all_played_cards'] += f', {card}' if len(gameState['all_played_cards']) else str(card)
        self.hand.remove(card)

if __name__ == '__main__':
    p = Player(False)

    for i in p.fmap:
        print(i)

    text = input('hey, command me boy\n')
    while text != 'quit':
        p._process_command(text)
        text = input('BOI I NEED MORE\n')

    print(gameState)
