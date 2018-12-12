#Merge Sort for # of inversions
# Reference https://www.geeksforgeeks.org/counting-inversions/

def countInversions(array):
    #Recursive Merge sort used to count inversions
    #If parameter given is of length 1, return
    if len(array) == 1:
        return 0, array
    #otherwise, divide and conquer recursively
    else:
        a = array[:int(len(array)/2)] # copy of first half of input array
        b = array[int(len(array)/2):] # copy of second half
        aInvs, a = countInversions(a)    # recursively call on 1st half of input, return # of inversions and sorted array
        bInvs, b  = countInversions(b)  # recursively call on 2nd half, ...
        
        #sorted result
        sortedArray = []
        i = 0
        j = 0
        #sum returned inversion counts
        inversions = 0 + aInvs + bInvs
    #iterate through each array comparing and swaping values - until either pointer exceeds length of array
    while i < len(a) and j < len(b):
        # append smallest value to sortedArray
        if a[i] <= b[j]:
            sortedArray.append(a[i])
            i += 1
        else:
            sortedArray.append(b[j])
            j += 1
            # for no inversions, iterator = length
            # therefore, length - iterator = number of inversions
            inversions += (len(a)-i)
    #if either pointer exceeds it's respective half array's length, append remainder of values
    sortedArray += a[i:]
    sortedArray += b[j:]
    #return # of inversions and result of merge
    return inversions, sortedArray 