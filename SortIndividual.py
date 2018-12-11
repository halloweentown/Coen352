import Mutate
import numbers as np
import random as rng
import globalVariables as gv

#inputArray = [1,2,3,4]
#power = 3
#n = len(inputArray)
#minSortLength = n
#maxSortLength = n^power

class SortIndividual:
    def __init__(self):
        # ~~~~~~~~~~~~~ member Variables
        #TODO swaps
        sort=[]
        for i in range(gv.n):
            swap = []
            swap.append(rng.randint(0,100))
            swap.append(rng.randint(0,100))
            #print (swap)
            sort.append(swap)
            #print (sort)
        
       
        # fitness
        efficiency = len(sort)      
        #print(efficiency)
        effectivenes = 0            # fitness
        age = 0                       # Number of iterations survived
        #TODO N2H - mutation history
        # mHistory = []
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