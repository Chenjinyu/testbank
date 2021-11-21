"""
We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]

Explanation:
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.

https://leetcode.com/problems/binary-tree-pruning/
"""


class TreeNode:  # Definition for a binary tree node.
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:  # Recursion
        """
        from bottom to top traversal.
        """
        def containsOne(node):
            if not node: return False  # travers to the end of node's right or left, returns False.
            left_node = containsOne(node.left)
            right_node = containsOne(node.right)
            if not left_node: node.left = None
            if not right_node: node.right = None
            return node.val == 1 or left_node or right_node

        return root if containsOne(root) else None

    def pruneTree(self, root: TreeNode) -> TreeNode:
        stack = []