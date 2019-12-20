"""
Remove Nth Node From End of List


Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

Solution: find in Solution.md


"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # for some corner cases like the ListNode only has one node.
        # dummy for return a Null ListNode.
        # however, we need return the ListNode, even its a NULL.
        dummy = ListNode(0)
        # add dummy Node before head, as the first one Node in the linked list.
        dummy.next = head

        # line 43 to 53, calculate the list length to the position of n.
        # eventually get n - 1 Node,
        length = 0
        first = head
        while first:
            length += 1
            first = first.next

        length -= n
        first = dummy
        while length > 0:
            length -= 1
            first = first.next

        # find the n - 1 node, and link to next of n node.
        first.next = first.next.next
        # return the whole ListNode, except dummy.
        return dummy.next

