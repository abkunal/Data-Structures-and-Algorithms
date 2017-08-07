""" Roman to Integer - https://leetcode.com/problems/roman-to-integer 
    
    Given a roman numeral, convert it to an integer.

    Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0
        i = 0
        while i < len(s)-1:
            # if the symbol appears after a larger or equal symbol, it is added 
            if d[s[i]] >= d[s[i+1]]:
                total += d[s[i]]
                i += 1
            # if symbol appears before a larger symbol, it is subtracted
            else:
                total += d[s[i+1]] - d[s[i]]
                i += 2
        if i == len(s)-1:
            total += d[s[i]]
        return total

a = Solution()
