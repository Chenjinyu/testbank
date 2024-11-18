# used for LeetCode

from typing import Optional, Union, List, Boolean
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
    def __init__(self):
        self.head = None
        print('__init__ is called')
    
    # @staticmethod
    # def __new__(cls, node_list: List[Optional[Union[int, str]]]) -> None:
    #     print('__new__ is called')
        
    def __iter__(self):
        # self returns the LinkedListNodes itself, but as defalut, class object is not iterable, until overwrite the __iter__()
        node = self.head
        while node:
            yield node
            node = node.next
            
    def is_empty(self) -> bool:
        return self.head == None
            
    def add_to_tail(self, node: Union[ListNode, int]):
        """
        Add an ListNode to the end(push). 
        1. if only has the head attr, then the new node to the end need to loop to the end, and add the new node to the next.
        2. if has head and tail, the LinkedList needs to maintenance the head and tail everytime when the node changes.
        """
        if not isinstance(node, ListNode):
            node = ListNode(node)
            
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
    
    def to_list(self) -> List[int]:
        result = []
        
        # self returns the LinkedListNodes itself, but as defalut, class object is not iterable, until overwrite the __iter__()
        for cur_node in self:
            result.append(cur_node.val)
        return result
    
    def __repr__(self) -> str:
        """
        __repr__ method returns a string representation of the class object. 
        """
        if not self:
            return "[]"
        nodes = []
        for node in self:
            nodes.append(str(node.val))
            
        return("[" + ", ".join(nodes) + "]")
    
    
class LinkedListNodes:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
                    
    def is_empty(self) -> bool:
        return self.head == None
    
    def push(self, new_node:Union[ListNode, int]):
        if not isinstance(new_node, ListNode):
            new_node = ListNode(new_node)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    def pop(self) -> int:
        """Pop value from the LinkedListNode tail """
        if self.is_empty():
            return None
        
        val = self.tail.value
        
        # everytime operates the node, the linkedListNodes needs to maintenance. 
        if self.tail == self.head:
            self.tail = None
            self.head = None
        else:
            cur_node = self.head
            
            while cur_node != self.tail:
                cur_node = cur_node.next
            
            self.tail = cur_node
            self.tail.next = None   # disconect the last one node.
            
        return val            
    
    def to_list(self) -> List[int]:
        result = []
        
        # self returns the LinkedListNodes itself, but as defalut, class object is not iterable, until overwrite the __iter__()
        for cur_node in self:
            result.append(cur_node.val)
        
        return result
    
    
    def __repr__(self) -> str:
        values = self.to_list()
        return 'LinkedList([' + ', '.join(str(value) for value in values) + '])'


def build_linked_list(node_list) -> ListNode:
    if not len(node_list):
        return None
    linked_list = LinkedList()
    for node in node_list:
        linked_list.add_to_tail(ListNode(node))
    return linked_list
            
    # def _print_linked_list(self) -> List:
    #     return self.node_list
            
        
def build_linked_list_node(node_list) -> ListNode:
    if not len(node_list):
        return None
    linked_list_nodes = LinkedListNodes()
    for node in node_list:
        linked_list_nodes.push(ListNode(node))
    return linked_list_nodes
    

test_list = build_linked_list_node([1,2,3])
print(test_list.to_list())    
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
