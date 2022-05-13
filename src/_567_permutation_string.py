# https://leetcode.com/problems/permutation-in-string/
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counter, window, match = Counter(s1), len(s1), 0
        for i in range(len(s2)):
            if s2[i] in counter:
                match += self.check_match(counter, s2[i], -1)
            if i >= len(s1) and s2[i - len(s1)] in counter:
                match += self.check_match(counter, s2[i - len(s1)], 1)
            if match == len(counter):
                return True

        return False

    def check_match(self, counter: Counter, char: str, counter_increment: int) -> int:
        match = -1 if not counter[char] else 0
        counter[char] += counter_increment
        if not counter[char]:
            match += 1
        return match
