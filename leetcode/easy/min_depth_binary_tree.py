""" Minimum Depth of Binary Tree - 
    https://leetcode.com/problems/minimum-depth-of-binary-tree/

    Given a binary tree, find its minimum depth.

    The minimum depth is the number of nodes along the shortest path from 
    the root node down to the nearest leaf node.

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            if root.left is not None and root.right is not None:
                return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
            elif root.left is None and root.right is not None:
                return 1 + self.minDepth(root.right)
            elif root.left is not None and root.right is None:
                return 1 + self.minDepth(root.left)
            else:
                return 1
        return 0
            

a = Solution()
t1 = TreeNode(3);
t2 = TreeNode(9);
t3 = TreeNode(20);
t4 = TreeNode(15);
t5 = TreeNode(7);

t1.left = t2;
t1.right = t3;
t2.left = t4;
t3.right = t5

x1 = TreeNode(1)
x2 = TreeNode(2)
x1.left = x2

#print(a.minDepth(t1))
#print(a.minDepth(x1))