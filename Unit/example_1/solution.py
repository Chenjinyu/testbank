from .list_node import ListNode


class Solution:
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        merged = cursor = ListNode() if l1 or l2 else None

        while l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1

            cursor.val = l1.val
            cursor.nxt = ListNode()
            cursor = cursor.nxt
            l1 = l1.nxt

        if nxt := l1 or l2:
            cursor.val = nxt.val
            cursor.nxt = nxt.nxt

        return merged