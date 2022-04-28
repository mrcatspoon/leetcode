# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        max_len = 0
        for i in range(len(s)):
            substring = set()
            for j in range(i, len(s)):
                if s[j] in substring:
                    max_len = max(len(substring), max_len)
                    break
                else:
                    substring.add(s[j])
            else:
                max_len = max(len(substring), max_len)
                break
        return max_len
