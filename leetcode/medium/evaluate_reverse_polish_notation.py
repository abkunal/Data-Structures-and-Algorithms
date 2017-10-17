""" Evaluate Reverse Polish Notation - 
    https://leetcode.com/problems/evaluate-reverse-polish-notation/

    Evaluate the value of an arithmetic expression in Reverse Polish Notation.

    Valid operators are +, -, *, /. Each operand may be an integer or another expression.

    Some examples:
      ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
      ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            print(stack)
            if token in ['/', '*', '+', '-']:
                a = stack.pop()
                b = stack.pop()
                print(b,a,token)
                if token == '/':
                    if (b < 0 and a > 0) or (a < 0 and b > 0):
                        stack.append(-int(abs(b) / abs(a)))
                    else:
                        stack.append(int(b / a))
                elif token == '*':
                    stack.append(b * a)
                elif token == '-':
                    stack.append(b - a)
                else:
                    stack.append(b + a)
            else:
                stack.append(int(token))

        return stack.pop()


# a = Solution()
# print(a.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))