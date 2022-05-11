# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
from functools import reduce


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = tuple(int(digit) for digit in str(n))
        return reduce(lambda x, y: x * y, digits) - sum(digits)
