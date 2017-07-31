""" Symmetric Tree - https://leetcode.com/problems/symmetric-tree

    Given a binary tree, check whether it is a mirror of itself 
    (ie, symmetric around its center).

    For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

        1
       / \
      2   2
     / \ / \
    3  4 4  3
    But the following [1,2,2,null,3,null,3] is not:
    
        1
       / \
      2   2
       \   \
       3    3

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def inorder(root, path, direc, string):
          if root:
            inorder(root.left, path, direc, "left")
            path.append(root.val)
            direc.append(string)
            inorder(root.right, path, dirc, "right")

        # find the inorder traversal of the tree along with the position of
        # the nodes
        path = []
        direc = []
        inorder(root, path, direc, "middle")

        # replace "left" with "right" and vice-versa
        # and compare with the original direction
        rev = []
        for d in direc:
          if d == "left":
            rev.append("right")
          elif d == "right":
            rev.append("left")
          else:
            rev.append(d)

        # if directions are same, the trees is symmetric
        return path == path[::-1] and direc == rev        