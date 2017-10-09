""" Remove Duplicates from Sorted Array II - 
    https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

    Follow up for "Remove Duplicates":
    What if duplicates are allowed at most twice?

    For example,
    Given sorted array nums = [1,1,1,2,2,3],

    Your function should return length = 5, with the first five elements of nums 
    being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        pos = 1
        current = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if current == nums[i]:
                count += 1
                if count <= 2:
                    nums[pos] = nums[i]
                    pos += 1
            else:
                current = nums[i]
                nums[pos] = nums[i]
                count = 1
                pos += 1

        return pos


# a = Solution()
# a.removeDuplicates([1,1,1,2,2,3])