from pcard import *


class GameRecord():
    def __init__(self, player_hand, dealer_hand, gain, discards):
        self.player_hand = str(player_hand)
        self.dealer_hand = str(dealer_hand)
        self.discards = str(discards)
        self.gain = gain

    def __str__(self):
        return ",".join([self.player_hand,
                         self.dealer_hand, str(self.gain), self.discards])
