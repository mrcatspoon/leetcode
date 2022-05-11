# https://leetcode.com/problems/shuffle-the-array/
from itertools import chain, islice
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return list(chain(*zip(islice(nums, n), islice(nums, n, len(nums)))))
