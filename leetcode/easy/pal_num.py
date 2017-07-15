""" Palindrome Numbers: https://leetcode.com/problems/palindrome-number

    Determine whether an integer is a palindrome. Do this without extra space.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        length = 0
        temp = int(n)

        # find the number of digits in the given integer
        while temp != 0:
          length += 1
          temp = temp // 10

        power = length - 1
        temp = int(n)

        # at each step converge towards the middle and compare numbers from both ends
        while temp:
          right = temp % 10               # find the rightmost digit
          temp = temp // 10

          left = (n // (10**power)) % 10  # find the leftmost digit
          if left != right:
            return False

          power -= 1
          if power <= length // 2:
            break
        return True

# a = Solution()
# print(a.isPalindrome(1234321))