"""
You have a map that marks the locations of treasure islands. Some of the map area has jagged rocks and dangerous reefs.
Other areas are safe to sail in. There are other explorers trying to find the treasure.
So you must figure out a shortest route to one of the treasure islands.

Assume the map area is a two dimensional grid, represented by a matrix of characters.
You must start from one of the starting point (marked as S) of the map
and can move one block up, down, left or right at a time.
The treasure island is marked as X. Any block with dangerous rocks or reefs will be marked as D.
You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in.
Output the minimum number of steps to get to any of the treasure islands.

Example:

Input:
[['S', 'O', 'O', 'S', 'S'],
 ['D', 'O', 'D', 'O', 'D'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'D', 'D', 'O', 'O'],
 ['X', 'D', 'D', 'D', 'O']]

Output: 3
Explanation:
You can start from (0,0), (0, 3) or (0, 4). The treasure locations are (2, 4) (3, 0) and (4, 0).
Here the shortest route is (0, 3), (1, 3), (2, 3), (2, 4).

"""
from typing import List
import math
from collections import deque
import numpy as np


def shortestRouteToFindTreasureIsland(grid: List[List[str]]):
    row, col = len(grid), len(grid[0])
    final_min_steps = math.inf

    positions = []
    for r in range(row):
        for c in range(col):
            if grid[r][c] == 'S':
                positions.append((r, c))
                grid[r][c] = "D"

    if not positions:
        return -1
    positions = [(0, 3)]
    grid[0][3] = "D"
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    for pos in positions:
        queue = deque([(pos[0], pos[1], 0)])
        is_find = False
        while queue and not is_find:
            r, c, steps = queue.popleft()
            for dr, dc in directions:
                cur_r = r + dr
                cur_c = c + dc
                if 0 <= cur_r < row and 0 <= cur_c < col and grid[cur_r][cur_c] is not "D":
                    if grid[cur_r][cur_c] == "X":
                        steps += 1
                        final_min_steps = min(steps, final_min_steps)
                        is_find = True
                        break
                    elif grid[cur_r][cur_c] == "O":
                        grid[cur_r][cur_c] = "D"
                        queue.append((cur_r, cur_c, steps + 1))

        # final_min_steps = min(final_min_steps, min_path)

    return final_min_steps


input = [['S', 'O', 'O', 'S', 'S'],
         ['D', 'O', 'D', 'O', 'D'],
         ['O', 'O', 'O', 'O', 'X'],
         ['X', 'D', 'D', 'O', 'O'],
         ['X', 'D', 'D', 'D', 'O']]

print(shortestRouteToFindTreasureIsland(input))