import random
'''
    Contains all information related to current card shoe being used as
    source of cards for current game.
'''


class Shoe():
    def __init__(self, cards):
        self.cards = cards
        self.shuffle()

    def draw(self):
        newCard = self.cards.pop(0)

        return newCard

    def shuffle(self):
        for _ in range(random.randint(1, 100)):
            random.shuffle(self.cards)

    def __repr__(self):
        return f'{self.cards}'
