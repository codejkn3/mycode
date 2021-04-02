'''
 A dice player class
Author: John Nealy
'''

from random import randint

class Player:
  def __init__(self):
    self.dice = []

  def roll(self):
    self.dice = [] # clears current dice
    for i in range(3): # generate 3 "rolls" and put each roll result in the list
      self.dice.append(randint(1,6))

  def get_dice(self):
    return self.dice

class Cheat_Swapper(Player):
  def cheat(self):
    self.dice[-1] = 6 # swap the last roll out for a value of 6

class Cheat_Loaded_Dice(Player):
  def cheat(self):
    i = 0
    while i < len(self.dice): # cheat by bumping up each rolled value by 1
      if self.dice[i] < 6:
        self.dice[i] += 1
      i += 1

