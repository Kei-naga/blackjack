from pcard import *

# 手札
class Hand(Deck):
    # deckを継承して空の手札に
    def __init__(self):
        super().__init__()
        self.clear()

    # 得点計算
    def score(self):
        s = 0
        ace = 0
        for card in self:
            if card.number > 10:
                s += 10
            elif card.number == 1:
                ace += 1
                s += 11
            else:
                s += card.number
        for i in range(ace):
            if s > 21:
                s -= 10
            else:
                break
        return s
