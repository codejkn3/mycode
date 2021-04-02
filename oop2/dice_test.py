'''
Test the objects created in cheatdice.py
John Nealy
'''
from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice

# instantiate cheaters
cheater1 = Cheat_Swapper()
cheater2 = Cheat_Loaded_Dice()

#players roll the dice
cheater1.roll()
cheater2.roll()

#now they cheat - shameful!
cheater1.cheat()
cheater2.cheat()

#print the results and declare a winner or a draw
print("Cheater 1 rolled" + str(cheater1.get_dice()))
print("Cheater 2 rolled" + str(cheater2.get_dice()))

if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
  print("Draw!")

elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
  print("Cheater 1 wins!")

else:
  print("Cheater 2 wins!")

