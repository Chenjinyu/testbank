"""
LC 110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
Example 1:
Given the following tree [3,9,20,null,null,15,7]:
   3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:
Given the following tree [1,2,2,3,3,null,null,4,4]:
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4

Return false.

"""
from collections import namedtuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        balancedStatusWithHeight = namedtuple(
            'balancedStatusWithHeight', ('balanced', 'height'))

        def check_balanced(root):
            if not root:
                return balancedStatusWithHeight(True, -1)

            left_result = check_balanced(root.left)
            if not left_result.balanced:
                return balancedStatusWithHeight(False, 0)

            right_result = check_balanced(root.right)
            if not right_result.balanced:
                return balancedStatusWithHeight(False, 0)

            is_balanced = abs(left_result.height - right_result.height) <= 1
            height = max(left_result.height, right_result.height) + 1

            return balancedStatusWithHeight(is_balanced, height)

        return check_balanced(root).balanced

