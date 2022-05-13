# https://leetcode.com/problems/divide-two-integers/

import math
from typing import Tuple

MIN_INT_32 = -(2 ** 31)
MAX_INT_32 = -MIN_INT_32 - 1


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 1:
            return dividend
        if divisor == -1:
            return self.limit_result(-dividend)
        if dividend == divisor:
            return 1
        if abs(divisor) > abs(dividend):
            return 0

        is_negative = False
        if divisor < 0:
            divisor = -divisor
            is_negative = not is_negative
        if dividend < 0:
            dividend = -dividend
            is_negative = not is_negative

        raw_log2 = math.log2(divisor)
        int_log2 = int(raw_log2)
        if raw_log2 == int_log2:
            quotient = dividend >> int_log2
            return self.limit_result(-quotient if is_negative else quotient)

        quotient = ""
        dividend_str = str(dividend)
        divisor_len = int(math.log10(divisor)) + 1
        dividend_number = int(dividend_str[:divisor_len])
        if divisor > dividend_number:
            divisor_len += 1
            dividend_number = int(dividend_str[:divisor_len])

        for i in range(divisor_len, len(dividend_str) + 1):
            step_result, step_divisor = self.find_step_divisor(dividend_number, divisor)
            if step_divisor > dividend_number:
                step_result = 0
            subtraction_result = str(dividend_number - step_divisor)
            if i < len(dividend_str):
                subtraction_result += dividend_str[i]
            dividend_number = int(subtraction_result)
            quotient += str(step_result)

        quotient = int(quotient)
        return self.limit_result(-quotient if is_negative else quotient)

    def find_step_divisor(self, number: int, divisor: int) -> Tuple[int, int]:
        step_result, step_divisor = 1, divisor
        while number >= step_divisor + divisor:
            step_divisor += divisor
            step_result += 1
        return step_result, step_divisor

    def limit_result(self, n: int) -> int:
        if n > MAX_INT_32:
            return MAX_INT_32
        elif n < MIN_INT_32:
            return MIN_INT_32
        return n
