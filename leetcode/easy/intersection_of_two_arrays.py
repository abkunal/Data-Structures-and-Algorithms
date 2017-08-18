""" Intersection of Two Arrays

    Given two arrays, write a function to compute their intersection.

    Example:
    Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

    Note:
    Each element in the result must be unique.
    The result can be in any order.
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        same = {}
        for i in nums1:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for j in nums2:
            if j in d:
                same[j] = True
                
        return list(same.keys())