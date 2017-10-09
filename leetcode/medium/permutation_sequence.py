""" Permutation Sequence - https://leetcode.com/problems/permutation-sequence
    
    The set [1,2,3,…,n] contains a total of n! unique permutations.

    By listing and labeling all of the permutations in order,
    We get the following sequence (ie, for n = 3):

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"
    Given n and k, return the kth permutation sequence.

    Note: Given n will be between 1 and 9 inclusive.
"""

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from math import factorial
        numbers = list(range(1, n+1))
        perm = ''
        k -= 1
        while n > 0:
            n -= 1
            index, k = divmod(k, factorial(n))
            perm += str(numbers[index])
            numbers.remove(numbers[index])
        return perm


# a = Solution()
# print(a.getPermutation(5,33))