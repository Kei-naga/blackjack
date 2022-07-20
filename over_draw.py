#!/usr/bin/env python3

from pcard import *
from player import *

deck = Deck()
player = Player("You",100)
dealer = Dealer()

print(deck)
for i in range(50):
    card = deck.draw()

player.draw(deck)
player.draw(deck)
player.draw(deck) # error will occur here
player.draw(deck)
print(player.hand)
print(deck)
