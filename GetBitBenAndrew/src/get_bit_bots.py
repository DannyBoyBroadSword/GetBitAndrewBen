'''
Created on Sep 15, 2014

@author: eliotkaplan
'''

from robot import *
import random

class Human_Robot(Robot):
    
    def get_move(self):
        print("-"*20)
        print("{}'s turn!".format(self.name))
        print("-"*20)
        hands = copy(self.get_hands())
        my_hand = hands.pop(self.name)
        limbs = self.get_limbs()
        print("Other robots' hands: {}".format(hands))
        print("Your hand: {}".format(my_hand))
        print("The player order is: SHARK",end="")
        for robot in self.get_order():
            print(", {} ({})".format(robot, limbs[robot]), end="")
        print()
        move = int(input("What card would you like to play? "))
        return move

class Random_Robot(Robot):

    def get_move(self):
        hand = self.get_hands()[self.name]
        return random.choice(hand)