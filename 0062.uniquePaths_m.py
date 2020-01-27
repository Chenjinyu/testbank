"""
62. Unique Paths
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

* - - - - - -
- - - - - - -
- - - - - - $

Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:
Input: m = 7, n = 3
Output: 28

"""
import numpy as np

class Solution:
    """
    Amazon OA Problem
    Uber OA Problem
    Apple OA Problem
    Microsoft OA Problem
    Facebook OA Problem

    dynamic programming.
    """
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Time Complexity: O(M  N)
        Space Complexity: O(M + N)
        """
        # mem = [[0 for _ in range(m)] for _ in range(n)]
        mem = np.zeros((n, m), dtype=int)

        def uniquePathsDP(i, j):
            # if i = 0 or j = 0 means in the only has one row or one column,
            # the robot only has one unique path to go. either right or down.
            if i == 0 or j == 0:
                mem[i][j] = 1
            else:
                # go right
                mem[i][j] += uniquePathsDP(i - 1, j) if mem[i - 1][j] == 0 else mem[i - 1][j]
                # go down
                mem[i][j] += uniquePathsDP(i, j - 1) if mem[i][j - 1] == 0 else mem[i][j - 1]
            return mem[i][j]

        # there use disorder, from n-1 and m-1 to 0.
        # because i == 0 or j == 0 is the dp's exit.
        return uniquePathsDP(n - 1, m - 1)

    def uniquePaths2(self, m: int, n: int) -> int:
        """
        Time Complexity: O(M * N)
        Space Complexity: O(M * N)
        """
        # set default to 1, coz when n = 1 or m = 1, there only has one unique path go to
        # either right or down.
        mem = np.full((n, m), 1, dtype=int)

        for i in range(1, n):
            for j in range(1, m):
                mem[i][j] = mem[i][j - 1] + mem[i - 1][j]

        return mem[n - 1][m - 1]


if __name__ == "__main__":
    testcases = [
        {'m': 23, 'n': 21, 'e': 513791607420},
        {'m': 3, 'n': 2, 'e': 3},
        {'m': 7, 'n': 3, 'e': 28},
    ]
    for case in testcases:
        actual_result = Solution().uniquePaths2(case['m'], case['n'])
        print("Input: {}\nExpected: {}\nAcutal: {}\nis_Passed: {}".format(case['m'],
                                                                          case['e'],
                                                                          actual_result,
                                                                          actual_result == case['e']))
