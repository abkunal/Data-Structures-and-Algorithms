""" Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones

    Given a binary array, find the maximum number of consecutive 1s in this array.

    Example 1:
    Input: [1,1,0,1,1,1]
    Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s.
        The maximum number of consecutive 1s is 3.
    Note:

    The input array will only contain 0 and 1.
    The length of input array is a positive integer and will not exceed 10,000
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = 0
        sofar = 0
        for i in nums:
            if i == 1:
                sofar += 1
                if sofar > maxi:
                    maxi = sofar
            else:
                sofar = 0
        return maxi

    def findMaxConsecutiveOnes2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = "".join(list(map(str, nums))).split("0")
        return len(max(a, key=lambda x:len(x)))