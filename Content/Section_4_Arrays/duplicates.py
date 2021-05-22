# Duplicates in an array
#The problem is that we want to find duplicates in a one-dimensional array of integers in 
# O(N) running time where the integer values are smaller than the length of the array
#Ex. [1, 2, 3, 1, 5] dup is 1

def dup(l1):
    # This is an empty list to record what number we have seen so far
    seen = []
    # loop through the entire array of numbers
    for i in l1:
        #This will see if we have seen this number before
        if i in seen:
            return i
        #Add this value that we seen to the list
        seen.append(i)
    return None

if __name__ == '__main__':
    
    x = [1,2,3,1,5]

    print(dup(x))