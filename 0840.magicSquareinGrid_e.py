"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column,
and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).



Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
"""
from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        count = 0

        if row_len < 3 or col_len < 3:
            return count

        def fuck_the_magic(a, b, c, d, e, f, g, h, i):
            # as question describe, the 3 x 3 grid filled with distinct numbers from 1 to 9.
            if sorted([a, b, c, d, e, f, g, h, i]) == list(range(1, 10)):
                if (a + b + c == d + e + f == g + h + i == a + e + i == c + e + g
                        == a + d + g == b + e + h == c + f + i):
                    return True

        for row in range(row_len - 2):
            for col in range(col_len - 2):
                if fuck_the_magic(grid[row][col], grid[row][col + 1], grid[row][col + 2],
                                  grid[row + 1][col], grid[row + 1][col + 1], grid[row + 1][col + 2],
                                  grid[row + 2][col], grid[row + 2][col + 1], grid[row + 2][col + 2]):
                    count += 1

        return count
