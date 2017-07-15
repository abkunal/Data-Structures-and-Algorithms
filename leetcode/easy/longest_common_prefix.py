""" Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix 

    Write a function to find the longest common 
    prefix string amongst an array of strings.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # trivial cases
        if len(strs) == 1:
            return strs[0]
        elif len(strs) == 0:
            return ''

        # stores the longest common prefix
        longest = ""
        size = 0
        j = 0

        # find the longest common prefix for the first two strings
        while j < len(strs[0]) and j < len(strs[1]):
            if strs[0][j] == strs[1][j]:
                size += 1
            else:
                break
            j += 1
        longest = strs[0][:size]

        # find the longest common prefix for all the remaining strings
        for i in range(2, len(strs)):
            j = 0
            size = 0
            while j < len(longest) and j < len(strs[i]):
                if longest[j] == strs[i][j]:
                    size += 1
                else:
                    break
                j += 1
            longest = longest[:size]
            
        return longest

    def longestCommonPrefix2(self, strs):
        """ Vertical scanning algorithm. """
        if not strs:
            return None

        # for each character in strs[0] at position i, compare it with 
        # character at i-th position for all the strings.
        for i in range(len(strs[0])):
            char = strs[i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]

#a = Solution()
#print(a.longestCommonPrefix(['a','a','b']))