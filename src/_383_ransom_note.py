# https://leetcode.com/problems/ransom-note/


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        magazine = list(magazine)
        for char in ransomNote:
            try:
                index = magazine.index(char)
            except ValueError:
                return False
            magazine.pop(index)
        return True
