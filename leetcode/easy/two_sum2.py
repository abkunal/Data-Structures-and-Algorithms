""" Two Sum II - Input array is sorted - 
    https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

    Given an array of integers that is already sorted in ascending order, 
    find two numbers such that they add up to a specific target number.

    The function twoSum should return indices of the two numbers such that 
    they add up to the target, where index1 must be less than index2. 
    Please note that your returned answers (both index1 and index2) are not zero-based.

    You may assume that each input would have exactly one solution and 
    you may not use the same element twice.

    Input: numbers={2, 7, 11, 15}, target=9
    Output: index1=1, index2=2

"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # meet in the middle algorithm
        l = 0
        r = len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            # numbers found
            if total == target:
                return [l+1, r+1]
            # if the sum of numbers is less than target, increase l by 1
            elif total < target:
                l += 1
            # sum of numbers is greater than target, decrease r by 1
            else:
                r -= 1

# a = Solution()
# print(a.twoSum([2,7,11,19], 9))