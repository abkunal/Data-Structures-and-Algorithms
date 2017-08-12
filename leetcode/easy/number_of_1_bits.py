""" Number of 1 Bits - https://leetcode.com/problems/number-of-1-bits/ 
    
    Write a function that takes an unsigned integer and returns the number 
    of ’1' bits it has (also known as the Hamming weight).

    For example, the 32-bit integer ’11' has binary representation 
    00000000000000000000000000001011, so the function should return 3.
"""

class Solution:
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        assert n >= 0
        ones = 0
        while n != 0:
            if n % 2 == 1:
                ones += 1
            n = n // 2
        return ones

    def hammingWeight2(self, n):
        """ Python style """
        assert n >= 0
        return bin(n)[2:].count('1')

# a = Solution()
# print(a.hammingWeight(24))
