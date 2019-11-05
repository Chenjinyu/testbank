"""
[LeetCode] 236. Lowest Common Ancestor of a Binary Tree: [Medium]
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
       3
    /------\
    5       1
  /  \     /  \
 6    2   0    8
     / \
    7   4

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.

related: 1.easy/4.Trees/235.lowestCommonAncestorOfABinarySearchTree.py
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or p == root or q == root: return root
        # in the recursion, p or q finally will equal root(root's child)
        # and return the `root`(p or q) to left_node or right_node.
        # also we can understand the self.lowestCommonAncestor here is to find the node which equals p or q.
        left_node = self.lowestCommonAncestor(root.left, p, q)
        # the recursion is one by one, left first and then right node.
        # so, if right_node and left_node can be found in each side, it says, the two nodes exist in right and left.
        right_node = self.lowestCommonAncestor(root.right, p, q)
        # if left_node and right_node are found, both are exist, the current root is the lowest common ancestor.
        if left_node and right_node: return root
        # if only one side node be found, no matter its p or q, we can know, they are in the same side.
        # and the first find the node is the lowest common ancestor.
        return left_node if left_node else right_node