# https://leetcode.com/problems/fibonacci-number/
from functools import lru_cache


class Solution:
    @lru_cache
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
