""" Balanced Binary Tree

    Given a binary tree, determine if it is height-balanced.

    For this problem, a height-balanced binary tree is defined as a binary tree
    in which the depth of the two subtrees of every node never differ by more than 1.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))
        def balanced(root):
            if root:
                return (abs(height(root.left) - height(root.right)) <= 1) and balanced(root.left) and balanced(root.right)
            return True
        return balanced(root)