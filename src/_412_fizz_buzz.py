# https://leetcode.com/problems/fizz-buzz/
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            div_3 = i % 3 == 0
            div_5 = i % 5 == 0
            if div_3 and div_5:
                i = "FizzBuzz"
            elif div_3:
                i = "Fizz"
            elif div_5:
                i = "Buzz"
            result.append(str(i))
        return result
