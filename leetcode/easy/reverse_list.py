""" Reverse Linked List - https://leetcode.com/problems/reverse-linked-list
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
    
        cur = head
        new_head = ListNode(cur.val)
        cur = cur.next
        while cur is not None:
            node = ListNode(cur.val)
            node.next = new_head
            new_head = node
            cur = cur.next
        return new_head

# a = Solution()
# l1 = ListNode(10)
# l2 = ListNode(20)

# l1.next = l2

# b = a.reverseList(l1)