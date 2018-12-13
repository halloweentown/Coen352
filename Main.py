#COEN 352 Project
#import Mutate
import matplotlib.pyplot as plt
import numbers as np
import random as rng
import SortIndividual
import globalVariables
from countInversions import *
import globalVariables as gv

# Tournament selection of best sort
def cull(parent, child):
    if child.effectiveness > parent.effectiveness:
        del child
        b = parent
    else:
        del parent
        b = child
    return  b

# Input array to be sorted
inputArray = gv.inputArray
print("initial # of inversions was " + str(countInversions(inputArray)))

# Create initial sort to be evolved
parent0=SortIndividual.SortIndividual()     
parent0.applySort(inputArray)               # Apply sort to array of inputs
parent0.calcFitness()                       # Calculate original parent fitness
OGPF = parent0.effectiveness                # Original parent effectiveness
nEffectiveness = []                         # List containing effectiveness scores
nIterations = []                            # List containing iteration indices

for i in range(1000):
    # Mutate Offspring of individual
    nEffectiveness.append(parent0.effectiveness)
    child = parent0.mutate()
    print("Parent effectiveness = " + str(parent0.effectiveness))
    print("Child effectiveness = " + str(child.effectiveness))
    parent0 = cull(parent0, child)
    print(parent0.effectiveness) 
    nIterations.append(i)

print("O.G. Parent Fitness = " + str(OGPF))
print('nEffectiveness: ', nEffectiveness)
print('nIterations: ', nIterations)


plt.plot(nIterations,nEffectiveness, color='g')
#plt.plot(nIterations,nEfficiency, color='orange')
plt.xlabel('Evolution Iteration')
plt.ylabel('Effectiveness in Number of Inversions')
plt.title('Fitness vs Evolution Iteration')
plt.show()
# End condition (# of iterations, and/or fitness criteria)


'''_,inversions=countInversions.countInversions(inputArray)
print(sorted)
sorted,_=countInversions.countInversions(inputArray)
print(inversions)
print(countInversions.countInversions(inputArray))'''

# Reference code for raw input
# username = raw_input("What is your login? :  ")

# x = np.array()

    
