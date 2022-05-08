# https://leetcode.com/problems/binary-search/
from typing import List


class Solution:
    __slots__ = ()

    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return -1
