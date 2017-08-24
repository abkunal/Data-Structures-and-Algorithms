""" Two Sum IV - Input is a BST - 
    https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

    Given a Binary Search Tree and a target number, return true if there exist 
    two elements in the BST such that their sum is equal to the given target.

    Example 1:
    Input: 
        5
       / \
      3   6
     / \   \
    2   4   7

    Target = 9

    Output: True
    
    Example 2:
    Input: 
        5
       / \
      3   6
     / \   \
    2   4   7

    Target = 28

    Output: False
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def preorder(root, path):
            if root:
                path[root.val] = path.get(root.val, 0) + 1
                preorder(root.left, path)
                preorder(root.right, path)
        
        path = {}
        preorder(root, path)

        for i in path:
            if (k - i) == i:
                if path[i] > 1:
                    return True
            elif (k-i) in path:
                return True
        return False