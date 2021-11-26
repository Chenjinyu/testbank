"""
Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Note:
Bonus points if you could solve it both recursively and iteratively.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def isSymmetricRecur(self, root: TreeNode) -> bool:
        def isMirror(node1: TreeNode, node2: TreeNode):
            if node1 == node2 is None:
                return True
            if node1 is None or node2 is None:
                return False

            return all(((node1.val == node2.val),
                       isMirror(node1.left, node2.right),
                       isMirror(node1.right, node2.left)))
        return isMirror(root, root)


    def isSymmetricIterative(self, root: TreeNode) -> bool:
        if root is None:
            return True

        right_side_list = []
        left_side_list = []

        right_node = root.right
        left_node = root.left

        right_side_list.append(right_node.val)
        left_side_list.append(left_node.val)

        while right_node:
            right_side_list.extend(
                [
                    right_node.right.val if right_node.right else None,
                    right_node.left.val if right_node.left else None
                ]
            )
            # todo: why the right_node.right is None, but the right_node.left has a node.
            # it will lose at least one value from node.left
            if right_node.right is not None:
                right_node = right_node.right
            else:
                right_node = right_node.left

        while left_node:
            left_side_list.extend(
                [
                    left_node.left.val if left_node.left else None,
                    left_node.right.val if left_node.right else None
                ]
            )
            # todo: why the left_node.left is None, but the left_node.right has a node.
            # it will lose at least one value from node.right
            if left_node.left is not None:
                left_node = left_node.left
            else:
                left_node = left_node.right

        print(right_side_list)
        print(left_side_list)
        return right_side_list == left_side_list


if __name__ == "__main__":
    # [9,-42,-42,null,76,76,null,null,13,null,13]
    root = TreeNode(9)
    node2_0 = TreeNode(-42)
    node2_1 = TreeNode(-42)

    root.left = node2_0
    root.right = node2_1

    node3_1 = TreeNode(76)
    node3_2 = TreeNode(76)

    node2_0.right = node3_1
    node2_0.left = None
    node2_1.right = None
    node2_1.left = node3_2

    node4_1 = TreeNode(13)
    node4_2 = TreeNode(13)

    node3_1.right = node4_1
    node3_1.left = None

    node3_2.left = node4_2
    node3_2.right = None

    print(Solution().isSymmetricIterative(root))