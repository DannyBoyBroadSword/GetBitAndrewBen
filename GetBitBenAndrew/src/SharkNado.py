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
            paass
            #players.append(playerObject(thePlayers))
        start = True
        
    
           
    
    def advance(self):
       # for player in self.players:
            #self.CardHandler()
            
            
        
        
        #TODO evaluate future moves from another function recursively
<<<<<<< HEAD
       # pass

=======
       pass
'''
>>>>>>> branch 'master' of https://github.com:443/DannyBoyBroadSword/GetBitAndrewBen.git
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
        for elem in order:
            orders = order[elem]
            limbList.append(orders)
            
        #if len(order) <= 3 and (limbList[0] = 1 or limbList[1] = 1 or limbList[2] = 1):
            #Sharknado.Robot.end = True
        
        #if len(Robot.get_order()) <= 3 and (limbList[0] = 1 or limbList[1] = 1 or limbList[2] = 1):
            #Sharknado.Robot.end = True
    
    def endGame(self):
        #if  Sharknado.Robot.end = True:
            #myHand = Robot.get_hands()
            #myHand = myHand{self.name}
           # return myHand[-1]
           pass
        
    
        
    def back3tie(self):
        limbs = Robot.get_limbs(self)
        lastthree = [] #people have lastthree todo 
        myLimbs = limbs{self.name}
        endangered = list(limbs.keys())
        for elem in range(len(endangered)):
            if endangered[elem] > 0 and Robot.get_order(elem) <= len(endangered)//2:
                lastthree.append(endangered[elem])
        
            
            
<<<<<<< HEAD
=======
        #Placement
        #their cards
        #our cards
    #front
 
    
>>>>>>> branch 'master' of https://github.com:443/DannyBoyBroadSword/GetBitAndrewBen.git
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
<<<<<<< HEAD
      
=======
    
    '''  
>>>>>>> branch 'master' of https://github.com:443/DannyBoyBroadSword/GetBitAndrewBen.git
