"""
Spiral Matrix(螺旋矩阵)
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],   -> -> ->
 [ 4, 5, 6 ],  | ->     |
 [ 7, 8, 9 ]   <- <- <- |
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

idea: from left to right, from top to button, from last row right to left and from first col button to top
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        pass

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
            ]
    matrix = [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]
    # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    # matrix = [[2,5],[8,4],[0,-1]]
    print(Solution().spiralOrder(matrix))
    
    
    
"""
235. Lowest Common Ancestor of a Binary Search Tree: [Easy]
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

       6
    /------\
    2       8
  /  \     /  \
 0    4   7    9
     / \
    3   5
     
     
Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.


Complexity Analysis

Time Complexity: O(N)O(N), where NN is the number of nodes in the BST. In the worst case we might be visiting all the nodes of the BST.
Space Complexity: O(N)O(N). This is because the maximum amount of space utilized by the recursion stack would be NN since the height of a skewed BST could be NN.

"""

class Solution:
    def lowestCommonAncestorRecursion(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Value of current node or parent node.
        parent_val = root.val

        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # If both p and q are greater than parent. the root has to move the next root(root.right)
        # eg, p = 3, q = 5, the root = root.right, it should be 4.
        if p_val > parent_val and q_val > parent_val:    
            return self.lowestCommonAncestor(root.right, p, q)
        # If both p and q are lesser than parent
        elif p_val < parent_val and q_val < parent_val:    
            return self.lowestCommonAncestor(root.left, p, q)
        # We have found the split point, i.e. the LCA node.
        else:
        # basic logic is if the p < root, and q > root, the curent node is the lowest common ancestor.
            return root
        
    # the second function is more straightful to understand.
    def lowestCommonAncestorLoop(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # Start from the root node of the tree
        node = root

        # Traverse the tree
        while node:

            # Value of current node or parent node.
            parent_val = node.val

            if p_val > parent_val and q_val > parent_val:    
                # If both p and q are greater than parent
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                # If both p and q are lesser than parent
                node = node.left
            else:
                # We have found the split point, i.e. the LCA node.
                return node
              
              
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
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (!root || p == root || q == root): return root
        # in the recursion, p or q finally will euqal root(root's child)
        # and return the `root`(p or q) to left_node or right_node. 
        # also we can understand the self.lowestCommonAncestor here is to find the node which equals p or q.
        left_node = self.lowestCommonAncestor(root.left, p, q)
        # the recursion is one by one, left first and then right node. 
        # so, if right_node and left_node can be found in each side, it says, the two nodes exist in right and left.
        right_node = self.lowestCommonAncestor(root.right, p, q)
        # if left_node and right_node are found, both are exist, the current root is the lowest common ancestor.
        if (left_node and right_node): return root
        # if only one side node be found, no matter its p or q, we can know, they are in the same side. 
        # and the first find the node is the lowest common ancestor.
        return left_node if left_node else right_node
