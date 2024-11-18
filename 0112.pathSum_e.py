"""
112. Path Sum
Given a binary tree and a sum, determine if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Amazon OA Problem
    Facebook OA Problem
    """
    def hasPathSumBFSIter(self, root: TreeNode, sum: int) -> bool:
        """
        since the data should be read from the top.
        the order should be root, left and right.
        """
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, path_sum = stack.pop()

            if path_sum == sum and not node.left and not node.right:
                return True

            if node.left:
                stack.append((node.left, path_sum + node.left.val))
            if node.right:
                stack.append((node.right, path_sum + node.right.val))

        return False

    def hasPathSumIssueExample(self, root: TreeNode, sum: int) -> bool:
        """

        """
        if not root:
            return False
        stack = [root]
        path_sum = 0
        while stack:
            node = stack.pop()

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

            # path_sum add cur node.val it effect the path_sum value
            # compare with hasPathSumBFS, the path_sum result relates to each node.
            # coz, different node, the sum is different. so, could not be the global path_sum to calculate.
            path_sum += node.val
            if path_sum == sum and not node.left and not node.right:
                return True

        return False
    

    def hasPathSum2024(self, root: Optional[TreeNode], sum:int) -> bool:
        if not root:
            return False
        
        stack = [(root, 0)]
        
        while stack:
            node, prev_val = stack.pop()
            if node.left == None and node.right == None:
                if (node.val + prev_val) == sum:
                    return True
            
            prev_val += node.val
            
            if node.left:
                stack.append((node.left, prev_val))
            if node.right:
                stack.append((node.right, prev_val))
            
            
        return False
        

# case 1
# [5,4,8,11,null,13,4,7,2,null,null,null,1]
# 22
# output: true

# case 2
# [1]
# 1
# output: true
