""" Count Primes - https://leetcode.com/problems/count-primes
    
    Description:

    Count the number of prime numbers less than a non-negative number, n.
"""


from math import sqrt

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int

        Using Sieve of eratosthenes
        """
        # base case
        if n == 0: return 0
        
        # initialize all numbers below n as True (is prime)
        primes = [True for i in range(n)]
        if n > 1:
            primes[0] = primes[1] = False
        else:
            primes[0] = False
        
        # iterate over all numbers and set their multiples to False (is not prime)
        for i in range(2, int(sqrt(n+1))+1):
            for j in range(2*i, n+1, i):
                primes[j] = False
        if n > 2: primes[2] = True

        # count the number of primes (number of elements set to True)
        count = 0
        for i in primes:
            if i is True: count += 1
        return count

# a = Solution()
# print(a.Solution(454))
