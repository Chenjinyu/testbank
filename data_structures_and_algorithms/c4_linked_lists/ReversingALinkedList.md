## Reversing a linked list

While reversing a linked list is a common interview problem in itself, it is also a technique that can be a step in solving different problems. Elegantly performing the reversal requires a good understanding of how to move pointers around, which we will aim to achieve in this article.

Imagine that we have a linked list **1 -> 2 -> 3 -> 4**, and we want to return **4 -> 3 -> 2 -> 1**. Let's say we keep a pointer curr that represents the current node we are at. Starting with **curr** at the **1**, we need to get the **2** to point to **curr**. The problem is, once we iterate (**curr = curr.next**) to get to the 2, we no longer have a pointer to the 1 because it is a singly linked list. To get around this, we can use another pointer **prev** that tracks the previous node.

At any given node curr, we can set **curr.next = prev** to switch the direction of the arrow. Then, we can update prev to be curr in preparation for the next node. However, if we change **curr.next**, how can we get to the next node? We can use a temporary variable **nextNode** to point to the next node before changing any of the other pointers.

```python
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next # first, make sure we don't lose the next node
        curr.next = prev      # reverse the direction of the pointer
        prev = curr           # set the current node to prev for the next node
        curr = next_node      # move on
        
    return prev
```

The time complexity of this algorithm is O(n) where n is the number of nodes in the linked list. The while loop runs n times, and the work done at each iteration is O(1). The space complexity is O(1) as we are only using a few pointers.

This exercise is a great one to practice operations on a linked list because it demonstrates the thought process needed. Solutions to linked list problems are usually simple and elegant - to get to them, think about what you need, and solve the problem one step at a time. In this example, we had the following thought process:

1. When we are at a node curr, we need to set its next pointer to the node we were at previously.
    - Use a prev pointer to track the previous node.
2. The prev pointer needs to also update every iteration.
    - Set prev = curr, but only after changing curr.next.
3. If we set curr.next = prev, then we lose the reference to curr.next.
    - Use nextNode to keep a reference to curr.next.

Let's look at another example.
```html
Example: 24. Swap Nodes in Pairs

Given the head of a linked list, swap every pair of nodes. For example, given a linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6, return a linked list 2 -> 1 -> 4 -> 3 -> 6 -> 5.
```