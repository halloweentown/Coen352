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
    if child.fitness > parent.fitness:
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
OGPF = parent0.calcFitness()                  # Calculate original parent fitness
OGPE = parent0.effectiveness                # Original parent effectiveness
nEffectiveness = []                         # List containing effectiveness scores
nEfficiency = []                            # List containing efficiency scores
nIterations = []                            # List containing iteration indices
nFitness = []                               # List containing fitness scores

for i in range(gv.nEvolutions):
    # Mutate Offspring of individual
    nEffectiveness.append(parent0.effectiveness)
    nEfficiency.append(parent0.efficiency)
    nFitness.append(parent0.fitness)
    child = parent0.mutate()
    
    print("Parent effectiveness = " + str(parent0.effectiveness))
    print("Parent fitness = " + str(parent0.fitness))
    print("Child effectiveness = " + str(child.effectiveness))
    print("Child fitness = " + str(child.fitness))
    
    parent0 = cull(parent0, child)
    
    print(parent0.effectiveness)
    
    nIterations.append(i)
    
    gv.iEvolution = i

print('Survivor fitness = ' + str(child.fitness))
print('Survivor effectiveness = ' + str(child.effectiveness))
print("O.G. Parent Effectiveness = " + str(OGPE))
print("O.G. Parent Fitness = " + str(OGPF))
print('nEffectiveness: ', nEffectiveness)
print('nEfficiency: ', nEfficiency)
print('nIterations: ', nIterations)


plt.plot(nIterations,nEffectiveness, color='g')
plt.plot(nIterations,nEfficiency, color='orange')
plt.xlabel('Evolution Iteration')
plt.ylabel('Fitness')
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

    
