"""
36.Valid Sudoku

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

"""
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            num_row = [v for v in row if v != "."]
            if len(set(num_row)) < len(num_row):
                print("row return false")
                return False

        col_length = len(board[0])
        row_length = len(board)
        for col in range(col_length):
            col_list = []
            for row in range(row_length):
                col_list.append(board[row][col])

            num_col = [v for v in col_list if v != "."]
            if len(set(num_col)) < len(num_col):
                print("col return false")
                return False

        col_start = 0
        result = []
        for index in range(row_length):
            result.append([board[index][0:3], board[index][3:6], board[index][6:9]])
        zip_result = []
        for zip_time in [0, 3, 6]:
            zip_result.extend(zip(result[zip_time], result[zip_time + 1], result[zip_time + 2]))

        for v in zip_result:
            v_result = v[0] + v[1] + v[2]
            v_result = [val for val in v_result if val != "."]
            if len(v_result) > len(set(v_result)):
                print("sub board return false")
                return False

        return True

    # def get_sub_board(self, board, index):
    #     col_start = 0
    #     col_length = len(board[0])
    #     row_length = len(board)
    #     while col_start < col_length:
    #         sub_board_list = []
    #         row_start = 0
    #         while row_start < row_length:
    #             sub_board_list.append(board[row_start][col_start])
    #             col_start += 1
    #             if col_start // 3 == 0:
    #                 break
    #         row_start += 1
    #         if row_start // 3 == 0:
    #             break
    #
    #         sub_board_set = [v for v in sub_board_list if v != "."]
    #         print(sub_board_set)
    #         if len(set(sub_board_set)) < len(sub_board_set):
    #             print("sub board return false")
    #             return False


if __name__ == "__main__":
    board = \
        [
            ["5", "3", "9", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
    # board = \
    #     [
    #         ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    #         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #         [".", "9", "8", ".", ".", ".", ".", "6", "."],
    #         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    #         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #         [".", "6", ".", ".", ".", ".", "2", "8", "."],
    #         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #         [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    #     ]
    print(Solution().isValidSudoku(board))
