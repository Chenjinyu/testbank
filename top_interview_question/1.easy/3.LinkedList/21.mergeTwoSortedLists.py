"""
Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # stays at the begin for return the whole linked list.
        newNode = ListNode(-1)

        # new_node links to next node, and move to the end of the linked list.
        new_node = newNode

        while l1 and l2:
            if l1.val <= l2.val:
                new_node.next = l1
                l1 = l1.next
            else:
                new_node.next = l2
                l2 = l2.next
            new_node = new_node.next

        # either l1 or l2, after the WHILE loop, might one of them points to None.
        new_node.next = l1 if l1 is not None else l2
        return newNode.next

    def mergeTwoListRecur(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val <= l2.val:
            l1.next = self.mergeTwoListRecur(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoListRecur(l1, l2.next)
            return l2


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(3)
    c = ListNode(4)
    d = ListNode(5)
    e = ListNode(8)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    a1 = ListNode(2)
    b1 = ListNode(4)
    c1 = ListNode(7)
    d1 = ListNode(8)
    e1 = ListNode(9)
    f1 = ListNode(21)
    a1.next = b1
    b1.next = c1
    c1.next = d1
    d1.next = e1
    e1.next = f1

    resultNode = Solution().mergeTwoListRecur(a, a1)
    while resultNode:
        print(resultNode.val)
        resultNode = resultNode.next