""" Invert Binary Tree - https://leetcode.com/problems/invert-binary-tree/ 

    Invert a binary tree.

         4
       /   \
      2     7
     / \   / \
    1   3 6   9
    to
         4
       /   \
      7     2
     / \   / \
    9   6 3   1
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def find_internal_nodes(node, internals):
            if node:
                if node.left is None and node.right is None:
                    return
                internals.append(node)
                find_internal_nodes(node.left, internals)
                find_internal_nodes(node.right, internals)

        internals = []
        find_internal_nodes(root, internals)

        for n in range(len(internals) - 1, -1, -1):
            internals[n].left, internals[n].right = internals[n].right, internals[n].left
        return root

# a = Solution()

# n1 = TreeNode(4)
# n2 = TreeNode(2)
# n3 = TreeNode(7)
# n4 = TreeNode(1)
# n5 = TreeNode(3)
# n6 = TreeNode(6)
# n7 = TreeNode(9)

# n1.left = n2
# n1.right = n3
# n2.left = n4
# n2.right = n5
# n3.left = n6
# n3.right = n7

# r = a.invertTree(n1)