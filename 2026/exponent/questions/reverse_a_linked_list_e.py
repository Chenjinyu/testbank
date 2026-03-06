class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: ListNode) -> ListNode:
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


# debug your code below
head = ListNode(1, ListNode(2))
reversed_head = reverse_list(head)
print(reversed_head.val)
print(reversed_head.next.val)