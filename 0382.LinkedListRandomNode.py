"""
382. Linked List Random Node

Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();

随机采样算法 Reservoir Sampling, 论点

假设现在要从 n 个数里面随机选择一个数，那么通过 Reservoir sampling 选择的流程如下:

1. 记最终选择的数为 result
2. 遍历数组，对于数组第 i 个数，以 1/i 的概率将其赋给result（i从1开始，所以第一个数肯定会赋给result）
3. 遍历完数组后得到的 result 即为产生的随机数

假设现在有数组 [1, 2, 3], 随机产生一个数，那么按照上面的流程有

1. 遍历第一个数时，result = 1
2. 遍历第二个数时，result = 2 的概率为 1/2, 即 result = 1 的概率也是 1/2
3. 遍历第三个数时，result = 3 的概率为 1/3, result = 1 的概率为 (1 - 1/3) * 1/2 = 1/3, 同理 result = 2 的概率也是 1/3
"""
import random


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

        
class Solution:
    dummy = ListNode(0)
    
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.dummy.next = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        curr_node = self.dummy.next
        count = result = 0
        while curr_node:
            count += 1
            if random.random() < (1.0 / count):
                result = curr_node.val
                
            curr_node = curr_node.next
        return result


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
