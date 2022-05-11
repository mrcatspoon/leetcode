# https://leetcode.com/problems/reshape-the-matrix/
from itertools import chain
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat

        mat = chain(*mat)
        result = []
        for i in range(r):
            result.append([])
            for j in range(c):
                result[i].append(next(mat))

        return result
