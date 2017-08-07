""" K'th Smallest Element - This is a geeksforgeeks problem
    http://practice.geeksforgeeks.org/problems/kth-smallest-element/0

Given an array and a number k where k is smaller than size of array, 
    the task is to find the k’th smallest element in the given array. 
    It is given that all array elements are distinct. 
"""
from random import randint

def partition(A, l, r): 
    p = A[l]
    j = l 

    for i in range(l + 1, r + 1): 
        if A[i] < p:
            j += 1
            A[j], A[i] = A[i], A[j]
    A[j], A[l] = p, A[j]
    return j


def quick_select(A, l, r, k): 
    """ Using a randomized variation of quick sort with O(n) average case. """
    if l == r:
        return A[l]

    ran = randint(l, r)
    A[l], A[ran] = A[ran], A[l]
    j = partition(A, l, r)
    
    if j+1 == k:
        return A[j]
    elif j+1 < k:
        return quick_select(A, j+1, r, k)
    else:
        return quick_select(A, l, j-1, k)