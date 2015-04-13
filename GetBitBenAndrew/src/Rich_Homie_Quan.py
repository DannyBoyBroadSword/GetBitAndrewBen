'''
Created on Mar 24, 2015

@author: andrewhennessy

NEED TO FIND MATH TO FIND OUR STRATEGY
'''
from robot import *;
from findertools import move
from get_bit import*;

#Confirm that we can reference robot names with self definition. 
# robot self.get_limbs(self)



class Rich_Homie_Quan(Robot):
    '''
    classdocs
    '''
    def __init__(self, score,hand,previousCard,predictedScore,*robots):
        for robot in self.robots:
            self.score = self.scoreStart()
            self.hand = self.get_hands()
            self.previousCard = None;
            self.predictedScore = None;
   
     
    def get_move(self):
        #Essentially made everything self to enable acces of all functions for each player. 
        if self.Robot.start() == True:
            self.startGame()
        for robot in self.robots:
            self.engine(robot)
        #MainCallEngine.
    
    def previousCard(self):
        for robot in self.robots:
            self.attachHand(robot)
    
    def game_start(self):
        #please iterate through all players. 
        self.cards_played = []
        for robot in self.robots:
            self.score = self.startScore()
            
    def engine(self,robot):
        return self.getScore()
        
            
        

        
        
    def handScore(self):
        self.cardMargin = self.previousCard[:0]-self.previousCard[:-1]
        return self.cardMargin*20
        
    def attachHand(self,robot):
        self.robot.get_hands()
        
    def get_previousCard(self):
        for card in range(len(5)):
            if card not in self.hand:
                self.previousCard.append(card)  
      
    
    def limbs(self):
        return self.get_limbs
    
    def position(self):
        return Robot.get_order(self).index(self)
    
    def getScore(self):
        return self.score()
    
    def predictiveScore(self):
        self.thoseScores = []
        self.average = None
        for cards in self.hand:
            self.thoseScores.append(self.predictionEngine(cards))
        self.highest = max(self.thoseScores)
        if len(self.thoseScores)>0:
            for scores in range(len(self.thoseScores)):
                self.average += scores[self.thoseScores]
            self.average = self.average/len(self.thoseScores)
            if self.average<self.highest:
                return (self.average+self.highest)/(self.thoseScores+1)
        else:
            return self.highest
                                  
    def predictingHandScore(self,card):
        self.cardMargin = self.previousCard[:0]-self.previousCard[:-1]
        return self.cardMargin*20
        
    def predictionEngine(self,card):
        ((self.PreviousScores[:-1])+(100/(self.limbs()) + 100/(self.position()+1) + self.predictingHandScore(card)))
            
        
    #TODO evaluate against out stategy takes in inputs from stat handler and advance to change and autotune strategy
    
    def startGame(self, start):
        #ikr
        pass
        
    def scoreStart(self):
        self.previousPositions.append(self.position())
        return 100/(self.limbs() + 100/self.position+1) + 100
    
    def score(self):
        self.PreviousScores.append(100/(self.limbs()) + 100/(self.position()+1) + (self.handScore()))    
        self.score = 100/(self.limbs()) + 100/(self.position()+1) + self.handScore()
        return self.score
   
   
   
