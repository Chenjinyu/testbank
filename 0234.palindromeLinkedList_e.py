"""
Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        length = 0
        stay_head = head
        while head:
            length += 1
            head = head.next

        if length == 0:
            return True
        if length == 1:
            return True

        mid_pos = length // 2
        is_even = length % 2 == 0
        first_half_node_val_list = []
        second_half_node_val_list = []
        cur_node = stay_head
        nxt_node = None
        while length > 0:
            if is_even and mid_pos >= length:
                nxt_node = cur_node
                break
            if not is_even and mid_pos + 1 >= length:
                nxt_node = cur_node.next
                break

            length -= 1
            first_half_node_val_list.append(cur_node.val)
            cur_node = cur_node.next

        while mid_pos > 0:
            mid_pos -= 1
            second_half_node_val_list.append(nxt_node.val)
            nxt_node = nxt_node.next
        if first_half_node_val_list[::-1] == second_half_node_val_list:
            return True
        return False

    def isPalindromeImprove(self, head: ListNode) -> bool:
        if not head:
            return True
        if head.next is None:
            return True

        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next

        mid_len = len(val_list) // 2
        is_even = len(val_list) % 2 == 0
        first_half_list = val_list[: mid_len][::-1]
        second_half_list = val_list[mid_len if is_even else mid_len + 1:]
        return first_half_list == second_half_list



if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(0)
    c = ListNode(1)
    # d = ListNode(1)

    a.next = b
    b.next = c
    # c.next = d
    # d.next = e
    print(Solution().isPalindromeImprove(a))
