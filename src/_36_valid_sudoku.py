# https://leetcode.com/problems/valid-sudoku/
from typing import Iterable, List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                values = (board[ii][jj] for ii in range(i, i + 3) for jj in range(j, j + 3) if board[ii][jj] != ".")
                if self.has_duplicates(values):
                    return False

        for i in range(9):
            if self.has_duplicates(value for value in board[i] if value != "."):
                return False
            if self.has_duplicates(board[j][i] for j in range(9) if board[j][i] != "."):
                return False

        return True

    def has_duplicates(self, values: Iterable[str]) -> bool:
        unique_values = set()
        for value in values:
            if value in unique_values:
                return True
            unique_values.add(value)
        return False
