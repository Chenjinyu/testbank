class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:

    def reverse_list_node(self, head: ListNode):
        prev = None
        curr = head
        # allow curr as the while condition.
        while curr:
            # next will be None, if curr.next is None
            next = curr.next
            curr.next = prev
            # prev will be the last one node when curr is None.
            prev = curr
            curr = next
            # curr.next, prev, curr = prev, curr, next

        return prev

    def reverse_sublist(self, L: ListNode, start, finish):
        dummy_head = sublist_head = L
        for _ in range(1, start):
            sublist_head = sublist_head.next
            print('sublist_head value: {}'.format(sublist_head.value))

        sublist_iter = sublist_head.next
        print('sublist_iter value: {}'.format(sublist_iter.value))
        for _ in range(finish - start):
            temp = sublist_iter.next
            print("sublist_iter value in for loop: {}".format(sublist_iter.value))
            # let sublist_iter.next link to linked node right step by step.
            # the sublist_iter will move to the right-most.
            sublist_iter.next = temp.next
            # temp is the right-most node, and link to the sublist_head.next
            temp.next = sublist_head.next
            # so that sublist_head.next can link the temp.
            sublist_head.next = temp
        return dummy_head


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
g = ListNode(7)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

result = Solution().reverse_list_node(a)
while result:
    print(result.value)
    result = result.next
