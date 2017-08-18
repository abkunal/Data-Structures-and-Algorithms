""" Intersection of Two Arrays II - leetcode.com/problems/intersection-of-two-arrays-ii/

    Given two arrays, write a function to compute their intersection.

    Example:
    Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

    Note:
    Each element in the result should appear as many times as it shows in both arrays.
    The result can be in any order.
    Follow up:
    What if the given array is already sorted? How would you optimize your algorithm?
    What if nums1's size is small compared to nums2's size? Which algorithm is better?
    What if elements of nums2 are stored on disk, and 
    the memory is limited such that you cannot load all elements into the memory at once?

"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d1 = {}
        d2 = {}
        # find number count in nums1
        for i in nums1:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        # find number count in nums2
        for i in nums2:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1
        inter = []
        # find common numbers with same count
        for key in d1:
            if key in d2:
                inter.extend([key]*min(d1[key], d2[key]))
        return inter