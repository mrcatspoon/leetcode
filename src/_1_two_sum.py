# https://leetcode.com/problems/two-sum/
from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_multidict = defaultdict(list)
        for i, num in enumerate(nums):
            nums_multidict[num].append(i)
        for i, num in enumerate(nums):
            indexes = nums_multidict.get(target - num)
            if not indexes:
                continue
            if len(indexes) == 2:
                return list(indexes)
            if indexes[0] != i:
                return [i, indexes[0]]
