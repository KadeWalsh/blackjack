'''
    Card object contains all data about specific card, such as the actual
    card, the suit, and its count value in relation to blackajck
'''


class Card():
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        if self.number in 'TJQK':
            self.value = 10
        elif self.number == 'A':
            self.value = 11
        else:
            self.value = int(self.number)

    def __repr__(self):
        return f'{self.number}{self.suit}'
