"""
Convert Sorted Array to Binary Search Tree
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        length = len(nums)
        if length == 0:
            return None

        mid_pos = length // 2
        node = TreeNode(nums[mid_pos])
        # when only one node left.
        if mid_pos == 0:
            return node

        node.left = self.sortedArrayToBST(nums[:mid_pos])
        node.right = self.sortedArrayToBST(nums[mid_pos + 1:])

        return node


if __name__ == "__main__":
    nums = [-10,-3,0,5,9]
    print(Solution().sortedArrayToBST(nums))
