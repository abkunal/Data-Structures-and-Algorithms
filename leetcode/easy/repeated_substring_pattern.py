""" Repeated Substring Pattern

    Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

    Example 1:
    Input: "abab"

    Output: True

    Explanation: It's the substring "ab" twice.
    Example 2:
    Input: "aba"

    Output: False
    Example 3:
    Input: "abcabcabcabc"

    Output: True

    Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        
        Insights:

        - the first char of s equals first char of repeated substring.
        - the last char of s equals last char of repeated substring.
        - if s has a repeated substring pattern, then that substring occurs
          at least 2 times.
          Hence (s + s)[1:-1] must include s if s is made up of a repeated substring.

          Eg: s = "abab"
              first char = "a", last char = "b"
              s + s = "abababab"
              (s + s)[1:-1] = "bababa" contains s (index 1-4)
        """

        return (s+s)[1:-1].find(s) != -1