# https://leetcode.com/problems/shuffle-string/
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        idx_map = dict(zip(indices, s))
        return "".join(idx_map[i] for i in range(len(s)))
