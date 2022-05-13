# https://leetcode.com/problems/subrectangle-queries/
from typing import List


class SubrectangleQueries:
    __slots__ = ("_rectangle",)

    def __init__(self, rectangle: List[List[int]]):
        self._rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self._rectangle[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        try:
            return self._rectangle[row][col]
        except IndexError:
            return -1
