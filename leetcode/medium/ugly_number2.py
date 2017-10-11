""" Ugly Number II - https://leetcode.com/problems/ugly-number-ii

    Write a program to find the n-th ugly number.

    Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
    For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

    Note that 1 is typically treated as an ugly number, and n does not exceed 1690.
"""

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        
        ugly = [1]
        two_index = 0
        three_index = 0
        five_index = 0

        next_mul_of_2 = ugly[two_index] * 2
        next_mul_of_3 = ugly[three_index] * 3
        next_mul_of_5 = ugly[five_index] * 5

        for i in range(n-1):
            num = min(next_mul_of_2, next_mul_of_3, next_mul_of_5)
            ugly.append(num)

            if num == next_mul_of_2:
                two_index += 1
                next_mul_of_2 = ugly[two_index] * 2
            if num == next_mul_of_3:
                three_index += 1
                next_mul_of_3 = ugly[three_index] * 3
            if num == next_mul_of_5:
                five_index += 1
                next_mul_of_5 = ugly[five_index] * 5

        return ugly[-1]


# a = Solution()
# print(a.nthUglyNumber(130))