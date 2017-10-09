""" Binary Tree Right Side View - 
    https://leetcode.com/problems/binary-tree-right-side-view/

    Given a binary tree, imagine yourself standing on the right side of it, 
    return the values of the nodes you can see ordered from top to bottom.

    For example:
    Given the following binary tree,
       1            <---
     /   \
    2     3         <---
     \     \
      5     4       <---
    You should return [1, 3, 4].
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.nodes = {}
        def right(root, level):
            if root:
                right(root.right, level + 1)
                if level not in self.nodes:
                    self.nodes[level] = root.val
                right(root.left, level + 1)
        right(root, 0)
        nodes = []
        for i in range(max(self.nodes)+1):
            nodes.append(self.nodes[i])
        return nodes



# a = Solution()
# t1 = TreeNode(1)
# t2 = TreeNode(2)
# t3 = TreeNode(3)
# t4 = TreeNode(4)
# t5 = TreeNode(5)
# t1.right = t3
# t1.left = t2
# t2.right = t5
# # t3.right = t4
# a.rightSideView(t1)