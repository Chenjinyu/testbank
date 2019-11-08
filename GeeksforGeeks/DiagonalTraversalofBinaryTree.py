"""
Consider lines of slope -1 passing between nodes. Given a Binary Tree, print all diagonal elements in a binary tree belonging to same line.

Input : Root of below tree

        8
      /   \
     3    10
    /   /   \
   1   6    14
     /  \   /
    4   7  13

Output :
Diagonal Traversal of binary tree :
 8 10 14
 3 6 7 13
 1 4
"""
from collections import defaultdict, deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def diagonal_traversal(self, root):
        diagonal_dic = defaultdict(list)
        queue = deque([(root, 0)])
        max_idx = 0
        result = []
        while queue:
            node, idx = queue.popleft()
            max_idx = max(max_idx, idx)
            diagonal_dic[idx].append(node.data)
            if node.right:
                queue.append((node.right, idx))
            if node.left:
                queue.append((node.left, idx + 1))
        for key in range(max_idx + 1):
            result += diagonal_dic[key]

        return result


# Driver Program
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.right.right.left = Node(13)
root.left.right.left = Node(4)
root.left.right.right = Node(7)

print(Solution().diagonal_traversal(root))
# 8 10 14 3 6 7 13 1 4