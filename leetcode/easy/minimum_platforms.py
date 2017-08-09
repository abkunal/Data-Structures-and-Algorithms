""" Minimum Platforms - http://practice.geeksforgeeks.org/problems/minimum-platforms/0 
    
    Given arrival and departure times of all trains that reach a railway station, 
    find the minimum number of platforms required for the railway station so that no train waits.

    NOTE: Time intervals are in 24 hour format(hhmm),preceding zeros are insignificant.
    Consider the example for better understanding of input.

    Example:

    INPUT:

    1
    6 
    900  940 950  1100 1500 1800
    910 1200 1120 1130 1900 2000

    OUTPUT:

    3
"""

for t in range(int(input())):
    # get arrival and departure time of trains
    n = int(input())
    arr = list(map(int, input().split()))
    dep = list(map(int, input().split()))
    
    # a - index of arr, d - index of dep, sofar - number of platforms needed at some instant
    # maxi - maximum number of platforms needed.
    a,d,sofar,maxi = 1,0,0,0

    while a < n and d < n:
        # if a new train arrives, increase sofar
        if arr[a] < dep[d]:
            sofar += 1
            a += 1
            if sofar > maxi:
                maxi = sofar
        # if a train departs, decrease sofar
        else:
            sofar -= 1
            d += 1
    print(maxi)
