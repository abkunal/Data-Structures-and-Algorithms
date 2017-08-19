""" Number of Segments in a String - 
    https://leetcode.com/problems/number-of-segments-in-a-string

    Count the number of segments in a string, where a segment is 
    defined to be a contiguous sequence of non-space characters.

    Please note that the string does not contain any non-printable characters.

    Example:

    Input: "Hello, my name is John"
    Output: 5
"""

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        segments = 0
        space_pos = []
        i = 0
        while i < len(s):
            while i < len(s) and s[i] == " ":
                i += 1
            if i < len(s):
                segments += 1
            while i < len(s) and s[i] != " ":
                i += 1
        return segments

    def countSegments2(self, s):
        # A pythonic solution
        return len(s.split())