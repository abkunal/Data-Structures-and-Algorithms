""" Populating Next Right Pointers in Each Node - 
    https://leetcode.com/problems/populating-next-right-pointers-in-each-node

    Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }

    Populate each next pointer to point to its next right node. If there is no 
    next right node, the next pointer should be set to NULL.

    Initially, all next pointers are set to NULL.

    Note:

    You may only use constant extra space.
    
    You may assume that it is a perfect binary tree (ie, all leaves are at the 
    same level, and every parent has two children).
    
    For example,
    Given the following perfect binary tree,
             1
           /  \
          2    3
         / \  / \
        4  5  6  7
    
    After calling your function, the tree should look like:
             1 -> NULL
           /  \
          2 -> 3 -> NULL
         / \  / \
        4->5->6->7 -> NULL
"""

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        def point_next(root, right):
            if root:
                root.next = right
                point_next(root.left, root.right)

                if right is not None:
                    point_next(root.right, right.left)
                else:
                    point_next(root.right, right)
        point_next(root, None)

    def print_next_pointers(self, root):
        if root:
            print(root.val)
            self.print_next_pointers(root.next)


# a = Solution()
# t1 = TreeLinkNode(1)
# t2 = TreeLinkNode(2)
# t3 = TreeLinkNode(3)
# t4 = TreeLinkNode(4)
# t5 = TreeLinkNode(5)
# t6 = TreeLinkNode(6)
# t7 = TreeLinkNode(7)

# t1.left = t2
# t1.right = t3
# t2.left = t4
# t2.right = t5
# t3.left = t6
# t3.right = t7

# a.connect(t1)