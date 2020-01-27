"""
You have a map that marks the location of a treasure island.
Some of the map area has jagged rocks and dangerous reefs.
Other areas are safe to sail in. There are other explorers trying to find the treasure.
So you must figure out a shortest route to the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of characters.
You must start from the top-left corner of the map and can move one block up, down, left or right at a time.
The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner.
Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks.
You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is always safe.
Output the minimum number of steps to get to the treasure.

Example:

Input:
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

Output: 5
Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.
"""

from collections import deque

def solution(grid):
    row, col = len(grid), len(grid[0])

    q = deque([((0, 0), 0)])
    grid[0][0] = "D"
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while q:
        (x, y), step = q.popleft()

        for d in directions:
            dr = d[0] + x
            dc = d[1] + y
            if 0 <= dr < row and 0 <= dc < col:
                if grid[dr][dc] == "X":
                    return step + 1
                elif grid[dr][dc] == "O":
                    grid[dr][dc] = "D"
                    q.append(((dr, dc), step + 1))

    return -1

input = [['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

print(solution(input))