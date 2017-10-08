""" Remove Nth Node From End of List
    https://leetcode.com/problems/remove-nth-node-from-end-of-list/

    Given a linked list, remove the nth node from the end of list and return its head.

    For example,

       Given linked list: 1->2->3->4->5, and n = 2.

       After removing the second node from the end, the linked list becomes 1->2->3->5.
    Note:
    Given n will always be valid.
    Try to do this in one pass.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None: return None
        p = head
        cur = head
        for i in range(n):
            p = p.next
        while p and p.next is not None:
            p = p.next
            cur = cur.next
        if p:
            cur.next = cur.next.next
        else:
            head = head.next

        return head

    def print_list(self, head):
        cur = head
        while cur is not None:
            print(cur.val, end=" ")
            cur = cur.next
        print()


a = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
# l3.next = l4
# l4.next = l5
# a.print_list(l1)
a.print_list(a.removeNthFromEnd(l1, 3))