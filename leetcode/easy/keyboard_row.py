""" Keyboard Row - 

    Given a List of words, return the words that can be typed using letters of 
    alphabet on only one row's of American keyboard.

    Example 1:

    Input: ["Hello", "Alaska", "Dad", "Peace"]
    Output: ["Alaska", "Dad"]

    Note:

    You may use one character in the keyboard more than once.
    You may assume the input string will only contain letters of alphabet.
"""

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        f = set(['q', 'w','e','r','t','y','u','i','o','p'])
        s = set(['a','s','d','f','g','h','j','k','l'])
        t = set(['z','x','c','v','b','n','m'])
        res = []
        row = {1: f, 2: s, 3: t}
        for word in words:
            covered = 0
            l = None
            if word:
                if word[0].lower() in f:    
                    l = 1
                elif word[0].lower() in s:
                    l = 2
                else: l = 3
                
                for c in word.lower():
                    if c in row[l]:
                        covered += 1
                if covered == len(word):
                    res.append(word)
        return res