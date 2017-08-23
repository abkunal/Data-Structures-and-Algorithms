""" Relative Ranks - https://leetcode.com/problems/relative-ranks

    Given scores of N athletes, find their relative ranks and the people with 
    the top three highest scores, who will be awarded medals: "Gold Medal", 
    "Silver Medal" and "Bronze Medal".

    Example 1:
    
    Input: [5, 4, 3, 2, 1]
    Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
    
    Explanation: The first three athletes got the top three highest scores, 
    so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
    
    For the left two athletes, you just need to output their relative ranks according to their scores.
    
    Note:
    N is a positive integer and won't exceed 10,000.
    All the scores of athletes are guaranteed to be unique.
"""

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0: return []
        a = sorted(nums, reverse=True)
        d = {a[i]:str(i+1) for i in range(len(a))}
        res = []
        for i in range(len(nums)):
            if int(d[nums[i]]) >= 4:
                res.append(d[nums[i]])
            elif int(d[nums[i]]) == 3:
                res.append("Bronze Medal")
            elif int(d[nums[i]]) == 2:
                res.append("Silver Medal")
            else:
                res.append("Gold Medal")
        return res