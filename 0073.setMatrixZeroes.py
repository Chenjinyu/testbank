"""
Set Matrix Zeroes
Given a m * n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def setZeroesByPoint(row_ptr, col_ptr):
            i, j = 0, 0
            while i < col_length:
                matrix[row_ptr][i] = 0
                i += 1
            while j < row_length:
                matrix[j][col_ptr] = 0
                j += 1

        if not matrix: return []
        row_length = len(matrix)
        col_length = len(matrix[0])
        zero_pos = []
        for i in range(row_length):
            if 0 in matrix[i]:
                for j in range(col_length):
                    if matrix[i][j] == 0:
                        zero_pos.append([i, j])
        for row_ptr, col_ptr in zero_pos:
            setZeroesByPoint(row_ptr, col_ptr)

        return matrix


if __name__ == "__main__":
    matrix = [
              [0,1,2,0],
              [3,4,5,2],
              [1,3,1,5]
            ]
    Solution().setZeroes(matrix)
    print(matrix)