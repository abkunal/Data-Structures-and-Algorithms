""" Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree

    Given a binary tree, determine if it is a valid binary search tree (BST).

    Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
    Example 1:
        2
       / \
      1   3
    Binary tree [2,1,3], return true.
    Example 2:
        1
       / \
      2   3
    Binary tree [1,2,3], return false.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.order = []
        def inorder(root):
            if root:
                inorder(root.left)
                self.order.append(root.val)
                inorder(root.right)
        inorder(root)
        print(self.order)
        return self.order == sorted(self.order) and len(self.order) == len(set(self.order))

    def isValidBST2(self, root):
        """ Another Method """
        def inorder(root, lr, rr):
            if root:
                x = inorder(root.left, lr, root.val) and inorder(root.right, root.val, rr)
                print(root.val, lr, rr)
                if lr is not None and rr is not None:
                    return lr < root.val < rr and x
                elif lr is not None:
                    return lr < root.val and x
                elif rr is not None:
                    return root.val < rr and x
                else:
                    return x
            return True
        return inorder(root, None, None)