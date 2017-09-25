""" Subsets - https://leetcode.com/problems/subsets/

    Given a set of distinct integers, nums, return all possible subsets.

    Note: The solution set must not contain duplicate subsets.

    For example,
    If nums = [1,2,3], a solution is:

    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.subs = []
        def rec_subset(sofar, rest):
            if rest == []:
                self.subs.append(sofar)
            else:
                rec_subset(sofar + [rest[0]], rest[1:])
                rec_subset(sofar, rest[1:])
        
        rec_subset([], nums)

        return self.subs

    def subsets2(self, nums):
        """ Some fellow coder's iterative solution """
        res = [[]]
        for num in sorted(nums):
            res += [item + [num] for item in res]
        return res


# a = Solution()
# print(a.subsets2([1,2,3]))