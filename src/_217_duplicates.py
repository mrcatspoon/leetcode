from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_unique = set()
        for n in nums:
            if n in nums_unique:
                return True
            nums_unique.add(n)
        return False
