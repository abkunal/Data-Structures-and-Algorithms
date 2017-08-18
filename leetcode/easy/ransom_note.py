""" Ransom Note - https://leetcode.com/problems/ransom-note

    Given an arbitrary ransom note string and another string containing 
    letters from all the magazines, write a function that will return true 
    if the ransom note can be constructed from the magazines ; otherwise, 
    it will return false.

    Each letter in the magazine string can only be used once in your ransom note.

    Note:
    You may assume that both strings contain only lowercase letters.

    canConstruct("a", "b") -> false
    canConstruct("aa", "ab") -> false
    canConstruct("aa", "aab") -> true
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # solving in a general manner
        # could also be solved using dictionary
        a = [0] * 26
        for c in ransomNote:
            a[ord(c) % 97] += 1
        b = [0] * 26
        for c in magazine:
            b[ord(c) % 97] += 1
        
        for i in range(26):
            if a[i] > b[i]:
                return False
        return True