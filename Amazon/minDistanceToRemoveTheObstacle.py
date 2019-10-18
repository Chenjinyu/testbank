"""
You are in charge of preparing a recently purchased lot for Amazon’s building.
The lot is covered with trenches and has a single obstacle that needs to be taken down before the foundation is prepared
for the building. The demolition robot must remove the obstacle before the progress can be made on the building.
Write an algorithm to determine the minimum distance required for the demolition robot to remove the obstacle.

Assumptions:

The lot is flat, except the trenches and can be represented by a 2D grid.
The demolition robot must start at the top left corner of the lot, which is always flat, and can move on block up, down, right, left
The demolition robot cannot enter trenches and cannot leave the lot.
The flat areas are indicated by 1, areas with trenches are indicated by 0, and the obstacle is indicated by 9
Input: The input of the function has 3 arguments:

numRows – number of rows
numColumns – number of columns
lot – 2d grid of integers
Output: 
Return an integer that indicated the minimum distance traversed to remove the obstacle else return -1

Constraints: 1<= numRows, numColumns <= 1000

Example: numRows = 3, 
numColumns = 3 
lot = [
    [1, 0, 0], 
    [1, 0, 0], 
    [1, 9, 1] 
]
Output: 3

Explanation: Starting from the top-left corner, the demolition robot traversed the cells (0,0) -> (1,0)-> (2,0)->(2,1).
The robot moves 3 times to remove the obstacle “9”
"""
from collections import deque
import queue

class Solution:
    def minDistanceToRemoveObstacle(self, num_rows, num_cols, lot) -> int:
        # time complexity: O(N)
        if not num_rows or not num_cols: return -1
        """
        collections.deque is an alternative implementation of
        unbounded queues with fast atomic append() and popleft() operations
        that do not require locking and also support indexing.
        collections.deque([iterable[, maxlen]]), should be a list inside.
        so that can be append and pop.
        """
        # initial the start point,
        q = deque([((0, 0), 0)])  # ((x, y), step)
        matrix = lot
        while q:
            (x, y), step = q.popleft()
            # the directions. right, left, down and up.
            # loop the four directions. if find 1, mark it as visited and go around away it.
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                if 0 <= x + dx < num_rows and 0 <= y + dy < num_cols:
                    if matrix[x + dx][y + dy] == 9:
                        return step + 1
                    elif matrix[x + dx][y + dy] == 1:
                        # mark visited
                        matrix[x + dx][y + dy] = 0
                        # append new point to the queue
                        q.append(((x + dx, y + dy), step + 1))

        return -1


if __name__ == "__main__":
    num_rows = 3
    num_cols = 3
    lot = [
            [1, 0, 0],
            [0, 0, 0],
            [1, 1, 9]
        ]
    print(Solution().minDistanceToRemoveObstacle(num_rows, num_cols, lot))
