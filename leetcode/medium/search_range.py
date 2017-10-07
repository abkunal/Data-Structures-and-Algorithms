""" Search for a Range - https://leetcode.com/problems/search-for-a-range

    Given an array of integers sorted in ascending order, find the starting 
    and ending position of a given target value.

    Your algorithm's runtime complexity must be in the order of O(log n).

    If the target is not found in the array, return [-1, -1].

    For example,
    Given [5, 7, 7, 8, 8, 10] and target value 8,
    return [3, 4].
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return [-1,-1]
        def binary_search(low, high, nums, target):
            if low >= high:
                return low

            mid = (low+high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid+1, high, nums, target)
            return binary_search(low, mid-1, nums, target)

        # find left-most
        x = binary_search(0, len(nums)-1, nums, target)
        if nums[x] != target:
            return [-1,-1]
        
        while nums[x] == target:
            l = x
            if x -1 < 0: break
            x = binary_search(0,x - 1, nums, target)
        
        # find right-most
        x = binary_search(0, len(nums)-1, nums, target)
        while nums[x] == target:
            r = x
            if x + 1 >= len(nums): break
            x = binary_search(x+1, len(nums)-1, nums, target)
        return [l, r]


# a = Solution()
# print(a.searchRange([5, 7, 7, 10], 8))