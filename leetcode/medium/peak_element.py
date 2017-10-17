""" Find Peak Element - https://leetcode.com/problems/find-peak-element

    A peak element is an element that is greater than its neighbors.

    Given an input array where num[i] ≠ num[i+1], find a peak element and 
    return its index.

    The array may contain multiple peaks, in that case return the index to 
    any one of the peaks is fine.

    You may imagine that num[-1] = num[n] = -∞.

    For example, in array [1, 2, 3, 1], 3 is a peak element and your function 
    should return the index number 2.
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums)
        
        while low <= high:
            mid = (low + high) // 2
            if mid - 1 >= 0 and mid + 1 < len(nums):
                if nums[mid-1] < nums[mid] > nums[mid+1]:
                    return mid
                elif nums[mid-1] > nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            elif mid-1 >= 0:
                if nums[mid] > nums[mid-1]:
                    return mid
                return mid-1
            elif mid + 1 < len(nums):
                if nums[mid] > nums[mid+1]:
                    return mid
                return mid+1
            else:
                return mid


# a = Solution()
# print(a.findPeakElement([0,1,0,1,0]))