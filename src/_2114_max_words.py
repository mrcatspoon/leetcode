# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(sentence.count(" ") + 1 for sentence in sentences)
