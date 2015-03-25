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
        players = []
        for thePlayers in range(len(Robot.get_order(self))):
            players.append(playerObject(thePlayers))
        start = True
           
     
    def advance(self):
        
        #TODO evaluate future modes from another function recursively
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
        for Sharknado.Robot.player in Sharknado.Robot.players:
            
        #TODO high low evalutation using card handler to pass good data into strategy evaluate.
            pass
    
    def heapPush(self, heap, value):
        heap.append(value)
        i = len(heap)-1
        while heap[i] < heap[(i-1)//2] and i > 0:
            heap[i],heap[(i-1)//2] = heap[(i-1)//2],heap[i]
            i = (i-1)//2
    
    def heapPop(self, heap):
        heap[0],heap[len(heap)-1] = heap[len(heap)-1],heap[0]
        pop = heap.pop()
        i = 0
        while 2*i+1 < len(heap) and (heap[i] > heap[2*i+1] or heap[i] > heap[2*i+2]):
            if 2*i+2 >= len(heap) and heap[i] > heap[2*i+1]:
                heap[i],heap[2*i+1] = heap[2*i+1],heap[i]
                break
            elif heap[i] == heap[2*i+1] and heap[i] == heap[2*i+2]:
                break
            elif heap[2*i+1] < heap[2*i+2]:
                heap[i],heap[2*i+1] = heap[2*i+1],heap[i]
                i = 2*i+1
            elif heap[2*i+2] < heap[2*i+1]:
                heap[i],heap[2*i+2] = heap[2*i+2],heap[i]
                i = 2*i+2
        return pop
    
class playerObject(Sharknado(Robot)):
    def __init__(self,order):
        self.rank = order
        self.actual_cards = Robot.get_hands()
        self.probable_cards = Robot.get_hands()
    
