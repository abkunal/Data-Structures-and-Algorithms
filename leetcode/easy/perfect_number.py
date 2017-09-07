""" Perfect Number - 

    
    We define the Perfect Number is a positive integer that is equal to the sum 
    of all its positive divisors except itself.

    Now, given an integer n, write a function that returns true when it is a 
    perfect number and false when it is not.
    
    Example:
    
    Input: 28
    Output: True
    
    Explanation: 28 = 1 + 2 + 4 + 7 + 14
    
    Note: The input number n will not exceed 100,000,000. (1e8)
"""

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool

        Using Euclid-Euler Theorem
        """
        primes = [2,3,5,7,13,17,19,31]
        for p in primes:
            euclid = (1 << (p-1)) * ((1 << (p)) - 1)
            if euclid == num:
                break
        return euclid == num

    def checkPerfectNumber2(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1: return False

        total = 0
        
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                total += i
        
                if i * i != num:
                    total += num // i
        
        return total - num == num