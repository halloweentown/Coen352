import Mutate
import numbers as np
import random as rng
import globalVariables as gv
#below from mutate class merge
import numpy as np
import random as rng
import globalVariables as gV
import SortIndividual
from countInversions import *
import copy

class SortIndividual:
    def __init__(self):
        # ~~~~~~~~~~~~~ member Variables
        #TODO swaps
        self.sort=[]
        self.sortResult=[]
        for i in range(int(gv.n/4)):
            swap = []
            swap.append(rng.randint(0,gv.n - 1))
            swap.append(rng.randint(0,gv.n - 1))
            #check that x and y are different, correct if same
            while swap[0]==swap[1]:
                swap.pop()
                swap.append(rng.randint(0,gv.n - 1))
            #print (swap)
            self.sort.append(swap)
            #print (sort)       
        # fitness 
        self.efficiency = len(self.sort)    # Number of swaps    
        self.effectiveness = 0              # Number of inversions
        self.fitness = 0
        self.age = 0                        # Number of iterations survived
        #TODO N2H - mutation history
        self.mHistory = []
        return
    
    # ~~~~~~~~~~~~~~~ member Methods
    def print (self):
        # What should be returned when printing the object?
        return
    
    #sort method
    def applySort(self,inputArray):
        # iterate through every swap in sort
        for swap in self.sort:
            #if value at index swap[0] is greater than value at swap[1], SWAP
            #print(inputArray[swap[0]], inputArray[swap[1]])
            if inputArray[swap[0]] > inputArray[swap[1]]:
                inputArray[swap[0]],inputArray[swap[1]] = inputArray[swap[1]], inputArray[swap[0]]
           # print(inputArray[swap[0]], inputArray[swap[1]])
        self.sortResult = inputArray
        return
    
    def calcFitness (self):
        # measure and set fitness parameters of sort
        self.efficiency = len(self.sort)
        self.effectiveness, _ = countInversions(self.sortResult)  
        
        if gv.iEvolution < int(0.9 * gv.nEvolutions):
            self.fitness = 0.7 * self.effectiveness + 0.3 * self.efficiency
        else:
            self.fitness = 0.5 * self.efficiency + 0.5 * self.effectiveness
        return 
    
    '''different mutation functions'''
    def add (self):
        # add new swap tuple to sort
        #i=0
        #for i in range(4):
            # check if sort is already larger than specified max length
            if (len(self.sort) < gV.maxSortLength):
                newSwap = []
                newSwap.append(rng.randint(0,gv.n - 1))
                newSwap.append(rng.randint(0,gv.n - 1))
                #check that x and y are different, otherwise correct 
                while newSwap[0]==newSwap[1]:
                    newSwap.pop()
                    newSwap.append(rng.randint(0,gv.n - 1))
                #Insert at random index 
                self.sort.insert(rng.randint(0,len(self.sort)), newSwap)
                #Insert mutation abrieviation
                self.mHistory.append('A')        
                return
            else:
                self.mHistory.append('~A')   
                return

    def delete (self):
        # delete swap from sort
        if (len(self.sort) > int(gV.minSortLength/10)):
            self.sort.pop(rng.randint(0,len(self.sort) - 1))
            #Insert mutation abrieviation
            self.mHistory.append('D') 
        else:
            self.mHistory.append('~D')               
        return
            
    #def modifiy (self):
        ## Changes the the value of indices in a swap
        #return
    
    def mutate (self):
    # select mutation to be applied
        # generates child (copy of iteself)
        child = copy.deepcopy(self) 
        #Choose which mutation will occur
        # Parameters: 4 element list, return 1, Replace after returned, probability of each element
        m = np.random.choice(4,1,True,p=[0.5, 0.5, 0, 0])
        #m = np.random.choice(4,1,True,p=[gv.m1p,gv.m2p,gv.m3p,gv.m4p])
   
        if m==0:
            #DO m1
            child.add()
        elif m==1:
            ##DO m2
            self.delete()
        #elif m==2:
            ##DO m3
            #self.modifiy()
        child.applySort(gv.inputArray)
        child.calcFitness()
        return child

##Time permitting
    ##def swap (self):
        ### Swap the order of two swaps in a sort
        ##return    