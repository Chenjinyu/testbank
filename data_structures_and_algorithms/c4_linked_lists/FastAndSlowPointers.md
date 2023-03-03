## Fast and slow pointers 

Fast and slow pointers is an implementation of the two pointers technique that we learned in the arrays and strings chapter. The idea is to have two pointers that don't move side by side. This could mean they move at different "speeds" during iteration, begin iteration from different locations, or any other abstract difference.

When the pointers move at different speeds, usually the "fast" pointer moves two nodes at each iteration, whereas the "slow" pointer moves one node at each iteration (although this is not always the case). Here's some pseudocode:

```python
// head is the head node of a linked list
function fn(head):
    slow = head
    fast = head

    while fast and fast.next:
        Do something here
        slow = slow.next
        fast = fast.next.next
```

>The reason we need the while condition to also check for fast.next is because if fast is at the final node, then fast.next is null, and fast.next.next will result in an error.

Let's look at some examples where fast and slow pointers can come in handy.

```html
Example 1: Given the head of a linked list with an odd number of nodes head, return the value of the node in the middle.

For example, given a linked list that represents 1 -> 2 -> 3 -> 4 -> 5, return 3.
```
As mentioned in the previous article, the easiest way to solve this problem would be to just convert the linked list into an array by iterating over it, and then just returning the number in the middle.

```java
function fn(head):
    array = int[]
    while head:
        array.push(head.val)
        head = head.next

    return array[array.length // 2]
```

This is basically "cheating", and would never pass as an acceptable solution in an interview. You may have realized that the difficulty in this problem comes from the fact that we don't know how long the linked list is. One thing we could do is iterate through the linked list once with a dummy pointer to find the length, then iterate from the head again once we know the length to find the middle.

```python
def get_middle(head):
    length = 0
    dummy = head
    while dummy:
        length += 1
        dummy = dummy.next
    
    for _ in range(length // 2):
        head = head.next
    
    return head.val
```

The most elegant solution comes from using the fast and slow pointer technique. If we have one pointer moving twice as fast as the other, then by the time it reaches the end, the slow pointer will be halfway through since it is moving at half the speed.

```python
def get_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow.val
```
The pointers use O(1) space, and if there are n nodes in the linked list, the time complexity is O(n) for the traversals.

```html
Example 2: 141. Linked List Cycle

Given the head of a linked list, determine if the linked list has a cycle.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
```

If a linked list has a cycle, you can imagine some group of nodes forming a circle, and traversal never ends as it moves around that circle infinitely. One way to try to solve this problem would be to just iterate through the list for an arbitrarily large amount of iterations. If there isn't a cycle, then we will eventually reach the end of the list. If there is a cycle, then we will never reach an end and after a huge amount of iterations, we can conclude that there is probably a cycle.

The problem with this approach is that it isn't an actual general solution. What if there is no cycle, but there just happens to be more nodes than the iteration cutoff? If we increase the iteration cutoff, we can always argue that we could pass in a longer linked list. If we make the cutoff too large, it becomes impractical, and we are hard coding which is a terrible practice.

The better approach is to use a fast and slow pointer. Imagine having two athletes running around a circular racetrack. If they run at different speeds, then the faster runner will eventually pass the slower one. We can apply this same logic here - if the fast and slow pointer ever point to the same node (except at the start), then we know there is a cycle. If there is no cycle, then the slow pointer will never catch up to the fast one before it reaches the end.

>Why will the pointers always meet, and the fast pointer won't "skip" over the slow pointer? After looping around the cycle, if the fast pointer is one position behind, then the pointers will meet on the next iteration. If the fast pointer is two positions behind, then it will be one position behind on the next iteration. This pattern continues - after looping around once, the fast pointer moves exactly one step closer to the slow pointer at each iteration.

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
```
This approach gives us a time complexity of O(n) and a space complexity of O(1), where n is the number of nodes in the linked list. Note that this problem can also be solved using hashing, although it would require O(n) space.


The hashing solution: if you continuously iterate using the next pointer, there are two possibilities:
1. If the linked list doesn't have a cycle, you will eventually reach null and finish.
2. If the linked list has a cycle, you will eventually visit a node twice. We can use a set to detect this.

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
```
This solution is added for the sake of brevity - the first one is better as it uses less space.

```html
Example 3: Given the head of a linked list and an integer k, return the kth node from the end.

For example, given the linked list that represents 1 -> 2 -> 3 -> 4 -> 5 and k = 2, return the node with value 4, as it is the 2nd node from the end.
```

```python
def find_node(head, k):
    slow = head
    fast = head

    for _ in range(k):
        fast = head.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow.val
```

For the same reasons as in the first example, the time complexity of this algorithm O(n) and the space complexity is O(1), where n is the number of nodes in the linked list.

Try solving these upcoming practice problems using the fast and slow pointer technique.