""" Two Sum - https://leetcode.com/problems/two-sum 
    
    Given an array of integers, return indices of the two numbers 
    such that they add up to a specific target.

    You may assume that each input would have exactly one solution, 
    and you may not use the same element twice.

    Example:
        Given nums = [2, 7, 11, 15], target = 9,

        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # using dictionary to store numbers and check for complement at each step
        dic = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in dic:
                return [dic[complement], i]
            dic[nums[i]] = i

# nums = [3,3]
# target = 6
# a = Solution()
# print(a.twoSum(nums, target))