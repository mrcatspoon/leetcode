# https://leetcode.com/problems/valid-anagram/
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s, t = Counter(s), Counter(t)
        for char, counter in s.items():
            if char not in t:
                return False
            t[char] -= counter
            if t[char] < 0:
                return False

        for counter in t.values():
            if counter != 0:
                return False

        return True
