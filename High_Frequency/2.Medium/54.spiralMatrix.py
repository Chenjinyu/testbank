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

"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # i spent almost 1 day to implement this function.
        # runtime: 36ms, faster than 73.57%.
        if not matrix: return []
        row_length = len(matrix)
        col_length = len(matrix[0])
        row1 = 0
        row2 = row_length - 1
        col1 = 0
        col2 = col_length - 1
        spiral_order_list = []
        while True:
            if row1 > row2: break
            if row2 < col1: break
            if col2 < col1: break
            if col1 > row2: break
            # from left to right for the matrix[up] row.
            for ptr in range(col1, col2 + 1):  # first row
                print("1. matrix[{}][{}]:{}".format(row1, ptr, matrix[row1][ptr]))
                spiral_order_list.append(matrix[row1][ptr])
            row1 += 1
            for ptr in range(row1, row2 + 1):  # last col
                print("2. matrix[{}][{}]:{}".format(ptr, col2, matrix[ptr][col2]))
                spiral_order_list.append(matrix[ptr][col2])
            col2 -= 1
            """
            why here need to set if row1 <= row2 and col1 <= col2:?
            if not, has an issue.
            """
            if row1 <= row2 and col1 <= col2:
                for ptr in range(col2, col1 - 1, -1):  # last row
                    print("3. matrix[{}][{}]:{}".format(col2, col1 - 1, row2, ptr, matrix[row2][ptr]))
                    spiral_order_list.append(matrix[row2][ptr])
                row2 -= 1
                for ptr in range(row2, row1 - 1, -1):  # first col
                    print("4. matrix[{}][{}]:{}".format(ptr, col1, matrix[ptr][col1]))
                    spiral_order_list.append(matrix[ptr][col1])
                col1 += 1

        return spiral_order_list

    def spiralOrderImprove(self, matrix: List[List[int]]) -> List[int]:
        def spiral_coords(r1, c1, r2, c2):
            for c in range(c1, c2 + 1):
                yield r1, c
            for r in range(r1 + 1, r2 + 1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1, -1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1

        if not matrix: return []
        answers = []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <=c2:
            for r, c in spiral_coords(r1, c1, r2, c2):
                answers.append(matrix[r][c])
            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1
        return answers


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