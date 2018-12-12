import Mutate
import numbers as np
import random as rng
import globalVariables as gv
#below from mutate class merge
import numpy as np
import random as rng
import globalVariables as gV
import SortIndividual

#inputArray = [1,2,3,4]
#power = 3
#n = len(inputArray)
#minSortLength = n
#maxSortLength = n^power

class SortIndividual:
    def __init__(self):
        # ~~~~~~~~~~~~~ member Variables
        #TODO swaps
        self.sort=[]
        for i in range(gv.n):
            swap = []
            swap.append(rng.randint(0,100))
            swap.append(rng.randint(0,100))
            #print (swap)
            self.sort.append(swap)
            #print (sort)
        
       
        # fitness 
        self.efficiency = len(self.sort)      
        #print(efficiency)
        self.effectivenes = 0            # fitness
        self.age = 0                       # Number of iterations survived
        #TODO N2H - mutation history
        self.mHistory = []
        return
    
    # ~~~~~~~~~~~~~~~ member Methods
    def fitness (self):
            # measure fitness parameters of sort
        
        return    
    #TODO fitness measurement: effi
    #TODO fitness measurement: effe
    #TODO mutation history
 
    def spawn (self,parent2):
            # generates child (copy of iteself)
            # 2nd parent in case of cross over
        return
    
    
    
    ##TODO probabilities as global variable
    ## probabilities of each mutation occuring
    #m1p = 0.25
    #m2p = 0.25
    #m3p = 0.25
    #m4p = 0.25
    
    # different mutation functions
    def add (self):
        # add new swap tuple to sort
        if (len(self.sort)<gV.maxSortLength):
            newSwap = []
            newSwap.append(rng.randint(0,100))
            newSwap.append(rng.randint(0,100))
            #Insert at random index 
            self.sort.insert(rng.randint(0,len(self.sort)), newSwap)
            #Insert mutation abrieviation
            self.mHistory.append('A')        
            return
        else:
            self.mHistory.append('~A')   
            return

    #def delete (self):
        ## delete swap from sort
            #self.insert(rng.randint(0,len(self)), swap)
            #swap.append(rng.randint(0,100))
            #swap.append(rng.randint(0,100))
            ##Insert at random index 
            #self.insert(rng.randint(0,len(self)), swap)
            ##Insert mutation abrieviation
            #self.mHistory.append('D')        
            #return
    #def modifiy (self):
        ## Changes the the value of indices in a swap
        #return
    
    #def mutate (self):
    ## select mutation to be applied
        ##Choose which mutation will occur
        ## Parameters: 4 element list, return 1, Replace after returned, probability of each element
        #m = np.random.choice(4,1,True,p=[m1p,m2p,m3p,m4p])
        #if m==0:
            ##DO m1
            #self.add()
        #elif m==1:
            ##DO m2
            #self.delete()
        #elif m==2:
            ##DO m3
            #self.modifiy()
        #else:
            ##DO m4
            ##DO NOTHING
            #return

##Time permitting
    ##def swap (self):
        ### Swap the order of two swaps in a sort
        ##return    