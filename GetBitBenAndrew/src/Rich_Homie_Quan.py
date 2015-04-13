'''
Created on Mar 24, 2015

@author: andrewhennessy

NEED TO FIND MATH TO FIND OUR STRATEGY
'''
from robot import *;
from findertools import move



class Rich_Homie_Quan(Robot):
    '''
    classdocs
    '''
   
     
    def get_move(self):
        #Essentially made everything self to enable acces of all functions for each player. 
        if self.Robot.start() == True:
            self.startGame()
        #MainCallEngine.
    
    
    def game_start(self):
        #please iterate through all players. 
        Rich_Homie_Quan.score = Rich_Homie_Quan.getScore(self)
        
    def card_refresh(self,move): #call this on refresh after death or stuff. 
        # this will have to be managed for each player. 
        self.move = move
        self.CardsPlayed.append(move)
        
    def handScore(self):
        self.get_hands()
        
    def previousCard(self):
        #get players previous card
        pass
    
    def limbs(self):
        return Robot.get_limbs(self)
    
    def position(self):
        return Robot.get_order(self).index(self)
    
    def getScore(self):
        return self.score
    
        


class StrategyEvaluate(Rich_Homie_Quan(Robot)):
    
    #def __init__(self,end=False,start=True,mid=False):
        
        
    #TODO evaluate against out stategy takes in inputs from stat handler and advance to change and autotune strategy
    
    def startGame(self, start):
        #ikr
        pass
        
    def scoreStart(self):
        self.previousPositions.append(self.position())
        return 100/(self.limbs() + 100/self.position+1) + 100
        
    def score(self):
        self.PreviousScores.append(100/(self.limbs()) + 100/(self.position()+1) + (self.handScore()))    
        self.score = 100/(self.limbs()) + 100/(self.position()+1) + 100/(self.handScore())
        
   
