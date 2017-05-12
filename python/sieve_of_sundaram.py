""" Sieve of Sundaram method to find prime numbers """

def sos(n):
    """ This method finds primes upto 2*n+2 for an integer n """
    N = (n-2) // 2
    
    # marking all the number as False
    marked = [False] * (n+1)

    for i in range(1, N):
        j = 1
        # marking all number of the form i + j + 2*i*j as True
        while i + j + 2*i*j <= N:
            marked[i+j+2*i*j] = True
            j += 1

    if n > 2:
        print(2, end=" ")
        
        i = 1
        # all number of the form 2*i+1 are primes such that marked[2*i+1] is False
        while 2 * i + 1 < n:
            if marked[2*i+1] is False:
                print(2*i+1, end=" ")
            i += 1
        print()
    elif n == 2:
        print(2)
    else:
        print(-1)

print(sos(5))
print(sos(100))
