"""
109. Convert Sorted List to Binary Search Tree


leetcode: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/solution/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        """
        Time Complexity: O(NlogN).
        Suppose our linked list consists of N elements. For every list we pass to our recursive function,
        we have to calculate the middle element for that list.
        For a list of size N, it takes N / 2 steps to find the middle element i.e. O(N) to find the mid.
        We do this for every half of the original linked list. From the looks of it, this seems to be an O(N^2) algorithm.
        However, on closer analysis, it turns out to be a bit more efficient than O(N^2).

        Space Complexity: O(logN).
        Since we are resorting to recursion, there is always the added space complexity of the recursion stack that comes into picture.
        This could have been O(N) for a skewed tree, but the question clearly states that we need to maintain the height balanced property.
        This ensures the height of the tree to be bounded by O(logN). Hence, the space complexity is O(logN).
        :param head:
        :return:
        """
        if not head:
            return None

        # after the findTheMidVal was called, the nodes of head list
        # splits into two parts. so that's why `node.left = self.sortedListToBST(head)`
        # only get the first-half of listNode
        mid = self.findTheMidVal(head)

        node = TreeNode(mid.val)

        # the head only has one node
        if head == mid:
            return node

        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)

        return node

    def findTheMidVal(self, head: ListNode) -> ListNode:
        """
        basic on the question, the BST, the left side of nodes must be <= root
        and right side of nodes must be >= root
        the ListNode is ascending ordered, so as long as find the mid node,
        that would be the tree top root.

        certainly, we could get the mid one when get the length and re-loop to the mid node,
        but it's not necessary.
        there uses an algorithm, is use two pointers called: one_step_ptr and two_step_ptr.
        because, when the two_step_ptr reach the end of the ListNode, the one_step_ptr is in the mid.
        one_step_ptr is what we want the tree root.
        :param head:
        :return:
        """
        prev_ptr = None
        one_step_ptr = head
        two_step_ptr = head

        while two_step_ptr and two_step_ptr.next:
            prev_ptr = one_step_ptr
            one_step_ptr = one_step_ptr.next
            two_step_ptr = two_step_ptr.next.next

        # when find the mid, the prev_ptr should be re-assigned to None.
        # so the head ListNode has split into two parts,
        # first-half one is the head to prev_ptr node.
        # second-half one is the mid to the end.
        if prev_ptr:
            prev_ptr.next = None

        return one_step_ptr
