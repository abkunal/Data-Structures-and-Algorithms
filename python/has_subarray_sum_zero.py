""" Find if there is a subarray of with 0 sum """

def subarray(arr):
    """ Returns True if there is a subarray with 0 sum, False otherwise """

    d = {}
    sofar = 0

    for i in range(len(arr)):
        sofar += arr[i]

        if sofar == 0 or sofar in d:
            return True
        d[sofar] = True
    return False

a = [1,2,-2,4]
print(subarray(a))
