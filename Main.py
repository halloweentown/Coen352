#COEN 352 Project
#import Mutate
import matplotlib.pyplot as plt
import numbers as np
import random as rng
import SortIndividual
import globalVariables
from countInversions import *
import globalVariables as gv
import pylab

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
parent0.calcFitness()                       # Calculate original parent fitness
OGPE = parent0.effectiveness                # Original parent effectiveness
OGPF = parent0.fitness                      # Original parent fitness
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
    
    nIterations.append(i)
    
    gv.iEvolution = i

print('Survivor fitness = ' + str(parent0.fitness))
print('Survivor effectiveness = ' + str(parent0.effectiveness))
print('Survivor History = ', parent0.mHistory)
print("O.G. Parent Effectiveness = " + str(OGPE))
print("O.G. Parent Fitness = " + str(OGPF))
print('nEffectiveness: ', nEffectiveness)
print('nEfficiency: ', nEfficiency)
print('nIterations: ', nIterations)


pylab.plot(nIterations,nEffectiveness, color='g', label='Effectiveness')
pylab.plot(nIterations,nEfficiency, color='orange', label='Efficiency')
pylab.plot(nIterations,nFitness, color='blue', label='Fitness')
pylab.xlabel('Evolution Iteration')
pylab.ylabel('Fitness')
pylab.title('Fitness vs Evolution Iteration: Randomly Sorted, Small Range')
pylab.legend(loc='upper left')
pylab.show()
# End condition (# of iterations, and/or fitness criteria)



    
