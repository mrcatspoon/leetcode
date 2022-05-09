# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from itertools import product
from typing import List

DIGITS_MAP = {
    "2": ("a", "b", "c"),
    "3": ("d", "e", "f"),
    "4": ("g", "h", "i"),
    "5": ("j", "k", "l"),
    "6": ("m", "n", "o"),
    "7": ("p", "q", "r", "s"),
    "8": ("t", "u", "v"),
    "9": ("w", "x", "y", "z"),
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        if len(digits) == 1:
            return DIGITS_MAP[digits]
        return ["".join(chars) for chars in product(*(DIGITS_MAP[digit] for digit in digits))]
