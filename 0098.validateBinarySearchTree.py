"""
Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def rightLargeLeftChecker(node, lower=float('-inf'), upper=float('inf')):
            if node is None:
                return True
            # it will iteration as possible as all nodes' value.
            # expect return False
            val = node.val
            if val <= lower or val >= upper:
                return False

            # let the val which is the top node's value compare with node.right's val
            # by val should < node.right.val
            if not rightLargeLeftChecker(node.right, val, upper):
                return False
            # let the val which is the top node's value compare with node.left's val
            # by val should > node.left.val
            if not rightLargeLeftChecker(node.left, lower, val):
                return False

            return True

        return rightLargeLeftChecker(root)

    def isValidBSTIteration(self, root: TreeNode) -> bool:
        if root is None:
            return True
        stack = [(root, float('-inf'), float('inf'))]

        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.left, val, upper))
            stack.append((root.right, lower, val))

        return True

    def isValidBSTInorderTraversal(self, root: TreeNode) -> bool:
        """
        Let's use the order of nodes in the inorder traversal Left -> Node -> Right.
        :param root:
        :return:
        """
        stack, in_order = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            # get each node's left object, to compare with the in_order.
            # the in_order should be Left -> Node -> Right ==> Left.val <= Node.val <= Right.val
            # so, in_order should be the largest value in each loop.
            root = stack.pop()
            # if next element in in_order traversal is smaller than the previous one
            # return False, it's not SBT.
            if root.val <= in_order:
                return False
            in_order = root.val
            root = root.right

        return True

