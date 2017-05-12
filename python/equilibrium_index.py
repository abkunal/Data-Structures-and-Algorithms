""" 
    Equilibrium index of an array is an index such that the sum of elements at
    lower indexes is equal to sum of elements at higher indexes
"""

def equilibrium_index(array):
    """ Returns the equilibrium index if it exists, -1 otherwise """

    total = sum(array)
    
    if total - array[0] == 0:
        return 0

    sofar = array[0]

    for i in range(1, len(array)):
        if sofar == total - array[i] - sofar:
            return i
        else:
            sofar += array[i]
    return -1

a = [-7,1,5,2,-4,3,0]
print(equilibrium_index(a))
