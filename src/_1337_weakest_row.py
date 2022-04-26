# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/submissions/
import operator
from itertools import islice
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        result = sorted(
            zip(range(len(mat)), map(sum, mat)),
            key=operator.itemgetter(1),
        )
        return [i for i, _ in islice(result, k)]
