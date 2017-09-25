""" Partition List - https://leetcode.com/problems/partition-list

    Given a linked list and a value x, partition it such that all nodes less 
    than x come before nodes greater than or equal to x.

    You should preserve the original relative order of the nodes in each of the 
    two partitions.

    For example:
    
    Given 1->4->3->2->5->2 and x = 3,
    return 1->2->2->4->3->5.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        temp = head
        prev_temp = head

        while temp is not None and temp.val >= x:
            prev_temp = temp
            temp = temp.next

        if temp is None:
            return head
        elif temp != prev_temp:
            prev_temp.next = temp.next
            temp.next = head
            head = temp

        prev = prev_temp
        mini = head
        trav = prev_temp.next

        while trav is not None:
            if trav.val < x:
                if trav == mini.next:
                    prev = trav
                    trav = trav.next
                    mini = mini.next
                else:
                    prev.next = trav.next
                    trav.next = mini.next
                    mini.next = trav
                    mini = trav
                    trav = prev.next
            else:
                prev = trav
                trav = trav.next
        return head

    def print_list(self, head):
        node = head
        while node is not None:
            print(node.val, end=' ')
            node = node.next
        print()


a = Solution()

def construct_list(array):
    start = ListNode(array[0])
    cur = start
    for i in range(1, len(array)):
        node = ListNode(array[i])
        cur.next = node
        cur = node
    return start

# l = construct_list([7,6,5,4,3,2,1])
# a.print_list(l)
# a.print_list(a.partition(l, 2))