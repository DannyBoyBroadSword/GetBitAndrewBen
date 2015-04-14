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
    
class initialization(Rich_Homie_Quan(Robot)):
    
    def __init__(self, score,hand,previousCard,predictedScore,*robots):
        for robot in self.robots:
            self.score = self.scoreStart()
            self.hand = self.get_hands()
            self.previousCard = None;
            self.predictedScore = None;
            
    def startGame(self, start):
        pass
        
    def scoreStart(self):
        self.previousPositions.append(self.position())
        return 100/(self.limbs() + 100/self.position+1) + 100

class moveManager(Rich_Homie_Quan(Robot)):
   
    def on_move(self):
        self.hand = self.get_hands()
        pass

    def execute_move(self):
        pass
    
     
    def get_move(self):
        #Essentially made everything self to enable acces of all functions for each player. 
        if self.Robot.start() == True:
            self.startGame()
        for robot in self.robots:
            self.engine(robot)
        #MainCallEngine.
        
    def game_start(self):
        #please iterate through all players. 
        self.cards_played = []
        for robot in self.robots:
            self.score = self.startScore()
    

class MainExecutionThread(Rich_Homie_Quan(Robot)):
    pass
        
class cardManager(Rich_Homie_Quan(Robot)):
        
   
    def previousCard(self):
        for robot in self.robots:
            self.attachHand(robot)


    def attachHand(self,robot):
        self.robot.get_hands()
        
    def get_previousCard(self):
        for card in range(len(Robot.get_order(self))):
            if self.hand.count(card) == 0  and self.hand.count(self.previousCard):
                self.previousCard.append(card)  
      
      
class scoring(Rich_Homie_Quan(Robot)):
    
    
    def handScore(self):
        self.cardMargin = self.previousCard[-1]-self.previousCard[-2]
        return self.cardMargin*(100/len(Robot.get_order(self)))
        
    
    def limbs(self):
        return self.get_limbs
    
    def position(self):
        return Robot.get_order(self).index(self)
    
    def getScore(self):
        return self.score()
    
    def score(self):
        self.PreviousScores.append(100/(self.limbs()) + 100/(self.position()+1) + (self.handScore()))    
        self.score = 100/(self.limbs()) + 100/(self.position()+1) + self.handScore()
        return self.score
    
class predictionEngine(Rich_Homie_Quan(Robot)):
    
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
                return (self.average+self.highest)/(len(self.thoseScores)+1)
        else:
            return self.highest
                                  
    def predictingHandScore(self,card):
        self.cardMargin = self.previousCard[-1]-self.previousCard[-2]
        return self.cardMargin*(100/len(Robot.get_order(self)))
        
    def predictionEngine(self,card):
        return ((100/(self.limbs()) + 100/(self.position()+1) + self.predictingHandScore(card)))
            
    
  
    
class cleanup(Rich_Homie_Quan(Robot)):
    
    def end_game(self):
        pass   
