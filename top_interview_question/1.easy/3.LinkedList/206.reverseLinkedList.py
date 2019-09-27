"""
Reverse Linked List


Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

Problem Solving: O(L)
1 -> 2 -> 3 -> None   --reverse-->>>  None <- 1 <- 2 <- 3

1. prev_node points to None, and current node points to head.
2. in the while loop:
   1st: Current Node points to None, Prev Node points to Cur node, and Cur node move to head.next.
   --> None <- 1 (prev). cur node is 2
   at this time, current node moves to next node. but does not point to prev.
   2nd: prev node is 1, cur node is 2. let cur node(2) points(cur_node.next = prev_node) to prev. cur node moves to next node.
   -->: None <- 1 <- 2 (prev), curr node is 3
3. at the end of loop. the prev node is 3. so return prev_node.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur_node = head
        prev_node = None
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node

        return prev_node

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    resultNode = Solution().reverseList(a)
    while resultNode:
        print(resultNode.val)
        resultNode = resultNode.next


