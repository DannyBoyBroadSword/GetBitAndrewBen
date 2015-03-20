'''
Created on Sep 15, 2014

@author: eliotkaplan
'''
from copy import copy

class Robot(object):
    def __init__(self, name):
        self.name = name

    def game_start(self):
        '''
        Called at the beginning of each game of get bit. Use it to reset your instance variables.
        '''
        pass
    
    def get_move(self):
        '''
        This is the function that is called to find out what you want to do.
        Return the number of the card that you want to return.
        '''
        return -1

    def get_order(self):
        '''
        Returns a list of the names of the robots in order,
        where the 0th robot is the one closest to the shark.
        '''
        return self.game.get_order()

    def get_hands(self):
        '''
        Returns a dictionary where the keys are the names of robots and
        the values are lists of integers representing the cards in that robot's hand.
        '''
        return {robot.name:copy(self.game.hands[robot]) for robot in self.game.robots}

    def get_limbs(self):
        '''
        Returns a dictionary where the keys are the names of robots and
        the values are lists of integers representing the number of limbs that robot
        has remaining.
        '''
        return {robot.name:self.game.limbs[robot] for robot in self.game.robots}