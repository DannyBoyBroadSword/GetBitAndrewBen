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
        #print(0)
        return 0
        
        
            

#class scheduler(Rich_Homie_Quan(Robot)):
        
    def get_move(self): #BENS INTIAL AND END START METHODS WILL ALSO NEED TO BE INTERFACED BY MAIN EXECUTION THREAD.
        #Essentially made everything self to enable acces of all functions for each player. 
        if self.start == True:
            self.start = False
            print("HIIHIHIHI"+str(0))
            return 0
        numBots = len(Robot.get_order(self))
        robotObjects = []
        for elem in range(numBots):
            themBots = self.get_order()
            robotObjects.append(themBots[elem])
            self.
        print(str(robotObjects))
        for robot in range(numBots):
            self.previousPositions = []
            self.position = Robot.get_order(self).index("Rich_Homie_Quan")
            
            alllimbs = Robot.get_limbs(self)
            #print(alllimbs)
            self.mylimbs = alllimbs.get("Rich_Homie_Quan")
            self.myScore = self.scoreStart()
            #self.start()
            self.hand = self.get_hands()
            self.previousCard = [];
            self.predictedScore = [];
            self.scores = []
            self.limbs = Robot.get_limbs(self)
            
        order = Robot.get_order(self)
        limbs = Robot.get_limbs(self)
        manlist = []
        limblist = []
        for i in range(len(order)):
            orders = order[i]
            manlist.append(orders)
            limblist.append(limbs[orders])
        if len(order) <= 3 and (limblist[0] == 1 or limblist[1] == 1 or limblist[2] == 1):
            return self.end_game()
            
            
        
        andrew = self.mainMethod()
        return andrew
        
   
    def on_move(self): #TODO: ON MOVE EXECUTE
        
        #reset all player score
        #if you're looking to reset everything, then it needs to be in game_start, as that is what kaplan
        #told us he calls at the start of every round
        
        pass

    
        
    
        
        #MainCallEngine.
        
    def game_start(self):#TODO ON START EXECUTION. 
        #please iterate through all players. 
        print("Hi we make meth")
        
        self.start = True
        
            
    def execute_move(self,scoreForMove): #TODO: ON EXECUTION OF MOVE FROM MAIN EXECUTION THREAD
        #print(self.scores)
        print(self.scores)
        print(self.scores.index(scoreForMove))
        return self.scores.index(scoreForMove)
    

#class MainMoveComputationThread(Rich_Homie_Quan(Robot)):
    #tasks that run at defined times will need to be managed inside their subclasses. mentiones with todo flag
    #never play a score that is more than 150 unless you have one one limb and less than 3 players. BEN.
    def mainMethod(self):
        numBots = len(Robot.get_order(self))
        ideal4 =[]
        ideal3 =[]
        ideal2 =[]
        ideal1=[]
        average = 0
        hands = Robot.get_hands(self)
        myHand = hands[self.name]
        for card in myHand:
            #print(self.score)
            self.scores.append(self.myScore)
            print(self.scores)
        for robot in range(len(robotObjects)):
            scores.append(self.predictiveScore())
        for options in range(len(self.scores)):
            #print(self.limbs)
            if self.mylimbs == 4:
                print("I smoke weed for a living")
                for robotScore4 in range(len(self.scores)):
                    print(str(len(self.scores))+"adlf")
                    #print(robotScore)
                    if (int(-1*int(self.myScore))+int(self.scores[robotScore4]))<=50:
                        ideal4.append(self.scores[options])
                if len(ideal4)>2:
                    return self.execute_move(min(ideal4, key=lambda x:abs(x-self.scores[options])))
                else:
                    print(ideal4[0])
                    return self.execute_move(ideal4[0])
            elif self.mylimbs == 3:
                print("I smoke crack for a living")
                for robotScore3 in range(len(self.scores)):
                    if -1*self.myScore+self.scores[robotScore3]>=75:
                        ideal3.append(self.scores[options])
                if len(ideal3)>2:
                    return self.execute_move(min(ideal3, key=lambda x:abs(x-self.scores[options])))
                else:
                    return self.execute_move(ideal3[0])
                #play the score slightly higher than the rest
                #pass
                #Rich_Homie_Quan.execute_move(Rich_Homie_Quan[availableMoves])
            elif self.mylimbs == 2:
                print("I smoke meth for a living")
                for robotScore2 in range(len(self.scores)):
                    if -1*self.myScore+self.scores[robotScore2]>=185:
                        ideal2.append(self.scores[options])
                if len(ideal2)>2:
                    return self.execute_move(min(ideal2, key=lambda x:abs(x-self.scores[options])))
                else:
                    return self.execute_move(ideal2[0])
                #play the score higher than the rest.
                #pass
                
            elif self.mylimbs == 1:
                print("I smoke marijuana for a living")
                for robotScore1 in range(len(self.scores)):
                    if -1*self.myScore+self.scores[robotScore1]>=285:
                        ideal1.append(self.scores[options])
                if len(ideal1)>2:
                    return self.execute_move(min(ideal1, key=lambda x:abs(x-self.scores[options])))
                else:
                    return self.execute_move(ideal1[0])
                #play the score higher than the rest.
                
            else:
                print("WEED")   
                
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
        print(self.cardMargin*(100/len(Robot.get_order(self))))
        return self.cardMargin*(100/len(Robot.get_order(self)))
        
    
    def limbs(self):
        alllimbs = Robot.get_limbs(self)
        self.mylimbs = alllimbs.get(self)
        return self.mylimbs
    
    def position(self):
        self.position = Robot.get_order(self).index(self)
    
    #def getScore(self):
        #return self.score()
        
    def scoreStart(self):
        self.previousPositions.append(self.position)
        return 100/self.mylimbs + (100/(self.position+1)) + 100     
    
    def score(self):
        self.PreviousScores.append(100/(self.limbs()) + 100/(self.position+1) + (self.handScore()))    
        self.myScore = 100/(self.limbs()) + 100/(self.position+1) + self.handScore()
        return self.myScore
    
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
        myHand = hands.get(self)
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
        myPos = Robot.get_order(self).index("Carol")
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
        print(myHand[-1])
        return myHand[-1]
           
