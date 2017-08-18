""" Valid Perfect Square - https://leetcode.com/problems/valid-perfect-square/

    Given a positive integer num, write a function which returns True 
    if num is a perfect square else False.

    Note: Do not use any built-in library function such as sqrt.

    Example 1:

    Input: 16
    Returns: True
    Example 2:

    Input: 14
    Returns: False

"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # using binary search tecnihuq
        def sqrt(x, low, high):
            if low >= high:
                return x == low**2
            
            mid = (low + high) // 2
            if mid**2 == x:
                return True
            elif mid**2 < x:
                return sqrt(x, mid + 1, high)
            else:
                return sqrt(x, low, mid - 1)
        
        return sqrt(num, 1, num)