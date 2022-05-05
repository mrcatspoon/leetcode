# https://leetcode.com/problems/min-stack/


class MinStack:
    __slots__ = "_stack", "_min_value"

    def __init__(self):
        self._stack = []
        self._min_value = None

    def push(self, val: int) -> None:
        self._stack.append(val)
        if self._min_value is None or val < self._min_value:
            self._min_value = val

    def pop(self) -> None:
        element = self._stack.pop()
        if element == self._min_value:
            self._min_value = min(self._stack) if self._stack else None

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_value
