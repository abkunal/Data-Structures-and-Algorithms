""" Letter Combinations of a Phone Number - 
    https://leetcode.com/problems/letter-combinations-of-a-phone-number/

    Given a digit string, return all possible letter combinations that the 
    number could represent.

    Input: Digit string "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    
    Note:
    Although the above answer is in lexicographical order, your answer 
    could be in any order you want.
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        from itertools import product
        
        if not digits: return []
        
        mapping = {'0':' ', '1': '*','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        r = [mapping[d] for d in digits]
        res = list(product(*r))
        for i in range(len(res)):
            res[i] = "".join(res[i])
        
        return res