""" 
    Maximum subarray size, such that all the subarrays of that size have sum
    less than k. 
"""

def max_size(arr, k):
    """ 
        Return the maximum size such that all the subarrays of that size have
        sum less than k, 
        -1 otherwise
    """
    prefix = [0] * (len(arr) + 1)
    
    for i in range(len(arr)):
        prefix[i+1] = arr[i] + prefix[i]

    return search(prefix, k)

def search(prefix, k):
    """ Same as max_size """
    n = len(prefix)-1
    size, left, right = -1, 1, n

    while left <= right:
        mid = (left + right) // 2
        
        for i in range(mid, n+1):
            if (prefix[i] - prefix[i-mid]) > k:
                i -= 1
                break

        i += 1

        if i == n+1:
            # subarrays of size mid exists, try if subarrays of size > mid exist
            left = mid + 1
            size = mid
        else:
            # subarrays of size mid doesn't exists, try something smaller
            right = mid - 1
    
    return size


