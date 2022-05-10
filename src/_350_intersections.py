# https://leetcode.com/problems/intersection-of-two-arrays-ii/
from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums, counter = nums2, Counter(nums1)
        else:
            nums, counter = nums1, Counter(nums2)

        intersections = []
        for num in nums:
            if (counter.get(num) or 0) > 0:
                intersections.append(num)
                counter[num] -= 1

        return intersections
