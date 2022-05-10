# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums_multidict = defaultdict(list)
        for i, num in enumerate(numbers):
            nums_multidict[num].append(i + 1)
        for i, num in enumerate(numbers):
            indexes = nums_multidict.get(target - num)
            if not indexes:
                continue
            if len(indexes) == 2:
                return list(indexes)
            if indexes[0] != i:
                return [i + 1, indexes[0]]
