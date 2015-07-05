# -----------
# User Instructions
# 
# Write a function, deal(numhands, n=5, deck), that 
# deals numhands hands with n cards each.
#

import random # this will be a useful library for shuffling

# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the 
# Instructor Comments box below).

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

def deal(numhands, n=5, deck=mydeck):
    # Your code here.
    hands = []
    cards = []
    i = 0
    for h in range(0, numhands):
        hand = []
        for card in range(0, n):

            while (True):
                i = random.randint(0, 51)
                if i not in cards: break

            hand.append(mydeck[i])
        hands.append(hand)
    return hands

print deal(2)

