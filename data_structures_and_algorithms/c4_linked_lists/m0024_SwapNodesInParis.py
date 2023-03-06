"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]
"""
from typing import Optional
from list_node import ListNode, LinkedList, build_linked_list
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        FUCK, I STILL CANNOT UNDERSTAND.
        To summarize the steps:
            1. Performs an edge swap from A -> B -> C to A <-> B C.
            2. Make sure we can still access the rest of the list beyond the current pair
            3. Now that A <-> B is isolated from the rest of the list, save a pointer to A to connect it with the rest of the list later.
            4. Connect the previous pair to the rest of the list. In this case connecting A -> D.
            5. Use a dummy pointer to keep a reference to what we want to return.
            6. Avoid cycles by handling the case when there's an odd number of nodes.
        """
        # check edge care: linked list has 0 or 1 node, just return
        if not head or not head.next:
            return head
        dummy = head.next # Step 5. cause after the swap, the next should move to the first
        prev_node = None # Initialize for step 3
        while head and head.next:
            if prev_node:
                # making connection
                prev_node.next = head.next # Step 4. Connect the previous pair to the rest of the list. In this case connecting A -> D.
            prev_node = head # Step 3
                
            next_node = head.next.next # Step 2
            head.next.next = head # Step 1
            
            head.next = next_node # Step 6
            head = next_node # Move onto the next pair
            
        return dummy
        
        
    def swapPairs2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Much easier to understand. 
        """
        # check edge care: linked list has 0 or 1 node, just return
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        prev = dummy
        curr = head
        while curr and curr.next:
            third = curr.next.next
            second = curr.next
            second.next = curr
            curr.next = third
            prev.next = second # makes link back to previous node. eg. 0 -> 2
            prev = curr # moves to the next swap
            curr = third # moves to the next swap
            
        return dummy.next

head = ListNode(1)
node2 = ListNode(2)
head.next = node2
node3 = ListNode(3)
node2.next = node3
node4 = ListNode(4)
node3.next = node4
# head.set_next(ListNode(2).set_next(ListNode(3).set_next(ListNode(4))))
    # head.set_next(ListNode(i))
ans = Solution().swapPairs(head)
# while ans and ans.next:
#     print(ans.val)
#     ans = ans.next

