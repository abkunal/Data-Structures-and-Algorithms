""" Convert BST to Greater Tree - https://leetcode.com/problems/convert-bst-to-greater-tree

    Given a Binary Search Tree (BST), convert it to a Greater Tree such that
    every key of the original BST is changed to the original key plus sum of 
    all keys greater than the original key in BST.

    Example:

    Input: The root of a Binary Search Tree like this:
                  5
                /   \
               2     13

    Output: The root of a Greater Tree like this:
                 18
                /   \
              20     13
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return("Value: " + str(self.val)) 

    def __str__(self):
        return("Value: " + str(self.val))


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sofar = 0

        def inorder(root):
            if root:
                inorder(root.right)
                root.val += self.sofar
                self.sofar = root.val
                inorder(root.left)

        inorder(root)
        

# a = Solution()
# t1 = TreeNode(5)
# t2 = TreeNode(2)
# t3 = TreeNode(13)

# t1.left = t2
# t1.right = t3

# print(a.convertBST(t1))