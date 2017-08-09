""" Maximum of all subarrays of size k
    http://practice.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k/0

    Given an array and an integer k, find the maximum for each and every contiguous subarray of size k.

    Example:

    Input:
    2
    9 3
    1 2 3 1 4 5 2 3 6
    10 4
    8 5 10 7 9 4 15 12 90 13

    Output:
    3 3 4 5 5 5 6
    10 10 10 15 15 90 90
"""

from collections import deque

for t in range(int(input())):
    # get input
    n, k = input().split()
    n, k = int(n), int(k)
    arr = list(map(int, input().split()))
    
    # using deque, maintain the invariant, the front of the deque will always be the largest
    # and the rear of deque will always be th smallest.
    d  = deque()
    for i in range(k):
        # if the last element of the deque is smaller than or equal to current 
        # element in a, pop it out
        while len(d) and arr[i] >= d[-1][0]:
            d.pop()
        d.append((arr[i], i))
    

    for i in range(k, n):
        # print the maximum number
        print(d[0][0], end=" ")
        
        # remove all elements that are out of bounds
        while len(d) and d[0][1] <= i - k:
            d.popleft()
        
        # remove smaller elements
        while len(d) and arr[i] >= d[-1][0]:
            d.pop()
    
        d.append((arr[i], i))
    print(d[0][0])
