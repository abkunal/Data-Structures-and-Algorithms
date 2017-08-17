""" Power of Three - https://leetcode.com/problems/power-of-three

  Given an integer, write a function to determine if it is a power of three.

  Follow up:
  Could you do it without using any loop / recursion?

"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        from math import log10
        if n <= 0: return False
        x = log10(n) / log10(3)
        return x == int(x)


# a = Solution()
# print(a.isPowerOfThree(3))
# print(a.isPowerOfThree(81))
# print(a.isPowerOfThree(45))