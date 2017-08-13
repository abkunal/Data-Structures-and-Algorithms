""" Contains Duplicate II - https://leetcode.com/problems/contains-duplicate-ii

    Given an array of integers and an integer k, find out whether there are 
    two distinct indices i and j in the array such that nums[i] = nums[j] and 
    the absolute difference between i and j is at most k.
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # store indices of all the numbers
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]].append(i)
            else:
                d[nums[i]] = [i]

        # compare the indices of a given number
        for key in d:
            for i in range(len(d[key])-1):
                if d[key][i+1] - d[key][i] <= k:
                    return True
        return False

# a = Solution()
# print(a.containsNearbyDuplicate([1,2,3,4,1], 5))