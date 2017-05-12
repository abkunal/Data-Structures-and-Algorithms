""" Prefix Sum Array """


""" Example of a prefix sum Array - geeksforgeeks.org
    
    Input  : arr[] = {10, 20, 10, 5, 15}
    Output : prefixSum[] = {10, 30, 40, 45, 60}
    Explanation : While traversing the array, update 
    the element by adding it with its previous element.
    prefixSum[0] = 10, 
    prefixSum[1] = prefixSum[0] + arr[1] = 30, 
    prefixSum[2] = prefixSum[1] + arr[2] = 40 and so on.
"""

def prefix_sum_array(array):
    """ Takes an array of integers and returns its prefix sum array """
    prefix_arr = [None] * len(array)
    
    sofar = array[0]
    prefix_arr[0] = array[0]

    for i in range(1, len(array)):
        sofar += array[i]
        prefix_arr[i] = sofar

    return prefix_arr

a = [10, 20, 10, 15, 30]
print(prefix_sum_array(a))
