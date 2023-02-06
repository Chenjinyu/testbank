"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

"""
from typing import Optional
import math

from LC_2023.model import ListNode
# Definition for singly-linked list.

        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def _get_node_len(head: ListNode):
            dump = head
            count = 0
            while dump:
                count += 1
                dump = dump.next
            return count
        node_len = _get_node_len(head)
        mid_len = math.floor(node_len / 2) + 1
        print(mid_len)
        steps = 1
        while steps < mid_len:
            print(head.val)
            head = head.next
            steps += 1
                
        return head
    
    
    def middleNode2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp and temp.next:
            head = head.next
            temp = temp.next.next
            
        return head
        
        
                
                
print(math.ceil(5/2) - 1)