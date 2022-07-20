import random

# カードの定義
class PlayingCard:
#    SUIT_LIST = ('♣', '♢', '♡', '♠')
    SUIT_LIST = ('C', 'D', 'H', 'S')
    NUMBER_LIST = ('', 'A', '2', '3', '4', '5', '6',
                   '7', '8', '9', '10', 'J', 'Q', 'K')

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def output(self):
        return self.suit + self.NUMBER_LIST[self.number]

    def __str__(self):
        return self.suit + self.NUMBER_LIST[self.number]

    # 同値演算するために必要
    def __eq__(self, other):
        return self.suit == other.suit
    # ハッシュ可能に←カードの値は変化しない
    def __hash__(self):
        return hash((self.suit, self.number))

# デッキ定義
class Deck(list):
    def __init__(self):
        super().__init__()
        # 全カード用意
        self.extend([PlayingCard(x, y+1)
                     for x in PlayingCard.SUIT_LIST
                     for y in range(13)])
        self.shuffle()

    # デッキから一枚取り出す
    def pop(self):
        return super().pop()
    draw = pop

    def change(self, discards):
        self.clear()
        self.append(discards)
        discards.clear()
        random.shuffle(self)

    # デッキをシャッフル
    def shuffle(self):
        random.shuffle(self)

    def __str__(self):
        return " ".join([str(c) for c in self])

    # デッキのランダムなところにカード挿入
    def insert(self, card):
        i = random.randint(0, len(self))
        super().insert(i, card)

class Discards(Deck):
    def __init__(self):
        super().__init__()
        self.clear()

# テスト
if __name__ == "__main__":
    card1 = PlayingCard(PlayingCard.SUIT_LIST[3], 1)
    card2 = PlayingCard(PlayingCard.SUIT_LIST[0], 11)
    card3 = PlayingCard(PlayingCard.SUIT_LIST[2], 12)
    card4 = PlayingCard(PlayingCard.SUIT_LIST[1], 13)
    print(card1, card2, card3, card4)

    deck = Deck()
    print(deck)
