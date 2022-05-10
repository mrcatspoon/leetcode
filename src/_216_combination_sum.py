# https://leetcode.com/problems/combination-sum-iii/
from typing import List


class Solution(object):
    __slots__ = ("result",)

    def __init__(self):
        self.result = []

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1, min(n, 10)))
        self.backtracking(nums, k, n, [])
        return self.result

    def backtracking(self, nums: List[int], k: int, n: int, path: List[int]):
        if k < 0 or n < 0:
            return
        if k == n == 0:
            self.result.append(path)
        for i in range(len(nums)):
            self.backtracking(
                nums=nums[i + 1 :],
                k=k - 1,
                n=n - nums[i],
                path=path + [nums[i]],
            )
