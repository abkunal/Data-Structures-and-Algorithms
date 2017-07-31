""" Same Tree - https://leetcode.com/problems/same-tree
    
    Given two binary trees, write a function to check if they are equal or not.
    
    Two binary trees are considered equal if they are structurally identical 
    and the nodes have the same value.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def inorder(root, path, string):
          if root:
            inorder(root.left, path, "left")
            path.append((root.val, string))
            inorder(root.right, path, "right")

        # calculate inorder traversal of both of the given trees with their
        # node position values and compare them
        path1 = []
        inorder(p, path1, "val")
        path2 = []
        inorder(q, path2, "val")
        
        return path1==path2


a = Solution()
t = TreeNode(10)
r = TreeNode(10)
t.right = r

x = TreeNode(10)
y = TreeNode(10)
x.left = y

print(a.isSameTree(t, x))