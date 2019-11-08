"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""
from typing import List

class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]: return False
        row, col = len(board), len(board[0])

        visited = set()
        for i in range(row):
            for j in range(col):
                # only the search returns True, then return True.
                # since the word path has not matched, have to avoid these returns.
                if self.search(board, word, 0, i, j, visited) == True:
                    return True

        return False

    def search(self, board, word, start, row_index, col_index, visited):
        if start == len(word): return True
        row, col = len(board), len(board[0])
        if row_index >= 0 and row_index < row and \
                col_index >= 0 and col_index < col and \
                board[row_index][col_index] == word[start] and \
                (row_index, col_index) not in visited:
            start += 1
            # visited.add() is the backtracking algorithm.
            visited.add((row_index, col_index))
            # tmp = board[row_index][col_index]
            # board[row_index][col_index] = '#'
            result = self.search(board, word, start, (row_index - 1), col_index, visited) \
                     or self.search(board, word, start, (row_index + 1),col_index,visited) \
                     or self.search(board, word, start, row_index, col_index - 1, visited) \
                     or self.search(board, word, start, row_index,col_index + 1, visited)
            visited.remove((row_index, col_index))
            # board[row_index][col_index] = tmp
            return result
        return False
