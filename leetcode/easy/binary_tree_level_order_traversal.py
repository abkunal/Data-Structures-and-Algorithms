""" Binary Tree Level Order Traversal II - 
    https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

    Given a binary tree, return the bottom-up level order traversal of its 
    nodes' values. (ie, from left to right, level by level from leaf to root).

    For example:
    Given binary tree [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    return its bottom-up level order traversal as:
    [
      [15,7],
      [9,20],
      [3]
    ]
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # inorder traversal of a binary tree
        def inorder(root, path, level):
            if root:
                inorder(root.left, path, level + 1)
                path.append((level, root.val))
                inorder(root.right, path, level + 1)

        # getting nodes of tree along with their
        path = []
        inorder(root, path, 1)

        # if tree is not empty, return an array of arrays of nodes by their 
        # level order
        if path:
            maxi = max(path)
            levels = [[] for i in range(maxi[0])]
            for node in path:
                levels[node[0]-1].append(node[1])
            return levels[::-1]
        else:
            return []


a = Solution()
t1 = TreeNode(3);
t2 = TreeNode(9);
t3 = TreeNode(20);
t4 = TreeNode(15);
t5 = TreeNode(7);

t1.left = t2;
t1.right = t3;
t3.left = t4;
t3.right = t5

print(a.levelOrderBottom(t1))