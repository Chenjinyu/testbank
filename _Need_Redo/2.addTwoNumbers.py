"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

the path: High_Frequency/2.Medium/2.addTwoNumbers.py

idea: in one while: check the sum and the decimal which will be added into the next list node.
      sum_val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + decimal_mark
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pass


if __name__ == "__main__":
    a = ListNode(2)
    b = ListNode(4)
    c = ListNode(3)

    a.next = b
    b.next = c

    a1 = ListNode(5)
    a2 = ListNode(6)
    a3 = ListNode(4)

    a1.next = a2
    a2.next = a3
    head = Solution().addTwoNumbers(a, a1)
    while head:
        print(head.val)
        head = head.next