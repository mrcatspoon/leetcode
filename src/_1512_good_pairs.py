# https://leetcode.com/problems/number-of-good-pairs/
from collections import Counter
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        for num, repetition in Counter(nums).most_common():
            pairs += repetition * (repetition - 1) // 2
        return pairs
