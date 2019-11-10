"""
Linked List Cycle

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

 ---        ---        ---         ---
| 3 |  --> | 2 |  --> | 0 |  -->  | 4 |  --
 ---        ---        ---         ---     |
            ^                              |
            |______________________________|


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

 ---        ---
| 1 |  --> | 2 |  --
 ---        ---    |
  ^                |
  |________________|

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

 ---
| 1 |
 ---

Follow up:

Can you solve it using O(1) (i.e. constant) memory?

"""

from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        walked_node_ip_list = []
        while head:
            if id(head) in walked_node_ip_list:
                return True
            walked_node_ip_list.append(id(head))
            head = head.next
        return False

if __name__ == "__main__":
    a = ListNode(3)
    b = ListNode(2)
    c = ListNode(0)
    d = ListNode(4)

    a.next = b
    b.next = c
    c.next = d
    d.next = b
    print(Solution().hasCycle(a))
