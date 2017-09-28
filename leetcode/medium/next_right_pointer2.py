""" Populating Next Right Pointers in Each Node II - 
    https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

    Follow up for problem "Populating Next Right Pointers in Each Node".

    What if the given tree could be any binary tree? Would your previous 
    solution still work?

    Note:
    You may only use constant extra space.
    
    For example,

    Given the following binary tree,
             1
           /  \
          2    3
         / \    \
        4   5    7

    After calling your function, the tree should look like:
             1 -> NULL
           /  \
          2 -> 3 -> NULL
         / \    \
        4-> 5 -> 7 -> NULL
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
        tail = dummy = TreeLinkNode(0)

        while root:
            tail.next = root.left
            if tail.next:
                tail = tail.next
            tail.next = root.right
            if tail.next:
                tail = tail.next
            root = root.next
            if not root:
                tail = dummy
                root = dummy.next


    def print_next_pointers(self, root):
        if root:
            print(root.val)
            self.print_next_pointers(root.next)

    def print_three_pointers(self, root):
        if root.left: print("left:", root.left.val)
        if root.right: print("right:", root.right.val)
        if root.next: print("next:", root.next.val)


# a = Solution()
# t1 = TreeLinkNode(1)
# t2 = TreeLinkNode(2)
# t3 = TreeLinkNode(3)
# t4 = TreeLinkNode(4)
# t5 = TreeLinkNode(5)
# t6 = TreeLinkNode(6)
# t7 = TreeLinkNode(7)
# t8 = TreeLinkNode(8)

# t1.left = t2
# t1.right = t3
# t2.left = t4
# t2.right = t5
# t3.right = t6
# t4.left = t7
# t7.left = t8

# a.connect(t1)