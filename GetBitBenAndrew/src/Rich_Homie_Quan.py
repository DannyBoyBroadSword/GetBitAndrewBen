'''
Created on Mar 24, 2015

@author: andrewhennessy

NEED TO FIND MATH TO FIND OUR STRATEGY
'''
from robot import *;
from get_bit import*;

#Confirm that we can reference robot names with self definition. 
# robot self.get_limbs(self)
#will have to exclude our bot from robots when creating non native objects aka djKhaled's PRedictive objects. 

class Rich_Homie_Quan(Robot):
    
    class initialization(Rich_Homie_Quan(Robot)):
        
        def __init__(self, score,hand,previousCard,predictedScore,*robots,scores,limbs):
            for robot in self.robots:
                self.score = self.scoreStart()
                self.hand = self.get_hands()
                self.previousCard = None;
                self.predictedScore = None;
                self.scores = []
                self.limbs = self.get_limbs()
                
        def startGame(self, start):
            #ANDREW FOR THE LOVE OF GOD STOP GETTING RID OF MY STUFF. PLEASE. I KEEP TELLING YOU NOT TO,
            #AND YOU KEEP DELETING IT KEEP MY GODDAM CODE THE WAY IT IS AND LET ME DEAL WITH IT
            self.start = False
            return 0
            
        def scoreStart(self):
            self.previousPositions.append(self.position())
            return 100/(self.limbs() + 100/self.position+1) + 100
    
    class scheduler(Rich_Homie_Quan(Robot)):
       
        def on_move(self): #TODO: ON MOVE EXECUTE
            #reset all player score
            #if you're looking to reset everything, then it needs to be in game_start, as that is what kaplan
            #told us he calls at the start of every round
            
            pass
    
        def execute_move(self,scoreForMove): #TODO: ON EXECUTION OF MOVE FROM MAIN EXECUTION THREAD
            #Robot.get_move(Rich_Homie_Quan.scores.index(scoreForMove))
            pass
        
         
        def get_move(self): #BENS INTIAL AND END START METHODS WILL ALSO NEED TO BE INTERFACED BY MAIN EXECUTION THREAD.
            #Essentially made everything self to enable acces of all functions for each player. 
            if self.start == True:
                self.startGame()
            
            #MainCallEngine.
            
        def game_start(self):#TODO ON START EXECUTION. 
            #please iterate through all players. 
            self.start = True
            self.scores = []
            self.hand = self.get_hands()
            self.limbs = self.get_limbs
            self.cards_played = []
            for robot in self.robots:
                self.score = self.startScore()
        
    
    class MainMoveComputationThread(Rich_Homie_Quan(Robot)):
        #tasks that run at defined times will need to be managed inside their subclasses. mentiones with todo flag
        #never play a score that is more than 150 unless you have one one limb and less than 3 players. BEN.
        def mainMethod(self):
            hands = Robot.get_hands()
            myHand = hands[self.name]
            for card in myHand:
                Rich_Homie_Quan.scores.append(Rich_Homie_Quan.scoring.getScore())
            for robot in self.robots:
                    self.scores.append(self.predictiveScore())
            for robot in self.robots:
                for options in range(len(Rich_Homie_Quan.scores)):
                    if Rich_Homie_Quan.limbs >= 4:
                        #play the score slightly lower than the rest.
                        #Rich_Homie_Quan.scheduler.execute_move(Rich_Homie_Quan.scores[availableMoves])
                        pass
                    elif Rich_Homie_Quan.limbs >= 3:
                        #play the score slightly higher than the rest
                        pass
                        #Rich_Homie_Quan.scheduler.execute_move(Rich_Homie_Quan.scores[availableMoves])
                    elif Rich_Homie_Quan.limbs == 2:
                        #play the score higher than the rest.
                        pass
                        
                    elif Rich_Homie_Quan.limbs == 1:
                        #play the score higher than the rest.
                        Rich_Homie_Quan.scheduler.execute_move(max(Rich_Homie_Quan.scores))
                    
                        
                    
                
            
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
            return self.cardMargin*16.66667
            
        def predictionEngine(self,card):
            return ((100/(self.limbs()) + 100/(self.position()+1) + self.predictingHandScore(card)))
                
        
      
        
    class cleanup(Rich_Homie_Quan(Robot)):
        
        def endStart(self):
            order = Robot.get_order()
            limbs = Robot.get_limbs()
            manlist = []
            limblist = []
            for elem in order:
                order[elem] = orders
                manlist.append(orders)
                limblist.append(limbs[orders])
            if len(order) <= 3 and (limblist[0] = 1 or limblist[1] = 1 or limblist[2] = 1):
                self.end_game()
        
        def end_game(self):
            myHand = Robot.get_hands()
            myHand = myHand[self.name]
            return myHand[-1]
               
