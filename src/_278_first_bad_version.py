# https://leetcode.com/problems/first-bad-version/


class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1

        low, high = 1, n
        while low < high:
            mid = (low + high) // 2
            is_bad = isBadVersion(mid)
            if is_bad:
                high = mid
            else:
                low = mid + 1

        return high
