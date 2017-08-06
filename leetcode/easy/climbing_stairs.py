""" Climbing Stairs - https://leetcode.com/problems/climbing-stairs

    You are climbing a stair case. It takes n steps to reach to the top.

    Each time you can either climb 1 or 2 steps. 
    In how many distinct ways can you climb to the top?

    Note: Given n will be a positive integer.
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # A fibonacci based solution
        cur, prev = 1, 0
        for i in range(n):
            cur, prev = cur + prev, cur
        return cur
