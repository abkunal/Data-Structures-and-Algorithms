""" Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers
    
    Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

    Example:
    Given a = 1 and b = 2, return 3.
"""

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # Learned this method from here - 
        # https://discuss.leetcode.com/topic/49771/java-simple-easy-understand-solution-with-explanation
        if a == 0: return b
        if b == 0: return a

        maxi = 0x7FFFFFFF
        mask = 0xFFFFFFFF

        while b != 0:
            carry = a & b
            a = (a ^ b) & mask
            b = (carry << 1) & mask
        return a if a <= maxi else ~(a ^ mask)

#a = Solution()
#print(a.getSum(10, 34))
