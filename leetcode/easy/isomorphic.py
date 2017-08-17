""" Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings
    
    Given two strings s and t, determine if they are isomorphic.

    Two strings are isomorphic if the characters in s can be replaced to get t.

    All occurrences of a character must be replaced with another character 
    while preserving the order of characters. No two characters may map to 
    the same character but a character may map to itself.

    For example,
    Given "egg", "add", return true.

    Given "foo", "bar", return false.

    Given "paper", "title", return true.

    Note:
    You may assume both s and t have the same length.
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapped = set()
        mappings = {}
        
        if len(s) != len(t): return False
        
        for i in range(len(s)):
            # if current character is already mapped, then check its value
            if s[i] in mappings:
                if mappings[s[i]] != t[i]:
                    return False
            # if current char is not mapped, check whether some other char
            # is mapped to the same value
            else:
                if t[i] in mapped:
                    return False
                mappings[s[i]] = t[i]
                mapped.add(t[i])
        return True


# a = Solution()
# print(a.isIsomorphic("egg", "add"))