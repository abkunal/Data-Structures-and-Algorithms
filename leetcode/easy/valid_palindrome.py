""" Valid Palindrome - https://leetcode.com/problems/valid-palindrome/

    Given a string, determine if it is a palindrome, 
    considering only alphanumeric characters and ignoring cases.

    For example,
    "A man, a plan, a canal: Panama" is a palindrome.
    "race a car" is not a palindrome.

    Note:
    Have you consider that the string might be empty? 
    This is a good question to ask during an interview.

    For the purpose of this problem, we define empty string as valid palindrome.

"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        a = [s[i] for i in range(len(s)) if (97 <= ord(s[i]) <= 122) or (48 <= ord(s[i]) <= 57)]
        return a == a[::-1]

a = Solution()
print(a.isPalindrome("A man, a plan, a canal: Panama"))