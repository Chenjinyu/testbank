"""
146. LRU Cache
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

from collections import OrderedDict

"""
Amazon OA Problem
Microsoft OA Problem
Facebook OA Problem
Apple OA Problem
Oracle OA Problem
Google OA Problem
VMware OA Problem
Uber OA Problem
Expeida OA Problem
Sanpchat OA Problem
"""


class LRUCache(OrderedDict):
    """
    Time Complexity: O(1)
    Space Complexity: O(N)
    """

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)


class DoubleLinkedNode:
    def __init__(self, key=0, value=0, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:
    """
    Time Complexity: O(1)
    Space Complexity: O(N)
    """
    def __init__(self, capacity):
        self.capacity = capacity
        # cache store the key: node object
        self.cache = {}
        self.size = 0
        # define the head and tail, the new node will be added into between the head and tail
        self.head = DoubleLinkedNode()
        self.tail = DoubleLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        # head.next.prev = node must be the first to assign
        # obviously, otherwise, the head.next already be node.
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        prev = self.tail.prev
        self._remove_node(prev)
        return prev

    def get(self, key):
        node = self.cache.get(key, None)
        if not node:
            return -1

        self._move_to_head(node)
        return node.value

    def put(self, key, value):
        node = self.cache.get(key, None)

        if not node:
            newNode = DoubleLinkedNode(key, value)

            self.cache[key] = newNode

            self._add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1

        else:
            # update the value
            node.value = value
            self._move_to_head(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)