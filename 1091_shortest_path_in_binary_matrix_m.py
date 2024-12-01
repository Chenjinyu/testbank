"""
1091. Shortest Path in Binary Matrix

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1

https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
"""
from typing import List, Union
from collections import deque

class Solution:
    def shortestPathBinaryMatrixWithQueue(self, grid: List[List[int]]) -> int:
        """
        Unlike DFS, BFS does not require revisiting nodes or checking for alternative paths 
        because the first valid path to the target is already the shortest.
        In DFS, you might visit the target node multiple times, each with a different path length. 
        This is why you need to track and compare all possible paths to find the shortest one
        """
        matrix_len = len(grid)
        if grid[0][0] == 1 or grid[matrix_len-1][matrix_len-1] == 1: # there is no path could start or no ends
            return -1
        
        queue = deque([(0, 0, 1)]) # mark as visited
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        grid[0][0] = 1
        while queue:
            x, y, path_len = queue.popleft()
            if x == matrix_len - 1 and y == matrix_len - 1:
                return path_len
            
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < matrix_len and 0 <= new_y < matrix_len and grid[new_x][new_y] == 0:
                    grid[new_x][new_y] = 1
                    queue.append((new_x, new_y, path_len + 1))
                
        return -1
    
    def shortestPathBinaryMatrixWithQueueWithAddiSpaceForSeenStorage(self, grid: List[List[int]]) -> int:
        matrix_len = len(grid)
        if grid[0][0] == 1 or grid[matrix_len-1][matrix_len-1] == 1: # there is no path could start or no ends
            return -1
        
        def validated(row, col):
            return 0 <= row < matrix_len and 0 <= col < matrix_len and grid[row][col] == 0
        
        seen = set([(0, 0)]) # or seen = {(0, 0)}
        queue = deque([(0, 0, 1)]) # mark as visited
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        grid[0][0] = 1
        while queue:
            x, y, path_len = queue.popleft()
            if x == matrix_len - 1 and y == matrix_len - 1:
                return path_len
            
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if validated(dx, dy) and grid[new_x][new_y] not in seen:
                    seen.add((new_x, new_y))
                    queue.append((new_x, new_y, path_len + 1))
                
        return -1
        
    
    def shortestPathBinaryMatrixWithRecurion(self, grid: List[List[int]]) -> Union[int, float]: # reach out maximum recursion depth exceeded
        """
        Traversal Order:
        In the recursive implementation of BFS, you often explore multiple paths from the current node 
        without automatically prioritizing the shortest path.
        This means you might visit the same cell multiple times via different routes, requiring you to compare the lengths of these paths.
        
        No Centralized Queue:
        Unlike iterative BFS, which uses a queue to enforce a level-by-level exploration order, 
        recursion lacks a global structure to manage the "layers."
        Without a queue to handle nodes by proximity to the start, the recursion will explore deeper paths before returning to shallower ones.
        
        Backtracking:
        Backtracking is necessary in recursive BFS because you need to ensure the grid or path state is reset after exploring a path.
        When you return from one recursive call, you "backtrack" to undo any changes 
        (e.g., marking a cell as visited) so that other paths can explore the same cell.
        """
        matrix_len = len(grid)
        if grid[0][0] == 1 or grid[matrix_len-1][matrix_len-1] == 1: # there is no path could start or no ends
            return -1
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        shortest_path = float('inf')
        def bsf(dx, dy, path_len):
            nonlocal shortest_path
            if dx == matrix_len - 1 and dy == matrix_len - 1:
                shortest_path = min(shortest_path, path_len)
                return 
            grid[dx][dx] = 1 # Mark as visited
            for x, y in directions:
                new_dx, new_dy = dx + x, dy + y
                if 0 <= new_dx < matrix_len and 0 <= new_dy < matrix_len and grid[new_dx][new_dy] == 0:
                    bsf(new_dx, new_dy, path_len + 1)
            grid[dx][dx] = 0 # Unmark for backtracking, since the cell will be visited many times.
            
        bsf(0, 0, 1)
        
        return shortest_path if shortest_path != float('inf') else -1
        
            