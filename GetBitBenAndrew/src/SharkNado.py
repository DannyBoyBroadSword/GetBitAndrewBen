'''
Created on Mar 24, 2015

@author: andrewhennessy

NEED TO FIND MATH TO FIND OUR STRATEGY
'''
from robot import *;


class Sharknado(Robot):
    '''
    classdocs
    '''
   
     
    def get_move(self):
        
        #TODO execute all play call methods from here
        pass  
    
    def game_start(self):
        print(dict.keys(Robot.get_limbs(self)))
        players = []
        for thePlayers in range(len(Robot.get_order(self))):
            pass
            #players.append(playerObject(thePlayers))
        start = True
        
    
           
    
    def advance(self):
       # for player in self.players:
            #self.CardHandler()
            
            
        
        
        #TODO evaluate future moves from another function recursively
       pass
'''
#class StrategyEvaluate(Sharknado(Robot)):
    
    def __init__(self,end=False,start=True,mid=False):
        
        
    #TODO evaluate against out strategy takes in inputs from stat handler and advance to change and autotune strategy
        pass
    
    def startGame(self, start):
        if Sharknado.Robot.start == True:
            Sharknado.Robot.start = False
            Sharknado.Robot.mid = True
            return 0

    def endStart(self, end):
        order = Robot.get_order()
        limbList = []
        for item in order:
            limbList.append(order[item])
        if len(Robot.get_order()) <= 3 and (limbList[0] = 1 or limbList[1] = 1 or limbList[2] = 1):
            Sharknado.Robot.end = True
    
    def endGame(self):
        if Sharknado.Robot.end = True:
            myHand = Robot.get_hands()
            myHand = myHand{self.name}
            return myHand[-1]
        
    
        
    def back3tie(self):
        limbs = Robot.get_limbs(self)
        myLimbs = limbs{self.name}
        for elem in range(0,2):
            if limbs[elem] < 0:
                
            
            
        Placement
        their cards
        our cards
    front
 
    
    def StatHandler(self):
        #TODO evalutes errors from played cards learn and Helps Strategy Evalute
        pass
        
    def CardHandler(self):
        return self.get_hands()
        
        #TODO manages other cards in terms of their objects helps the evaluate sibiling function
        pass
    
class playerObject(Sharknado(Robot)):
    def __init__(self,order):
        self.rank = order
        self.actual_cards = Robot.get_hands()
        self.probable_cards = Robot.get_hands()
    
    '''  
