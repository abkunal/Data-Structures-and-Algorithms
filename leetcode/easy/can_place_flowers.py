""" Can Place Flowers - https://leetcode.com/problems/can-place-flowers/

    Suppose you have a long flowerbed in which some of the plots are planted 
    and some are not. However, flowers cannot be planted in adjacent plots - 
    they would compete for water and both would die.

    Given a flowerbed (represented as an array containing 0 and 1, 
    where 0 means empty and 1 means not empty), and a number n, return if n 
    new flowers can be planted in it without violating the no-adjacent-flowers rule.

    Example 1:
    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: True
    
    Example 2:
    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: False
    
    Note:
    
    The input array won't violate no-adjacent-flowers rule.
    The input array size is in the range of [1, 20000].
    n is a non-negative integer which won't exceed the input array size.
"""

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # find the index of first flower (1)
        try:    
            fp = flowerbed.index(1)
        except ValueError:
            fp = -1
        
        # plant in all legal empty plots
        left = fp - 2
        for i in range(left, -1, -2):
            n -= 1
        
        if fp == -1:
            if len(flowerbed) % 2 == 0:
                return n <= len(flowerbed) // 2
            else:
                return n <= (len(flowerbed) // 2 + 1)
        
        # plant in all the empty legal plots to the right of first planted flower
        for i in range(fp+1, len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1

        if len(flowerbed) > 2 and flowerbed[-1] == 0 and flowerbed[-2] == 0:
            n -= 1
        return n <= 0