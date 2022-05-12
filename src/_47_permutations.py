# https://leetcode.com/problems/permutations-ii/
from itertools import permutations
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, set(permutations(nums, len(nums)))))
