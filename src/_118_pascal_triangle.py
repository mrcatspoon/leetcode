# https://leetcode.com/problems/pascals-triangle/
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            row = [0] * (i + 1)
            row[0] = row[-1] = 1
            if len(row) >= 3:
                prev_row = result[-1]
                for j in range(len(row)):
                    if row[j] == 1:
                        continue
                    row[j] = prev_row[j] + prev_row[j - 1]
            result.append(row)

        return result
