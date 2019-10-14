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