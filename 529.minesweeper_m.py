"""
Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine,
'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent
(above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to
this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'),
return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B')
and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8')
representing the number of adjacent mines.
Return the board when no more squares will be revealed.
"""
from collections import deque

class Solution(object):
    def updateBoard(self, board, click):
        def check_mine(i, j):
            res = 0
            for ni, nj in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                    if board[ni][nj] == "M":
                        res += 1
            return res

        queue = deque([click])
        seen = set(tuple(click))
        while queue:
            i, j = queue.popleft()
            if board[i][j] == "M":
                board[i][j] = "X"
                return board
            num = check_mine(i, j)
            if num > 0:
                board[i][j] = str(num)
                continue
            board[i][j] = "B"
            for ni, nj in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and (ni, nj) not in seen:
                    if board[ni][nj] == "E":
                        queue.append((ni, nj))
                        seen.add((ni, nj))
        return board


if __name__ == "__main__":
    board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
    click = [3,0]
    print(Solution().updateBoard(board, click))
    print([["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]])