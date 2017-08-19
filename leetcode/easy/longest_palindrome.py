""" Longest Palindrome - https://leetcode.com/problems/longest-palindrome/

    Given a string which consists of lowercase or uppercase letters, 
    find the length of the longest palindromes that can be built with those letters.

    This is case sensitive, for example "Aa" is not considered a palindrome here.

    Note:
    Assume the length of given string will not exceed 1,010.

    Example:

    Input:
    "abccccdd"

    Output:
    7

    Explanation:
    One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1: return len(s)
        
        from collections import Counter
        c = Counter(s)

        evens = 0
        odd = 0
        k = None

        for key in c:
            if c[key] % 2 == 0:
                evens += c[key]
            elif c[key] > odd:
                odd = c[key]
                k = key
        for key in c:
            if key != k and c[key] % 2 == 1:
                evens += c[key] - 1

        return evens + odd


# a = Solution()
# print(a.longestPalindrome("abcccda"))