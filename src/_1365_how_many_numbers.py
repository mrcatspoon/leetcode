# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_map = {}
        for i, num in enumerate(sorted(nums)):
            if num not in sorted_map:
                sorted_map[num] = i

        return [sorted_map.get(num, 0) for num in nums]
