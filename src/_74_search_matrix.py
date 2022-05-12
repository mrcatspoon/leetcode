# https://leetcode.com/problems/search-a-2d-matrix/
from bisect import bisect_right
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_index = bisect_right(tuple(matrix[i][0] for i in range(len(matrix))), target)
        row = matrix[row_index - 1]

        low, high = 0, len(row)
        while low < high:
            mid = (low + high) // 2
            if row[mid] == target:
                return True
            if row[mid] < target:
                low = mid + 1
            else:
                high = mid

        return False


print(
    Solution().searchMatrix(
        matrix=[[1], [3]],
        target=1,
    )
)
print(
    Solution().searchMatrix(
        matrix=[
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60],
        ],
        target=3,
    )
)
print(
    Solution().searchMatrix(
        matrix=[
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60],
        ],
        target=13,
    )
)
