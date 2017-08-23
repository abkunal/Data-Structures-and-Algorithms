""" Base 7 - https://leetcode.com/problems/base-7

    Given an integer, return its base 7 string representation.

    Example 1:
    Input: 100
    Output: "202"
    
    Example 2:
    Input: -7
    Output: "-10"
    
    Note: The input will be in range of [-1e7, 1e7].
"""

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return "0"
        if num > 0:
            v = []
            while num != 0:
                v.append(str(num%7))
                num = num // 7
            return "".join(v[::-1])
        else:
            num = abs(num)
            v = []
            while num != 0:
                v.append(str(num%7))
                num = num // 7
            return "-"+"".join(v[::-1])