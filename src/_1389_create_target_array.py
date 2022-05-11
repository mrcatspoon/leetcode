# https://leetcode.com/problems/create-target-array-in-the-given-order/
from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for i, num in zip(index, nums):
            result.insert(i, num)
        return result
