# used for LeetCode

from typing import Optional, Union, List
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next
        
    def set_next(self, node):
        self.next = node
    
    def __repr__(self):
        return str(self.val)
        

class LinkedList:
    # Union[int, str, None] == Optional[Union[int, str]]
    def __init__(self) -> None:
        self.head = None
        print('__init__ is called')
    
    # @staticmethod
    # def __new__(cls, node_list: List[Optional[Union[int, str]]]) -> None:
    #     print('__new__ is called')
        
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            
    def add_to_tail(self, node: ListNode):
        if self.head == None:
            self.head = node
            return
        for curr_node in self:
            pass
            
        curr_node.set_next(node)
        
    def remove_from_head(self) -> ListNode:
        if self.head == None:
            return None
        
        temp = self.head
        self.head = self.head.next # move to the next node, the first node will be isolated.
        return temp
    
    
    def __repr__(self) -> str:
        if not self:
            return "[]"
        nodes = []
        for node in self:
            nodes.append(str(node.val))
            
        return("[" + ", ".join(nodes) + "]")
    
    
def build_linked_list(node_list) -> ListNode:
    if not len(node_list):
        return None
    linked_list = LinkedList()
    for node in node_list:
        linked_list.add_to_tail(ListNode(node))
    return linked_list
            
    # def _print_linked_list(self) -> List:
    #     return self.node_list
            
        

# print('________bases________')            
# print(dir(LinkedList.__bases__))
# print('________getatrribute________')
# print(dir(LinkedList.__getattribute__))
# print('________dir________')
# print(dir(LinkedList.__dir__))
# test_list = build_linked_list([1,2,3])
# print(test_list)
# dir(test_list)
# using the __ddd__ to get the linkedlist instead of a funciton.
