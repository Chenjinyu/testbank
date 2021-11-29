import numpy as np
from collections import deque
test = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
# expected output: 1 5 9 13 14 10 6 2 3 7 11 15 16 12 8 4


def dfs_deque(test):
    # depth-first-search in 2D matrix
    row, col = len(test), len(test[0])
    ans = ""
    visited = np.full((row, col), False, dtype=bool)
    # visited = np.full((2, 2), 'c', dtype=str)  # full fills matrix with different types
    stack = deque([(0, 0)])
    while stack:
        r, c = stack.popleft()

        if r < 0 or r >= row or c < 0 or c >= col or visited[r][c]:
            continue

        ans += " " + str(test[r][c])
        visited[r][c] = True
        # stack.appendleft((r, c - 1))  # left
        # go right is the last step
        stack.appendleft((r, c + 1))  # right
        # second step in the deque queue, when the first down finish, it will go up, but all of them are True.
        # so, until pop the right grid.
        stack.appendleft((r - 1, c))  # up
        stack.appendleft((r + 1, c))  # down

    return ans


def dfs_deque_right_append(test):
    # depth-first-search in 2D matrix
    row, col = len(test), len(test[0])
    ans = ""
    visited = np.full((row, col), False, dtype=bool)
    # visited = np.full((2, 2), 'c', dtype=str)  # full fills matrix with different types
    stack = deque([(0, 0)])
    while stack:
        r, c = stack.pop()

        if r < 0 or r >= row or c < 0 or c >= col or visited[r][c]:
            continue

        ans += " " + str(test[r][c])
        visited[r][c] = True
        stack.append((r, c + 1))  # right
        stack.append((r - 1, c))  # up
        stack.append((r + 1, c))  # down


    return ans



def dfs(test):
    # depth-first-search in 2D matrix
    row, col = len(test), len(test[0])
    ans = ""
    visited = np.full((row, col), False, dtype=bool)
    # visited = np.full((2, 2), 'c', dtype=str)  # full fills matrix with different types
    stack = [(0, 0)]
    while stack:
        r, c = stack.pop()

        if r < 0 or r >= row or c < 0 or c >= col or visited[r][c]:
            continue

        ans += " " + str(test[r][c])
        visited[r][c] = True
        stack.append((r, c - 1))  # left
        stack.append((r, c + 1))  # right
        stack.append((r - 1, c))  # up
        stack.append((r + 1, c))  # down

    return ans


print(dfs_deque_right_append(test))
print(" 1 5 9 13 14 10 6 2 3 7 11 15 16 12 8 4")
