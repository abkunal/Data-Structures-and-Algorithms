""" Power of Two - https://leetcode.com/problems/power-of-two

    Given an integer, write a function to determine if it is a power of two.
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        return not (n & n - 1)

# a = Solution()
# print(a.isPowerOfTwo(2))
# print(a.isPowerOfTwo(3))
# print(a.isPowerOfTwo(38593824))
# print(a.isPowerOfTwo(0))