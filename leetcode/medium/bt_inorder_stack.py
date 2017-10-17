""" Binary Tree Inorder Traversal - 
    https://leetcode.com/problems/binary-tree-inorder-traversal

    Given a binary tree, return the inorder traversal of its nodes' values.

    For example:
    Given binary tree [1,null,2,3],
       1
        \
         2
        /
       3
    return [1,3,2].

    Note: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        current = root
        stack = []
        seq = []
        while stack != [] or current is not None:
            if current is None:
                top = stack.pop()
                seq.append(top.val)
                current = top.right
            else:
                stack.append(current)
                current = current.left
        return seq


# a = Solution()
# t1 = TreeNode(1)
# t2 = TreeNode(2)
# t3 = TreeNode(3)
# t4 = TreeNode(4)
# t5 = TreeNode(5)
# t6 = TreeNode(6)
# t7 = TreeNode(7)
# t1.left = t2
# t1.right = t3
# t2.left = t4
# t2.right = t5
# t3.left = t6
# t3.right = t7
# a.inorderTraversal(t3)