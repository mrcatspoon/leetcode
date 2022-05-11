# https://leetcode.com/problems/running-sum-of-1d-array/
from itertools import islice
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(islice(nums, i)) for i in range(1, len(nums) + 1)]
