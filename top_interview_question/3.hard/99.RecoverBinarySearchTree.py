"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
  
Example 3:
Input: [5, 3, 8, null, 7, 6, 2]
  5
 /  \
3    8
\   / \
 7  6  2
Output: [5,3,8,null,2,6,7]
  5
 /  \
3    8
\   / \
 2  6  7
Follow up:
A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverTreeWithStack(self, node: TreeNode):
        """
        basically, in the if pred and node.val < pred.val, this logic
        only uses for finding the two elements.
        """
        stack = []
        # first node uses to store the element first time found, which value bigger than current node.
        # so first node = previous node
        # second node uses to store the element second time found, which value smaller than previous node.
        # so second node = current node.
        first = second = prev = None

        while stack or node:
            while node:
                # append curr node to stack
                stack.append(node)
                # move node to node left leaf.
                node = node.left
            # pop up the last one node.
            node = stack.pop()
            if prev and node.val < prev.val:  # because previous node should not large than curr node.
                # if match the condition, second equals to the curr node.
                second = node
                if first is None:
                    first = prev  # which needs to swap
                else:
                    break
            prev = node  # prev node move to next node.
            node = node.right
        print(first.val, second.val)
        first.val, second.val = second.val, first.val


if __name__ == "__main__":
    root = TreeNode(5)
    left_node_1 = TreeNode(3)
    left_node_2 = TreeNode(7)
    root.left = left_node_1
    left_node_1.right = left_node_2

    right_node_1 = TreeNode(8)
    right_node_2 = TreeNode(6)
    right_node_3 = TreeNode(2)

    root.right = right_node_1
    right_node_1.left = right_node_2
    right_node_1.right = right_node_3

    Solution().recoverTreeWithStack(root)

