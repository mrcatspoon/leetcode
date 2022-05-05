# https://leetcode.com/problems/valid-parentheses/

ROUND, SQUARE, CURLY = 1, 2, 3
BRACKETS = {"(": ROUND, ")": ROUND, "[": SQUARE, "]": SQUARE, "{": CURLY, "}": CURLY}
OPENED = {"(", "[", "{"}


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in OPENED:
                stack.append(char)
            else:
                if not stack or BRACKETS[stack[-1]] != BRACKETS[char]:
                    return False
                stack.pop()
        return not stack
