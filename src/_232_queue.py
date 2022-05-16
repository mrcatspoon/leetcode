# https://leetcode.com/problems/implement-queue-using-stacks/


class MyQueue:
    __slots__ = ("_queue",)

    def __init__(self):
        self._queue = []

    def push(self, x: int) -> None:
        self._queue.append(x)

    def pop(self) -> int:
        return self._queue.pop(0)

    def peek(self) -> int:
        return self._queue[0]

    def empty(self) -> bool:
        return not self._queue
