"""

    Given a binary tree, return the level order traversal of its nodes' values. 
    (ie, from left to right, level by level).

    For example:
    Given binary tree [3,9,20,null,null,15,7],
      3
     / \
    9  20
      /  \
     15   7
    return its level order traversal as:
    [
    [3],
    [9,20],
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
    def levelOrder(self, root):
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
        l = [self.level[key] for key in range(max(self.level)+1)]
        return l