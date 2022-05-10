# https://leetcode.com/problems/move-zeroes/
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) <= 1:
            return

        i, break_at = 0, len(nums)
        while i <= break_at:
            try:
                num = nums[i]
            except IndexError:
                return

            if num == 0:
                nums.append(nums.pop(i))
                break_at -= 1
            else:
                i += 1
