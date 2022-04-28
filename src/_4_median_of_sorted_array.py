# https://leetcode.com/problems/median-of-two-sorted-arrays/
from itertools import chain
from statistics import median
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if nums1 and nums2:
            nums = tuple(chain(nums1, nums2))
        elif nums1:
            nums = nums1
        else:
            nums = nums2
        return median(nums) if nums else 0.0
