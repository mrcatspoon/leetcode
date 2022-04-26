# https://leetcode.com/problems/roman-to-integer/
MAP = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        nums = [MAP[char] for char in s]
        for i in range(len(nums)):
            current_element = nums[i]
            next_element = nums[i + 1] if i < len(nums) - 1 else 0
            if current_element >= next_element:
                result += current_element
            else:
                result -= current_element
        return result if result > 0 else -result
