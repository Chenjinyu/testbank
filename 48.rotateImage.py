"""
48. Rotate Image
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
Problem solving：
1. have to deepCopy the matrix, because in-place replacement will re-write item which we will use later.

Note: List[~i] = List[length - 1 - i]

[::-1] vs list.reverse()
[::-1] gives a new list in reversed.
list.reverse() reverses the list in-place, no return.
"""
from typing import List
from copy import deepcopy

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        copied_matrix = deepcopy(matrix)
        for row_index in range(len(matrix)):
            length = len(matrix[0])
            col_index = 0
            while col_index < length:
                matrix[row_index][col_index] = copied_matrix[~col_index][row_index]
                col_index += 1

    def rotate2(self, matrix2: List[List[int]]) -> None:
        # zip(*a) is equal to zip(a[0], a[1], a[2]..., a[n])
        matrix2[:] = map(list, zip(*matrix2[::-1]))

    def rotate3(self, matrix3: List[List[int]]) -> None:
        n = len(matrix3)
        for i in range(n / 2):
            for j in range(n - n / 2):
                matrix3[i][j], matrix3[~j][i], matrix3[~i][~j], matrix3[j][~i] = \
                    matrix3[~j][i], matrix3[~i][~j], matrix3[j][~i], matrix3[i][j]


if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Solution().rotate2(matrix)
    print(matrix)
    print([[7, 4, 1], [8, 5, 2], [9, 6, 3]])
