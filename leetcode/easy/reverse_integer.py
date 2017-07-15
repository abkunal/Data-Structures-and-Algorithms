""" Reverse Integer - https://leetcode.com/problems/reverse-integer

    
    Reverse digits of an integer.

        Example1: x = 123, return 321
        Example2: x = -123, return -321

    Note:
        The input is assumed to be a 32-bit signed integer. 
        Your function should return 0 when the reversed integer overflows.
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # for negative integers
        if x < 0:
            rev = int("-" + str(x)[::-1][:-1])   
            if -2**31 <= rev < 2**31:
                return rev
            else:
                return 0
        # for positive integers
        else:
            rev = int(str(x)[::-1])
            if -2**31 <= rev < 2**31:
                return rev
            else:
                return 0
        

#a = Solution()
#print(a.reverse(1234567))