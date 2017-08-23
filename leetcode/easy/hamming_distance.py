""" Hamming Distance - https://leetcode.com/problems/hamming-distance
    
    The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

    Given two integers x and y, calculate the Hamming distance.

    Note:
    0 ≤ x, y < 231.

    Example:

    Input: x = 1, y = 4

    Output: 2

    Explanation:
    1   (0 0 0 1)
    4   (0 1 0 0)
           ?   ?

    The above arrows point to positions where the corresponding bits are different.
"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bx = bin(x)
        by = bin(y)
        print(bx, by)
        if bx[0] == '-':
            bx = bx[3:]
        else: bx = bx[2:]
        
        if by[0] == '-':
            by = by[3:]
        else: by = by[2:]
        
        distance = 0
        if len(bx) < len(by):
            bx = "0" * (len(by) - len(bx)) + bx
        if len(by) < len(bx):
            by = "0" * (len(bx) - len(by)) + by
        
        print(bx, by)
        for i in range(len(bx)):
            if bx[i] != by[i]:
                distance += 1
        return distance

    def hammingDistance2(self, x, y):
        # Using bitwise XOR
        return bin(x^y).count('1')