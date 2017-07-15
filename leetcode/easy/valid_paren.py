""" Valid Parenthesis - https://leetcode.com/problems/valid-parentheses

    Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    The brackets must close in the correct order, "()" and "()[]{}" are all 
    valid but "(]" and "([)]" are not.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # stack to store open brackets
        stack = []
        paren = ['(', '{', '[']
        dic = {')': '(', '}': '{', ']':'['}

        # for each character in s
        for c in s:
            # c is an open bracket, push onto stack
            if c in paren:
                stack.append(c)
            # c is a closed bracket
            else:
                # stack is empty, no open bracket found
                if len(stack) == 0:
                    return False
                # top element is not the correct bracket, not valid string
                elif stack.pop() != dic[c]:
                    return False
        # open brackets left in the stack, no corresponding closed brackets found
        if len(stack) != 0:
            return False
        return True

# a = Solution()
# print(a.isValid("(((())))"))