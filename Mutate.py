import numpy as np
import random as rng
import globalVariables as gV
import SortIndividual

##TODO probabilities as global variable
## probabilities of each mutation occuring
#m1p = 0.25
#m2p = 0.25
#m3p = 0.25
#m4p = 0.25

class Mutate:
# different mutation functions
    def add (self):
        # add new swap to sort
        if (len(self)<gV.maxSortLength):
            swap = []
            swap.append(rng.randint(0,100))
            swap.append(rng.randint(0,100))
            #Insert at random index 
            self.insert(rng.randint(0,len(self)), swap)
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