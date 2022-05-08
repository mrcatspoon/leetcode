# https://leetcode.com/problems/zigzag-conversion/
from collections import defaultdict


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        num_rows_range = tuple(range(numRows))
        zig_range = num_rows_range[-2:0:-1]

        s_iter = iter(s)
        zig_rows = defaultdict(list)
        try:
            while True:
                for i in num_rows_range:
                    zig_rows[i].append(next(s_iter))
                for i in zig_range:
                    zig_rows[i].append(next(s_iter))
        except StopIteration:
            pass

        return "".join(char for i in num_rows_range for char in zig_rows[i])
