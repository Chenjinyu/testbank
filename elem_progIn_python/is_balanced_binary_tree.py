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
            'BalancedStatusWithHeight', 'balanced height')

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


    def isBalanced2(self, root):
        """
        Example 2:
        Given the following tree [1,2,2,3,3,null,null,4,4]:
               1
              / \
             2   2
            / \
           3   3
          / \
         4   4
        """
        is_balance, _ = self.dfs(root)
        return is_balance

    def dfs(self, node):
        # No.1. when node is left-4, it returns True, 1. and is the same with right-4
        # No.2. when node is left-3, it return True, 2. but the right-3 return True, 1. is still is a balance subtree
        if not node:
            # No.1. the 4.left is None, so return True, 0
            # No.1. the 4.right is None, so return True, 0
            return True, 0
        left_is_balance, left_height = self.dfs(node.left)
        right_is_balance, right_height = self.dfs(node.right)
        is_balance = True
        if left_is_balance is False or right_is_balance is False or abs(left_height - right_height) > 1:
            is_balance = False

        # No.1. when the node is 4, the left_height and right_height equal 0.
        # because the left_height and right_height get from 4-node.left and 4-node.right.
        return is_balance, max(left_height, right_height) + 1


if __name__ == "__main__":
    root = TreeNode(1)
    left_node_1 = TreeNode(1)
    left_node_2 = TreeNode(2)
    left_node_3 = TreeNode(3)
    left_node_4 = TreeNode(4)
    root.left = left_node_1
    root.right = left_node_1

    root.left.left = left_node_2
    root.right.right = left_node_2

    root.left.left.left = left_node_3
    root.left.left.right = left_node_3

    root.left.left.left.left = left_node_4
    root.left.left.left.right = left_node_4

    print(Solution().isBalanced(root))
