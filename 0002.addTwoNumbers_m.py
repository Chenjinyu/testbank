"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # faster than 10.88%. not efficient.
        # because it speed time to read tow listNodes, and create new list node.
        def getListAsNum(list_node: ListNode):
            n = ""
            while list_node:
                n += str(list_node.val)
                list_node = list_node.next
            return int(n[::-1])

        n_l_1 = getListAsNum(l1)
        n_l_2 = getListAsNum(l2)

        sum_two_str = str(n_l_1 + n_l_2)
        sum_two_str = sum_two_str[::-1]
        head = ListNode(0)
        dump = head
        i = 0
        while i < len(sum_two_str):
            dump.val = sum_two_str[i]
            child_node = ListNode(None)
            if i == len(sum_two_str) - 1:
                dump.next = None
            else:
                dump.next = child_node
            dump = dump.next
            i += 1

        return head

    """
    Amazon OA Problem.
    """
    def addTwoNumbersEfficient(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        the two list, the decimal will set to next value.
        # faster than 79.93%. the percentage is not always correct.
        """
        result = ListNode(None)
        # normal, we call dummy.
        dummy = result
        dicimal_mark = 0

        while l1 or l2 or dicimal_mark:
            # the () must be there. and check if l1 or l2 None, coz, two ListNode has different length
            sum_val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + dicimal_mark
            dicimal_mark, sum_val = divmod(sum_val, 10)

            if dummy.val is None:
                # the condition is used for the first node get the value.
                dummy.val = sum_val
            else:
                # dummy's next should be a node need to be created with the sum_val.
                dummy.next = ListNode(sum_val)
                dummy = dummy.next
               
            #check if l1 or l2 None, coz, two ListNode has different length
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return result


if __name__ == "__main__":
    a = ListNode(2)
    b = ListNode(4)
    c = ListNode(3)

    a.next = b
    b.next = c

    a1 = ListNode(5)
    a2 = ListNode(6)
    a3 = ListNode(4)

    a1.next = a2
    a2.next = a3
    head = Solution().addTwoNumbersEfficient(a, a1)
    print("-----")
    while head:
        print(head.val)
        head = head.next
