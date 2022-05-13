# https://leetcode.com/problems/first-unique-character-in-a-string/
from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_indexes = defaultdict(list)
        for i, char in enumerate(s):
            char_indexes[char].append(i)
        return next((indexes[0] for indexes in char_indexes.values() if len(indexes) == 1), -1)
