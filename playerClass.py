'''
    Contains all information about a specific player in current game
'''
import settings as CONFIG
import time


class Player:
    def __init__(self, name):
        self.name = name

        self.reset()

    def updateCount(self):
        self.count = sum([card.value() for card in self.cards])

    def draw(self, cardShoe):
        if len(self.cards) >= 2:
            time.sleep(CONFIG.DRAW_DELAY)
        self.cards.append(cardShoe.draw())
        self.count = sum([card.value for card in self.cards])

        if self.count > 21 and '11' in [str(c.value) for c in self.cards]:
            self.count -= 10

    def reset(self):
        self.cards = []
        self.count = 0
        self.stay = False
        self.busted = False

    def __repr__(self):
        return f'{self.name:<10}: {str(self.cards):<20}  Total: '\
            f'{self.count if self.count <= 21 else "BUSTED"}'
