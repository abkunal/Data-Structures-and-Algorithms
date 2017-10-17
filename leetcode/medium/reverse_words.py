""" Reverse Words in a string -
    https://leetcode.com/problems/reverse-words-in-a-string/

    Given an input string, reverse the string word by word.

    For example,
    Given s = "the sky is blue",
    return "blue is sky the".
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1])


# a = Solution()
# print(a.reverseWords("the sky is blue"))