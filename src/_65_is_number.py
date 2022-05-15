# https://leetcode.com/problems/valid-number/


class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            int(s)
            return True
        except ValueError:
            pass
        try:
            float(s)
            if "n" in s:
                return False
            return True
        except ValueError:
            pass
        return False
