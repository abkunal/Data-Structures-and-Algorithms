""" Construct String from Binary Tree - 
    https://leetcode.com/problems/construct-string-from-binary-tree

    You need to construct a string consists of parenthesis and integers from a 
    binary tree with the preorder traversing way.

    The null node needs to be represented by empty parenthesis pair "()". 
    And you need to omit all the empty parenthesis pairs that don't affect 
    the one-to-one mapping relationship between the string and the original binary tree.

    Example 1:
    Input: Binary tree: [1,2,3,4]
           1
         /   \
        2     3
       /    
      4     

    Output: "1(2(4))(3)"

    Explanation: Originallay it needs to be "1(2(4)())(3()())", 
    but you need to omit all the unnecessary empty parenthesis pairs. 
    And it will be "1(2(4))(3)".
    
    Example 2:
    Input: Binary tree: [1,2,3,null,4]
           1
         /   \
        2     3
         \  
          4 

    Output: "1(2()(4))(3)"

    Explanation: Almost the same as the first example, 
    except we can't omit the first parenthesis pair to break the one-to-one 
    mapping relationship between the input and the output.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def preorder(root):
            if root:
                sofar = "(" + str(root.val)

                x = preorder(root.left)
                y = preorder(root.right)

                if x and y:
                    sofar += x + y + ")"
                elif x:
                    sofar += x + ")"
                elif y:
                    sofar += "()" + y + ")"
                else:
                    sofar += ")"
                return sofar
            return None

        a = preorder(t)

        if a is None:
            return ""
        return a[1:-1]
        

# a = Solution()

# t1 = TreeNode(1)
# t2 = TreeNode(2)
# t3 = TreeNode(3)
# t4 = TreeNode(4)

# t1.left = t2
# t1.right = t3
# t2.right = t4

# print(a.tree2str(t1))