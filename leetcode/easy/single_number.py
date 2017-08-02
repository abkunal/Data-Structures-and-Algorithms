""" Single Number - https://leetcode.com/problems/single-number

    Given an array of integers, every element appears twice except for one. 
    Find that single one.

    Note:
    Your algorithm should have a linear runtime complexity. 
    Could you implement it without using extra memory?

"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        c = Counter(nums)
        for val in c:
            if c[val] == 1:
                return val

        # optimised solution using bitwise XOR by someone on leetcode
        # x = 0
        # for i in nums:
        #   x = x^i
        # return x

#a = Solution()
#print(a.singleNumber([1,2,4,6,4,2,5,6,1]))