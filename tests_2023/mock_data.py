from typing import Optional, List
from LC_2023.model import ListNode
  
        
def render_test_nodes(node_list: List[int]) -> ListNode:
    head = tail = ListNode(node_list[0])
    for node in node_list[1:]:
        tail.next = ListNode(node)
        tail = tail.next
    return head


def list_test_nodes(head: Optional[ListNode]):
    while head:
        print(f"node val: {head.val}, node.next: {head.next if head.next else 'None'}")
        print(head.val)
        head = head.next


def node_traversal(head: ListNode) -> List:
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
        
    return lst
        

# node_list = [1,2,3,4,5]
# test_head = render_test_nodes(node_list)
# print(list_test_nodes(test_head))
