#COEN 352 Project
#import Mutate
import numbers as np
import random as rng
import SortIndividual
import globalVariables
import countInversions

# Input array to be sorted
inputArray = [9,3,13,19,13,22,22,62,66,73,79,82,96,99,115,127,130,134,143,171,182,189,189,213,225,227,230,242,244,246,253,288,297,307,329,340,374,382,391,409,422,424,434,440,442,448,458,471,477,498,511,521,528,533,549,551,562,573,581,581,585,586,586,587,588,598,612,643,651,651,685,699,699,708,711,745,760,764,766,777,779,785,786,804,812,813,829,830,843,871,876,910,915,917,918,928,940,977,988,991]

# Create initial sort to be evolved
a=SortIndividual.SortIndividual()
print(a.sort)

# Mutate Offspring of individual
a.add()
print(a.sort)

# Tournament selection of best sort

# Print Survivor's specs

# End condition (# of iterations, and/or fitness criteria)


'''_,inversions=countInversions.countInversions(inputArray)
print(sorted)
sorted,_=countInversions.countInversions(inputArray)
print(inversions)
print(countInversions.countInversions(inputArray))'''

# Reference code for raw input
# username = raw_input("What is your login? :  ")

# x = np.array()

def cull (poolOfContenders):
    # Reduce number of individuals to specified population
    return
    
