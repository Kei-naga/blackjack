from hand import Hand
from pcard import *

# ディーラー、プレイヤ共通定義
class Person:

    def __init__(self, name):
        self.name = name    # dealer or player
        self.hand = Hand()  # 持ち札
        self.open = True    # 片方表示するか

    def draw(self, deck):
        self.hand.append(deck.draw())

    def score(self):
        return self.hand.score()

    def discarding(self, discards):
        discards.append(self.hand)
        self.hand.clear()

class Player(Person):
    def __init__(self, name, coin):
        super().__init__(name)
        self.coin = coin    # 持ち金


class Dealer(Person):
    def __init__(self):
        super().__init__("Dealer")
        self.open = False

# test
if __name__ == "__main__":
    p = Player("Alice", 100)
    print(p.coin)
    d = Dealer()
    print(p.hand)
