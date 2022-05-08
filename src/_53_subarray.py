# https://leetcode.com/problems/maximum-subarray/
from itertools import islice
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # TODO: not efficient
        result = max_chunk = nums[0]
        for num in islice(nums, 1, len(nums)):
            max_chunk = max(num, max_chunk + num)
            result = max(result, max_chunk)

        return result
