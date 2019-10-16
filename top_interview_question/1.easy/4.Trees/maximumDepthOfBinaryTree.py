"""
Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepthRecursion(self, root: TreeNode) -> int:
        """
        Depth-First Search (DFS) strategy:
        Time: O(N).
        Space complexity: O(log(N))
        in the worst case, the tree is completely unbalanced,
        e.g. each node has only left child node, the recursion call would occur N times (the height of the tree),
        therefore the storage to keep the call stack would be O(N).
        But in the best case (the tree is completely balanced), the height of the tree would be log(N).
        Therefore, the space complexity in this case would be O(log(N)).
        """
        if root is None:
            return 0

        return 1 + max(self.maxDepthRecursion(root.left), self.maxDepthRecursion(root.right))


    def maxDepthIteration(self, root: TreeNode) -> int:
        """
        FILO (First-In-Last-Out)
        Time: O(N).
        Space complexity: O(log(N))
        in the worst case, the tree is completely unbalanced, e.g. each node has only left child node,
        the recursion call would occur N times (the height of the tree),
        therefore the storage to keep the call stack would be O(N).
        But in the average case (the tree is balanced), the height of the tree would be log(N).
        Therefore, the space complexity in this case would be O(log(N)).
        """
        stack = []  # stores a dict
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack is not []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))

        return depth



if __name__ == "__main__":
    tree_root = TreeNode(3, 9, 20)
    print(Solution().maxDepthRecursion(tree_root))
