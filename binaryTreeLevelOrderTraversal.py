"""
Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]


Note: you cannot resolve all the node in one loop, eg levelOrder() as below.
has to step to each node, node.right and node.right in loop or recursion. eg. levelOrderImprove

#todo: how to improve the levelOrder()?
"""
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        order_traverasl_list = []
        if root is None:
            return order_traverasl_list.append([])

        order_traverasl_list.append([root.val])
        left_node = root.left
        right_node = root.right
        while left_node or right_node:
            level_node_val = [
                left_node.left.val if left_node.left else None,
                left_node.right.val if left_node.right else None,
                right_node.left.val if right_node.left else None,
                right_node.right.val if right_node.right else None,
              ]
            order_traverasl_list.append([v for v in level_node_val if v is not None])

            left_node = left_node.left
            right_node = right_node.right

        return order_traverasl_list

    def levelOrderImprove(self, root: TreeNode) -> List[List[int]]:
        order_traverasl_list = []
        if not root:
            return order_traverasl_list

        def levelChecker(node, level):
            # in each loop, only has one node and add node.right and left to list
            # and them loop to next node, do the same.
            if len(order_traverasl_list) == level:
                order_traverasl_list.append([])

            order_traverasl_list[level].append(node.val)

            if node.left:
                levelChecker(node.left, level + 1)

            if node.right:
                levelChecker(node.right, level + 1)

        levelChecker(root, 0)
        return order_traverasl_list


if __name__ == "__main__":
    root = TreeNode(3)
    node2_0 = TreeNode(9)
    node2_1 = TreeNode(20)

    root.left = node2_0
    root.right = node2_1

    node3_1 = TreeNode(15)
    node3_2 = TreeNode(7)

    node2_1.right = node3_1
    node2_1.left = node3_2

    print(Solution().levelOrderImprove(root))
