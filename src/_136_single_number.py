# https://leetcode.com/problems/single-number/
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums = sorted(nums)
        for i in range(0, len(nums), 2):
            el1 = nums[i]
            el2 = nums[i + 1] if i + 1 < len(nums) else None
            if el1 != el2:
                return el1
