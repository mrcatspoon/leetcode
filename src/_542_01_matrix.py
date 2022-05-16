# https://leetcode.com/problems/01-matrix/
import math
from itertools import product
from typing import List, Tuple

Matrix = List[List[int]]


class Solution:
    def updateMatrix(self, mat: Matrix) -> Matrix:
        def item_filter(item: Tuple[int, int]) -> bool:
            return mat[item[0]][item[1]] > 0

        m, n = len(mat), len(mat[0])

        for i, j in filter(item_filter, product(range(m), range(n))):
            top = mat[i - 1][j] if i > 0 else math.inf
            left = mat[i][j - 1] if j > 0 else math.inf
            mat[i][j] = min(top, left) + 1

        for i, j in filter(item_filter, product(range(m - 1, -1, -1), range(n - 1, -1, -1))):
            bottom = mat[i + 1][j] if i < m - 1 else math.inf
            right = mat[i][j + 1] if j < n - 1 else math.inf
            mat[i][j] = min(mat[i][j], bottom + 1, right + 1)

        return mat
