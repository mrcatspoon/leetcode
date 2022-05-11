# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/
from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        first, second = s.split(":")

        cells = []
        for column in range(ord(first[0]), ord(second[0]) + 1):
            column_char = chr(column)
            for row in range(ord(first[1]), ord(second[1]) + 1):
                cells.append(column_char + chr(row))

        return cells
