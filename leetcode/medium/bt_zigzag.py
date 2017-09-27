""" Binary Tree Zigzag Level Order Traversal - 
    https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

    Given a binary tree, return the zigzag level order traversal of its nodes' 
    values. (ie, from left to right, then right to left for the next level and 
    alternate between).

    For example:
    Given binary tree [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    return its zigzag level order traversal as:
    [
      [3],
      [20,9],
      [15,7]
    ]
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        self.level = {}
        def inorder(root, level):
            if root:
                if level in self.level:
                    self.level[level].append(root.val)
                else:
                    self.level[level] = [root.val]
                inorder(root.left, level + 1)
                inorder(root.right, level + 1)
        inorder(root, 0)
        order = []
        for i in range(max(self.level)+1):
            if i%2 == 0:
                order.append(self.level[i])
            else:
                order.append(self.level[i][::-1])
        return order