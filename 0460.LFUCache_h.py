"""
460. LFU Cache
Design and implement a data structure for Least Frequently Used (LFU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity,
it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem,
when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Note that the number of times an item is used is the number of calls to the get and put functions for that item
since it was inserted. This number is set to zero when the item is removed.


Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""
import heapq

class LFUCache:
    """
    Amazon OA Problem
    Apple OA Problem
    Microsoft OA Problem
    Google OA Problem
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_dict = {}
        self.cache_list = []

    def get(self, key: int) -> int:
        cache = self.cache_dict.get(key, None)
        if not cache:
            return -1

        for item in self.cache_list:
            if item[1] == key:
                item[0] += 1
                break

        heapq.heapify(self.cache_list)
        return cache

    def put(self, key: int, value: int) -> None:
        cache = self.cache_dict.get(key, None)

        if not cache:
            heapq.heappush(self.cache_list, [0, key])
            self.cache_dict[key] = value

            if len(self.cache_dict) > self.capacity:
                freq, key = heapq.heappop(self.cache_list)
                del self.cache_dict[key]
        else:
            self.cache_dict[key] = value
            for item in self.cache_list:
                if item[1] == key:
                    item[0] += 1
                    break
            heapq.heapify(self.cache_list)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    """
    ["LFUCache","put","put","get","put","get","get","put","get","get","get"]
    [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
    """
    l = LFUCache(2)
    l.put(1, 1)
    l.put(2, 2)
    l.get(1)
    l.put(3, 3)
    l.get(2)
    l.get(3)
    l.put(4, 4)
    l.get(1)
    l.get(3)
    l.get(4)