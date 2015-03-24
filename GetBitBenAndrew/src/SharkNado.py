'''
Created on Mar 24, 2015

@author: andrewhennessy

NEED TO FIND MATH TO FIND OUR STRATEGY
'''
from robot import *;

class Player(object):
    '''
    classdocs
    '''


    def __init__(self, order,hand,):
        pass
        
     
    def play(self):
        #TODO execute all play call methods from here
         pass  
     
    def advance(self):
        #TODO evalute future modes from another function recursively
        pass
    
    def StrategyEvaluate(self):
        #TODO evaluate against out strategy takes in inputs from stat handler and advance to change and autotune strategy
        pass
    
    def StatHandler(self):
        #TODO evalutes errors from played cards learn and Helps Strategy Evalute
        pass
        
    def CardHandler(self):
        #TODO manages other cards in terms of their objects helps the evaluate sibiling function
        pass
    
    def SiblingEvalute(self):
        #TODO high low evalutation using card handler to pass good data into strategy evaluate.
        pass
    
    
         