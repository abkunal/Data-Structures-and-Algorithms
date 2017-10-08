""" Search in Rotated Sorted Array - 
    https://leetcode.com/problems/search-in-rotated-sorted-array

    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

    You are given a target value to search. If found in the array return its index, otherwise return -1.

    You may assume no duplicate exists in the array.
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 1: return -1

        def find_intersection(low, high, nums):
            mid = (low + high) // 2
            if nums[(mid+1)%len(nums)] < nums[mid] > nums[(mid-1)%len(nums)]:
                return mid, (mid+1) % len(nums)
            elif nums[mid] < nums[high]:
                return find_intersection(low, mid, nums)
            else:
                return find_intersection(mid, high, nums)

        def binary_search(low, high, nums, target):
            if low >= high:
                return low
            mid = (low+high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid+1, high, nums, target)
            else:
                return binary_search(low, mid-1, nums, target)

        if len(nums) < 3:
            if target in nums:
                return nums.index(target)
            else:
                return -1
        elif nums[0] < nums[-1]:
            x = binary_search(0, len(nums)-1, nums, target)
            if nums[x] == target:
                return x
            return -1
        else:
            inter = find_intersection(0, len(nums)-1, nums)
            if nums[inter[1]] <= target and nums[-1] >= target:
                x = binary_search(inter[1], len(nums)-1, nums, target)
                if nums[x] == target:
                    return x
                return -1
            else:
                x = binary_search(0, inter[0], nums, target)
                if nums[x] == target:
                    return x
                return -1


# a = Solution()
# print(a.search([3,5,1], 0))