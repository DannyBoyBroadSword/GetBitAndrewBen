'''
Created on Mar 24, 2015

@author: andrewhennessy

NEED TO FIND MATH TO FIND OUR STRATEGY
'''
from robot import *;

#Confirm that we can reference robot names with self definition. 
# robot self.get_limbs(self)
#will have to exclude our bot from robots when creating non native objects aka djKhaled's PRedictive objects. 

class Rich_Homie_Quan(Robot):

#class initialization(Rich_Homie_Quan(Robot)):
    
    #def __init__(self,name):
        #self.name = name
        
            
    def startGame(self):
        #ANDREW FOR THE LOVE OF GOD STOP GETTING RID OF MY STUFF. PLEASE. I KEEP TELLING YOU NOT TO,
        #AND YOU KEEP DELETING IT KEEP MY GODDAM CODE THE WAY IT IS AND LET ME DEAL WITH IT
        self.start = False
        
        return 0
        
    def scoreStart(self):
        self.previousPositions.append(self.position())
        return 100/(self.limbs() + 100/self.position+1) + 100

#class scheduler(Rich_Homie_Quan(Robot)):
        
    def get_move(self): #BENS INTIAL AND END START METHODS WILL ALSO NEED TO BE INTERFACED BY MAIN EXECUTION THREAD.
        #Essentially made everything self to enable acces of all functions for each player. 
        if self.start == True:
            self.startGame()
            
        order = Robot.get_order(self)
        limbs = Robot.get_limbs(self)
        manlist = []
        limblist = []
        for i in range(len(order)):
            orders = order[i]
            manlist.append(orders)
            limblist.append(limbs[orders])
        if len(order) <= 3 and (limblist[0] == 1 or limblist[1] == 1 or limblist[2] == 1):
            self.end_game()
            
            
        if self.start == False:
            self.mainMethod()
        
        def sendMove(self,move):
            return move
   
    def on_move(self): #TODO: ON MOVE EXECUTE
        
        #reset all player score
        #if you're looking to reset everything, then it needs to be in game_start, as that is what kaplan
        #told us he calls at the start of every round
        
        pass

    def execute_move(self,scoreForMove): #TODO: ON EXECUTION OF MOVE FROM MAIN EXECUTION THREAD
        Robot.get_move.sendMove(self.score.index(scoreForMove))
        pass
    
        
        #MainCallEngine.
        
    def game_start(self):#TODO ON START EXECUTION. 
        #please iterate through all players. 
        numBots = len(Robot.get_order(self))
        self.start = True
        for robot in range(numBots):
            self.score = 0
            #self.start()
            self.hand = self.get_hands()
            self.previousCard = [];
            self.predictedScore = None;
            self.scores = []
            self.limbs = Robot.get_limbs(self)
    

#class MainMoveComputationThread(Rich_Homie_Quan(Robot)):
    #tasks that run at defined times will need to be managed inside their subclasses. mentiones with todo flag
    #never play a score that is more than 150 unless you have one one limb and less than 3 players. BEN.
    def mainMethod(self):
        numBots = len(Robot.get_order(self))
        ideal4 =[]
        ideal3 =[]
        ideal2 =[]
        ideal1=[]
        average = None
        hands = Robot.get_hands(self)
        myHand = hands[self.name]
        for card in myHand:
            self.scores.append(self.score)
        for robot in range(numBots):
            self.scores.append(self.predictiveScore())
        for options in range(len(self.scores)):
            if self.limbs == 4:
                for robotScore in self.scores:
                    if -self.scores+self.scores[robotScore]<=50:
                        ideal4.append(self.scores[options])
                    if len(ideal4)>2:
                        self.execute_move(min(ideal4, key=lambda x:abs(x-self[options])))
                    else:
                        self.execute_move(ideal4[0])
            elif self.limbs == 3:
                for robotScore in self.scores:
                    if -self.scores+self.scores[robotScore]>=75:
                        ideal3.append(self.scores[options])
                    if len(ideal3)>2:
                        self.execute_move(min(ideal3, key=lambda x:abs(x-self[options])))
                    else:
                        self.execute_move(ideal3[0])
                #play the score slightly higher than the rest
                pass
                #Rich_Homie_Quan.execute_move(Rich_Homie_Quan[availableMoves])
            elif self.limbs == 2:
                for robotScore in self.scores:
                    if -self.scores+self.scores[robotScore]>=185:
                        ideal2.append(self.scores[options])
                    if len(ideal2)>2:
                        self.execute_move(min(ideal2, key=lambda x:abs(x-self[options])))
                    else:
                        self.execute_move(ideal2[0])
                #play the score higher than the rest.
                pass
                
            elif self.limbs == 1:
                for robotScore in self.scores:
                    if -self.scores+self.scores[robotScore]>=285:
                        ideal1.append(self.scores[options])
                    if len(ideal1)>2:
                        self.execute_move(min(ideal1, key=lambda x:abs(x-self[options])))
                    else:
                        self.execute_move(ideal1[0])
                #play the score higher than the rest.
                
                    
                
#class cardManager(Rich_Homie_Quan(Robot)):
        
   
    def previousCard(self):
        numBots = len(Robot.get_order(self))
        for robot in numBots:
            self.attachHand(robot)


    def attachHand(self,robot):
        return Robot.get_hands()
        
    def get_previousCard(self):
        for card in range(len(Robot.get_order(self))):
            if self.hand.count(card) == 0  and self.hand.count(self.previousCard):
                self.previousCard.append(card)  
      
      
#class scoring(Rich_Homie_Quan(Robot)):
    
    
    def handScore(self):
        self.cardMargin = self.previousCard[-1]-self.previousCard[-2]
        return self.cardMargin*(100/len(Robot.get_order(self)))
        
    
    def limbs(self):
        return Robot.get_limbs(self)
    
    def position(self):
        return Robot.get_order(self).index("Rich_Homie_Quan")
    
    #def getScore(self):
        #return self.score()
    
    def score(self):
        self.PreviousScores.append(100/(self.limbs()) + 100/(self.position()+1) + (self.handScore()))    
        self.score = 100/(self.limbs()) + 100/(self.position()+1) + self.handScore()
        return self.score
    
#class predictionEngine(Rich_Homie_Quan(Robot)):
    
    def predictiveScore(self):
        self.thoseScores = []
        self.average = 0
        for cards in self.hand: 
            self.thoseScores.append(self.predictionEngine(cards))
        self.highest = max(self.thoseScores)
        if len(self.thoseScores)>=2:
            for Iterscores in range(len(self.thoseScores)):
                self.average += self.thoseScores[Iterscores]
                # BIG BIG PROBLEM RIGHT HERE I DON'T KNOW WHAT YOU'RE TRYING TO DO SO I CAN'T FIX IT
                # BUT YOU ARE TRYING TO CALL A CERTAIN INDEX OF A LIST WITH THE INDEX BEING A LIST
                # THAT DOESN'T MAKE ANY SENSE. UP TO YOU TO FIX IT
            self.average = self.average/len(self.thoseScores)
            if self.average<self.highest:
                return (self.average+self.highest)/(len(self.thoseScores)+1)
        else:
            return self.highest
                                  
    def predictingHandScore(self,card):
        hands = Robot.get_hands(self)
        myHand = hands.get('Rich_Homie_Quan')
        if len(self.previousCard) >= 2:
            self.cardMargin = (self.previousCard[-1])-(self.previousCard[-2])
            return self.cardMargin*(100/len(Robot.get_order(self)))
        elif len(self.previousCard) == 1:
            return self.previousCard[0]*(100/len(Robot.get_order(self)))
        else:
            return (100/len(Robot.get_order(self)))
        
    def predictionEngine(self,card):
        myLimbs = Robot.get_limbs(self)
        myLimbs = myLimbs.get('Rich_Homie_Quan')
        myPos = Robot.get_order(self).index("Rich_Homie_Quan")
        return ((100/(myLimbs) + 100/(myPos+1) + int(self.predictingHandScore(card))))
            
    
  
    
#class cleanup(Rich_Homie_Quan(Robot)):
    
    def endStart(self):
        order = Robot.get_order(self)
        limbs = Robot.get_limbs(self)
        manlist = []
        limblist = []
        for elem in order:
            orders = order[elem]
            manlist.append(orders)
            limblist.append(limbs[orders])
        if len(order) <= 3 and (limblist[0] == 1 or limblist[1] == 1 or limblist[2] == 1):
            self.end_game()
    
    def end_game(self):
        myHand = Robot.get_hands()
        myHand = myHand[self.name]
        return myHand[-1]
           
