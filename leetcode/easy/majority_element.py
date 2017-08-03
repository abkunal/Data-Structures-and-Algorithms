""" Majority Element - https://leetcode.com/problems/majority-element/
    
    Given an array of size n, find the majority element. 
    The majority element is the element that appears more than ⌊ n/2 ⌋ times.

    You may assume that the array is non-empty and the majority 
    element always exist in the array.

"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # store the count of all the numbers
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        # check for majority element
        for key in d:
            if d[key] > len(nums) // 2:
                return key

#a = Solution()
#print(a.majorityElement([1,2,1,1,4,1]))