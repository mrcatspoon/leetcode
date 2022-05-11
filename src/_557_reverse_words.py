# https://leetcode.com/problems/reverse-words-in-a-string-iii/


class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) == 1:
            return s
        return " ".join("".join(reversed(word)) for word in s.split(" "))
