""" Combinations - https://leetcode.com/problems/combinations

    Given two integers n and k, return all possible combinations of k numbers 
    out of 1 ... n.

    For example,
    If n = 4 and k = 2, a solution is:

    [
      [2,4],
      [3,4],
      [2,3],
      [1,2],
      [1,3],
      [1,4],
    ]
"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.combs = []
        def rec_combine(sofar, rest, k):
            if len(sofar) == k:
                self.combs.append(sofar)
            else:
                rec_combine(sofar + [rest[0]], rest[1:], k)
                if len(sofar) + len(rest) - 1 >= k:
                    rec_combine(sofar, rest[1:], k)
                
        rec_combine([], [i for i in range(1, n+1)], k)
        return self.combs


# a = Solution()
# a.combine(4,1)