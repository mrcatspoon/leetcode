# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/


class Solution:
    def minimumSum(self, num: int) -> int:
        if num % 1111 == 0:
            return (num // 1111) * 22

        num = sorted(str(num))
        return int(num[0] + num[2]) + int(num[1] + num[3])
