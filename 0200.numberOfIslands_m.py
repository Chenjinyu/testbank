"""
200. Number of Islands
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3

Example 3:
Input:
11000
11100
00100
00111
Output: 3
"""
from typing import List
from collections import deque


class Solution:
    """
    Oracle OA Problem
    Amazon OA Problem
    Facebook OA Problem
    Google OA Problem
    Apple OA Problem
    LinkedIn OA Problem
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        queue = []
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    queue.append([i, j])
                    grid[i][j] = '0'
                    while queue:
                        element = queue.pop(0)
                        for d in directions:
                            x = element[0] + d[0]
                            y = element[1] + d[1]
                            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '0':
                                queue.append([x, y])
                                grid[x][y] = '0'
        return count

    def num_islands_bfs(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        grid_row, grid_col = len(grid), len(grid[0])
        num_islands = 0
        neighbor = deque()
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for r in range(grid_row):
            for c in range(grid_col):
                if grid[r][c] == "1":
                    num_islands += 1
                    neighbor.append((r, c))
                while neighbor:
                    row, col = neighbor.popleft()
                    for d in direction:
                        dr = d[0] + row
                        dc = d[1] + col
                        # if dr < 0 or dc < 0 or dr >= grid_row or dc >= grid_col or grid[dr][dc] == "0":
                        #     continue
                        # grid[dr][dc] = "0"
                        # neighbor.append((dr, dc))
                        if 0 <= dr < grid_row and 0 <= dc < grid_col and grid[dr][dc] is not '0':
                            neighbor.append((dr, dc))
                            # let the 4 directions to 0, so that when neighbor does not have 1, it will
                            # jump out the while, and search next not neighbor cell and count += 1
                            grid[dr][dc] = "0"

        return num_islands

    def num_islands_bfs_error(self, grid: List[List[str]]) -> int:
        """
        error reason:
        1. neighbor.append() should after the checking of row and col, grid[row][col].
        """
        if not grid: return 0
        grid_row = len(grid)
        grid_col = len(grid[0])
        num_islands = 0
        neighbor = deque()
        for r in range(grid_row):
            for c in range(grid_col):
                if grid[r][c] == "1":
                    num_islands += 1

                    neighbor.append((r, c - 1))
                    neighbor.append((r, c + 1))
                    neighbor.append((r - 1, c))
                    neighbor.append((r + 1, c))
                while neighbor:
                    row, col = neighbor.popleft()

                    if row < 0 or col < 0 or row >= grid_row or col >= grid_col or grid[row][col] == "0":
                        continue

                    grid[row][col] = "0"
                    # if 0 <= row < grid_row and 0 <= col < grid_col and grid[row][col] is not '0':
                    #     grid[row][col] = "0"

        return num_islands

    def num_islands_dfs(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        grid_row = len(grid)
        grid_col = len(grid[0])
        num_islands = 0

        def dfs(grid, row, col):
            nonlocal grid_col
            nonlocal grid_row

            if row < 0 or col < 0 or row >= grid_row or col >= grid_col or grid[row][col] == "0":
                return

            grid[row][col] = "0"
            dfs(grid, row, col + 1)
            dfs(grid, row, col - 1)
            dfs(grid, row + 1, col)
            dfs(grid, row - 1, col)

        for r in range(grid_row):
            for c in range(grid_col):
                if grid[r][c] == "1":
                    num_islands += 1
                    dfs(grid, r, c)

        return num_islands


if __name__ == "__main__":
    testcases = [
        {'s': [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"],
               ["0", "0", "0", "0", "0"]], 'e': 1},
        {'s': [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"],
               ["0", "0", "0", "1", "1"]], 'e': 5},
        {'s': [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"],
               ["0", "0", "0", "1", "1"]], 'e': 3},
    ]
    is_pass = True
    for case in testcases:
        actual_result = (Solution().num_islands_bfs(case['s']))
        print("Input: {}\nExpected: {}\nAcutal: {}\nis_Passed: {}".format(case['s'],
                                                                          case['e'],
                                                                          actual_result,
                                                                          actual_result == case['e']))
        if actual_result != case['e']:
            is_pass = False

    if not is_pass:
        print("!!!!-----FAILED------!!!!")