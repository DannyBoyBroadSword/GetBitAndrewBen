'''
Created on Mar 24, 2015

@author: andrewhennessy

NEED TO FIND MATH TO FIND OUR STRATEGY
'''
from robot import *;



class Rich_Homie_Quan(Robot):
    '''
    classdocs
    '''
   
     
    def get_move(self):
        CardsPlayed.append(#CardPlayed)
        if Sharknado.Robot.start == True:
            self.startGame()
        #TODO execute all play call methods from here
        pass  
    
    def game_start(self):
        CardsPlayed=[]
        score = scoreStart()
        previousPositions = []
        previousScores = []
        
    def card_refresh(self): #call this on refresh after death or stuff. 
        CardsPlayed=[]
           
    
    def advance(self):
       # for player in self.players:
            #self.CardHandler()
        #TODO evaluate future moves from another function recursively
        pass


#class StrategyEvaluate(Sharknado(Robot)):
    
    #def __init__(self,end=False,start=True,mid=False):
        
        
    #TODO evaluate against out strategy takes in inputs from stat handler and advance to change and autotune strategy
    
    def startGame(self, start):
        Sharknado.Robot.start = False
        Sharknado.Robot.mid = True
        return 0

    def endStart(self, end):
        order = Robot.get_order()
        limbList = []
        for elem in order:
            orders = order[elem]
            limbList.append(orders)
            
        #if len(order) <= 3 and (limbList[0] = 1 or limbList[1] = 1 or limbList[2] = 1):
            #Sharknado.Robot.end = True
        
    
    def endGame(self):
        #if  Sharknado.Robot.end = True:
            #myHand = Robot.get_hands()
            #myHand = myHand{self.name}
           # return myHand[-1]
           pass
        
    def scoreStart(self):
        Startposition = Robot.get_order().index("Sharknado")
        previousPositions.append(position)
        Startlimbs = Robot.get_limbs().get("Sharknado")
        
    def score(self):
        position = Robot.get_order().index("Sharknado")
        previousPositions.append(position)
        limbs = Robot.get_limbs().get("Sharknado")
        handScore = 5-(CardsPlayed.list(4) + CardsPlayed().list(5))
        PreviousScores.append(100/(limbs) + 100/(position+1) + 100/(handScore))
            
        score = 100/(limbs) + 100/(position+1) + 100/(handScore)
        max = 300
   
